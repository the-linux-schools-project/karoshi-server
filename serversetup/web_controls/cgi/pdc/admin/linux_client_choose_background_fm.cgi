#!/bin/bash
#Copyright (C) 2012  Paul Sharrad

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
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Linux Client Background"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH1=180
	WIDTH2=480
	HEIGHT=300
	CHARS=25
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=mobileactionbox
	TABLECLASS=mobilestandard
	WIDTH1=90
	WIDTH2=192
	HEIGHT=120
	CHARS=11
fi


[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Linux Client Background"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="'"$DIV_ID"'">'
else

	WIDTH=100
	ICON1=/images/submenus/client/upload.png

	echo '
	<div class="sectiontitle">'$"Linux Client Background"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Linux_Client_Background"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the background that you want for your linux clients."'</span></a></div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<form action="/cgi-bin/admin/linux_client_background_upload_fm.cgi" method="post">
				<button class="info" name="_UPLOAD_" value="_">
					<img src="'$ICON1'" alt="'$"Upload Background"'">
					<span>'$"Upload a new background."'</span><br>
					'$"Upload Background"'
				</button>
			</form>
		</td>

	</tr></tbody></table></form>
	<br></div><div id="infobox">'
fi

function show_status {
echo '<script>'
echo 'alert("'"$MESSAGE"'");'
echo 'window.location = "/cgi-bin/admin/linux_client_choose_background_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function upload_background {
echo '<script>'
echo 'alert("'"$MESSAGE"'");'
echo 'window.location = "/cgi-bin/admin/linux_client_background_upload_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#Check to see if any backgrounds have been uploaded
if [ ! -d /var/lib/samba/netlogon/linuxclient/backgrounds ]
then
	MESSAGE=$"No client backgrounds have been uploaded."
	upload_background
fi

if [[ $(ls -1 /var/lib/samba/netlogon/linuxclient/backgrounds | wc -l) = 0 ]]
then
	MESSAGE=$"No client backgrounds have been uploaded."
	upload_background
fi

echo '<form action="/cgi-bin/admin/linux_client_choose_background.cgi" method="post"><table class="'"$TABLECLASS"'" style="text-align: left;" ><tbody>'

#Get the default background
DEFAULTBACKGROUND=notset
[ -f /var/lib/samba/netlogon/linuxclient/backgrounds/defaultbackground ] && source /var/lib/samba/netlogon/linuxclient/backgrounds/defaultbackground

for BACKGROUNDS in /var/lib/samba/netlogon/linuxclient/backgrounds/*.png
do
	BACKGROUND=$(basename "$BACKGROUNDS" | sed 's/.png$//g')
	BACKGROUND_SHORT="${BACKGROUND:0:$CHARS}"
	if [ "$BACKGROUND" = "$DEFAULTBACKGROUND" ]
	then
		echo '<tr><td style="width: '"$WIDTH1"'px; vertical-align: top; background-color: rgb(204, 0, 0); text-align: left;"><b>'$"Default Background"'</b><br><br>'"$BACKGROUND_SHORT"'</td><td>

		<button class="info" name="___ChooseBackground___" value="___ACTION___choose___BACKGROUND___'"$BACKGROUND"'___">
		<img src="/images/linuxclient/backgrounds/'"$BACKGROUND"'.png" style="width:'"$WIDTH2"'px;height:'"$HEIGHT"'px;" alt="'"$BACKGROUND"'">
		<span>'"$BACKGROUND"'</span>
		</button>
		</td></tr>'
	else
		echo '<tr><td style="width: '"$WIDTH1"'px; vertical-align: top; text-align: left;">'"$BACKGROUND_SHORT"'</td><td>
		<button class="info" name="___ChooseBackground___" value="___ACTION___choose___BACKGROUND___'"$BACKGROUND"'___">
		<img src="/images/linuxclient/backgrounds/'"$BACKGROUND"'.png" style="width:'"$WIDTH2"'px;height:'"$HEIGHT"'px;" alt="'"$BACKGROUND"'">
		<span>'"$BACKGROUND"'</span>
		</button>
		</td><td style="width: '"$WIDTH1"'px; vertical-align: top;">
		<button class="info" name="___DeleteBackground___" value="___delete___BACKGROUND___'"$BACKGROUND"'___">
		<img src="/images/submenus/file/delete.png" alt="'$"Delete"'<br>'"$BACKGROUND"'">
		<span>'$"Delete"'<br>'"$BACKGROUND"'</span>
		</button>
		</td></tr>'
	fi
done

echo '</tbody></table></form><br></div></div>'
[ "$MOBILE" = no ] && echo '</div>'
echo '</body></html>'
exit
