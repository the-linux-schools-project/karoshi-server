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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Linux Client Software Controls"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
'

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

echo '</head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/linux_client_software_controls_fm.cgi";'
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

#Assign VERSION
DATANAME=VERSION
get_data
VERSION="$DATAENTRY"

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
fi

#########################
#Check data
#########################
#Check to see that VERSION is not blank
if [ -z "$VERSION" ]
then
	MESSAGE=$"The linux version must not be blank."
	show_status
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Linux Client Software Controls"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
else
	WIDTH=100
	ICON1=/images/submenus/client/software.png

	echo '<form action="/cgi-bin/admin/linux_client_install_software_packages.cgi" name="selectservers" method="post">
<input name="_VERSION_" value="'"$VERSION"'" type="hidden">

	<div class="sectiontitle">'$"Linux Client Software Controls"' - '"$VERSION"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Linux_Client_Software_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the locations that you want to enable updates and software installs for."'</span></a></div>

	<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info infonavbutton" name="_UPLOAD_" value="_">
				<img src="'$ICON1'" alt="'$"Software Packages"'">
				<span>'$"View software packages."'</span><br>
				'$"Software Packages"'
			</button>
	</td>

	</tr></tbody></table>
	</form></div><div id="infobox"><form action="/cgi-bin/admin/linux_client_software_controls2.cgi" name="selectservers" method="post">'
fi

function show_software_status {
#Check current settings
if [ -f "/var/lib/samba/netlogon/linuxclient/$VERSION/software/install/$LOCATION"_install ]
then
	SICON="/images/submenus/client/allowed.png"
	SSTATUS=no
else
	SICON="/images/submenus/client/denied.png"
	SSTATUS=yes
fi
if [ -f "/var/lib/samba/netlogon/linuxclient/$VERSION/software/install/$LOCATION"_updates ]
then
	UICON="/images/submenus/client/allowed.png"
	USTATUS=no
else
	UICON="/images/submenus/client/denied.png"
	USTATUS=yes
fi

#if [ -f /var/lib/samba/netlogon/linuxclient/nonfree/auto ]
#then
#	AICON="/images/submenus/client/allowed.png"
#	ASTATUS=no
#else
#	AICON="/images/submenus/client/denied.png"
#	ASTATUS=yes
#fi
#if [ -f /var/lib/samba/netlogon/linuxclient/nonfree/graphics-drivers ]
#then
#	GICON="/images/submenus/client/allowed.png"
#	GSTATUS=no
#else
#	GICON="/images/submenus/client/denied.png"
#	GSTATUS=yes
#fi
#if [ -f /var/lib/samba/netlogon/linuxclient/nonfree/restricted-extras ]
#then
#	RICON="/images/submenus/client/allowed.png"
#	RSTATUS=no
#else
#	RICON="/images/submenus/client/denied.png"
#	RSTATUS=yes
#fi
#if [ -f /var/lib/samba/netlogon/linuxclient/nonfree/firmware-nonfree ]
#then
#	FICON="/images/submenus/client/allowed.png"
#	FSTATUS=no
#else
#	FICON="/images/submenus/client/denied.png"
#	FSTATUS=yes
#fi


echo '<tr><td>'"$LOCATION"'</td><td>'$"Enable software install"'</td><td>
<button class="info" name="_SoftwareInstall_" value="_SOFTWARE_'"$SSTATUS"'_LOCATION_'"$LOCATION"'_">
<img src="'"$SICON"'" alt="'$"Install"'">
<span>'$"This will make the Linux clients install any software in the software install lists on boot up."'</span>
</button>
</td></tr>
<tr><td>'"$LOCATION"'</td><td>'$"Enable updates"'</td><td>
<button class="info" name="_SoftwareUpdates_" value="_UPDATES_'"$USTATUS"'_LOCATION_'"$LOCATION"'_">
<img src="'"$UICON"'" alt="'$"Install"'">
<span>'$"This will make the Linux clients update their software packages on boot up."'</span>
</button>
</td></tr>'
#echo '<tr><td style="width: 180px;">'$"Auto"'</td><td><a class="info" href="javascript:void(0)"><input name="_AUTO_'$ASTATUS'_" type="image" class="images" src="'$AICON'" value=""><span>'$"Set this to auto to hide the software control dialog from appearing when setting up the clients."'</span></a></td></tr>
#<tr><td style="width: 180px;">'$"Proprietary graphics"'</td><td><a class="info" href="javascript:void(0)"><input name="_GRAPHICS_'$GSTATUS'_" type="image" class="images" src="'$GICON'" value=""><span>'$"This will tell the linux clients to install the relevant proprietary graphics driver for the client."'</span></a></td></tr>
#<tr><td style="width: 180px;">'$"Restricted extras"'</td><td><a class="info" href="javascript:void(0)"><input name="_RESTRICTED_'$RSTATUS'_" type="image" class="images" src="'$RICON'" value=""><span>'$"This will install software that in a few countries licenses may be required."'</span></a></td></tr>
#<tr><td style="width: 180px;">'$"Firmware"'</td><td><a class="info" href="javascript:void(0)"><input name="_FIRMWARE_'$FSTATUS'_" type="image" class="images" src="'$FICON'" value=""><span>'$"This will install proprietary firmware."'</span></a></td></tr>'
}

#Show controls for auto, graphics drivers and restricted extras
echo '<input name="_VERSION_" value="'"$VERSION"'" type="hidden"><table id="myTable" class="tablesorter" style="text-align: left;" ><thead><tr><th style="width: 200px;"><b>'$"Location"'</b></th><th style="width: 200px;">'$"Action"'</th><th></th></tr></thead><tbody>'

LOCATION=all
show_software_status

if [ -f /var/lib/samba/netlogon/locations.txt ]
then
	LOCATION_COUNT=$(wc -l < /var/lib/samba/netlogon/locations.txt)
else
	LOCATION_COUNT=0
fi

COUNTER=1
while [ "$COUNTER" -lt "$LOCATION_COUNT" ]
do
	LOCATION=$(sed -n "$COUNTER,$COUNTER"'p' /var/lib/samba/netlogon/locations.txt)
	show_software_status
	let COUNTER="$COUNTER"+1
done
echo '</tbody></table></form></div>'
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></body></html>'
exit

