#!/usr/bin/perl -w
#
#$Id: watch_dhcp.pl,v 1.11 2002/10/03 12:41:56 edelrio Exp $
#
use strict;
use diagnostics;

use Net::DHCP::Watch;
use Getopt::Long;

# Parameters
my ($Server, $Client, $Ether, $Timeout, $Sleep, $Wait,
    $Start, $Stop, $Copy, $Copyf, @Copy_Files, $Ident,
    $help);

GetOptions(
	   'server:s'     => \$Server,
           'client:s'     => \$Client,
	   'ether:s'      => \$Ether,
	   'timeout:s'    => \$Timeout,
	   'sleep:s'      => \$Sleep,
	   'try:s'        => \$Wait, 
	   'start:s'      => \$Start, 
	   'stop:s'       => \$Stop,
	   'scopy:s'      => \$Copy,
	   'ident:s'      => \$Ident,
	   'files:s'      => \$Copyf,
	   'help!'        => \$help
);

&usage if ($help);
#
# Varibles
#
my $sagent = '/usr/bin/ssh-agent -s'; # secure agent
my $sadd   = '/usr/bin/ssh-add';

#
# default parameters
#
$Server ||= '127.0.0.1'; # server name
# if you are NOT on a UNIX machine
# put ip and ethernet address here
$Client ||= qx[/sbin/ifconfig eth0 | /bin/sed 's/:/ /' | /bin/grep "inet addr" | /bin/awk '{print \$3}' ];
chomp($Client);
$Ether  ||= qx[ /sbin/ifconfig eth0 | /bin/grep HWaddr | /bin/awk '{print \$5}'];
chomp($Ether);

$Timeout ||= 10;                              # network timeout
$Sleep   ||= 300;                             # sleep between checks
$Wait    ||= 4;                               # tries before action
$Start   ||= '/etc/rc.d/init.d/dhcpd start';  # start dhcp server
$Stop    ||= '/etc/rc.d/init.d/dhcpd stop';   # stop  dhcp server
$Copy    ||= '';                              # copy dhcpd conf files
$Ident   ||= '/root/.ssh/dhcp-identity';# SSH identity
$Copyf   ||= '/etc/dhcpd.conf,/var/state/dhcp/dhcpd.leases'; # conf files 
@Copy_Files = split(/[\s,]+/, $Copyf);                       # to copy

#
# Get conf files.
#
if ($Copy) {
    # add identity
    my @agent = qx[ $sagent ];
    foreach my $env ( @agent ) {
	if ($env =~ s/;.*export.*$//) {
	    my ($key,$val) = split(/[\s=]/, $env);
	    $ENV{$key} = $val;
	}
    }

    my $ok = qx[ $sadd $Ident ];
    &copy_conf($Copy, @Copy_Files);
}
#
# Init Monitor
#
my $dhcpw = new Net::DHCP::Watch({
		client  => $Client,
		server  => $Server,
		ether   => $Ether,
		tiemout => $Timeout
	});

# start
# make an infinite loop watching for availability of server,
# with the following rules:
my $stat = $dhcpw->status;
my $local_dhcp = 0;
while (1) {
        # if server is on-line: just sleep (and update conf files?).
	if ( $stat->{Bad} ) { 
	    print 
		$stat->{Time},
		": Remote DHCP on $Server unavailable (",
		$stat->{Bad},
		").\n";
	}

	if ( $stat->{Ok}  ) {
	    print $stat->{Time},
	    ": Remote DHCP on $Server online (".$stat->{Ok}.").\n";
	    &copy_conf($Copy, @Copy_Files) if $Copy && !$local_dhcp;
	}
        #  if server is off-line more than $Wait times: starts local server.
	if ( $stat->{Bad} > $Wait && !$local_dhcp ) {
		my $start_dhcp = qx[ $Start ];
		$local_dhcp = 1;
		print $stat->{Time},": Starting local DHCP daemon\n";
	}

        #  if server is back on-line more than $Wait times: stops local server.
	if ( $stat->{Ok}  > $Wait && $local_dhcp ) {
		my $stop_dhcp  = qx[ $Stop ];
		print $stat->{Time},": Stoping local DHCP daemon\n";
		$local_dhcp = 0;
	}
        # sleep time should be ~ MAX_LEASE_TIME/(number_of_times_to_wait+1)
	sleep($Sleep);
}
continue {
    # we need to stop/start the local server
    if ( $local_dhcp ) {
	my $stop_dhcp = qx[ $Stop ];
    }
    # get status   
    $stat = $dhcpw->status;
    # start
    if ( $local_dhcp ) {
        my $start_dhcp = qx[ $Start ];
    }
}

#
# copy_conf
#
sub copy_conf() {
    my $fserv = shift;
    my @files = @_;
    my $scp    = '/usr/bin/scp -q -p -B';    # secure copy
    foreach my $f ( @files ) {
	my $ok = qx[ $scp $fserv:$f $f ];
    }
}

#
# usage
#
sub usage {
    print 
	"\n$0:\tmonitor a remote DHCP server and launch",
	" a local server when needed.\n\n";
    print
	"Usage: $0 [--server=server] [--ether=ether]\n",
	"\t[--timeout=timeout] [--sleep=sleep] [--wait=wait]\n",
	"\t[--start=start] [--stop=stop]\n",
	"\t[--scopy=scopy_from] [--copy-files=conf,file,list]\n",
	"\t[--ident=ident]";

    print
	"\n",
	" server:  DHCP server name or IP.\n",
	" ether:   Local ethernet address.\n",
	" timeout: Timeout for network operations.\n",
	" sleep:   Interval between monitoring.\n",
	" try:     Number of successive (bad/ok) tries before taking action (start/stop).\n",
	" start:   Command to start the local DHCP daemon.\n",
	" stop:    Command to stop  the local DHCP daemon.\n",
        " copy:    If set, indicates a user\@host to secure-copy DHCP server files from (defaults to false, i.e. do not copy and needs ssh(1) and scp(1)).\n",
	" files:   List of files that need to be copied (defaults: /etc/dhcpd.conf,/var/state/dhcp/dhcpd.leases).\n",
	" ident:   SSH Identity to use with scp (default: \${HOME}/.ssh/dhcp-identity.\n";
    print "\nAll options have reasonable values on a UNIX/Linux machine.\n";
    print
	" Notes:\n", 
	"   .- This script will fail if remote DHCP server contains unresolvable server names in its configuration.\n\n",
      ".- It uses secure shell (ssh and scp) to update configuration files.\n\n",
      ".- The machine that is running the test MUST BE a KNOWN client of the remote DHCP server.\n";

    exit(0);
}

