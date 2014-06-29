#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

#This file is part of Karoshi Server.
#
#Karoshi Server is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Karoshi Server is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Karoshi Server.  If not, see <http://www.gnu.org/licenses/>.

#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

#Language
TITLE="Manage Print Queues"
HTTPS_ERROR="You must access this page via https."
ACCESS_ERROR1="You must be a Karoshi Management User to complete this action."
DELETEPRINTMSG="Deleting print job"
CLEARQUEUEMSG="Clearing the printer queue."
ENABLEMSG="Enabling the printer queue."
DISABLEMSG="Disabling the printer queue."
TESTMSG="Testing the printer queue."

LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER


function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="0; URL=printers.cgi"></head><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body><div id="pagecontainer">'
#########################
#Assign data
########################
PRINTER_COMMAND_DATA=`echo $DATA | sed 's/_QUEUENAME_/ QUEUENAME_/g'`
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers_control.cgi | cut -d' ' -f1`

PRINTER_ACTION=none
#Get printer name
PRINTDATA=`echo ${PRINTER_COMMAND_DATA[$COUNTER]}`
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
if [ `echo $PRINTDATA | grep -c _setlocation_` = 1 ]
then
PRINTER_ACTION=setlocation
PRINTMSG=$TESTMSG
fi
if [ `echo $PRINTDATA | grep -c _setppd_` = 1 ]
then
PRINTER_ACTION=setppd
fi
if [ `echo $PRINTDATA | grep -c _clearqueue_` = 1 ]
then
PRINTER_ACTION=clearqueue
PRINTMSG=$CLEARQUEUEMSG
fi
if [ `echo $PRINTDATA | grep -c _jobid_` = 1 ]
then
END_POINT=6
#Assign jobid
JOBCOUNTER=5
while [ $JOBCOUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$JOBCOUNTER`
if [ `echo $DATAHEADER'check'` = jobid'check' ]
then
let JOBCOUNTER=$JOBCOUNTER+1
JOBID=`echo $DATA | cut -s -d'_' -f$JOBCOUNTER`
PRINTER_ACTION=removejobid
break
fi
let JOBCOUNTER=$JOBCOUNTER+1
done
if [ $JOBID'null' != null ]
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
