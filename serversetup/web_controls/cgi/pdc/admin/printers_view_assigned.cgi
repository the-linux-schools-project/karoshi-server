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
#  _PRINTACTION_
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Assigned Printers"'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\_\%-'`
#########################
#Assign data to variables
#########################
END_POINT=3
#Assign PRINTACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PRINTACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		PRINTACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Check to see that PRINTACTION is not blank
if [ -z "$PRINTACTION" ]
then
	MESSAGE=$"No Printers have been assigned to a location."
	show_status
fi
PRINTACTION=`echo $PRINTACTION | sed 's/%3A/:/g'`

ACTION=`echo $PRINTACTION | cut -d: -f1`
LOCATION=`echo $PRINTACTION | cut -d: -f2`
PRINTER=`echo $PRINTACTION | cut -d: -f3`
#Check to see that ACTION is not blank
if [ -z "$ACTION" ]
then
	MESSAGE=$"You have not chosen a print action."
	show_status
fi
#Check to see that LOCATION is not blank
if [ -z "$LOCATION" ]
then
	MESSAGE=$"The location must not be blank."
	show_status
fi
#Check to see that PRINTER is not blank
if [ -z "$PRINTER" ]
then
	MESSAGE=$"The printer must not be blank."
	show_status
fi
#Check to see that ACTION is corect
if [ $ACTION != delete ] && [ $ACTION != default ]
then
	MESSAGE=$"The action type is not correct."
	show_status
fi
#Check to see that location.txt exists
if [ ! -f /var/lib/samba/netlogon/locations.txt ]
then
	MESSAGE=$"The location file does not exit."
	show_status
fi

#Check to see that LOCATION exists
if [ `grep -c $LOCATION /var/lib/samba/netlogon/locations.txt` = 0 ]
then
	MESSAGE=$"This location does not exist."
	show_status
fi

#Check to see that printer.txt exists
if [ ! -f /var/lib/samba/netlogon/printers.txt ]
then
	MESSAGE=$"The printer file does not exist."
	show_status
fi

#Check to see that PRINTER queue exits
echo printer is $PRINTER"<br>"
if [ `grep -c ",$PRINTER," /var/lib/samba/netlogon/printers.txt` = 0 ]
then
	MESSAGE=$"The printer queue does not exist."
	show_status
fi
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers_view_assigned.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/printers_view_assigned $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$LOCATION:$PRINTER
if [ $? = 101 ]
then
	MESSAGE=`echo $"There was a problem with this action." $"Please check the karoshi web administration logs for more details."`
	show_status
fi
exit
