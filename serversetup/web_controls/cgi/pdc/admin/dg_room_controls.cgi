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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Client Internet Controls"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	2: { sorter: "ipAddress" },
	3: { sorter: "MAC" }
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
END_POINT=6
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

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/dg_room_controls_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$ERRORMSG7
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


#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH=70
	WIDTH2=150
	WIDTH3=175
	WIDTH4=100
	ICON1=/images/assets/curriculum_computer.png
	ICON2=/images/submenus/system/clock.png
	ICON3=/images/submenus/internet/client_allowed.png
	ICON4=/images/submenus/internet/client_denied.png
	ICON5=/images/submenus/internet/client_allowed.png
	ICON6=/images/submenus/internet/client_denied.png
	TABLETITLE=''$"Client Internet Controls"' - '$LOCATION''

	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
	echo '<div id="'$DIV_ID'"><div id="titlebox">'
else
	DIV_ID=menubox
	TABLECLASS=mobilestandard
	WIDTH=70
	WIDTH2=90
	WIDTH3=110
	WIDTH4=110
	ICON1=/images/assets/curriculum_computerm.png
	ICON2=/images/submenus/system/clockm.png
	ICON3=/images/submenus/internet/client_allowedm.png
	ICON4=/images/submenus/internet/client_deniedm.png
	ICON5=/images/submenus/internet/client_allowedm.png
	ICON6=/images/submenus/internet/client_deniedm.png
	TABLETITLE="$LOCATION"

	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"Client Internet Controls"'</span>
	<a href="/cgi-bin/admin/dg_room_controls_fm.cgi">'$"Client Internet Controls"'</a>
	</div></div><div id="mobileactionbox">
	'
fi

echo '
<div class="sectiontitle">'$TABLETITLE' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Room_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the client computers that you want to allow or deny internet access to."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH4'px; text-align:center;">
		<form action="dg_room_controls_fm.cgi" method="post">
			<button class="info" name="_Location_" value="_">
				<img src="'$ICON1'" alt="'$"Location"'">
				<span>'$"Choose location."'</span><br>
				'$"Location"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH4'px; text-align:center;">
		<form action="dg_reset_room_controls_fm.cgi" method="post">
			<button class="info" name="_ResetTimes_" value="_">
				<img src="'$ICON2'" alt="'$"Reset times"'">
				<span>'$"View the scheduled reset times."'</span><br>
				'$"Reset times"'
			</button>
		</form>
	</td>
'

[ "$MOBILE" = yes ] && echo '</tr><tr>'

echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH4'px; text-align:center;">
		<form action="dg_room_controls2.cgi" method="post">
			<button class="info" name="_AllowAll_" value="_LOCATION_'"$LOCATION"'_ACTION_allowall_ASSET_na_">
				<img src="'$ICON3'" alt="'$"Allow All"'">
				<span>'$"Allow internet access for all assets."'</span><br>
				'$"Allow All"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH4'px; text-align:center;">
		<form action="dg_room_controls2.cgi" method="post">
			<button class="info" name="_DenyAll_" value="_LOCATION_'"$LOCATION"'_ACTION_denyall_ASSET_na_">
				<img src="'$ICON4'" alt="'$"Deny All"'">
				<span>'$"Deny internet access for all assets."'</span><br>
				'$"Deny All"'
			</button>
		</form>
	</td>

'

[ "$MOBILE" = yes ] && echo '</tr><tr>'

echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH4'px; text-align:center;">
		<form action="dg_room_controls2.cgi" method="post">
			<button class="info" name="_AllowAllMedia_" value="_LOCATION_'"$LOCATION"'_ACTION_allowallmedia_ASSET_na_">
				<img src="'$ICON5'" alt="'$"Allow All Media"'">
				<span>'$"Allow media access for all assets."'</span><br>
				'$"Allow All Media"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH4'px; text-align:center;">
		<form action="dg_room_controls2.cgi" method="post">
			<button class="info" name="_DenyAllMedia_" value="_LOCATION_'"$LOCATION"'_ACTION_denyallmedia_ASSET_na_">
				<img src="'$ICON6'" alt="'$"Deny All Media"'">
				<span>'$"Deny media access for all assets."'</span><br>
				'$"Deny All Media"'
			</button>
		</form>
	</td>
'

echo '</tr></table><br>'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

if [ -d /opt/karoshi/asset_register/locations/"$LOCATION"/ ]
then
	if [[ $(ls -1 /opt/karoshi/asset_register/locations/"$LOCATION"/ | wc -l) -gt 0 ]]
	then
		echo '<table id="myTable" class="tablesorter" style="text-align: left;" >
		<thead><tr><th style="width: '"$WIDTH"'px;"><b>'$"Asset"'</b></th>'

		[ "$MOBILE" = no ] && echo '<th style="width: '"$WIDTH3"'px;"><b>'$"Mac-address"'</b></th><th style="width: '"$WIDTH2"'px;"><b>'$"Tcpip"'</b></th>'

		echo '<th><b>'$"Access"'</b></th><th><b>'$"Media Access"'</b></th></tr></thead><tbody>'

		for ASSETS in "/opt/karoshi/asset_register/locations/$LOCATION/"*
		do
			ASSET=$(basename "$ASSETS")
			source /opt/karoshi/asset_register/locations/"$LOCATION/$ASSET"
			#Only show certain asset types
			if [ "$ASSETTYPE" = 1 ] || [ "$ASSETTYPE" = 3 ] || [ "$ASSETTYPE" = 5 ] || [ "$ASSETTYPE" = 7 ] || [ "$ASSETTYPE" = 9 ]
			then
				CONTROLMSG=$"Deny access"
				COLOUR=#096F16
				ACTION=deny
			if [ -f /opt/karoshi/server_network/internet_room_controls/"$LOCATION/$ASSET" ]
			then
				CONTROLMSG=$"Allow access"
				COLOUR=#FF0000
				ACTION=allow
			fi

			CONTROLMSG2=$"Deny media access"
			COLOUR2=#096F16
			ACTION2=denymedia
			if [ -f /opt/karoshi/server_network/internet_media_room_controls/"$LOCATION/$ASSET"_media ]
			then
				CONTROLMSG2=$"Allow media access"
				COLOUR2=#FF0000
				ACTION2=allowmedia
			fi


			echo '<tr><td>'"$ASSET"'</td>'

			[ "$MOBILE" = no ] && echo '<td>'"$MAC1"'</td><td>'"$TCPIP1"'</td>'

			echo '<td><form action="/cgi-bin/admin/dg_room_controls2.cgi" method="post">
			<input name="_ACTION_'"$ACTION"'_LOCATION_'"$LOCATION"'_ASSET_'"$ASSET"'_" type="submit" class="button" style="color:'"$COLOUR"';" value="'"$CONTROLMSG"'"></form></td>

			<td><form action="/cgi-bin/admin/dg_room_controls2.cgi" method="post"><input name="_ACTION_'"$ACTION2"'_LOCATION_'"$LOCATION"'_ASSET_'"$ASSET"'_" type="submit" class="button" style="color:'"$COLOUR2"';" value="'"$CONTROLMSG2"'"></form></td>
			</tr>
			'
			fi
		done
	fi
fi
echo '</tbody></table></div>'
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></body></html>'
exit
