#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

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
########################
#Required input variables
########################
#  _GROUPNAME_ The name of the mon monitor group to add
#  _TCPIP_  IP numbers of the devices in the group to check
#   _INTERVAL_  The time interval between each check.
#  _DESCRIPTION_
#  _MONITORTYPES_ The type of monitors to use to check the services.
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_view ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_view
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\%+-'`
#########################
#Assign data to variables
#########################
END_POINT=8
#Assign _MONITOR_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MONITORcheck ]
then
let COUNTER=$COUNTER+1
MONITOR=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/monitors_view.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
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
#########################
#Check data
#########################
#Check to see that MONITOR is not blank
if [ $MONITOR'null' = null ]
then
MESSAGE=$ERRORMSG5
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/monitors_delete.cgi | cut -d' ' -f1`
#Delete monitor

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MONITOR:" | sudo -H /opt/karoshi/web_controls/exec/monitors_delete
MONITOR=`echo $MONITOR | sed 's/%25%25%25%25%25/_/g'`

EXEC_STATUS=`echo $?`
MONITOR=`echo $MONITOR | sed 's/+/ /g'`
MESSAGE=`echo $MONITOR - $DELETEDMSG`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=$ERRORMSG8
fi
if [ $EXEC_STATUS = 102 ]
then
MESSAGE=$ERRORMSG5
fi
if [ $EXEC_STATUS = 103 ]
then
MESSAGE=$ERRORMSG9
fi
show_status
exit
