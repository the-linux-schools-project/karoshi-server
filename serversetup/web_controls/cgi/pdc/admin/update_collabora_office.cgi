#!/bin/bash
#Change password
#Copyright (C) 2017  Paul Sharrad

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
source /opt/karoshi/server_network/security/password_settings
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER" ] && source "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER"
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
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Update Collabora Office"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/stuHover.js"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+')
#########################
#Assign data to variables
#########################
END_POINT=7
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

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

[ -z "$ACTION" ] && ACTION=view

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

#Check password settings
source /opt/karoshi/server_network/security/password_settings

echo '<form action="/cgi-bin/admin/update_collabora_office.cgi" method="post">'

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Update Collabora Office"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div>'
else
	echo '<table class="standard" style="text-align: left;" ><tbody>
	<tr><td><div class="sectiontitle">'$"Update Collabora Office"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Collabora_Office"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will update Collabora Office to the latest version."'</span></a></td></tr></tbody></table><br><br>
'
fi

if [ "$ACTION" =  update ]
then
	Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/update_collabora_office.cgi | cut -d' ' -f1)
	echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ACTION:" | sudo -H /opt/karoshi/web_controls/exec/update_collabora_office
	if [ "$?" = 0 ]
	then
		echo "<ul><li>"$"Collabora has now been updated""</li></ul>"
	fi
else
	echo 'This will update Collabora Office to the latest version.<br><br>Collabora Code version information can be viewed here:<br><br>
<a href="https://hub.docker.com/r/collabora/code/tags/" target="_blank">https://hub.docker.com/r/collabora/code/tags/</a><br><br><input type="hidden" name="_ACTION_" value="update"><br><input value="'$"Submit"'" class="button" type="submit"></div>'
fi

[ "$MOBILE" = no ] && echo '</div>'

echo '</form></div></body></html>'
exit

