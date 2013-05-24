#!/bin/sh
#
# start/stop portmap daemon.

### BEGIN INIT INFO
# Provides:          portmap
# Required-Start:    $network $local_fs
# Required-Stop:     $network $local_fs
# Default-Start:     S 2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: The RPC portmapper
# Description:       Portmap is a server that converts RPC (Remote
#                    Procedure Call) program numbers into DARPA
#                    protocol port numbers. It must be running in
#                    order to make RPC calls. Services that use
#                    RPC include NFS and NIS.
### END INIT INFO

test -f /sbin/portmap || exit 0

. /lib/lsb/init-functions

OPTIONS=""
if [ -f /etc/default/portmap ]; then
  . /etc/default/portmap
elif [ -f /etc/portmap.conf ]; then
  . /etc/portmap.conf
fi

case "$1" in
    start)
	log_begin_msg "Starting portmap daemon..."
	pid=$( pidofproc -p /var/run/portmap.pid /sbin/portmap )
	if [ -n "$pid" ] ; then
	      log_begin_msg "Already running."
	      log_end_msg 0
	      exit 0
	fi
	start-stop-daemon --start --quiet --oknodo --exec /sbin/portmap -- $OPTIONS
	log_end_msg $?

	if [ -f /var/run/portmap.upgrade-state ]; then
	  log_begin_msg "Restoring old RPC service information..."
	  sleep 1 # needs a short pause or pmap_set won't work. :(
	  pmap_set </var/run/portmap.upgrade-state
	  log_end_msg $?
	  rm -f /var/run/portmap.upgrade-state
	else
	  if [ -f /var/run/portmap.state ]; then
	    sleep 1 # needs a short pause or pmap_set won't work. :(
	    pmap_set </var/run/portmap.state
	    rm -f /var/run/portmap.state
	  fi
	fi

	mkdir -p /lib/init/rw/sendsigs.omit.d
	rm -f /lib/init/rw/sendsigs.omit.d/portmap
	ln -s /var/run/portmap.pid /lib/init/rw/sendsigs.omit.d/portmap

	;;
    stop)
	log_begin_msg "Stopping portmap daemon..."
	pmap_dump >/var/run/portmap.state
	start-stop-daemon --stop --quiet --oknodo --exec /sbin/portmap
	log_end_msg $?
	;;
    force-reload)
	$0 restart
	;;
    restart)
	$0 stop
	$0 start
	;;
    status)
	status_of_proc -p /var/run/portmap.pid /sbin/portmap portmap && exit 0 || exit $?
	;;
    *)
	log_success_msg "Usage: /etc/init.d/portmap {start|stop|force-reload|restart|status}"
	exit 1
	;;
esac

exit 0

