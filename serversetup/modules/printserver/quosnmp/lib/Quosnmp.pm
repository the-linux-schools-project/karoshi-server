#!/usr/bin/perl
# Quosnmp.pm
# Version 1.8.9 Final
# A perl module of support functions for quosnmp, which is a CUPS backend for 
# print accounting and quota enforcement.
#
# Released by Marcus Lauer (marcus.lauer at nyu dot edu)
# Available at http://quosnmp.sourceforge.net
#
# Copyright (C) 2007-2009 by Marcus Lauer (marcus.lauer at nyu dot edu) except 
# where previous copyright is in effect.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307,
# USA.
#
# Development supported by the Center for Information Technology at New York 
# University (NYU) and the Wilf Department of Politics at NYU.
#
# Based on accsnmp v1.02.20070124 by jeff hardy (hardyjm at potsdam dot edu)
# The original header for accsnmp can be found below.
# ############
## accsnmp
## v1.02.20070124
## jeff hardy (hardyjm at potsdam dot edu)
## backend wrapper hardware accounting for cups
##
## ############
## Copyright 2007, Jeff Hardy (hardyjm at potsdam dot edu)
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307,
## USA.
##
## ###########


use strict;

package Quosnmp;
require Exporter;
our @ISA = qw(Exporter);
our @EXPORT_OK = qw(checkTimestampExpiration getUserPrintQuota getUserPagecount parseConfigFile readLockfile readQuotaFile reportStatus setDefaultVars touchLockfile updateUserPagecount validQuota writeDataFile writeLockfile);


## ###########
## Internal Variables


##
## ###########


## ###########
## Exported functions

sub checkTimestampExpiration {
	# Arguments: timestamp and reference to config value hash
	# Returns: 1 if the timestamp is expired (later than localtime), 0 otherwise.

	my ( $timestampPart, $VARS_Ref ) = @_;

	# First, make sure that this function was passed a timestamp.
	if ( !defined($timestampPart) || length($timestampPart) == 0 ) {
		return(0); # No timestamp means it must not expire.
	}

	# Also make sure that the timestampPart is a valid timestamp.
	unless ( &validTimestamp($timestampPart) ) {
		&reportStatus( 3, "This quota has an invalid timestamp. It is assumed to be expired or unusable.", $VARS_Ref );
		return(1);
	}

	my @currentTime = localtime;
	my @nowTime = (($currentTime[5]+1900), ($currentTime[4]+1), $currentTime[3], $currentTime[2], $currentTime[1]);

	my @timeStamp = split(/(\d\d)/,$timestampPart); # Splits CCYYMMDDhhmm into _blank_ CC _blank_ YY etc.
	my @endTime = ((($timeStamp[1]*100)+$timeStamp[3]), $timeStamp[5], $timeStamp[7], $timeStamp[9], $timeStamp[11]);

	for (my $counter = 0; $counter < 5; $counter++) {
		# Compare each part of the time.  Note that we keep looping only if the 
		# two values are equal.  Thus is the years are the same, we check the 
		# months, if those are the same we check the days, and so on.
		if ( $nowTime[$counter] > $endTime[$counter] ) {
			&reportStatus( 3, "This quota expired on $endTime[0]\-$endTime[1]\-$endTime[2] at $endTime[3]\:$endTime[4].", $VARS_Ref );
			return(1);
		}
		elsif ( $nowTime[$counter] < $endTime[$counter] ) {
			return(0);
		}
	}

	return(0); # Default is not expired (but it'll be expired in a minute!)
}


sub getUserPrintQuota {
	# Args: username, reference to config value hash
	# Returns: user's print quota
	#
	# As far as quotas go:
	# * The user quota _always_ has the highest priority
	# * The group which gives the highest quota has second priority, e.g. will be used if 
	# no user quota is found.
	# * The default quota _always_ has the lowest priority.  It will only be used if no 
	# other quota is found.
	#
	# As far as quota adjustments go, all adjustments are summed together.
	#
	# Possible return values:
	# undef  No quota files found at all, printing not allowed (this is a weird outcome).
	# U      Unlimited printing allowed (no quota).
	# N      Printing explictly not allowed.
	# n>0    Quota is n pages.

	my ( $userName, $VARS_Ref ) = @_;

	&reportStatus( 3, "Calculating user\'s print quota.", $VARS_Ref );

	my $acctQuota;
	my $acctAdjustments;
	my $acctQuotaFile;

	# First, look for a per-user quota.  This quota has exclusive top priority.
	my $quotaFile = $$VARS_Ref{QUOTA_DIRECTORY} . "/" . $userName . "_user_quota";
	( $acctQuota, $acctAdjustments ) = &readQuotaFile( $quotaFile, $VARS_Ref );

	# These values can turn out to be undefined.
	if ( defined($acctAdjustments) ) {
		&reportStatus( 3, "Found $acctAdjustments pages of adjustments in file $quotaFile for user $userName.", $VARS_Ref );
	}

	if ( defined($acctQuota) ) {
		$acctQuotaFile = $quotaFile;
		&reportStatus( 3, "Using quota file $quotaFile.", $VARS_Ref );
	}

	# Look for per-group quota and adjustments for each group the user is in, but only collect the former if no user quota was found.
	my $quotaCandidate;
	my $quotaFileCandidate;
	my $latestAdjustments;

	my ($name,$passwd,$gid,$members) = getgrent();

	while ( defined($name) && length($name) > 0 ) {
		# This next line will allow me to use a simple pattern match.
		my $testmembers = " " . $members . " ";

		if ( $testmembers =~ m/\s$userName\s/ ) {
			my $testQuotaFile = $$VARS_Ref{QUOTA_DIRECTORY} . "/" . $name . "_group_quota";

			if ( -e $testQuotaFile ) {
				my ($testQuota, $latestAdjustments) = &readQuotaFile( $testQuotaFile, $VARS_Ref );

				# Every adjustment find in our search is used.
				if ( defined($latestAdjustments) ) {
					&reportStatus( 3, "Found $latestAdjustments pages of adjustments in file $quotaFile for user $userName.", $VARS_Ref );
					$acctAdjustments = $acctAdjustments + $latestAdjustments;
				}

				# Only grab the highest group quota, and only if a user quota is not already set.
				if ( !defined($acctQuota) && defined($testQuota) ) {
					if ( $testQuota =~ m/^[UN]$/ ) {
						# Unlimited printing ("U") and Cannot print ("N").  Use this quota.
						$acctQuota = $testQuota;
						$acctQuotaFile = $testQuotaFile;
						&reportStatus( 3, "Using quota file $testQuotaFile.", $VARS_Ref );
						last; # Exit loop so that this quota and no other will be used.
					}

					if ( !defined($quotaCandidate) ) { # Always grab the first value we find.
						$quotaCandidate = $testQuota;
						$quotaFileCandidate = $testQuotaFile;
					}
					elsif ( $testQuota > $quotaCandidate ) { # If the new quota is larger than the old, store it.
						$quotaCandidate = $testQuota;
						$quotaFileCandidate = $testQuotaFile;
					}
				}
			}
		}

		($name,$passwd,$gid,$members) = getgrent();
	}

	setgrent(); # In case we call this function again!

	# If we found an applicable group quota file and no user quota file, set the quota values from the best group quota.
	if ( defined($quotaCandidate) && !defined($acctQuota) ) {
		$acctQuota = $quotaCandidate;
		$acctQuotaFile = $quotaFileCandidate;
		&reportStatus( 3, "Using quota file $quotaFileCandidate.", $VARS_Ref );
	}

	# If no group quota was found either, use the default quota.
	my $testQuotaFile = $$VARS_Ref{QUOTA_DIRECTORY} . "/print_quota";
	($quotaCandidate, $latestAdjustments) = &readQuotaFile( $testQuotaFile, $VARS_Ref );

	# Every adjustment is used.
	if ( defined($latestAdjustments) ) {
		&reportStatus( 3, "Found $latestAdjustments pages of adjustments in file $quotaFile for user $userName.", $VARS_Ref );
		$acctAdjustments = $acctAdjustments + $latestAdjustments;
	}

	# If there is no quota yet and we found one in the default file, set the quota to that value.
	if ( !defined($acctQuota) && defined($quotaCandidate) ) {
		$acctQuota = $quotaCandidate;
		$acctQuotaFile = $testQuotaFile;
		&reportStatus( 3, "Using quota file $testQuotaFile.", $VARS_Ref );
	}

	# Report the results of our search.
	if ( defined($acctQuota) ) {
		&reportStatus( 3, "Using quota of $acctQuota pages from file $acctQuotaFile for user $userName.", $VARS_Ref );
		if ( defined($acctAdjustments) ) {
			&reportStatus( 3, "A total of $acctAdjustments pages of adjustments were found for user $userName.", $VARS_Ref );
		}
	}
	else {
		&reportStatus( 3, "No applicable quota files found at all!", $VARS_Ref );
		$acctQuota = "N"; # User cannot print.
	}

	# Determine the official "final" quota value.
	my $finalQuota;

	if ( $acctQuota =~ m/^U$/ ) {
		$finalQuota = "U";
		&reportStatus( 2, "User $userName has an unlimited quota.", $VARS_Ref );
	}
	elsif ( $acctQuota =~ m/^N$/ ) {
		$finalQuota = "N";
		&reportStatus( 2, "User $userName is not allowed to print.", $VARS_Ref );
	}
	else {
		$finalQuota = $acctQuota;

		if ( defined($acctAdjustments) ) {
			# Add the summed adjustments to the quota we're using to get the "true" quota.
			$finalQuota = $finalQuota + $acctAdjustments;
		}

		&reportStatus( 2, "User $userName has a quota of $finalQuota pages.", $VARS_Ref );
	}

	return($finalQuota);
}


sub getUserPagecount {
	# Args: username and reference to config value hash
	# Returns: user's historical pagecount (or undef on error)

	my ( $userName, $VARS_Ref ) = @_;

	my $histPages;
	my $accFile = "$$VARS_Ref{ACCOUNTING_DIRECTORY}/$userName";

	if ( ! -e $accFile ) {
		&reportStatus( 3, "Creating an accounting file for $userName.", $VARS_Ref );

		# Create the accounting file.
		&writeDataFile(0,$accFile,"0");

		# Set appropriate permissions (will only work if CUPS is running as root!)
		chown ( (getpwnam("lp"))[2], (getpwnam($userName))[3], "$accFile" );
		chmod (0640,"$accFile");

		# Return a pagecount of zero (no accounting file means that no printing has been done yet).
		return(0);
	}

	my $remainingTries = 3;
	my $fileWasOpened = 0;

	while ( $remainingTries > 0 ) { # Loop in case some other process is writing to the file.
		open(ACC_FH, "<$accFile") and $fileWasOpened = 1;

		if ( $fileWasOpened == 1 ) {
			last;
		}
		else {
			$remainingTries--; 
			&reportStatus( 3, "Waiting $$VARS_Ref{DISK_RETRY_PERIOD} seconds to retry opening accounting file.", $VARS_Ref );
			sleep($$VARS_Ref{DISK_RETRY_PERIOD});
		}
	}

	if ( $fileWasOpened == 0 ) {
		&reportStatus( 1, "Unable to open user accounting file $accFile", $VARS_Ref );
		return();
	}

	# Now get the pagecount.
	flock( ACC_FH, 2 );
	$histPages = <ACC_FH>;
	flock( ACC_FH, 8 );
	close( ACC_FH );

	if ( defined($histPages) ) {
		chomp($histPages);
		&reportStatus( 2, "Pagecount for user $userName is currently $histPages page(s).", $VARS_Ref );
		return($histPages);
	}
	else {
		&reportStatus( 1, "Could not get pagecount for user $userName.", $VARS_Ref );
		return();
	}
}


sub parseConfigFile {
	# Args: reference to config value hash, reference to job blacklist array, reference to email mapping hash
	# Returns: 0 if the config file was not found, 1 otherwise.

	my ( $VARS_Ref, $JOB_BLACKLIST_Ref, $EMAIL_LIST_Ref ) = @_;

	if ( ! -e $$VARS_Ref{CONFIG_FILE}) {
		return(0);
	}

	open( CONFIG_FH, "<$$VARS_Ref{CONFIG_FILE}" ) or return(0);
	flock( CONFIG_FH, 2 ); # Lock the config file. Note that programs such as vi and emacs will ignore this...

	# Here is where we go through every line and categorize them all.
	my $currentPrinter = 1;
	my $currentPrinterName = "ALL";
	my $inEmailList = 0;

	while ( my $nextLine = <CONFIG_FH> ) {
		chomp($nextLine); # One error message uses nextLine, so get rid of any trailing newline.
		(my $editedLine, my $commentText) = split( /#/, $nextLine, 2 ); # If there is a comment, remove it.

		# Ignore all empty or all-whitespace lines, including formerly all-comment lines.
		if ( !defined($editedLine) || length($editedLine) == 0 || $editedLine =~ m/^\s*$/ ) {
			&reportStatus( 3, "Empty/Comment line", $VARS_Ref );
			next; # Do nothing
		}
		# If we get an e-mail list header, then set a variable such that we expect the next few lines to be e-mail mappings.
		elsif ( $editedLine =~ m/^\s*\[EMAIL_LIST\]/ ) {
			$inEmailList = 1;
			$currentPrinter = 0; # An e-mail list section cannot contain printer properties.
			&reportStatus( 3, "Starting an EMAIL_LIST", $VARS_Ref );
			next;
		}
		# If we get a per-printer variable definition header, figure out whether it matches the printer we're printing to.
		elsif ( $editedLine =~ m/^\s*\[(.+)\]/ ) {
			if ( $inEmailList == 1 ) {
				$inEmailList = 0; # No printer properties section can contain an e-mail address list.
				&reportStatus( 3, "Ending an EMAIL_LIST (started printer section)", $VARS_Ref );
			}

			if ( $$VARS_Ref{PRINTER} =~ m/^$1$/ ) {
				$currentPrinter = 1;
			}
			else {
				$currentPrinter = 0;
			}
			$currentPrinterName = $1;
			&reportStatus( 3, "The following lines apply to printer $1 (current printer: $$VARS_Ref{PRINTER})", $VARS_Ref );

			next;
		}
		# Process this line as an e-mail address.
		elsif ( $inEmailList == 1 ) {
			$editedLine =~ s/\s+//g; # Remove any whitespace (probably leading or trailing whitespace).
			my ( $alias, $address ) = split( /:/, $editedLine );
			$$EMAIL_LIST_Ref{$alias} = $address;

			&reportStatus( 3, "Adding user $alias, email $address to EMAIL_LIST", $VARS_Ref );
			next;
		}
		# Variable definitions. Process these lines and set the appropriate global value.
		elsif ( $currentPrinter == 1 ) {
			if ( $inEmailList == 1 ) {
				$inEmailList = 0; # No printer properties section can contain an e-mail address list.
				&reportStatus( 3, "Ending an EMAIL_LIST (found variable definition)", $VARS_Ref );
			}

			(my $key, my $setting) = split( /=/, $editedLine, 2 ); # Split the line on the first equals sign.
			$key =~ tr/a-z/A-Z/; # Make key all-uppercase.
			$key =~ s/\s+//g; # Get rid of excess spaces (e.g. between the key and the "=").
			$setting =~ s/^\s+//; # Ged rid of leading spaces which were between the "=" and the setting.
			$setting =~ s/\s+$//; # Ged rid of trailing spaces as well.

			if ( $key =~ m/^ENFORCE_QUOTA$/ ) {
				my $newSetting = &makeBoolean($setting);

				if ( defined($newSetting) ) {
					$$VARS_Ref{ENFORCE_QUOTA} = $newSetting;
					&reportStatus( 3, "Setting ENFORCE_QUOTA to $newSetting", $VARS_Ref );
				}
			}
			elsif ( $key =~ m/^SAVE_JOBS$/ ) {
				my $newSetting = &makeBoolean($setting);

				if ( defined($newSetting) ) {
					$$VARS_Ref{SAVE_JOBS} = $newSetting;
					&reportStatus( 3, "Setting SAVE_JOBS to $newSetting", $VARS_Ref );
				}
			}
			elsif ( $key =~ m/^JOB_BLACKLIST$/ && length($setting) > 0 ) {
				my @tempArray = split( /\,/, $setting );
				for ( my $counter = 0; $counter <= $#tempArray; $counter++ ) {
					$$JOB_BLACKLIST_Ref[$counter] = $tempArray[$counter];
				}
				&reportStatus( 3, "Setting JOB_BLACKLIST to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^HEADER_DISCOUNT$/ ) {
				$$VARS_Ref{HEADER_DISCOUNT} = $setting;
				&reportStatus( 3, "Setting HEADER_DISCOUNT to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^PRINT_ON_LOW_TONER$/ && $setting =~ m/^\d+$/ ) {
				my $newSetting = &makeBoolean($setting);

				if ( defined($newSetting) ) {
					$$VARS_Ref{PRINT_ON_LOW_TONER} = $newSetting;
					&reportStatus( 3, "Setting PRINT_ON_LOW_TONER to $newSetting", $VARS_Ref );
				}
			}
			elsif ( $key =~ m/^PAGE_LOG$/ ) {
				my $newSetting = &makeBoolean($setting);

				if ( defined($newSetting) ) {
					$$VARS_Ref{PAGE_LOG} = $newSetting;
					&reportStatus( 3, "Setting PAGE_LOG to $newSetting", $VARS_Ref );
				}
			}
			elsif ( $key =~ m/^PAGE_LOG_FILE$/ && length($setting) > 0 ) {
				$$VARS_Ref{PAGE_LOG_FILE} = $setting;
				&reportStatus( 3, "Setting PAGE_LOG_FILE to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^ERROR_LOG$/ ) {
				my $newSetting = &makeBoolean($setting);

				if ( defined($newSetting) ) {
					$$VARS_Ref{ERROR_LOG} = $newSetting;
					&reportStatus( 3, "Setting ERROR_LOG to $newSetting", $VARS_Ref );
				}
			}
			elsif ( $key =~ m/^ERROR_LOG_FILE$/ && length($setting) > 0 ) {
				$$VARS_Ref{ERROR_LOG_FILE} = $setting;
				&reportStatus( 3, "Setting ERROR_LOG_FILE to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^DEBUG_LEVEL$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{DEBUG_LEVEL} = $setting;
				&reportStatus( 3, "Setting DEBUG_LEVEL to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^OVER_QUOTA_NOTIFY$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{OVER_QUOTA_NOTIFY} = $setting;
				&reportStatus( 3, "Setting OVER_QUOTA_NOTIFY to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^SMTP_SERVER$/ ) {
				$$VARS_Ref{SMTP_SERVER} = $setting;
				&reportStatus( 3, "Setting SMTP_SERVER to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^OVER_QUOTA_EMAIL_MESSAGE$/ ) {
				$$VARS_Ref{OVER_QUOTA_EMAIL_MESSAGE} = $setting;
				&reportStatus( 3, "Setting OVER_QUOTA_EMAIL_MESSAGE to \"$setting\"", $VARS_Ref );
			}
			elsif ( $key =~ m/^BACKEND_DIRECTORY$/ && -r $setting && -d $setting ) {
				$$VARS_Ref{BACKEND_DIRECTORY} = $setting;
				&reportStatus( 3, "Setting BACKEND_DIRECTORY to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^BINARY_DIRECTORY$/ && -r $setting && -d $setting ) {
				$$VARS_Ref{BINARY_DIRECTORY} = $setting;
				&reportStatus( 3, "Setting BINARY_DIRECTORY to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^ACCOUNTING_DIRECTORY$/ && -w $setting && -d $setting ) {
				$$VARS_Ref{ACCOUNTING_DIRECTORY} = $setting;
				&reportStatus( 3, "Setting ACCOUNTING_DIRECTORY to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^QUOTA_DIRECTORY$/ && -r $setting && -d $setting ) {
				$$VARS_Ref{QUOTA_DIRECTORY} = $setting;
				&reportStatus( 3, "Setting QUOTA_DIRECTORY to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^PAGE_MULTIPLIER$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{PAGE_MULTIPLIER} = $setting;
				&reportStatus( 3, "Setting PAGE_MULTIPLIER to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^PAGECOUNT_QUERY_METHOD$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{PAGECOUNT_QUERY_METHOD} = $setting;
				&reportStatus( 3, "Setting PAGECOUNT_QUERY_METHOD to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^STATUS_QUERY_METHOD$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{STATUS_QUERY_METHOD} = $setting;
				&reportStatus( 3, "Setting STATUS_QUERY_METHOD to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^BACKEND_RETRIES$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{BACKEND_RETRIES} = $setting;
				&reportStatus( 3, "Setting BACKEND_RETRIES to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^HARD_STALL_TIMEOUT$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{HARD_STALL_TIMEOUT} = $setting;
				&reportStatus( 3, "Setting HARD_STALL_TIMEOUT to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^SOFT_STALL_TIMEOUT$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{SOFT_STALL_TIMEOUT} = $setting;
				&reportStatus( 3, "Setting SOFT_STALL_TIMEOUT to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^SNMP_COMMUNITY$/ && length($setting) > 0 ) {
				$$VARS_Ref{SNMP_COMMUNITY} = $setting;
				&reportStatus( 3, "Setting SNMP_COMMUNITY to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^TCP_QUERY_PORT$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{TCP_QUERY_PORT} = $setting;
				&reportStatus( 3, "Setting TCP_QUERY_PORT to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^HP_ADVANCED_STATUS$/ ) {
				my $newSetting = &makeBoolean($setting);

				if ( defined($newSetting) ) {
					$$VARS_Ref{HP_ADVANCED_STATUS} = $newSetting;
					&reportStatus( 3, "Setting HP_ADVANCED_STATUS to $newSetting", $VARS_Ref );
				}
			}
			elsif ( $key =~ m/^LOCK_PRINTER$/ ) {
				my $newSetting = &makeBoolean($setting);

				if ( defined($newSetting) ) {
					$$VARS_Ref{LOCK_PRINTER} = $newSetting;
					&reportStatus( 3, "Setting LOCK_PRINTER to $newSetting", $VARS_Ref );
				}
			}
			elsif ( $key =~ m/^UPDATE_LOCKFILE_TIMESTAMP$/ ) {
				my $newSetting = &makeBoolean($setting);

				if ( defined($newSetting) ) {
					$$VARS_Ref{UPDATE_LOCKFILE_TIMESTAMP} = $newSetting;
					&reportStatus( 3, "Setting UPDATE_LOCKFILE_TIMESTAMP to $newSetting", $VARS_Ref );
				}
			}
			elsif ( $key =~ m/^MONITOR_PAGECOUNT$/ ) {
				my $newSetting = &makeBoolean($setting);

				if ( defined($newSetting) ) {
					$$VARS_Ref{MONITOR_PAGECOUNT} = $newSetting;
					&reportStatus( 3, "Setting MONITOR_PAGECOUNT to $newSetting", $VARS_Ref );
				}
			}
			elsif ( $key =~ m/^NETWORK_POLLING_PERIOD$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{NETWORK_POLLING_PERIOD} = $setting;
				&reportStatus( 3, "Setting NETWORK_POLLING_PERIOD to $setting", $VARS_Ref );
			}
			elsif ( $key =~ m/^DISK_RETRY_PERIOD$/ && $setting =~ m/^\d+$/ ) {
				$$VARS_Ref{DISK_RETRY_PERIOD} = $setting;
				&reportStatus( 3, "Setting DISK_RETRY_PERIOD to $setting", $VARS_Ref );
			}
			else {
				&reportStatus( 1, "Invalid setting in config file: \"$editedLine\"", $VARS_Ref );
			}

			next;
		}
		# Stuff we're skipping because it does not apply to the current printer.
		elsif ( $currentPrinter == 0 ) {
			&reportStatus( 3, "Ignoring line which applies to printer \"$currentPrinterName\": \"$nextLine\"", $VARS_Ref );
			next;
		}
		# Everything else must be junk
		else {
			&reportStatus( 3, "Unknown line in config file: \"$nextLine\"", $VARS_Ref );
		}
	}

	flock( CONFIG_FH, 8 );
	close( CONFIG_FH );
	return(1);
}


sub readLockfile {
	# Args: full path to lockfile and reference to config value hash
	# Returns: array containing jobid of locking job and username (undef on errors)

	my ( $lockfile, $VARS_Ref ) = @_;

	if ( defined($lockfile) && -e $lockfile ) {
		my $lockfileOpened = 0;
		open( LOCK_FH, "<$lockfile" ) and $lockfileOpened = 1;

		if ( $lockfileOpened == 1 ) {
			flock( LOCK_FH, 2 );
			my $lockFileContent = <LOCK_FH>;
			flock( LOCK_FH, 8 );
			close( LOCK_FH );

			chomp($lockFileContent);
			my ( $lockingJob, $lockingPID, $lockingUser ) = split( /,/, $lockFileContent, 3 );

			&reportStatus( 3, "Found locking job \"$lockingJob\" with locking PID \"$lockingPID\" and username \"$lockingUser\" in lockfile.", $VARS_Ref );

			return($lockingJob, $lockingPID, $lockingUser);
		}
	}

	return();
}


sub readQuotaFile {
	# Arguments: file to read and reference to config value hash
	# Returns: two-element array containing numeric quota and/or adjustment value (undef on error)

	# Format of quota file:
	# Quotas can be simple numbers ("500") or adjustments ("+250", "-100").
	# Timestamps (optional) are of the format CCYYMMDDhhmm.
	# Associated quota and timestamp have comma between them: +250,200910011200 (10/01/2009, noon).
	# Separate quota/timestamp entries should appear on separate lines.

	my ( $quotafile, $VARS_Ref ) = @_;

	if ( !defined($quotafile) ) {
		return();
	}

	&reportStatus( 3, "Attempting to read quota file $quotafile", $VARS_Ref );

	if ( ! -e $quotafile ) {
		&reportStatus( 3, "Quota file $quotafile not found.", $VARS_Ref );
		return();
	}

	my $quota;
	my $adjustment;

	my $remainingTries = 3;
	my $fileWasOpened = 0;

	while ( $remainingTries > 0 ) {
		open(QUO_FH, "<$quotafile") and $fileWasOpened = 1;

		if ( $fileWasOpened == 1 ) {
			last;
		}
		else {
			$remainingTries--;
			&reportStatus( 3, "Waiting $$VARS_Ref{DISK_RETRY_PERIOD} seconds to retry opening quota file.", $VARS_Ref );
			sleep($$VARS_Ref{DISK_RETRY_PERIOD});
		}
	}

	if ( $fileWasOpened == 0 ) {
		&reportStatus( 1, "Unable to read quota file $quotafile", $VARS_Ref );
		return();
	}

	flock( QUO_FH, 2 ); # Lock the file in case another instance of, say, quosnmp-util is trying to edit it.

	while ( my $quotaLine = <QUO_FH> ) {
		chomp($quotaLine);

		# Each line may optionally have two parts, a quota and a timestamp.
		my ( $quotaPart, $timestampPart ) = split(/,/, $quotaLine);

		if ( defined($quotaPart) ) {
			if ( defined($timestampPart) ) {
				&reportStatus( 3, "Found quota of $quotaPart with expiration time $timestampPart.", $VARS_Ref );
			}
			else {
				&reportStatus( 3, "Found quota of $quotaPart with no expiration time.", $VARS_Ref );
			}

			# If the timestamp exists, check that it has not expired.
			my $expired = 0;

			if ( defined($timestampPart) && ( &checkTimestampExpiration($timestampPart,$VARS_Ref) == 1 ) ) {
				# If the quota exists and has expired, skip to the next quota line (if any).
				next;
			}

			# If the quota has not expired, process the quota part of the line.
			if ( $quotaPart =~ m/^\+(\d+)/ ) {
				if ( defined($adjustment) ) {
					$adjustment = $adjustment + $1;
				}
				else {
					$adjustment = $1;
				}
			}
			elsif ( $quotaPart =~ m/^\-(\d+)/ ) {
				if ( defined($adjustment) ) {
					$adjustment = $adjustment - $1;
				}
				else {
					$adjustment = -$1;
				}
			}
			else {
				$quota = $quotaPart; # The last quota in the file will be used if there is more than one (there should not be!)
			}
		}
	}

	flock( QUO_FH, 8 );
	close( QUO_FH );

	return ($quota, $adjustment);
}


sub reportStatus {
	# Args: messagetype, error text, and reference to config value hash
	# Results: logs error text to error logfile if logging is enabled and error level is appropriate.
	# NOTE: messagetype is a number from 0-3.  See below for what these values mean.

	my ( $messageType, $errorMsg, $VARS_Ref ) = @_;

	if ( defined($$VARS_Ref{QUIET_MODE}) && $$VARS_Ref{QUIET_MODE} == 1 ) {
		return; # Mode 1 is to not print anything.
	}

	unless ( defined($$VARS_Ref{ERROR_LOG}) && defined($$VARS_Ref{ERROR_LOG_FILE}) && defined($$VARS_Ref{DEBUG_LEVEL}) ) {
		return;
	}

	if ( $$VARS_Ref{ERROR_LOG} == 0 || $$VARS_Ref{DEBUG_LEVEL} < 0 ) {
		return; # We don't want to do logging.
	}

	my $errorPrefix;

	if ( $messageType == 0 ) {
		$errorPrefix = "FATAL_ERROR";
	}
	elsif ( $messageType == 1 ) {
		$errorPrefix = "ERROR";
	} 
	elsif ( $messageType == 2 ) {
		$errorPrefix = "INFO";
	}
	elsif ( $messageType == 3 ) {
		$errorPrefix = "DEBUG";
	}

	# All non-debug messages are printed to STDERR. These are the process status info.
	if ( $messageType <= 2 ) {
		if ( !defined($$VARS_Ref{QUIET_MODE}) || $$VARS_Ref{QUIET_MODE} == 0 ) {
			print STDERR "$errorPrefix: $errorMsg\n";
		}
	}

	# Under certain circumstances, messages are logged as well.
	if ( $messageType <= $$VARS_Ref{DEBUG_LEVEL} ) {
		my $openFailed = 0;
		my @errorTime = localtime;

		open( ERR_LOG_FH, ">>$$VARS_Ref{ERROR_LOG_FILE}" ) or $openFailed = 1;

		if ( $openFailed > 0 ) {
			# File permissions might be the problem
			my @userInfo = getpwnam("lp");
			chown( $userInfo[2], $userInfo[3], $$VARS_Ref{ERROR_LOG_FILE} );
			chmod( 0600, $$VARS_Ref{ERROR_LOG_FILE} );
			$openFailed = 0;
			open( ERR_LOG_FH, ">>$$VARS_Ref{ERROR_LOG_FILE}" ) or $openFailed = 2;
		}

		if ( $openFailed > 0 ) {
			print STDERR "ERROR: Logging errors to $$VARS_Ref{ERROR_LOG_FILE} has failed!";
			return;
		}

		flock( ERR_LOG_FH, 2 ); # Only allow one "chunk" of log data to be written at a time!
		seek( ERR_LOG_FH, 0, 2 );

		{
			my $currentFH = select( ERR_LOG_FH );
			local $| = 1;
			select( $currentFH );

			printf ERR_LOG_FH "%04d-%02d-%02d\t%02d:%02d:%02d\t",$errorTime[5]+1900,$errorTime[4]+1,$errorTime[3],$errorTime[2],$errorTime[1],$errorTime[0];
			print ERR_LOG_FH "$$VARS_Ref{JOB_NUMBER}\t$$VARS_Ref{PRINTER}\t$errorPrefix: $errorMsg\n";
		}

		if ( $messageType == 0 && $$VARS_Ref{DEBUG_LEVEL} >= 3 ) {
			# In this case, the script is going to exit so print a bunch of debug info.
			my $currentFH = select( ERR_LOG_FH );
			local $| = 1;
			select( $currentFH );

			my $argCount = 0;

			# Log arguments to script
			print ERR_LOG_FH "Arguments passed to backend:\t";
			while ( $argCount < $#ARGV ) {
				print ERR_LOG_FH "$argCount:$ARGV[$argCount]\t";
				$argCount++;
			}
			print ERR_LOG_FH "\n";

			# Log environment variables.
			print ERR_LOG_FH "Environment variables:\t";
			foreach my $eachKey (keys(%ENV)) {
				print ERR_LOG_FH "$eachKey==$ENV{$eachKey}\t";
			}
			print ERR_LOG_FH "\n";
		}

		flock( ERR_LOG_FH, 8 );
		close( ERR_LOG_FH );
	}
}


sub setDefaultVars {
	# Arguments: reference to config value hash
	# Results: sets values in quosnmp configuration variable array to sensible defaults.
	# Returns: 0 on error, 1 otherwise.

	my $VARS_Ref = $_[0];

	$$VARS_Ref{ENFORCE_QUOTA} = 1;
	$$VARS_Ref{SAVE_JOBS} = 0;
	$$VARS_Ref{HEADER_DISCOUNT} = 0;
	$$VARS_Ref{PAGE_LOG} = 1;
	$$VARS_Ref{PAGE_LOG_FILE} = "/var/log/cups/quosnmp_page_log";
	$$VARS_Ref{ERROR_LOG} = 1;
	$$VARS_Ref{ERROR_LOG_FILE} = "/var/log/cups/quosnmp_error_log";
	$$VARS_Ref{DEBUG_LEVEL} = 1;
	$$VARS_Ref{PAGE_MULTIPLIER} = 1;
	$$VARS_Ref{OVER_QUOTA_NOTIFY} = 0;
	$$VARS_Ref{SMTP_SERVER} = "smtp.example.com";
	$$VARS_Ref{OVER_QUOTA_EMAIL_MESSAGE} = "You have exceeded your print quota.\n";
	$$VARS_Ref{BACKEND_DIRECTORY} = "/usr/lib/cups/backend";
	$$VARS_Ref{BINARY_DIRECTORY} = "/usr/bin";
	$$VARS_Ref{ACCOUNTING_DIRECTORY} = "/var/log/cups/accounting";
	$$VARS_Ref{QUOTA_DIRECTORY} = "/var/log/cups/quotas";
	$$VARS_Ref{PAGECOUNT_QUERY_METHOD} = 0;
	$$VARS_Ref{STATUS_QUERY_METHOD} = 0;
	$$VARS_Ref{BACKEND_RETRIES} = 0;
	$$VARS_Ref{HARD_STALL_TIMEOUT} = 7200;
	$$VARS_Ref{SOFT_STALL_TIMEOUT} = 600;
	$$VARS_Ref{SNMP_COMMUNITY} = "public";
	$$VARS_Ref{TCP_QUERY_PORT} = 9100;
	$$VARS_Ref{HP_ADVANCED_STATUS} = 0;
	$$VARS_Ref{LOCK_PRINTER} = 1;
	$$VARS_Ref{UPDATE_LOCKFILE_TIMESTAMP} = 0;
	$$VARS_Ref{MONITOR_PAGECOUNT} = 1;
	$$VARS_Ref{NETWORK_POLLING_PERIOD} = 2;
	$$VARS_Ref{DISK_RETRY_PERIOD} = 3;
}


sub touchLockfile {
	# Args: reference to config value hash
	# Returns: 1 on success, 0 otherwise
	# Note: does not read the lockfile to determine that it is the lockfile for 
	#       this process. This is acceptable. Touching the lockfile is supposed 
	#       to stop a second process from running on the same printer, not deal 
	#       with the situation in which this has already happened.

	my $VARS_Ref = $_[0];

	if ( $$VARS_Ref{LOCK_PRINTER} == 1 && $$VARS_Ref{UPDATE_LOCKFILE_TIMESTAMP} == 1 ) {
		my $lockfile = $$VARS_Ref{LOCKFILE};
		my $returnVal = 0;

		if ( defined($lockfile) && -w $lockfile ) {
			my $atime = my $mtime = time();
			$returnVal = utime( $atime, $mtime, $lockfile );
		}

		if ( $returnVal == 1 ) {
			&reportStatus( 3, "Lockfile timestamp updated.", $VARS_Ref );
		}
		else {
			&reportStatus( 3, "Cannot update lockfile timestamp.", $VARS_Ref );
		}

		return($returnVal);
	}
	else {
		return(1);
	}
}


sub updateUserPagecount {
	# Arguments: username, pages printed, and reference to config value hash
	# Results: Updates accounting file while locking it the whole time
	# Returns: 1 on success, 0 on failure.

	my ( $userName, $additionalPages, $VARS_Ref ) = @_;

	if ( $additionalPages !~ /^[+-]?\d+$/ ) {
		if ( $additionalPages =~ /^[+-]?[UN]$/ ) { # Trying to add an "unlimited" or "no printing" is not really an error.
			&reportStatus( 3, "Cannot add special value $additionalPages to a pagecount.", $VARS_Ref );
			return(0);
		}
		else {
			&reportStatus( 1, "Cannot add a non-numeric value to a pagecount.", $VARS_Ref );
			return(0);
		}
	}

	my $accFile = "$$VARS_Ref{ACCOUNTING_DIRECTORY}/$userName";
	my $remainingTries = 3;
	my $fileWasOpened = 0;

	while ( $remainingTries > 0 ) {
		if ( -e $accFile ) {
			open(ACC_FH, "+<$accFile") and $fileWasOpened = 1;
		}
		else {
			open(ACC_FH, "+>$accFile") and $fileWasOpened = 1;
		}

		if ( $fileWasOpened == 1 ) {
			last;
		}
		else {
			$remainingTries--;
			&reportStatus( 3, "Waiting $$VARS_Ref{DISK_RETRY_PERIOD} seconds to retry opening accounting file.", $VARS_Ref );
			sleep($$VARS_Ref{DISK_RETRY_PERIOD});
		}
	}

	if ( $fileWasOpened == 0 ) {
		&reportStatus( 1, "Unable to set user page count because accounting file could not be opened.", $VARS_Ref );
		return(0);
	}

	flock( ACC_FH, 2 ); # Don't let any other process read the accounting data until we've updated it.

	my $totPages = <ACC_FH>;
	$totPages += $additionalPages;

	seek( ACC_FH, 0, 0 );
	{
		my $currentFH = select( ACC_FH );
		local $| = 1;
		select( $currentFH );

		print ACC_FH "$totPages";
		truncate(ACC_FH, length($totPages));
	}

	flock( ACC_FH, 8 );
	close( ACC_FH );

	# Also set permissions on accounting files to something secure.
	chown ( (getpwnam("lp"))[2], (getpwnam($userName))[3], "$accFile" );
	chmod (0640,"$accFile");

	&reportStatus( 2, "New pagecount for $userName has been set to $totPages pages.", $VARS_Ref );
	return(1);
}


sub validQuota {
	# Argumentss: a quota string to validate.
	# Returns: 1 if quota is valid, 0 if it is not valid.

	my $quota = $_[0];

	my $quotapart;
	my $timestamp;

	if ( $quota =~ m/^([+-]?\d+)(,\d{12})?$/ ) {
		$quotapart = $1;
		$timestamp = $2;
	}
	elsif ( $quota =~ m/^([UN])(,\d{12})?$/ ) {
		$quotapart = $1;
		$timestamp = $2;
	}

	if ( defined($1) ) {
		if ( defined($2) ) {
			my $realTimestamp = substr( $timestamp, 1 );

			if ( &validTimestamp($realTimestamp) ) {
				return(1); # Valid quota or adjustment with valid timestamp
			}
		}
		else {
			return(1); # Valid quota or adjustment with no timestamp.
		}
	}
	else {
		return(0); # If no quota was found, this is definitely invalid.
	}	
}


sub writeDataFile {
	# Args: mode, filename, data to write (optional)
	# Result: writes "data to write" to file "filename".
	#   In mode 0, it erases/creates the file in the process of writing to it. If no data to write is given, an empty file is created.
	#   In mode 1, it appends a line to the end of the file. If no data to write is given, this is a no-op.
	# Returns: 1 on success or 0 on failure (for use with "or" statement).

	my ( $writeMode, $outputFile, $dataToWrite ) = @_;

	# If the file does not exist then we cannot append to it, so change to create mode (mode 0).
	if ( ! -e $outputFile ) {
		$writeMode = 0;
	}

	if ( $writeMode == 0 ) {
		open( FH, ">$outputFile" ) or return(0);
	}
	elsif ( $writeMode == 1 ) {
		open( FH, "+>>$outputFile" ) or return(0);
	}
	flock( FH, 2 );

	# The old quota file format consisted of a single line with no newline.
	# If we find one of these in append mode, add a newline first.
	if ( $writeMode == 1 ) {
		seek( FH, 0, 0 );
		my $firstLine = <FH>;

		if ( defined($firstLine) && $firstLine !~ m/\n/ ) { # If there is a line but no newline...
			my $currentFH = select( FH );
			local $| = 1;
			select( $currentFH );

			seek( FH, 0, 2 ); # go to the end of the file...
			print FH "\n"; # and add a newline.
		}
	}

	# Now print out some actual data.
	seek( FH, 0, 2 );
	if ( defined($dataToWrite) ) {
		my $currentFH = select( FH );
		local $| = 1;
		select( $currentFH );

		print FH "$dataToWrite\n";
	}

	flock( FH, 8 );
	close( FH );

	return(1);
}

sub writeLockfile {
	# Args: full path to lockfile, jobID, username, reference to config value hash
	# Returns: 1 on success, 0 on failure. 

	my ( $lockfile, $jobID, $userName, $VARS_Ref ) = @_;

	unless ( defined($jobID) && defined($userName) && length($jobID) > 0 && length($userName) > 0 ) {
		return(0);
	}

	&reportStatus( 3, "Attempting to write \"$jobID,$$,$userName\" to lockfile", $VARS_Ref );

	my $lockfileOpened = 0;
	open( LOCK_FH, "+>$lockfile" ) and $lockfileOpened = 1;

	if ( $lockfileOpened == 1 ) {
		flock( LOCK_FH, 2 );

		my $fileContents = <LOCK_FH>;
		if ( !defined($fileContents) ) {
			my $currentFH = select( LOCK_FH );
			local $| = 1;
			select($currentFH);

			print LOCK_FH "$jobID,$$,$userName";
		}

		flock( LOCK_FH, 8 );
		close( LOCK_FH );

		# Now read from the lockfile which we just wrote to make sure that the desired content is actually present.
		my ( $lockingJob, $lockingPID, $lockingUser ) = &readLockfile( $lockfile, $VARS_Ref );

		# Note: This comparison is not quite the same as the one made by hasPrinter, so we are not using that function.
		if ( $lockingJob == $jobID && $lockingPID == $$ && $lockingUser == $userName ) {
			&reportStatus( 3, "Wrote \"$jobID,$$,$userName\" to lockfile", $VARS_Ref );
			return(1);
		}
		else {
			&reportStatus( 3, "Failed to write lockfile. Expected: \"$jobID,$$,$userName\", Actual:\"$lockingJob,$lockingPID,$lockingUser\"", $VARS_Ref );
			return(0);
		}
	}

	&reportStatus( 3, "Failed to open lockfile.", $VARS_Ref );

	return(0);
}

## End of exported functions
## ###########


## ###########
## Non-exported functions

sub makeBoolean {
	# Args: value to be interepreted
	# Returns: 1 for "true" values, 0 for "false" values, undef for other or undefined values.

	my $candidate = $_[0];

	if ( !defined($candidate) ) {
		return; # Undefined input results in an undefined output.
	}

	if ( $candidate =~ m/^0$/ ) { return(0); }
	if ( $candidate =~ m/^1$/ ) { return(1); }

	$candidate =~ tr/A-Z/a-z/;

	if ( $candidate =~ m/^t$/ || $candidate =~ m/^true$/ || $candidate =~ m/^y$/ || $candidate =~ m/^yes$/ || $candidate =~ m/^on$/ ) {
		return(1);
	}
	if ( $candidate =~ m/^f$/ || $candidate =~ m/^false$/ || $candidate =~ m/^n$/ || $candidate =~ m/^no$/ || $candidate =~ m/^off$/ ) {
		return(0);
	}

	return; # If the input does not match any of the above, it's not a boolean true or false, so return "undefined".
}


sub validTimestamp {
	# Args: timestamp
	# Returns: 1 if timestamp is valid (e.g. every part refers to an actual day, month, etc.), 0 if it is not valid.

	my $timestamp = $_[0];

	if ( !defined($timestamp) || length($timestamp) == 0 ) {
		return(0); # An empty timestamp should not be considered valid.
	}

	my @timeStamp = split(/(\d\d)/,$timestamp); # Splits CCYYMMDDhhmm into _blank_ CC _blank_ YY etc.
	my ( $year, $month, $day, $hour, $minute ) = ( (($timeStamp[1]*100)+$timeStamp[3]), $timeStamp[5], $timeStamp[7], $timeStamp[9], $timeStamp[11] );

	# Check for a valid month value.
	unless ( 1 <= $month && $month <= 12 ) {
		# Month is not between 1 and 12.
		return(0);
	}

	# Check for a valid day value.
	unless ( 1 <= $day && $day <= 31 ) {
		return(0);
	}

	# Check for days in the oddball months.
	if ( $month == 2 ) {
		if ( $day == 31 || $day == 30 ) {
			return(0); # No 31st or 30th day in February
		}
		elsif ( $day == 29 ) {
			if ( $year%4 != 0 ) {
				return(0); # Not a leap year
			}
			elsif ( $year%100 == 0 && $year%400 != 0 ) {
				return(0); # Also not a leap year
			}
		}
	}
	elsif ( $month == 4 || $month == 6 || $month == 9 || $month == 11 ) {
		if ( $day == 31 ) {
			return(0); # No 31st day in April, June, September or November
		}
	}

	# Check for a valid hour value.
	unless ( 0 <= $hour && $hour <= 23 ) {
		# Hour is not between 0 and 23.
		return(0);
	}

	# Check for a valid minute value.
	unless ( 0 <= $minute && $minute <= 59 ) {
		# Minute is not between 0 and 59.
		return(0);
	}

	# If everything is okay, return 1.
	return(1);
}

## End of non-exported functions
## ###########


1;
