#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

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
#  _SERVER_
#  _PASSWORD1_  Root Password
#  _PASSWORD2_  Checked against PASSWORD1 for typos.

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version


############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/update_servers_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_page {
echo "
<form action=\"/cgi-bin/admin/update_servers_fm.cgi\" method=\"post\" id=\"showdns\">
<input type=\"hidden\" name=\"_DAY_\" value=\"$DAY\">
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
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%+')
#########################
#Assign data to variables
#########################
END_POINT=16
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

#Assign _DAY_
DATANAME=DAY
get_data
DAY="$DATAENTRY"

#Assign HOURS
DATANAME=HOURS
get_data
HOURS=$(echo "$DATAENTRY" | tr -cd '0-9')


#Assign MINUTES
DATANAME=MINUTES
get_data
MINUTES=$(echo "$DATAENTRY" | tr -cd '0-9')

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

#Assign FORCEREBOOT
DATANAME=FORCEREBOOT
get_data
FORCEREBOOT="$DATAENTRY"

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Update Servers"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ "$MOBILE" = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: www.dynamicdrive.com
		* Visit Dynamic Drive at www.dynamicdrive.com for full source code
		***********************************************/
	</script>
	<script>
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head><body><div id="pagecontainer">'

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

#Check to see that DAY is not blank
if [ -z "$DAY" ]
then
	MESSAGE=$"You have not chosen a day for the update."
	show_status
fi

#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The server name cannot be blank."
	show_status
fi

#Check to see that SERVERTYPE is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$"The server type cannot be blank."
	show_status
fi

#Check to see that SERVERMASTER is not blank
if [ "$SERVERTYPE" = federatedslave ]
then
	if [ -z "$SERVERMASTER" ]
	then
		MESSAGE=$"The server master cannot be blank."
		show_status
	fi
fi

#Set force reboot to no if it is blank
[ -z "$FORCEREBOOT" ] && FORCEREBOOT=no

#Check to see that HOURS is not blank
if [ -z "$HOURS" ]
then
	MESSAGE=$"update failure."
	show_status
fi

#Check to see that MINUTES is not blank
if [ -z "$MINUTES" ]
then
	MESSAGE=$"update failure."
	show_status
fi

#Check that time is ok
if [ "$MINUTES" -gt 59 ]
then
	MESSAGE=$"Please enter a correct time."
	show_status
fi

#Check that time is ok
if [ "$MINUTES" -lt 0 ]
then
	MESSAGE=$"Please enter a correct time."
	show_status
fi

#Check that time is ok
if [ "$HOURS" -gt 23 ]
then
	MESSAGE=$"Please enter a correct time."
	show_status
fi

#Check that time is ok
if [ "$HOURS" -lt 0 ]
then
	MESSAGE=$"Please enter a correct time."
	show_status
fi

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/update_servers.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$DAY:$HOURS:$MINUTES:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$FORCEREBOOT:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/update_servers
show_page

echo "</div></body></html>"
exit
