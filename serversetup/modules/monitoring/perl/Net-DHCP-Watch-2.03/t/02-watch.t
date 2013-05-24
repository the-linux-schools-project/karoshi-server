#!/usr/bin/perl

use Test::More tests => 3;

use Net::DHCP::Watch;
use IO::Socket;

use diagnostics;
use strict;

SKIP: {

    my $client = $ENV{'DHCP_CLIENT'} || '127.0.0.1';
    my $server = $ENV{'DHCP_SERVER'} || '127.0.0.1';
    my $ether  = $ENV{'DHCP_ETHER'}  || '00:00:00:00:00:00';
    my $sock;
    skip("No privileged account or dhcp already running.", 3)
	unless ($sock = IO::Socket::INET->new(
 					      PeerAddr  => $server,
 					      PeerPort  => 'bootps(67)',
 					      LocalPort => 'bootpc(68)',
 					      Proto     => 'udp'
 					      ));
    $sock->close;

    my ($dhcpw, $s);
    # 1
    ok( $dhcpw = new Net::DHCP::Watch({
	client => $client,
	server => $server,
	ether  => $ether
	}),
	"Create object");
    # 2
    ok($dhcpw->watch(),
       "Open socket");
    # 3
    
    ok($s = $dhcpw->status(),
       "Bad Status");
}

