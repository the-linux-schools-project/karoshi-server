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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server
DISABLESORTCOL=4
[ "$MOBILE" = yes ] && DISABLESORTCOL=2

#Check if timout should be disabled
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
then
	TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Client Boot Controls"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>

<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	1: { sorter: "MAC" },
	2: { sorter: "ipAddress" },
	'"$DISABLESORTCOL"': { sorter: false },
    		}
		});
    } 
);
</script>

<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\+-')
#########################
#Assign data to variables
#########################
END_POINT=8
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

#Assign NETBOOT
DATANAME=NETBOOT
get_data
NETBOOT="$DATAENTRY"


#Assign _SEARCH_
if [ "$LOCATION"'null' = SEARCHNOTVALIDnull ]
then
	END_POINT=8
	DATANAME=SEARCH
	get_data
	SEARCH="$DATAENTRY"
fi

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/client_boot_controls_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You have not chosen a location."
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

if [ "$LOCATION"'null' = SEARCHNOTVALIDnull ]
then
	#Check to see that SEARCH is not blank
	if [ -z "$SEARCH" ]
	then
		MESSAGE=$"The asset search cannot be blank."
		show_status
	fi
	LOCATION=$SEARCH
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	WIDTH=100
	ICON1=/images/assets/location.png
	ICON2=/images/submenus/client/enable_all.png
	ICON3=/images/submenus/client/reset_all.png
	ICON4=/images/submenus/client/activate_changes.png
	ICON5=/images/submenus/client/wakeupall.png
	ICON6=/images/assets/curriculum_computer.png
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	WIDTH=90
	ICON1=/images/assets/locationm.png
	ICON2=/images/submenus/client/enable_allm.png
	ICON3=/images/submenus/client/reset_allm.png
	ICON4=/images/submenus/client/activate_changesm.png
	ICON5=/images/submenus/client/wakeupallm.png
	ICON6=/images/assets/curriculum_computerm.png
fi

echo '<form action="/cgi-bin/admin/client_boot_controls2.cgi" method="post">'
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
	echo '<div class="sectiontitle">'$"Client Boot Controls"'</div>'
fi
echo '
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="client_boot_controls_fm.cgi" class="info infonavbutton" name="_ChooseLocation" value="_">
			<img src="'"$ICON1"'" alt="'$"Choose Location"'">
			<span>'$"Choose the location."'</span><br>
			'$"Choose Location"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_EnableAll_" value="_ACTION_enableall_LOCATION_'"$LOCATION"'_ASSET_none_TCPIP_none_MACADDRESS_none_">
			<img src="'"$ICON2"'" alt="'$"Enable All"'">
			<span>'$"Enable all assets in this location."'</span><br>
			'$"Enable All"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_ResetAll_" value="_ACTION_resetall_LOCATION_'"$LOCATION"'_ASSET_none_TCPIP_none_MACADDRESS_none_">
			<img src="'"$ICON3"'" alt="'$"Reset All"'">
			<span>'$"Reset all assets."'</span><br>
			'$"Reset All"'
		</button>
	</td>

	'

	[ "$MOBILE" = yes ] && echo '</tr><tr>'

	echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_ActivateChanges_" value="_ACTION_activatechanges_LOCATION_'"$LOCATION"'_ASSET_none_TCPIP_none_MACADDRESS_none_">
			<img src="'"$ICON4"'" alt="'$"Activate Changes"'">
			<span>'$"Activate Changes and reload the DHCP configuration."'</span><br>
			'$"Activate Changes"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_WakeOnLanAll_" value="_ACTION_wakeonlanall_LOCATION_'"$LOCATION"'_ASSET_none_TCPIP_none_MACADDRESS_none_">
			<img src="'"$ICON5"'" alt="'$"Wake location"'">
			<span>'$"Wake on lan all assets in this location."'</span><br>
			'$"Wake location"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="/cgi-bin/admin/asset_register_view.cgi" class="info infonavbutton" name="_AssetRegister_" value="_ACTION_view_LOCATION_'"$LOCATION"'_">
			<img src="'"$ICON6"'" alt="'$"Asset Register"'">
			<span>'$"Asset Register"'</span><br>
			'$"Asset Register"'
		</button>
	</td>

</tr></tbody></table>
'

if [ "$MOBILE" = no ]
then
	echo '</div><div id="infobox">'
fi
Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/client_boot_controls.cgi | cut -d' ' -f1)
sudo -H /opt/karoshi/web_controls/exec/client_boot_controls "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$LOCATION:$SEARCH:$MOBILE:$NETBOOT:"

[ "$MOBILE" = no ] && echo '</div>'
echo "</div></form></div></body></html>"
exit
