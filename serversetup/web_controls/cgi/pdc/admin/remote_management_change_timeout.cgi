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
# _TIMEOUT_
##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Change Timeout"'</title><meta http-equiv="REFRESH" content="0; URL=remote_management_change_timeout_fm.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign TIMEOUT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TIMEOUTcheck ]
then
let COUNTER=$COUNTER+1
TIMEOUT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign NOTIMEOUT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = NOTIMEOUTcheck ]
then
let COUNTER=$COUNTER+1
NOTIMEOUT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$"You must access this page via https."
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$"You must be a Karoshi Management User to complete this action."
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$"You must be a Karoshi Management User to complete this action."
show_status
fi
#########################
#Check data
#########################
#Check to see that TIMEOUT is not blank
if [ $TIMEOUT'null' = null ]
then
MESSAGE=$"The timeout value must not be blank."
show_status
fi
#Check to see that TIMEOUT is a number
TIMEOUT=`echo $TIMEOUT | tr -cd '0-9\n'`
if [ $TIMEOUT'null' = null ]
then
MESSAGE=$"The timeout value must be a number between 1 and 99."
show_status
fi
#Make sure that NOTIMEOUT is a number
NOTIMEOUT=`echo $NOTIMEOUT | tr -cd '0-9.\n'`

#Check that timeout is between 1 and 99
if [ $TIMEOUT -lt 1 ] || [ $TIMEOUT -gt 99 ]
then
MESSAGE=$"The timeout value must be a number between 1 and 99."
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/remote_management_change_timeout.cgi | cut -d' ' -f1`
#Change password
sudo -H /opt/karoshi/web_controls/exec/remote_management_change_timeout $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$TIMEOUT:$NOTIMEOUT:
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $"There was a problem with this action." $"Please check the karoshi web administration logs for more details."`
else
MESSAGE=$"Your timeout setting has been changed."
fi
show_status
exit
