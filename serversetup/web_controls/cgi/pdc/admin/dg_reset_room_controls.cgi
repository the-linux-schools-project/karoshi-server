#!/bin/bash
#Copyright (C) 2012  Paul Sharrad

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Client Internet Controls"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%'`
#########################
#Assign data to variables
#########################
END_POINT=11
#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
then
let COUNTER=$COUNTER+1
ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign HOURS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = HOURScheck ]
then
let COUNTER=$COUNTER+1
HOURS=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
MINUTES=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign TIME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TIMEcheck ]
then
let COUNTER=$COUNTER+1
TIME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done


function show_status {
echo '<script>'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/dg_reset_room_controls_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function completed {
echo '<script>'
echo 'window.location = "/cgi-bin/admin/dg_reset_room_controls_fm.cgi";'
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
#Check to see that ACTION is not blank
if [ $ACTION'null' = null ]
then
MESSAGE=$"You have not entered an action."
show_status
fi
if [ $ACTION = add ]
then
#Check to see that HOURS are not blank
if [ $HOURS'null' = null ]
then
MESSAGE=$"You have not entered a time."
show_status
fi
#Check to see that MINUTES are not blank
if [ $MINUTES'null' = null ]
then
MESSAGE=$"You have not entered a time."
show_status
fi
fi
if [ $ACTION = delete ]
then
#Check to see that TIME is not blank
if [ $TIME'null' = null ]
then
MESSAGE=$"You have not entered a time."
show_status
fi
fi

Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/dg_reset_room_controls.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ACTION:$HOURS:$MINUTES:$TIME:" | sudo -H /opt/karoshi/web_controls/exec/dg_reset_room_controls
completed
echo '</div></body></html>'
exit
