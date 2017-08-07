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
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><meta http-equiv="REFRESH" content="0;url=helpdesk_view_fm.cgi"><title>'$"Help Desk"'</title></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=$(cat | tr -cd 'A-Za-z0-9\.%+_:\-')
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

#Assign DEPARTMENT
DATANAME=DEPARTMENT
get_data
DEPARTMENT="$DATAENTRY"

#Assign CATEGORY
DATANAME=CATEGORY
get_data
CATEGORY="$DATAENTRY"

#Assign REQUEST
DATANAME=REQUEST
get_data
REQUEST="$DATAENTRY"

#Assign JOBTITLE
DATANAME=JOBTITLE
get_data
JOBTITLE="$DATAENTRY"

#Assign LOCATION
DATANAME=LOCATION
get_data
LOCATION="$DATAENTRY"

#Assign ASSETNUMBER
DATANAME=ASSETNUMBER
get_data
ASSETNUMBER=$(echo "$DATAENTRY" | tr -cd 'A-Za-z0-9+')

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/helpdesk_add_fm.cgi";'
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
#Check data
#########################

#Check to see that NAME is not blank
if [ -z "$NAME" ]
then
	MESSAGE=$"You have not entered in your name."
	show_status
fi

#Check that JOBTITLE is not blank
if [ -z "$JOBTITLE" ]
then
	MESSAGE=$"You have not entered in a title for this job."
	show_status
fi

#Convert special characters
NAME=`echo $NAME | sed 's/+/ /g'`
JOBTITLE=`echo $JOBTITLE | sed 's/%0D%0A/ /g' | sed 's/+/ /g' | sed 's/%3E//g' | sed 's/%27//g' | sed 's/%22//g' | sed 's/%3F/?/g' | sed 's/%2C/,/g' | sed 's/%21/!/g' | sed 's/%2F/\//g' | sed 's/%26/\&/g'`
REQUEST=`echo $REQUEST | sed 's/%0D%0A/ /g' | sed 's/+/ /g' | sed 's/%3E//g' | sed 's/%27//g'  | sed 's/%22//g' | sed 's/%3F/?/g' | sed 's/%2C/,/g' | sed 's/%21/!/g' | sed 's/%2F/\//g' | sed 's/%28/(/g' | sed 's/%29/)/g' | sed 's/%3A/:/g' | sed 's/%26/\&/g'`
DEPARTMENT=`echo $DEPARTMENT | sed 's/%24/$/g' | sed 's/%26/\&/g'`
CATEGORY=`echo $CATEGORY | sed 's/%24/$/g'`
ASSETNUMBER=`echo $ASSETNUMBER | sed 's/+/ /g'`

#See if a default person has been declared for assigning jobs to
[ -f /opt/karoshi/server_network/helpdesk/defaultassign ] && ASSIGNED=`sed -n 1,1p /opt/karoshi/server_network/helpdesk/defaultassign`

#See if a default priority has been declared for assigning jobs to
[ -f /opt/karoshi/server_network/helpdesk/defaultpriority ] && PRIORITY=`sed -n 1,1p /opt/karoshi/server_network/helpdesk/defaultpriority`

#Add request
REQUESTNAME="`date +%s`.$$"

[ ! -d /opt/karoshi/server_network/helpdesk/log ] && mkdir -p /opt/karoshi/server_network/helpdesk/log
[ ! -d /opt/karoshi/server_network/helpdesk/todo ] && mkdir -p /opt/karoshi/server_network/helpdesk/todo
echo NAME='"'"$NAME"'"' > /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo DATE='"'"`date +%d-%m-%y`"'"' >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo DATE2='"'"`date +%s`"'"' >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo LOCATION='"'"$LOCATION" "$ASSETNUMBER"'"' >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo DEPARTMENT="$DEPARTMENT" >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo CATEGORY="$CATEGORY" >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo JOBTITLE='"'"$JOBTITLE"'"' >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo REQUEST='"'"$REQUEST"'"' >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo ASSIGNED='"'"$ASSIGNED"'"' >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo PRIORITY='"'"$PRIORITY"'"' >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo FEEDBACK="" >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo COMPLETEDDATE="" >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
echo COMPLETEDDATE2="" >> /opt/karoshi/server_network/helpdesk/todo/"$REQUESTNAME"
LOG_DATE=$(date +%F)
echo "$(date): Helpdesk - $REQUESTNAME added by $REMOTE_USER from $REMOTE_ADDR" >> "/opt/karoshi/server_network/helpdesk/log/$LOG_DATE"

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:yes:" | sudo -H /opt/karoshi/web_controls/exec/helpdesk_warning_message

exit
