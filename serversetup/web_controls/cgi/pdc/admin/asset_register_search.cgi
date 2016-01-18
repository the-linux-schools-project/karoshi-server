#!/bin/bash
#Copyright (C) 2013  Paul Sharrad

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

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Asset Register"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

ICON1=/images/assets/edit.png
ICON2=/images/assets/client_logs.png

if [ $MOBILE = yes ]
then
ICON1=/images/assets/editm.png
ICON2=/images/assets/client_logsm.png
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
ASSET=`echo $QUERY_STRING | tr -cd '0-9'`

function show_status {
echo '<script>'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/'$STARTCGI'";'
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

USERSTATUS=notset

#Check if the user is an admin or a tech user
if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_tech` -gt 0 ]
then
	USERSTATUS=tech
fi

#Check if the user is an admin or a tech user
if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` -gt 0 ]
then
	USERSTATUS=admin
fi

if [[ "$USERSTATUS" = notset ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#Check that asset has been set
if [ -z "$ASSET" ]
then
	MESSAGE=$"You have not entered in an asset number."
	show_status
fi


#Find asset location in asset register

ASSETPATH=`find /opt/karoshi/asset_register/locations -name $ASSET`

if [ -z $ASSETPATH ]
then
	MESSAGE=$"This asset does not exist in the asset register."
	show_status
fi

LOCATION=`echo $ASSETPATH | cut -d"/" -f6`

#Generate navigation bar
if [ $MOBILE = no ]
then
TABLECLASS=standard
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_$USERSTATUS
echo '<div id="actionbox">'
fi

echo '<form action="/cgi-bin/'$USERSTATUS'/asset_register_view.cgi" method="post">'
if [ $MOBILE = yes ]
then
TABLECLASS=mobilestandard
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Asset Register"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'

fi

echo '<b>'$"Asset Register"'</b><br><br>'

#Give a choice of seeing the asset in the asset register or viewing its internet logs if available.

echo '<table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">'$"Location"'</td><td>'$LOCATION'</td></tr>
<tr><td>'$"Asset Number"'</td><td>'$ASSET'</td></tr>
<tr><td>'$"View asset"'</td><td style="vertical-align: top;"><a class="info infoleft" href="javascript:void(0)"><input name="_ACTION_edit_LOCATION_'$LOCATION'_ASSET_'$ASSET'_" type="image" class="images" src="'$ICON1'" value=""><span>'$"View asset"'</span></a></td></tr>
<tr><td>'$"View internet logs"'</td><td style="vertical-align: top;">
<a class="info infoleft" href="javascript:void(0)"><input name="_ACTION_showlogs_LOCATION_'$LOCATION'_ASSET_'$ASSET'_" type="image" class="images" src="'$ICON2'" value=""><span>View internet logs</span></a></td></tr>
</tbody></table></form></div></div></body></html>'
exit


