#
#$Id: Watch.pm,v 2.3 2003/10/28 11:09:59 edelrio Exp $
#
# Net::DHCP::Watch
#
package Net::DHCP::Watch;

use strict;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use Carp;
use Config;
use Socket;
use Net::hostent;
use IO::Socket;

require Exporter;

@ISA       = qw(Exporter);
@EXPORT    = qw();
@EXPORT_OK = qw();

$VERSION = do { my @r=(q$Revision: 2.3 $=~/\d+/g); sprintf "%d."."%02d"x$#r,@r };

#
# new
#
sub new {
    my $proto  = shift;
    my $params = shift; 
    my $class  = ref($proto) || $proto;
    my $self   = {};
    bless($self, $class);
    $self->init($params);
    return $self;
}
#
# init: initalize parameters.
#
sub init {
    my $self   = shift;
    my $params = shift;
    my $h;

    # test if server hostname given is known (name or IP)
    $self->{Server} = $params->{server};
    unless ( $h = gethost($self->{Server}) ) {
	carp "Can not resolve: ",$self->{Server};
    }

    # test if client hostname given is known (name or IP)
    # and keep only the first IP address.
    $self->{Client} = $params->{client};
    unless ( $h = gethost($self->{Client}) ) {
	carp "Can not resolve: ",$self->{Client};
    }
    $self->{Client} = $h->addr_list->[0];


    # test if ethernet address is either an array of six bytes or
    # a string of hex bytes separated by ':'
    $self->{Ether}  = $params->{ether};

    if ( $self->{Ether} =~ m/^([0-9a-f]{1,2}:)+[0-9a-f]{1,2}$/i ) {
	my @eth = map( hex, split(':', $self->{Ether}) );
	$self->{Ether} = \@eth;
    }
    elsif ( scalar($self->{Ether}) != 6 ) {
	croak "Not a good ethernet addres: ",$params->{ether};
    }

    # can we use alarm() ?
    if ( $Config{d_alarm} eq 'define' ) {
	$self->{_Alarm} = 1;
    }
    else {
	carp "No alarm() function, network operation may hang";
	$self->{_Alarm} = 0;
    }

    # set the timeout (alarm)
    $self->{TimeOut} = $params->{timeout} || 10;

    # initialize status result to zero
    $self->{Last} = {
	Ok   => 0,
	Bad  => 0,
	Time => '0000-00-00 00:00:00 GMT'
    };
    return;
}

#
# watch: opens the udp socket to the server
#
sub watch {
    my $self = shift;
    if ( $self->{Watcher} ) {
	carp "Already watching.";
    }
    else {
	$self->{Watcher} = new IO::Socket::INET(
						PeerAddr  => $self->{Server},
						PeerPort  => 'bootps(67)',
						LocalAddr => inet_ntoa($self->{Client}),
						LocalPort => 'bootpc(68)',
						Proto     => 'udp',
						Timeout   => $self->{TimeOut}
						)
	    or carp "Can not watch: $!";
    }
    return $self->{Watcher};
}

#
# status: returns the present status
#
sub status {
    my $self = shift;
    # now the watch/unwatch cycle is carried by status.
    $self->watch unless( $self->{Watcher} );
    $self->dhcp_query or return;
    $self->unwatch;
    return $self->{Last};
}

#
# dhcp_query: sends an udp packet containig a DHCP message 
# of type DHCPDISCOVER and listens to the reply. The random transaction id
# must match.
#
sub dhcp_query {
    my $self = shift;
    my $reply; # holdspace for udp reply
    #
    # Test if socket is ok
    #
    unless ( $self->{Watcher} ) {
	carp "Not watching yet!";
	return;
    };
    #
    # Transaction ID
    #
    my $xid = int(rand(2**32-1));
    #
    # DHCP Message: Fixed-Format + Options 
    # (see Droms & Lemon, 1999, Apendixes C and D).
    #
    my @fields = (
                  # op
		  1,
                  # htype
		  1,
                  # hlen
		  6,
                  # hops
		  0,
                  # xid
		  $xid,
                  # secs
		  0,
                  # flags
		  0,
                  # ciaddr
		  $self->{Client},
                  # yiaddr
		  0,
                  # siaddr
		  0,
                  # giaddr
		  0,
                  # chaddr
		  @{ $self->{Ether} },
		  0,  0,  0,  0,  0,  0, 
		  0,  0,  0,  0,
                  # sname
		  "\0",
                  # file
		  "\0",
                  # Magic cookie (RFC)
		  99,130,83,99,
                  # option1 = DHCP-Message
		  53,
                  # length1 = 1
		  1,
                  # value1  = DHCPREQUEST
		  3
		  );
    my $query = pack(
		     # It's horrible, but it works
		     'CCCCNnna4NNNCCCCCCCCCCCCCCCCa64a128C*',
		     @fields
		     );
    my $serv_address;
    # I/O eval block
    eval {
	# SIG handling for alarm()
	local $SIG{ALRM} = sub { die "Alarm timeout\n" };
	# Send query
	alarm($self->{TimeOut})
	    if $self->{_Alarm}; 
	$self->{Watcher}->send($query, 0);
	alarm(0)
	    if $self->{_Alarm};
	# Get reply
	alarm($self->{TimeOut})
	    if $self->{_Alarm};
	$serv_address = $self->{Watcher}->recv($reply, 1024,  0);
	alarm(0)
	    if $self->{_Alarm};
    };
    # Die if not alarm
    if($@) {
	carp $@ unless $@ =~ /alarm/i;
    }
    # Verify
    # be sure $ret_xid is not equal to $xid
    my $ret_xid = !$xid;
    if ( $reply ) {
	$ret_xid = unpack('x4N',$reply);
    }
    # only if we've got a reply and the reply was correct all is ok.
    if ( $ret_xid == $xid ) {
	# Increment Ok count (max: 2**31-1)
	$self->{Last}->{Ok} %= 2147483647;
	$self->{Last}->{Ok}++;
	# Zero Bad
	$self->{Last}->{Bad} = 0;
    }
    else {
	# Zero ok
	$self->{Last}->{Ok} = 0;
	# Increment Bad count (max: 2**31-1)
	$self->{Last}->{Bad} %= 2147483647;
	$self->{Last}->{Bad}++;
    }
    # Get present time (GMT)
    $self->{Last}->{Time} = gmtime;
}
#
# close: just closes socket.
#
sub unwatch {
    my $self = shift;
    delete $self->{Watcher};
}
#
# Cleanup
# 
sub DESTROY {
    my $self = shift;
    $self->unwatch;
}

1;
__END__

=head1 NAME

Net::DHCP::Watch - A class for monitoring a remote DHCPD server.

=head1 SYNOPSIS


  use Net::DHCP::Watch;
  # server name
  my $Server = 'dhcpd.mydomain.com';
  # this machine ip and ethernet address
  my $IP     = '192.168.1.1';
  my $Ether  = '01:23:45:67:89:ab';
  # Net::DHCP::Watch object
  my $dhcpw = new Net::DHCP::Watch({
		server => $Server,
                client => $IP,
		ether  => $Ether
	});

  # Open network
  $dhcpw->watch();
  # Get status
  my $stat = $dhcpw->status;
  # print results
  if ( $stat->{Bad} ) print $stat->{Time},
    ": Remote DHCP on $Server unavailable (",$stat->{Bad},").\n";

  if ( $stat->{Ok}  ) print $stat->{Time},
    ": Remote DHCP on $Server online.\n";

=head1 DESCRIPTION

Net::DHCP::Watch is a module to help monitor remote DHCP servers. It
opens an udp socket to send and receive responses to and from a DHCP
server. It stores the last connection status information.

This module serves to implement This module can help to write some
simple code to implement a reliable DHCP service over complex or
simple networks.


=head1 METHODS

=over 4

=item B<new> 

Creates a new Net::DHCP::Watch object. The parameters are passed
through a hash with the following keys:

=over 4

=item I<Server>

DHCP server name or IP address to be monitored (not the local machine
performing the monitoring).

=item I<Client>

Name or IP addres to use for the local machine performing the
monitoring. Since there is no obvious way to determine that, it is
mandatory.

=item I<Ether>

Ethernet address of the local machine performing the monitoring. Since
there is no obvious way to determine that, it is mandatory. You can
pass a 6 element array of bytes or a ':' separated string of hex
values. In UNIX machines you can tipically do something like this:

	my $ether = qx[ /sbin/ifconfig eth0 | tail +1 |\
			head -1 | awk '{print \$5}'];
	chomp($ether);

=item I<Timeout>

The timeout for network operation (default 10s).

=back

=item B<watch>

Prepares for monitoring. Opens an UDP socket to the server. This
method could fail or interfere with the operation of a local DHCPd
server.

=item B<unwatch>

Closes monitoring. You should use this method before starting any local 
DHCP server.

=item B<status>

Try to comunicate with the server and returns the status in a hash. The
hash contains three keywords. I<Ok> will be true if the attempt completed
successfully, I<Bad> will be true if the attempt was not; they will
contain the number of successful (or unsuccessful) contiguous attempts
made. I<Time> contains the GMT time string of the last attempt.

=back

=head1 EXAMPLES

See the directory F<examples> in source distribution for an example.

=head1 BUGS

There should be a Net::DHCP class to handle the DHCP protocol.

=head1 LIMITATIONS

On platforms without I<alarm()> function defined the monitoring can
hang forever if some network problems show up (cable problem, etc)?

The machine that is running the test MUST BE a KNOWN client of the
remote DHCP server.

=head1 AUTHOR

Evilio del Rio, edelrio@icm.csic.es

=head1 ACKNOWLEDGEMENTS

I would like to acknowledge the valuable contributions of the people
who made suggestions to improve this code, specially to Nick Garfield
who provided the solution for monitoring disjoint networks.

=head1 SEE ALSO

L<perl(1)>, L<IO::Socket(3)>, L<Net::hostent(3)>. RFCs 2131 and 2132.

I<Ralph Droms & Ted Lemon>, B<The DHCP Handbook>, MacMillan
(Indianapolis), 1999.

=cut
