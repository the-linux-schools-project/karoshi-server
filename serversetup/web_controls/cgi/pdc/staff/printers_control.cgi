#!/bin/bash
#Copyright (C) 2007 paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

#Language
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css

TITLE="Manage Print Queues"
HTTPS_ERROR="You must access this page via https."
ACCESS_ERROR1="You must be a Karoshi Management User to complete this action."
ERRORMSG6="Your username cannot be blank."
ERRORMSG7="Your password cannot be blank."
ERRORMSG10="Authentication failure."
DELETEPRINTMSG="Deleting print job"
CLEARQUEUEMSG="Clearing the printer queue."
ENABLEMSG="Enabling the printer queue."
DISABLEMSG="Disabling the printer queue."
TESTMSG="Testing the printer queue."

SLEEPTIME=5

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/staff/printers.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
echo "Content-type: text/html"
echo ""
echo '<html><head><title>'$TITLE'</title><meta http-equiv='"'REFRESH'"' content='"'0; URL=printers.cgi'"'></head>'
echo '<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
echo '</head>'
echo '<body><div id="pagecontainer">'
#########################
#Assign data
########################

PRINTDATA=$DATA


#Check to see that the member of staff is not restricted
if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
	if [ `grep -c -w $REMOTE_USER /opt/karoshi/web_controls/staff_restrictions.txt` -gt 0 ]
	then
		sudo -H /opt/karoshi/web_controls/exec/record_staff_error $REMOTE_USER:$REMOTE_ADDR:$REMOTE_USER
		sleep $SLEEPTIME
		MESSAGE=$ERRORMSG10
		show_status
	fi
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/staff/printers_control.cgi | cut -d' ' -f1`
COUNTER=0

PRINTER_ACTION=none
#Get printer name
PRINTERNAME=`echo $PRINTDATA | cut -d_ -f2 | sed 's/123456789/_/g'`
#Check to see what action needs to be carried out
if [ `echo $PRINTDATA | grep -c _enable_` = 1 ]
then
	PRINTER_ACTION=enable
	PRINTMSG=$ENABLEMSG
fi
if [ `echo $PRINTDATA | grep -c _disable_` = 1 ]
then
	PRINTER_ACTION=disable
	PRINTMSG=$DISABLEMSG
fi
if [ `echo $PRINTDATA | grep -c _test_` = 1 ]
then
	PRINTER_ACTION=test
	PRINTMSG=$TESTMSG
fi
if [ `echo $PRINTDATA | grep -c _clearqueue_` = 1 ]
then
	PRINTER_ACTION=clearqueue
	PRINTMSG=$CLEARQUEUEMSG
fi
if [ `echo $PRINTDATA | grep -c _removejobid_` = 1 ]
then
	END_POINT=6
	#Assign jobid
	JOBCOUNTER=2
	while [ $JOBCOUNTER -le $END_POINT ]
	do
	if [ `echo $DATA | cut -s -d'_' -f$JOBCOUNTER` = jobid$PRINTERNAME ]
	then
		let JOBCOUNTER=$JOBCOUNTER+1
		JOBID=`echo $DATA | cut -s -d'_' -f$JOBCOUNTER`
		PRINTER_ACTION=removejobid
		break
	fi
	let JOBCOUNTER=$JOBCOUNTER+1
	done
	if [ -z "$JOBID" ]
	then
		PRINTMSG=`echo $DELETEPRINTMSG $JOBID.`
	fi
fi
#Show action to be taken
if [ $PRINTER_ACTION != none ]
then
	sudo -H /opt/karoshi/web_controls/exec/printers_control $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$PRINTERNAME:$PRINTER_ACTION:$JOBID
fi

echo "</div></body></html>"
exit
