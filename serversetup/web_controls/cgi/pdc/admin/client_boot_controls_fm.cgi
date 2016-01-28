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

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
	TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Client Boot Controls"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
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
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/view_karoshi_web_admin_log.cgi";'
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

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	ICON1=/images/assets/location.png
	ICON6=/images/assets/search.png
	SEARCHW=200
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
	ICON1=/images/assets/locationm.png
	ICON6=/images/assets/searchm.png
	SEARCHW=150
fi

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Client Boot Controls"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
else
	echo '<b>'$"Client Boot Controls"'</b><br><br></div><div id="infobox">'
fi

if [ -f /var/lib/samba/netlogon/locations.txt ]
then
	LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
else
	LOCATION_COUNT=0
fi

if [ $LOCATION_COUNT != 0 ]
then
	if [ -d /opt/karoshi/asset_register/locations/ ]
	then
		if [ `ls -1 /opt/karoshi/asset_register/locations/ | wc -l` -gt 0 ]
		then
			ROWCOUNT=6
			[ $MOBILE = yes ] && ROWCOUNT=3
			WIDTH=90
			[ $MOBILE = yes ] && WIDTH=70

			echo '<form action="/cgi-bin/admin/client_boot_controls.cgi" method="post"><table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
			<tr><td style="width: '$WIDTH'px;">'$"Search"'</td><td><input tabindex= "1" name="_LOCATION_SEARCHNOTVALID_SEARCH_" style="width: '$SEARCHW'px;" size="20" type="text"></td><td>

			<button class="info" name="_Search_" value="_BUTTON_">
			<img src="'$ICON6'" alt="'$"Search"'">
			<span>'$"Search"'</span>
			</button>
			</td></tr></tbody></table></form><br>'


			echo ''$"Choose Location"'<br><form action="/cgi-bin/admin/client_boot_controls.cgi" method="post"><table class="'$TABLECLASS'" style="text-align: left;" ><tbody><tr>'
			LOCCOUNTER=1

			for LOCATIONS in /opt/karoshi/asset_register/locations/*
			do
				LOCATION=`basename "$LOCATIONS"`

				echo '<td style="width: '$WIDTH'px; vertical-align: top; text-align: center;">

			<button class="info" name="_ShowLocation_" value="_LOCATION_'$LOCATION'_">
			<img src="'$ICON1'" alt="'$LOCATION'">
			<span>'$"Client Boot Controls"'<br>'$LOCATION'</span>
			</button>
			<br>'$LOCATION'</td>'
				[ $LOCCOUNTER = $ROWCOUNT ] && echo '</tr><tr>'
				let LOCCOUNTER=$LOCCOUNTER+1
				[ $LOCCOUNTER -gt $ROWCOUNT ] && LOCCOUNTER=1
				done

			echo "</tr></tbody></table></form><br>"
		fi
	else
		echo $"The asset register is not in use."
	fi
else
	echo $"The asset register is not in use."
fi
[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
