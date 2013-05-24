#!/bin/sh
#
# watch_dhcpd   This shell script takes care of starting and stopping
#               dhcpd if needed.
#
# chkconfig: - 64 36
# description: dhcpd provide access to Dynamic Host Control Protocol.
#
WDHCP=watch_dhcp
SERVER=dragui
IDENT="operator@${SERVER}"
TRY=3
SLEEP=300


# Source function library.
. /etc/rc.d/init.d/functions

# Source networking configuration.
. /etc/sysconfig/network

# Check that networking is up.
[ ${NETWORKING} = "no" ] && exit 0

[ -f /usr/sbin/dhcpd ] || exit 0
[ -f /etc/dhcpd.conf ] || exit 0

RETVAL=0

# See how we were called.
case "$1" in
  start)
	# Start daemons.
	echo -n "Starting watch_dhcpd: "
	/usr/local/sbin/${WDHCP}.pl --server=${SERVER} --try=${TRY} --sleep=${SLEEP} --scopy=${IDENT} --files=/etc/dhcpd.conf,/etc/dhcpd.master,/var/state/dhcp/dhcpd.leases > /var/log/${WDHCP} 2>&1 &
	RETVAL=$?
	[ $RETVAL -eq 0 ] && success
	echo
	[ $RETVAL -eq 0 ] && touch /var/lock/subsys/${WDHCP}
	;;
  stop)
	# Stop daemons.
	echo -n "Shutting down watch_dhcpd: "
	killproc ${WDHCP}.pl
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/${WDHCP}
	;;
  restart|reload)
	$0 stop
	$0 start
	RETVAL=$?
	;;
  status)
	status ${WDHCP}.pl
	RETVAL=$?
	;;
  *)
	echo "Usage: ${WDHCP} {start|stop|restart|status}"
	exit 1
esac

exit $RETVAL

