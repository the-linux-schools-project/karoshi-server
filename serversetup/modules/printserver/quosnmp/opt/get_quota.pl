#! /usr/bin/perl

# get_quota.pl
# Version 1.8.0 Final
# A web app for querying the user print quotas enforced by quosnmp
#
# Released by Marcus Lauer (marcus.lauer at nyu dot edu)
# Available at http://quosnmp.sourceforge.net
#
# Copyright (C) 2009 by Marcus Lauer (marcus.lauer at nyu dot edu)
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

###########
# IMPORTANT NOTE: There must be some authentication system in place for accessing this 
# script.  The details of that system is your problem. :)  You'll need something which 
# makes your web server authenticate against whatever your printing system authenticates 
# against.  For example, if you use SAMBA and serve this web app via Apache then maybe 
# something which accesses ntlm_auth would do the trick.  I'm using Apache2::AuthenNTLM 
# with a similar setup.  If you authenticate against an Active Directory and use Apache 
# then one of the LDAP or winbind modules might work.

# SET THIS to the path to the config file for your system.
my $CONFIG_FILE = "/etc/quosnmp/quosnmp.conf";


## ###########
## Only experts should modify the code below this line.

# Some modules we need.
use strict;
use warnings;
use Quosnmp qw(getUserPrintQuota getUserPagecount parseConfigFile setDefaultVars);


####
# Define a few variables
my @JOB_BLACKLIST = ();
my %EMAIL_LIST = ();
my %VARS = ();

&setDefaultVars( \%VARS );
$VARS{CONFIG_FILE} = $CONFIG_FILE;
$VARS{DISK_RETRY_PERIOD} = 0;
$VARS{PRINTER} = "";
$VARS{JOB_NUMBER} = "none";
$VARS{QUIET_MODE} = 1;

## MAIN

# Print out the header and body of the page to be returned.
print "Content-type: text/html\n\n";
print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n";
print "<HEAD>\n";
print "<TITLE>Your print quota</TITLE>\n";
print "<STYLE>\n";
print "div.ridgebox { border-color: #CFCFCF; border-width: 3px; border-style: outset; margin: 0px; padding: 10px 20px 10px 20px; display: inline-block; }\n";
print "p.name { text-align: center; font-size: 16pt; color: black; line-height: 16pt; }\n";
print "p.result { text-align: center; font-size: 12pt; color: black; line-height: 16pt; }\n";
print "p.noprint { text-align: center; font-size: 12pt; color: red; line-height: 16pt; }\n";
print "p.unlimited { text-align: center; font-size: 12pt; color: green; line-height: 16pt; }\n";
print "p.tiny { text-align: center; font-size: 9pt; color: black; line-height: 12pt; }\n";
print "body.nice { background-color: white; text-align: center; }\n";
print "</STYLE>\n";
print "</HEAD>\n";
print "<BODY CLASS=\"nice\">\n";

# Get the username of the person who accessed this page
if ( ! defined($ENV{'REMOTE_USER'}) ) {
	# If authentication failed, print an error.
	print "<P>You must enter your Politics username and password to access your print quota.</P></BODY>";
	exit;
}

my $username = $ENV{'REMOTE_USER'};

# Read in the config file.
my $configOK = &parseConfigFile( \%VARS, \@JOB_BLACKLIST, \%EMAIL_LIST );

# Get the current page count.
my $pageCount = &getUserPagecount( $username, \%VARS );

# Get the user print quota (if any).
my $printQuota = &getUserPrintQuota( $username, \%VARS );

# Now print out some sort of response based on the user's quota and pagecount.
print "<DIV CLASS=\"ridgebox\">\n";
print "<P CLASS=\"name\">Your username: $username</P>\n";

if ( $printQuota =~ /^N$/ ) {
	print "<P CLASS=\"noprint\">Apparently you are not allowed to print.</P>\n";
}
elsif ( $printQuota =~ /^U$/ ) {
	print "<P CLASS=\"unlimited\">You have an <STRONG>unlimited</STRONG> quota. Enjoy!\n";
}
else {
	# Calculate the remaining pages if any
	my $pagesLeft = $printQuota - $pageCount;

	if ( $pagesLeft > 0 ) {
		print "<P CLASS=\"result\">You have <STRONG>$pagesLeft</STRONG> pages left in your printing allowance.<BR>Pages printed: $pageCount, quota: $printQuota</P>\n";

		if ( $pageCount < 0 ) {
			print "<P CLASS=\"tiny\">\"Pages printed\" can be negative if a periodic (e.g. monthly) quota is in use.<BR>These \"negative\" pages are ones which rolled over from the previous period.<BR>One you use them up, you will be back to zero pages printed.</P>\n";
		}
	}
	else {
		print "<P CLASS=\"noprint\">You are over quota!<BR>pages printed: $pageCount, quota: $printQuota</P>\n";
	}
}

print "</DIV>\n";
print "</BODY>\n";
