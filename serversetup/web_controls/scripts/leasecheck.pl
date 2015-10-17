#!/usr/bin/perl
#
#Sourced from: https://gist.github.com/mattpascoe/4348991

#Get user input
my $userinput;
$userinput=$ARGV[0];

# Update the path to your lease file below
use strict;
use File::Copy;
#use DateTime;
 
#always parse a copy not the live file
#my $leasefile = '/var/lib/dhcpd/dhcpd.leases';
my $leasefile = '/var/lib/dhcp/dhcpd.leases';

my $tempfile  = '/tmp/dhcpd.leases';
copy($leasefile,$tempfile) or die "Copy failed: $!";
 
#my $LocalTZ = DateTime::TimeZone->new( name => 'local' );
my $LocalTZ = '';
 
open LEASES, "< $tempfile" or die $!;
my @lines = <LEASES>;
close LEASES;
 
 
#Get the state of each server
my $readit;
my $line;
#valid failover states
#unknown-state,  partner-down,  normal,  communications-interrupted, resolution-interrupted,  potential-conflict,  recover,   recover-done,   shutdown,   paused, and startup
# seems like I want the last failover statement
 
my $my_state="cant determine";
my $my_state_time="cant determine";
my $peer_state="cant determine";
my $peer_state_time="cant determine";
my $failover = 0;
 
foreach $line (@lines){
        if ($line=~/failover peer .*? state {/){
                $readit = 1;
                $failover = 1;
        }
        if ($readit){
                if ($line=~/my\sstate\s(.*?)\sat\s\d\s(.*?)\;/){
                        $my_state = $1;
                        $my_state_time = $2;
                }
                if ($line=~/partner\sstate\s(.*?)\sat\s\d\s(.*?)\;/){
                        $peer_state = $1;
                        $peer_state_time = $2;
                }
        }
        if ($readit && $line=~/^}/){
                $readit = 0;
        }
}

print "<table class='standard' style='text-align: left;' border='0' cellpadding='2' cellspacing='2'><tbody>\n";

if ($failover){
        $my_state_time = localize($my_state_time);
        my ($mdate, $mtime) = split (/ /,$my_state_time);
        $peer_state_time = localize($peer_state_time);
        my ($pdate, $ptime) = split (/ /,$peer_state_time);
 
        print "<tr><td style='width: 160px;'>Lease State</td><td>$my_state at $mtime on $mdate</td></tr>\n<tr><td>Partner state</td><td>$peer_state at $ptime on $pdate</td></tr>\n";
}
 
#Get the leases and their states
my @lease_states;
my $active = 0;
my $lease = 0;
my $ip;
my $mac='                 ';
my $end_date_time;
my $start_date_time;
my $start_time;
my $start_date;
my $name;
my $state;
 
foreach $line (@lines){
        if ($line=~/lease\s(\d+\.\d+\.\d+\.\d+)/){
                $ip=$1;
                $readit = 1;
                $lease++;
                $name="";
		$mac="";
        }
        if ($readit && $line=~/starts\s\d\s(\d+\/\d+\/\d+\s\d+:\d+:\d+)\;/){
                $start_date_time =$1;
  }
        if ($readit && $line=~/ends\s\d\s(\d+\/\d+\/\d+\s\d+:\d+:\d+)\;/){
                $end_date_time =$1;
#print $start_date_time;
#                $start_date_time = localize($start_date_time);
#                ($start_date, $start_time) = split (/T/,$start_date_time);
 
        }
        if ($readit && $line =~/hardware\sethernet\s(.*?)\;/){
                $mac=$1;
        }
        if ($readit && $line =~/client-hostname\s"(.*?)"\;/){
                $name=$1;
        }
        if ($readit){
                if ($line=~/^\s+binding\sstate\s(.*?)\;/){
                        $state = $1;
                        if ($state eq 'active'){
                                $active++;
                        }
                }
        }
        if ($readit && $line=~/^}/){
		if ($state eq $userinput){
			push (@lease_states,"<tr><td>$ip</td><td>$start_date_time</td><td>$end_date_time</td><td>$mac</td><td>$state</td><td>$name</td></tr>\n");
        		$readit = 0;
			}
        }
}

@lease_states=sort (@lease_states);
my $header=("<table id='myTable' class='tablesorter' style='text-align: left;' border='0' cellpadding='2' cellspacing='2'><thead><tr><th style='width: 120px;'><b>IP</b></th><th style='width: 150px;'><b>Start Time</b></th><th style='width: 150px;'><b>End Time</b></th><th style='width: 140px;'><b>Mac Address</b></th><th style='width: 80px;'><b>State</b></th><th style='width: 210px;'><b>Hostname</b></th></tr></thead><tbody>\n");

print "<tr><td style='width: 160px;'>Total leases</td><td>$lease</td></tr>\n";
print "<tr><td>Total active leases</td><td>$active</td></tr></tbody></table><br>\n";

if (defined $userinput) {
	print $header;
	print @lease_states;
	print "</tbody></table><br>\n";
}

sub localize{
# in format 2010/06/01 22:10:01
my $datetime=shift;
my ($date, $time) = split (/ /,$datetime);
my ($hr, $min, $sec) = split (/:/,$time);
my ($yr, $mo, $day)= split (/\//,$date);
#my $dt = DateTime->new(
#                        year   => $yr,
#                        month  => $mo,
#                        day    => $day,
#                        hour   => $hr,
#                        minute => $min,
#                        second => $sec,
#                        time_zone =>'UTC' );
 
#        $dt->set_time_zone($LocalTZ);
#        return $dt->datetime;
	return $datetime;
 
# use this to split the out
# ($date, $time) = split (/T/,$dt->datetime);
 
}
