#!/bin/bash
#Copyright (C) 2011 Paul Sharrad

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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

########################
#Required input variables
########################
#  _SHUTDOWN_  This can only have one of two values - shutdown or reboot.
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Service Status"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:-')
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

#Assign SERVICE
DATANAME=SERVICE
get_data
SERVICE="$DATAENTRY"

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/services_view_fm.cgi";'
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

if [[ $(grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################

#Check to see that a server has been picked to show services on
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The server name cannot be blank."
	show_status
fi
#Check to see that a server type is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$"The server type cannot be blank."
	show_status
fi
#Check to see that the action is not blank
if [ -z "$ACTION" ]
then
	MESSAGE=$ERRORMSG4
	show_status
fi
#Check to see that servermaster is not blank.
if [ "$SERVERTYPE" = federatedslave ]
then
	if [ ! -z "$SERVERMASTER" ]
	then 
		MESSAGE=$ERRORMSG5
		show_status
	fi
fi
#Check to see that the service is not blank
if [ -z "$SERVICE" ]
then
	MESSAGE=$ERRORMSG6
	show_status
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

if [ "$ACTION" = stop ]
then
	Action2=$"stopping"
fi

if [ "$ACTION" = start ]
then
	Action2=$"starting"
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	SERVERNAME2=$(echo "${SERVERNAME:0:9}" | cut -d. -f1)
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'"$SERVERNAME2"' '"$Action2 $SERVICE"'</span>
	<a href="/cgi-bin/admin/services_view_fm.cgi">'"$SERVERNAME"'</a>
	</div></div><div id="mobileactionbox">
	'
else
	echo '<div class="sectiontitle">'"$SERVERNAME"' - '"$Action2 $SERVICE"'</div><br>'
fi


Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/services_view2.cgi | cut -d' ' -f1)
#Show service status
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$ACTION:$SERVICE" | sudo -H /opt/karoshi/web_controls/exec/services_view2
[ "$MOBILE" = no ] && echo '</div>'
echo "</div></div></body></html>"
exit
