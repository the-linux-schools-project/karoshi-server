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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Add Reverse Proxy"'</title><meta http-equiv="REFRESH" content="0; URL=reverse_proxy_view_fm.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign TARGET
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = TARGETcheck ]
	then
		let COUNTER=$COUNTER+1
		TARGET=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign DESTINATION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = DESTINATIONcheck ]
	then
		let COUNTER=$COUNTER+1
		DESTINATION=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Check to see that TARGET is not blank
if [ -z "$TARGET" ]
then
	TARGET=webrootdir
fi
#Check to see that DESTINATION is not blank
if [ -z "$DESTINATION" ]
then
	MESSAGE=$"The web address to redirect to must not be blank."
	show_status
fi
#Check that the web TARGET is not already being redirected
if [ -f /opt/karoshi/server_network/reverseproxy/sites/$TARGET ]
then
	MESSAGE=`echo $TARGET - $"This address is already being redirected."`
	show_status
fi

#Make sure that the destination starts with http or https
if [ `echo "$DESTINATION" | grep -c ^http` = 0 ] && [ `echo "$DESTINATION" | grep -c ^https` = 0 ]
then
	MESSAGE=`echo "$DESTINATION" - $"The destination must start with http or https."`
	show_status
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/reverse_proxy_add.cgi | cut -d' ' -f1`
#Add proxy
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$TARGET:$DESTINATION:" | sudo -H /opt/karoshi/web_controls/exec/reverse_proxy_add
echo '</body></html>'
exit
