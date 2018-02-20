#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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
#  _MINUTES_
#  _HOUR_
#  _DAY_
#  _MONTH_
#  _DOFW_
#  _COMMAND_
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Schedule Job"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body><div id="pagecontainer">'
#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

#########################
#Get data input
#########################

DATA=$(cat | tr -cd 'A-Za-z0-9\._:\/*%+"-' | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g' | sed 's/%A0+//g' | sed 's/%A0//g')
#########################
#Assign data to variables
#########################
END_POINT=45
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

#Assign MINUTES
DATANAME=MINUTES
get_data
MINUTES="$DATAENTRY"

#Assign HOUR
DATANAME=HOUR
get_data
HOUR="$DATAENTRY"

#Assign DAY
DATANAME=DAY
get_data
DAY="$DATAENTRY"

#Assign MONTH
DATANAME=MONTH
get_data
MONTH="$DATAENTRY"

#Assign DOFW
DATANAME=DOFW
get_data
DOFW="$DATAENTRY"

#Assign COMMAND
DATANAME=COMMAND
get_data
COMMAND="$DATAENTRY"

#Assign SERVERNAME
DATANAME=SERVERNAME
get_data
SERVERNAME="$DATAENTRY"

#Assign SERVERTYPE
DATANAME=SERVERTYPE
get_data
SERVERTYPE="$DATAENTRY"

#Assign SERVERMASTER
DATANAME=SERVERMASTER
get_data
SERVERMASTER="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/cron_add_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

function show_jobs {
echo "
<form action=\"/cgi-bin/admin/cron_view.cgi\" method=\"post\" id=\"showdns\">
<input type=\"hidden\" name=\"_SERVERNAME_$SERVERNAME""_SERVERTYPE_$SERVERTYPE""_\" value=\"\">
</form>
<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('showdns').submit();
//-->
</script>
</div></div></body></html>
"
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

#########################
#Check data
#########################
#Check to see that MINUTES is not blank
if [ -z "$MINUTES" ]
then
	MESSAGE=$"The minutes must not be blank."
	show_status
fi
#Check to see that HOUR is not blank
if [ -z "$HOUR" ]
then
	MESSAGE=$"The hour must not be blank."
	show_status
fi
#Check to see DAY is not blank
if [ -z "$DAY" ]
then
	MESSAGE=$"The day must not be blank."
	show_status
fi
#Check to see MONTH is not blank
if [ -z "$MONTH" ]
then
	MESSAGE=$"The month must not be blank."
	show_status
fi
#Check to see DOFW is not blank
if [ -z "$DOFW" ]
then
	MESSAGE=$"The day of week must not be blank."
	show_status
fi
#Check to see COMMAND is not blank
if [ -z "$COMMAND" ]
then
	MESSAGE=$"The command must not be blank."
	show_status
fi
#Check to see SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The server must not be blank."
	show_status
fi

#Check to see that SERVERTYPE is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$"The server cannot be blank."
	show_status
fi

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/cron_add.cgi | cut -d' ' -f1)
#Add cron job
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$MINUTES:$HOUR:$DAY:$MONTH:$DOFW:$COMMAND:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:" | sudo -H /opt/karoshi/web_controls/exec/cron_add
show_jobs
echo "</div></body></html>"
exit

