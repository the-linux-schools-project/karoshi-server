#! /usr/bin/perl

# quosnmplibtest.pl
# Version 1.8.5 Final
# A little developer tool which tests various functions in Quosnmp.pm.

use strict;
use warnings;

use File::Temp qw(tempfile);
use File::stat;
use Quosnmp qw(checkTimestampExpiration getUserPrintQuota getUserPagecount parseConfigFile readLockfile readQuotaFile reportStatus setDefaultVars touchLockfile updateUserPagecount validQuota writeDataFile writeLockfile);

my %VARS = (
	CONFIG_FILE => "",
	PAGE_LOG => 1,
	PAGE_LOG_FILE => "/tmp/tempfile",
	ERROR_LOG => 1,
	ERROR_LOG_FILE => "/tmp/tempfile",
	DEBUG_LEVEL => 3,
	ACCOUNTING_DIRECTORY => "/tmp",
	QUOTA_DIRECTORY => "/tmp",
	DISK_RETRY_PERIOD => 0,
	QUIET_MODE => 1,
	JOB_NUMBER => 0,
	PRINTER => "none",
	LOCKFILE => "/tmp/quosnmp.lockfile"
);

###############
##

# Run these tests for now (others are presumably incomplete)
print STDOUT "\n"; # Purely for formatting.

&TESTsetDefaultVars;
&TESTparseConfigFile;
&TESTcheckTimestampExpiration;
&TESTvalidQuota;
&TESTreadQuotaFile;
&TESTgetUserPrintQuota;
&TESTgetUserPagecount;
&TESTwriteDataFile;
&TESTupdateUserPagecount;
&TESTreadLockfile;
&TESTwriteLockfile;
&TESTtouchLockfile;
&TESTreportStatus;

print STDOUT "\n"; # Purely for formatting.

###############
###############

# Test "checkTimestampExpiration"
sub TESTcheckTimestampExpiration {
	print STDOUT "checkTimestampExpiration... ";

	my @timestampValues = ( "209001010000", "200001010000", "200801010000", "201001000000", "201000010000", "209001010101", "201001011999", "201013010000", "201002300000", "209002290000", "201202290000", "200002290000", "209004310000", "" );
	my @timestampExpired = ( 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0 );

	for ( my $counter = 0; $counter <= $#timestampValues; $counter++ ) {
		my $eachTimestamp = $timestampValues[$counter];
		my $result = &checkTimestampExpiration($eachTimestamp);

		if ( $result != $timestampExpired[$counter] ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected: $timestampExpired[$counter], Got: $result\n";
			return();
		}
	#	print STDOUT "Timestamp: \"$eachTimestamp\", Calculated Result: $result, Correct Result: $timestampExpired[$counter]\n";
	}

	print STDOUT "Passed\n";
}


# Test "getUserPrintQuota"
sub TESTgetUserPrintQuota {
	print STDOUT "getUserPrintQuota... ";

	my @quotaFiles = ( "no file", "200", "+200", "-200", "2000", "+2000", "1000\n+200", "400\n+200", "1000\n+200\n-200,200001010000\n-50" );
	my @correctQuota = ( 500, 200, 700, 300, 2000, 2500, 1200, 600, 1150 );

	# Create a default quota file in /tmp
	open ( FH, ">/tmp/print_quota" );
	print FH "500\n";
	close ( FH );

	# Create one user quota file at a time.
	for ( my $counter = 0; $counter <= $#quotaFiles; $counter++ ) {
		if ( $counter > 0 ) { # counter=0 is the case where there is no user quota.
			open ( FH, ">/tmp/testuser_user_quota" );
			print FH "$quotaFiles[$counter]\n";
			close ( FH );
		}

		my $result = &getUserPrintQuota("testuser",\%VARS);

		if ( $counter > 0 ) {
			unlink ( "/tmp/testuser_user_quota" );
		}

		if ( $result !~ /^$correctQuota[$counter]$/ ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected: $correctQuota[$counter], Got: $result\n";
			unlink ( "/tmp/print_quota" );
			return();
		}
	}

	unlink ( "/tmp/print_quota" );
	print STDOUT "Passed\n";
}


# Test "getUserPagecount"
sub TESTgetUserPagecount {
	print STDOUT "getUserPagecount... ";

	my @accountingFiles = ( "no file", "200", "500", "700", "111111", "-66" );
	my @correctAccounting = ( 0, 200, 500, 700, 111111, -66 );

	for ( my $counter = 0; $counter <= $#accountingFiles; $counter++ ) {
		# Create one user accounting file at a time.
		if ( $counter > 0 ) { # counter=0 is the no file found condition.
			open ( FH, ">/tmp/testuser" );
			print FH "$accountingFiles[$counter]\n";
			close ( FH );
		}

		my $result = &getUserPagecount("testuser",\%VARS);

		if ( $counter > 0 ) {
			unlink ( "/tmp/testuser" );
		}

		if ( $result !~ /^$correctAccounting[$counter]$/ ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected: $correctAccounting[$counter], Got: $result\n";
			return();
		}
	}

	print STDOUT "Passed\n";
}


# Test "parseConfigFile"
sub TESTparseConfigFile {
	print STDOUT "parseConfigFile... ";

	my %PCFVARS = (
		CONFIG_FILE => "/tmp/quosnmp.conf",
		ENFORCE_QUOTA => 1,
		SAVE_JOBS => 1,
		HEADER_DISCOUNT => 1,
		PRINT_ON_LOW_TONER => 1,
		PAGE_LOG => 1,
		PAGE_LOG_FILE => "1",
		ERROR_LOG => 1,
		ERROR_LOG_FILE => "1",
		DEBUG_LEVEL => 1,
		PAGE_MULTIPLIER => 1,
		OVER_QUOTA_NOTIFY => 1,
		SMTP_SERVER => "1",
		OVER_QUOTA_EMAIL_MESSAGE => "1",
		BACKEND_DIRECTORY => "1",
		BINARY_DIRECTORY => "1",
		ACCOUNTING_DIRECTORY => "1",
		QUOTA_DIRECTORY => "1",
		PAGECOUNT_QUERY_METHOD => 1,
		STATUS_QUERY_METHOD => 1,
		BACKEND_RETRIES => 1,
		HARD_STALL_TIMEOUT => 1,
		SOFT_STALL_TIMEOUT => 1,
		SNMP_COMMUNITY => "1",
		TCP_QUERY_PORT => 1,
		HP_ADVANCED_STATUS => 1,
		LOCK_PRINTER => 1,
		NETWORK_POLLING_PERIOD => 1,
		DISK_RETRY_PERIOD => 1
	);
	my @JOB_BLACKLIST = ();
	my %EMAIL_LIST = ();

	# Create a config file which will add some value or other to all of these variables.
	open( FH, ">/tmp/quosnmp.conf" );
	print FH "ENFORCE_QUOTA = 0\nSAVE_JOBS = 0\nHEADER_DISCOUNT = 0\nPRINT_ON_LOW_TONER = 0\nPAGE_LOG = 0\nPAGE_LOG_FILE = /tmp/quosnmp.conf\nERROR_LOG = 0\nERROR_LOG_FILE = /tmp/quosnmp.conf\nDEBUG_LEVEL = 0\nPAGE_MULTIPLIER = 0\nOVER_QUOTA_NOTIFY = 0\nSMTP_SERVER = 0\nOVER_QUOTA_EMAIL_MESSAGE = 0\nBACKEND_DIRECTORY = /tmp\nBINARY_DIRECTORY = /tmp\nACCOUNTING_DIRECTORY = /tmp\nQUOTA_DIRECTORY = /tmp\nPAGECOUNT_QUERY_METHOD = 0\nSTATUS_QUERY_METHOD = 0\nBACKEND_RETRIES = 0\nHARD_STALL_TIMEOUT = 0\nSOFT_STALL_TIMEOUT = 0\nSNMP_COMMUNITY = 0\nTCP_QUERY_PORT = 0\nHP_ADVANCED_STATUS = 0\nLOCK_PRINTER = 0\nNETWORK_POLLING_PERIOD = 0\nDISK_RETRY_PERIOD = 0\nJOB_BLACKLIST = Bad,Worse\n[EMAIL_LIST]\ntest1:testing1\@example.com\ntest2:testing2\@example.com";
	close( FH );

	my $configOK = &parseConfigFile( \%PCFVARS, \@JOB_BLACKLIST, \%EMAIL_LIST );

	unlink("/tmp/quosnmp.conf");

	foreach my $key ( keys %PCFVARS ) {
		unless ( $PCFVARS{$key} =~ /^0$/ || $PCFVARS{$key} =~ /^\/tmp$/ || $PCFVARS{$key} =~ /^\/tmp\/quosnmp.conf$/ ) {
			print STDOUT "Failed on key $key\n";
			return();
		}
	}

	unless ( $#JOB_BLACKLIST == 1 && $JOB_BLACKLIST[0] =~ /^Bad$/ && $JOB_BLACKLIST[1] =~ /^Worse$/ ) {
		print STDOUT "Failed on job blacklist\n";
		print STDOUT "Item 1: $JOB_BLACKLIST[0], Expected: Bad\n";
		print STDOUT "Item 2: $JOB_BLACKLIST[1], Expected: Worse\n";
		return();
	}

	unless ( $EMAIL_LIST{test1} =~ /^testing1\@example.com$/ && $EMAIL_LIST{test2} =~ /^testing2\@example.com$/ ) {
		print STDOUT "Failed on e-mail list\n";
		print STDOUT "Item 1: $EMAIL_LIST{test1}, Expected: testing1\@example.com\n";
		print STDOUT "Item 2: $EMAIL_LIST{test2}, Expected: testing2\@example.com\n";
		return();
	}

	if ( $configOK == 0 ) {
		print STDOUT "Failed on overall config\n";
		return();
	}

	print STDOUT "Passed\n";
}


# Test "readLockfile"
sub TESTreadLockfile {
	print STDOUT "readLockfile... ";

	my @lockFiles = ( "no file", "1,test1", "723,username", "16,Mr. T" );
	my @jobIDs = ( "", 1, 723, 16 );
	my @userNames = ( "", "test1", "username", "Mr. T" );

	for ( my $counter = 0; $counter <= $#lockFiles; $counter++ ) {
		my $tempFileHandle;
		my $tempLockFile;

		if ( $counter > 0 ) {
			($tempFileHandle, $tempLockFile) = &tempfile(DIR => "/tmp");

			open( $tempFileHandle, ">$tempLockFile" );
			print $tempFileHandle "$lockFiles[$counter]";
			close( $tempFileHandle );
		}

		my ( $lockingJob, $lockingUser ) = &readLockfile($tempLockFile);

		if ( $counter > 0 ) {
			unlink($tempLockFile);
		}

		if ( $counter == 0 ) {
			if ( defined($lockingJob) || defined($lockingUser) ) {
				print STDOUT "Failed on item $counter\n";
				print STDOUT "Expected job: none, Got: $lockingJob\n";
				print STDOUT "Expected user: none, Got: $lockingUser\n";
				return();
			}
		}
		elsif ( $lockingJob !~ /^$jobIDs[$counter]$/ || $lockingUser !~ /^$userNames[$counter]$/ ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected job: $jobIDs[$counter], Got: $lockingJob\n";
			print STDOUT "Expected user: $userNames[$counter], Got: $lockingUser\n";
			return();
		}
	}

	print STDOUT "Passed\n";
}


# Test "readQuotaFile"
sub TESTreadQuotaFile {
	print STDOUT "readQuotaFile... ";

	my @quotaFiles = ( "no file", "200", "+200", "1000\n+200", "1000\n+200\n-200,200001010000\n-50" );
	my @correctQuota = ( undef, 200, 200, 1200, 1150 );

	for ( my $counter = 0; $counter <= $#quotaFiles; $counter++ ) {
		my $tempFileHandle;
		my $tempQuotaFile;

		if ( $counter > 0 ) {
			($tempFileHandle, $tempQuotaFile) = &tempfile(DIR => "/tmp");

			open( $tempFileHandle, ">$tempQuotaFile" );
			print $tempFileHandle "$quotaFiles[$counter]";
			close( $tempFileHandle );
		}

		my @resultArray = &readQuotaFile( $tempQuotaFile, \%VARS );
		my $result;
		if ( defined($resultArray[0]) && defined($resultArray[1]) ) {
			$result = $resultArray[0] + $resultArray[1];
		}
		elsif ( defined($resultArray[1]) ) {
			$result = 0 + $resultArray[1];
		}
		else {
			$result = $resultArray[0];
		}

		if ( $counter > 0 ) {
			unlink ( $tempQuotaFile );
		}

		if ( $counter == 0 ) {
			if ( defined($result) ) {
				print STDOUT "Failed on item $counter\n";
				print STDOUT "Expected: $correctQuota[$counter], Got: $result\n";
				return();
			}
		}
		elsif ( $result !~ /^$correctQuota[$counter]$/ ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected: $correctQuota[$counter], Got: $result\n";
			return();
		}
	}

	print STDOUT "Passed\n";
}


# Test "reportStatus"
sub TESTreportStatus {
	print STDOUT "reportStatus... ";

	$VARS{QUIET_MODE} = 0;

	my @statusTexts = ( "Testing 1 2 3", "Houston, we have a problem", "This is a test. This is only a test" );

	for ( my $counter = 0; $counter <= $#statusTexts; $counter++ ) {
		&reportStatus( 3, $statusTexts[$counter], \%VARS );

		open( FH, "/tmp/tempfile" );
		my @content = <FH>;
		close( FH );

		unlink( "/tmp/tempfile" );

		my $contentString = join( "", @content );
		chomp( $contentString );

		my @theTime = localtime();
		my $expectedString = sprintf( "%04d-%02d-%02d\t%02d:%02d:%02d\t0\tnone\tDEBUG: %s", $theTime[5]+1900, $theTime[4]+1, $theTime[3], $theTime[2], $theTime[1], $theTime[0], $statusTexts[$counter] );

		if ( $contentString !~ /^$expectedString$/m ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected: $expectedString, Got: $contentString\n";
			return();
		}
	}

	print STDOUT "Passed\n";

	$VARS{QUIET_MODE} = 1;
}


sub TESTsetDefaultVars {
	print STDOUT "setDefaultVars... ";

	my %REALVAR = (
		ENFORCE_QUOTA => 1,
		SAVE_JOBS => 0,
		HEADER_DISCOUNT => 0,
		PRINT_ON_LOW_TONER => 1,
		PAGE_LOG => 1,
		PAGE_LOG_FILE => "/var/log/cups/quosnmp_page_log",
		ERROR_LOG => 1,
		ERROR_LOG_FILE => "/var/log/cups/quosnmp_error_log",
		DEBUG_LEVEL => 1,
		PAGE_MULTIPLIER => 1,
		OVER_QUOTA_NOTIFY => 0,
		SMTP_SERVER => "smtp.example.com",
		OVER_QUOTA_EMAIL_MESSAGE => "You have exceeded your print quota.\n",
		BACKEND_DIRECTORY => "/usr/lib/cups/backend",
		BINARY_DIRECTORY => "/usr/bin",
		ACCOUNTING_DIRECTORY => "/var/log/cups/accounting",
		QUOTA_DIRECTORY => "/var/log/cups/quotas",
		PAGECOUNT_QUERY_METHOD => 0,
		STATUS_QUERY_METHOD => 0,
		BACKEND_RETRIES => 0,
		HARD_STALL_TIMEOUT => 7200,
		SOFT_STALL_TIMEOUT => 600,
		SNMP_COMMUNITY => "public",
		TCP_QUERY_PORT => 9100,
		HP_ADVANCED_STATUS => 0,
		LOCK_PRINTER => 1,
		UPDATE_LOCKFILE_TIMESTAMP => 0,
		MONITOR_PAGECOUNT => 1,
		NETWORK_POLLING_PERIOD => 2,
		DISK_RETRY_PERIOD => 3
	);
	my %TESTVAR = ();

	&setDefaultVars( \%TESTVAR );

	while ( my ( $key, $value ) = each( %TESTVAR ) ) {
		if ( $REALVAR{$key} !~ /$value/ ) {
			print STDOUT "Failed on key $key\n";
			return();
		}
	}

	print STDOUT "Passed\n";
}


# Test "updateUserPagecount"
sub TESTupdateUserPagecount {
	print STDOUT "updateUserPagecount... ";

	my @accountingFiles = ( "no file", "no file", "200", "500", "700", "111111", "-66", "521", "77" );
	my @accountingAddition = ( "no file", 60, "200", "352", "3", "913456", "17", "-21", "0" );
	my @correctAccounting = ( 0, 60, 400, 852, 703, 1024567, -49, 500, 77 );

	for ( my $counter = 0; $counter <= $#accountingFiles; $counter++ ) {
		# Create one user accounting file at a time.
		if ( $counter > 1 ) { # counter=0 or 1 are the no file found conditions.
			open ( FH, ">/tmp/testuser" );
			print FH "$accountingFiles[$counter]\n";
			close ( FH );
		}

		my $worked = &updateUserPagecount("testuser",$accountingAddition[$counter],\%VARS);

		# Read the resulting file.
		my $result;
		if ( $counter > 0 ) {
			open ( FH, "/tmp/testuser" );
			$result = <FH>;
			close ( FH );
			unlink ( "/tmp/testuser" );
		}

		if ( $counter == 0 ) {
			# Don't test the page count update.
		}
		elsif ( $result !~ /^$correctAccounting[$counter]$/ ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected: $correctAccounting[$counter], Got: $result\n";
			return();
		}

		if ( $counter == 0 ) {
			if ( $worked == 1 ) {
				print STDOUT "Failed on item $counter\n";
				print STDOUT "updateUserPagecount reported success, but in this case it should fail!\n";
				return();
			}
		}
		elsif ( $worked == 0 ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Unknown error reported by updateUserPagecount\n";
			return();
		}
	}

	print STDOUT "Passed\n";
}


# Test "validQuota"
sub TESTvalidQuota {
	print STDOUT "validQuota... ";

	my @quotaValues = ( "200", "+100", "-300", "000", "cat", "+cat", "-dog", "100,200901010000", "+200,200901010000", "-300,200901010000", "100,20090101000", "100,2009010100000", "200,200900010000" );
	my @quotaValid = ( 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0 );

	for ( my $counter = 0; $counter <= $#quotaValues; $counter++ ) {
		my $eachQuota = $quotaValues[$counter];
		my $result = &validQuota($eachQuota);

		if ( $result != $quotaValid[$counter] ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected: $quotaValid[$counter], Got: $result\n";
			return();
		}
	#	print STDOUT "Quota: \"$eachQuota\", Calculated Result: $result, Correct Result: $quotaValid[$counter]\n";
	}

	print STDOUT "Passed\n";
}


# Test "writeDataFile"
sub TESTwriteDataFile {
	print STDOUT "writeDataFile... ";

	my @modes = ( 0, 0, 1, 1, 1, 1 );
	my @data = ( "500", "333", "200", "700,200901010000", "+50", "-200,200902020000" );
	# Plus signs need to be escaped.
	my @expectedResult = ( "500", "333", "200", "200\n700,200901010000", "200\n700,200901010000\n\\+50", "200\n700,200901010000\n\\+50\n-200,200902020000" );

	for ( my $counter = 0; $counter <= $#data; $counter++ ) {
		my $succeeded = &writeDataFile( $modes[$counter], "/tmp/tempfile", $data[$counter] );

		open( FH, "/tmp/tempfile" );
		my @result = <FH>;
		close( FH );

		if ( $modes[$counter] == 0 ) {
			unlink("/tmp/tempfile");
		}

		my $flattenedresult = join( "", @result );
		chomp($flattenedresult);

		if ( $flattenedresult !~ /^$expectedResult[$counter]$/m ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected: \"$expectedResult[$counter]\", Got: \"$flattenedresult\"\n";
			return();
		}

		if ( $succeeded == 0 ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Unknown error reported by updateUserPagecount\n";
			return();
		}
	}

	if ( -e "/tmp/tempfile" ) {
		unlink("/tmp/tempfile");
	}

	print STDOUT "Passed\n";
}


# Test "writeLockfile"
sub TESTwriteLockfile {
	print STDOUT "writeLockfile... ";

	my @jobIDs = ( "", 1, 723, 16 );
	my @userNames = ( "", "test1", "username", "Mr. T" );
	my @lockFiles = ( "no file", "1,$$,test1", "723,$$,username", "16,$$,Mr. T" );

	for ( my $counter = 0; $counter <= $#lockFiles; $counter++ ) {
		my ( $tempFileHandle, $tempLockFile ) = &tempfile(DIR => "/tmp");

		my $succeeded = &writeLockfile( $tempLockFile, $jobIDs[$counter], $userNames[$counter], \%VARS );

		# Read back in what was written.
		my $result;
		if ( $counter > 0 ) {
			open( FH, "$tempLockFile" );
			$result = <FH>;
			close( FH );
		}

		unlink($tempLockFile);

		if ( $counter == 0 ) {
			if ( $succeeded == 1 ) {
				print STDOUT "Failed on item $counter\n";
				print STDOUT "writeLockfile reported success, but in this case it should fail!\n";
				return();
			}
		}
		elsif ( $result !~ /^$lockFiles[$counter]$/ ) {
			print STDOUT "Failed on item $counter\n";
			print STDOUT "Expected: \"$jobIDs[$counter],$$,$userNames[$counter]\", Got: \"$result\"\n";
			return();
		}
	}

	print STDOUT "Passed\n";
}

# Test "touchLockfile"
sub TESTtouchLockfile {
	print STDOUT "touchLockfile";

	# Make sure these are both enabled.
	my $originalULT = $VARS{UPDATE_LOCKFILE_TIMESTAMP};
	my $originalLP = $VARS{LOCK_PRINTER};

	$VARS{UPDATE_LOCKFILE_TIMESTAMP} = 1;
	$VARS{LOCK_PRINTER} = 1;

	my $madelockfile = &writeLockfile( $VARS{LOCKFILE}, 1, "temp", \%VARS );
 
	if ( $madelockfile != 1 ) {
		print STDOUT "Unable to create lockfile, could not test touchLockFile.\n";
		return();
	}
	else {
		$| = 1;
		for ( my $counter = 0; $counter < 3; $counter++ ) {
			sleep(1);
			print STDOUT ".";
		}
		print STDOUT " ";
		$| = 0;

		my $succeeded = &touchLockfile( \%VARS );
		my $currentTime = time();
		my $lockfileEndTime = stat($VARS{LOCKFILE})->mtime;

		unlink( $VARS{LOCKFILE} );

		if ( $succeeded != 1 || $lockfileEndTime < $currentTime ) {
			print STDOUT "Failed to touch lockfile\n";
			print STDOUT "  Expected modification time: \"$currentTime\", Got: \"$lockfileEndTime\"\n";
			return();
		}
	}

	$VARS{UPDATE_LOCKFILE_TIMESTAMP} = $originalULT;
	$VARS{LOCK_PRINTER} = $originalLP;

	print STDOUT "Passed\n";
}
