#!/bin/bash
#Add user
#Copyright (C) 2007  The karoshi Team

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
#  _RELAY_
#  _RADDRESS_
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server


echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Use E-mail relay"'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=4
#Assign RELAY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = RELAYcheck ]
then
let COUNTER=$COUNTER+1
RELAY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign RADDRESS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = RADDRESScheck ]
then
let COUNTER=$COUNTER+1
RADDRESS=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT lang
uage="Javascript">'
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
#Check to see that RELAY is not blank
if [ $RELAY'null' = null ]
then
MESSAGE=$"The relay option must not be blank."
show_status
fi
#Check to see that RELAY is set to direct or relay
if [ $RELAY != direct ] && [ $RELAY != relay ]
then
MESSAGE=$"Incorrect Relay option."
show_status
fi
#Check to see that relay address is not blank
if [ $RELAY = relay ]
then
if [ $RADDRESS'null' = null ]
then
MESSAGE=$"The Relay address must not be blank."
show_status
fi
fi

Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/email_relay2.cgi | cut -d' ' -f1`
#Make changes
sudo -H /opt/karoshi/web_controls/exec/email_relay $REMOTE_USER:$REMOTE_ADDR:$Checksum:$RELAY:$RADDRESS
if [ $RELAY = direct ]
then
MESSAGE=$"System configured to send e-mails directly."
else
MESSAGE=`echo $"System configured to relay e-mails to:" $RADDRESS`
fi
show_status
exit
