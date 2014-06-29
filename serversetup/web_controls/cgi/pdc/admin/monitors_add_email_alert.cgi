#!/bin/bash
#Copyright (C) 2010  Paul Sharrad

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
#  _EMAILTO_
#  _EMAILFROM_
# _MAILSERVER_
# _NAME_
##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_email_alert ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_email_alert
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\.%_:\-'`
#########################
#Assign data to variables
#########################
END_POINT=9
#Assign NAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = NAMEcheck ]
then
let COUNTER=$COUNTER+1
NAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign EMAILTO
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = EMAILTOcheck ]
then
let COUNTER=$COUNTER+1
EMAILTO=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign EMAILFROM
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = EMAILFROMcheck ]
then
let COUNTER=$COUNTER+1
EMAILFROM=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign MAILSERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MAILSERVERcheck ]
then
let COUNTER=$COUNTER+1
MAILSERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/monitors_add_email_alert_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function completed {
echo '<SCRIPT language="Javascript">'
echo 'window.location = "/cgi-bin/admin/monitors_view_email_alerts_fm.cgi";'
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
#Check to see that NAME is not blank
if [ $NAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that EMAILTO is not blank
if [ $EMAILTO'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that EMAILFROM is not blank
if [ $EMAILFROM'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check that MAILSERVER is not blank
if [ $MAILSERVER'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/monitors_add_email_alert.cgi | cut -d' ' -f1`
#Add alert information
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$EMAILTO:$EMAILFROM:$MAILSERVER:$NAME" | sudo -H /opt/karoshi/web_controls/exec/monitors_add_email_alert
EXEC_STATUS=`echo $?`

if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
show_status
fi
completed
exit

