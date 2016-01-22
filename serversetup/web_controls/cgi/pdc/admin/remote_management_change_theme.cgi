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
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Change Theme"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	MAXSTYLES=3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=mobileactionbox
	TABLECLASS=mobilestandard
	MAXSTYLES=1
fi

echo '<form action="/cgi-bin/admin/remote_management_change_theme2.cgi" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Change Theme"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="'$DIV_ID'">'
else
	echo '<table class="standard" style="text-align: left;" ><tbody><tr>
<td style="vertical-align: top;"><div class="sectiontitle">'$"Change Theme"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Web_Management_Themes"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the theme that you want for the Web Management."'<br><br>'$"This will not affect other web management users."'</span></a></td></tr></tbody></table><br></div><div id="infobox">'
fi

STYLESHEET2=`echo $STYLESHEET | cut -d. -f1`
echo $"Current theme": $STYLESHEET2"<br><br>"

echo '<table class="'$TABLECLASS'" style="text-align: left;" ><tbody><tr>'

STYLESHEET=`echo $STYLESHEET | cut -d. -f1`
STYLECOUNT=1
for THEMES in /var/www/html_karoshi/images/theme_preview/*
do

	STYLESHEETCHOICE=`basename $THEMES | sed 's/.png//g'`
	if [ $STYLESHEETCHOICE != $STYLESHEET ]
	then
		echo '<td style="width: 90px; vertical-align: top; height: 160px; text-align: left;">
		<button class="info" name="_SetTheme_" value="_THEMECHOICE_'$STYLESHEETCHOICE'_">
		<img style="width: 330px;" src="/images/theme_preview/'$STYLESHEETCHOICE'.png" alt="'$STYLESHEETCHOICE'">
		<span>'$STYLESHEETCHOICE'</span>
		</button>
		</td>'
		let STYLECOUNT=$STYLECOUNT+1
	fi
	if [ $STYLECOUNT -gt $MAXSTYLES ]
	then
		echo '</tr><tr>'
		STYLECOUNT=1
	fi
done
[ $STYLECOUNT = 1 ] && echo "<td></td>"
echo '</tr></tbody></table><br>'

[ $MOBILE = no ] && echo '</div>'

echo '</div></form></div></body></html>'
exit
