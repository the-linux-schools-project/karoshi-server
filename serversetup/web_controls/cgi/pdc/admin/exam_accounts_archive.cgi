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
#Submit button only!
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Archive the exam accounts"'</title><meta http-equiv="REFRESH" content="0; URL=exam_accounts_archive_fm.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head><body><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox3"><div id="titlebox"><div class="sectiontitle">'$"Archive the exam accounts"'</div></div><div id="infobox">'

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-+')
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

#Assign USERNAME
DATANAME=USERNAME
get_data
USERNAME="$DATAENTRY"

#Assign GROUP
DATANAME=GROUP
get_data
GROUP="$DATAENTRY"

#Assign SERVER
DATANAME=SERVER
get_data
SERVER="$DATAENTRY"

#Assign SHARE
DATANAME=SHARE
get_data
SHARE="$DATAENTRY"

#Assign EXCEPTIONLIST
DATANAME=EXCEPTIONLIST
get_data
EXCEPTIONLIST="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/exam_accounts_archive_fm.cgi";'
echo '</script>'
echo "</div></div></div></body></html>"
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

if [[ $(grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#Check to see that the server is not blank
if [ -z "$SERVER" ]
then
	MESSAGE=$"The servername cannot be blank."
	show_status
fi

if [ -z "$SHARE" ]
then
	MESSAGE=$"You have not chosen a network share."
	show_status
fi

if [ -z "$USERNAME" ] && [ -z "$GROUP" ]
then
	MESSAGE=$"You must choose either a user or a group to set the permissions for the archive."
	show_status
fi

if [ ! -f "/opt/karoshi/server_network/network_shares/$SERVER/$SHARE" ]
then
	MESSAGE=$"The share definition for this share does not exist."
	show_status
fi

#Check to see the the user and group can get to the share
source "/opt/karoshi/server_network/network_shares/$SERVER/$SHARE"

if [[ $(echo "$GROUPLIST" | grep -c "$GROUP") = 0 ]]
then
	MESSAGE=$"This group cannot access the network share."
	show_status
fi

DAY=$(date +%d)
MONTH=$(date +%b)
TIME=$(date +%T)
YEAR=$(date +%Y)
ARCHIVEFOLDER=$(echo "$DAY""_$MONTH""_$YEAR""_$TIME" | sed 's/:/_/g')

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/exam_accounts_archive.cgi | cut -d' ' -f1)

#Archive exam accounts
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$GROUP:$SERVER:$SHARE:$EXCEPTIONLIST:" | sudo -H /opt/karoshi/web_controls/exec/exam_accounts_archive

if [ "$?" = 0 ]
then
	#Get the network share details
	MESSAGE=$"All exam accounts have been archived to"": $SERVER: $SHARE /examfiles/$ARCHIVEFOLDER"
else
	MESSAGE=$"The exam accounts could not be archived"
fi
show_status
