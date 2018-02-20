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

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"E-Mail - SMS Alerts"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\.%_:\-')
#########################
#Assign data to variables
#########################
END_POINT=15
function get_data {
COUNTER=2
DATAENTRY=""
while [[ $COUNTER -le $END_POINT ]]
do
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [[ "$DATAHEADER" = "$DATANAME" ]]
	then
		let COUNTER="$COUNTER"+1
		DATAENTRY=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
		break
	fi
	let COUNTER=$COUNTER+1
done
}

#Assign NAME
DATANAME=NAME
get_data
NAME="$DATAENTRY"

#Assign EMAILTO
DATANAME=EMAILTO
get_data
EMAILTO="$DATAENTRY"

#Assign EMAILFROM
DATANAME=EMAILFROM
get_data
EMAILFROM="$DATAENTRY"

#Assign MAILSERVER
DATANAME=MAILSERVER
get_data
MAILSERVER="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
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
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [[ $(grep -c ^"$REMOTE_USER": /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################
#Check to see that NAME is not blank
if [ -z "$NAME" ]
then
	MESSAGE=$"You have not entered in a valid E-Mail address to send the alert to."
	show_status
fi
#Check to see that EMAILTO is not blank
if [ -z "$EMAILTO" ]
then
	MESSAGE=$"You have not entered in a valid E-Mail address to send the alert to."
	show_status
fi
#Check to see that EMAILFROM is not blank
if [ -z "$EMAILFROM" ]
then
	MESSAGE=$"You have not entered in a valid E-Mail address sender."
	show_status
fi
#Check that MAILSERVER is not blank
if [ -z "$MAILSERVER" ]
then
	MESSAGE=$"You have not entered in a valid E-Mail server."
	show_status
fi

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/monitors_add_email_alert.cgi | cut -d' ' -f1)
#Add alert information
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$EMAILTO:$EMAILFROM:$MAILSERVER:$NAME" | sudo -H /opt/karoshi/web_controls/exec/monitors_add_email_alert
if [ "$?" = 101 ]
then
	MESSAGE=$"There was a problem with this action." $"Please check the karoshi web administration logs for more details."
	show_status
fi
completed
exit

