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
#  _FIRSTNAME_
#  _SURNAME_
# _USERNAMESTYLE_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
#  _GROUP_      This is the primary group for the new user eg yr2000, staff, officestaff.

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Client Boot Controls"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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





echo '</head><body onload="submitForm()"><div id="pagecontainer">'
#########################
#Get data input
#########################

DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-')

#########################
#Assign data to variables
#########################
END_POINT=19
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

#Assign LOCATION
DATANAME=LOCATION
get_data
LOCATION="$DATAENTRY"

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

#Assign ASSETTYPE
DATANAME=ASSETTYPE
get_data
ASSETTYPE="$DATAENTRY"

#Assign ASSET
DATANAME=ASSET
get_data
ASSET="$DATAENTRY"

#Assign TCPIP
DATANAME=TCPIP
get_data
TCPIP="$DATAENTRY"

#Assign MACADDRESS
DATANAME=MACADDRESS
get_data
MACADDRESS="$DATAENTRY"

#Assign NETBOOT
DATANAME=NETBOOT
get_data
NETBOOT="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'");'
echo 'window.location = "/cgi-bin/admin/client_boot_controls_fm.cgi";'
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
#Check to see that LOCATION is not blank
if [ -z "$LOCATION" ]
then
	MESSAGE=$"You have not chosen a location."
	show_status
fi
#Check to see that ACTION is not blank
if [ -z "$ACTION" ]
then
	MESSAGE=$"The action cannot be blank."
	show_status
fi
#Check to see ASSET is not blank.
if [ -z "$ASSET" ]
then
	MESSAGE=$"You have not chosen an asset type."
	show_status
fi
if [ -z "$TCPIP" ]
then
	MESSAGE=$"The TCP IP address cannot be blank."
	show_status
fi
if [ -z "$MACADDRESS"  ]
then
	MESSAGE=$"The mac address cannot be blank."
	show_status
fi
if [ "$ACTION" = install ] || [ "$ACTION" = enableall ]
then
	if [ -z "$NETBOOT"  ]
	then
		MESSAGE=$"The netboot cannot be blank."
		show_status
	fi
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Client Boot Controls"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
else
	echo '<div class="sectiontitle">'$"Client Boot Controls"'</div></div><div id="infobox">'
fi

echo '<form name="myForm" id="myForm" action="/cgi-bin/admin/client_boot_controls.cgi" method="post"><input name="_LOCATION_" value="'"$LOCATION"'" type="hidden">''<input name="_ASSETTYPE_" value="'"$ASSETTYPE"'" type="hidden"><input name="_NETBOOT_" value="'"$NETBOOT"'" type="hidden"></form>
'
Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/client_boot_controls2.cgi | cut -d' ' -f1)

echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$LOCATION:$ACTION:$ASSET:$TCPIP:$MACADDRESS:$NETBOOT:" | sudo -H /opt/karoshi/web_controls/exec/client_boot_controls2

[ "$MOBILE" = no ] && echo '</div>'

echo "<script type='text/javascript'>document.myForm.submit();</script></div></div></body></html>"
exit
