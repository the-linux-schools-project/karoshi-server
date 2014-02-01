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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
########################
#Required input variables
########################
#  _HOUR_
#  _MINUTES_
# _LOCATION_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/wake_on_lan_add ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/wake_on_lan_add
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign HOUR
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = HOURcheck ]
then
let COUNTER=$COUNTER+1
HOUR=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign MINUTES
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MINUTEScheck ]
then
let COUNTER=$COUNTER+1
MINUTES=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign LOCATION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LOCATIONcheck ]
then
let COUNTER=$COUNTER+1
LOCATION=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Check to see that HOUR is not blank
if [ $HOUR'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that MINUTES is not blank
if [ $MINUTES'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that LOCATION fields are not blank
if [ $LOCATION'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
#Check that hour and minutes are correct
if [ $HOUR -gt 24 ]
then
MESSAGE=$ERRORMSG4
show_status
fi
if [ $MINUTES -gt 60 ]
then
MESSAGE=$ERRORMSG4
show_status
fi
#Add in wake on lan
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/wake_on_lan_add.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/wake_on_lan_add $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$HOUR:$MINUTES:$LOCATION
if [ `echo $?` = 0 ]
then
MESSAGE=`echo $LOCATION - $COMPLETEDMSG`
else
MESSAGE=$ERRORMSG5
fi
show_status
exit
