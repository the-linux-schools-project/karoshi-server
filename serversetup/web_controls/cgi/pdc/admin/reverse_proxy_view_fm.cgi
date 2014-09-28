#!/bin/bash
#Copyright (C) 2010  Paul Sharrad

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

WIDTH1=180
WIDTH2=180
WIDTH3=300
TABLECLASS=standard
ICON1=/images/submenus/web/delete.png
if [ $MOBILE = yes ]
then
	WIDTH1=180
	WIDTH2=90
	WIDTH3=300
	TABLECLASS=mobilestandard
	ICON1=/images/submenus/web/deletem.png
fi

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Reverse Proxy Sites"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script type="text/javascript" src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
		***********************************************/
	</script>
	<script type="text/javascript">
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head>
<body onLoad="start()"><div id="pagecontainer">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "reverse_proxy_add_fm.cgi"'
echo '</script>'
echo "</div></body></html>"
exit
}

#Check to see if there are any proxy sites
if [ ! -d /opt/karoshi/server_network/reverseproxy/sites/ ]
then
	MESSAGE=$"No web sites have been added to the reverse proxy list."
	show_status
fi

if [ `ls -1 /opt/karoshi/server_network/reverseproxy/sites/ | wc -l` = 0 ]
then
	MESSAGE=$"No web sites have been added to the reverse proxy list."
	show_status
fi

#Get reverse proxy server
PROXYSERVER=`sed -n 1,1p /opt/karoshi/server_network/reverseproxyserver | sed 's/ //g'`

if [ -z "$PROXYSERVER" ]
then
	MESSAGE=$"A reverse proxy server has not been setup."
	show_status
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox
fi

echo '<form action="/cgi-bin/admin/reverse_proxy_view.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"Reverse Proxy Sites"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="mobileactionbox">
'
else
	echo '<div id="'$DIV_ID'"><div id="titlebox">'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tr>'
[ $MOBILE = no ] && echo '<td style="width: '$WIDTH1'px; vertical-align: top;"><div class="sectiontitle">'$"Reverse Proxy Sites"'</div></td>'
echo '<td style="vertical-align: top;"><a href="reverse_proxy_add_fm.cgi"><input class="button" type="button" name="" value="'$"Add Reverse Proxy"'"></a></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Reverse_Proxy_Server#Viewing_and_Deleting_Reverse_Proxy_Entries"><img class="images" alt="" src="/images/help/info.png"><span>'$"The following sites are currently being redirected through this proxy server."'</span></a></td>
</tr></tbody></table><br>'

[ $MOBILE = no ] && echo '</div><div id="infobox">'

echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'

[ $MOBILE = no ] && echo '<td style="width: '$WIDTH2'px;"><b>'$"Target"'</b></td>'
echo '<td style="width: '$WIDTH3'px;"><b>'$"Destination"'</b></td><td><b>'$"Delete"'</b></td></tr>'

for SITES in /opt/karoshi/server_network/reverseproxy/sites/*
do
	SITE=`basename $SITES`
	SITE2=`echo $SITE | sed 's/%3A//g' | sed 's/%2F/\//g' | sed 's/\/\///g'`
	REDIRECT=`sed -n 6,6p /opt/karoshi/server_network/reverseproxy/sites/$SITE | cut -d' ' -f2- | sed 's/;//g'`
	echo '<tr>'
	[ $MOBILE = no ] && echo '<td>'$SITE2'</td>'
	echo '<td>'$REDIRECT'</td><td><a class="info" href="javascript:void(0)"><input name="_ACTION_DELETE_FOLDER_'$SITE'_" type="image" class="images" src="'$ICON1'" value="_ACTION_DELETE_FOLDER_'$SITE'_"><span>'$"Delete" $SITE2'</span></a></td></tr>'
done

echo '</tbody></table><br></div>'

[ $MOBILE = no ] && echo '</div>'

echo '</form></div></body></html>
'
exit
