#!/bin/bash
#Copyright (C) 2016 Matthew Jowett
#
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

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo 'Content-type: text/html

<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>'$"Setup richdocuments"'</title>
		<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
		<script src="/all/stuHover.js" type="text/javascript"></script>
	</head>
<body>
	<div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox3"><div id="titlebox">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%'`

#########################
#Assign data to variables
#########################
END_POINT=9

#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign _ADMINPASS1_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ADMINPASS1check ]
	then
		let COUNTER=$COUNTER+1
		ADMINPASS1=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/\.//g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign _ADMINPASS2_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ADMINPASS2check ]
	then
		let COUNTER=$COUNTER+1
		ADMINPASS2=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/\.//g'`
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

function completed {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi"'
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

#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The server cannot be blank."
	show_status
fi

# Check to see if the password field is empty.

if [ -z "$ADMINPASS1" ] || [ -z "$ADMINPASS2" ]; then
	MESSAGE=$"The password must not be blank."
	show_status
fi

# Check to see if the password was entered correctly (matches confirmation).

if [ "$ADMINPASS1" != "$ADMINPASS2" ]; then
	MESSAGE=$"The passwords do not match."
	show_status
fi

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/module_richdocuments.cgi | cut -d' ' -f1)

echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ADMINPASS1:$SERVERNAME:" | sudo -H /opt/karoshi/web_controls/exec/module_richdocuments
EXEC_STATUS=$?
if [ $EXEC_STATUS = 101 ]; then
MESSAGE=`echo $"There was a problem with this action." $"Please check the karoshi web administration logs for more details."`
completed
fi
echo '</div></div></div></body></html>'
exit
