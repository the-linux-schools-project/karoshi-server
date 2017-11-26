#!/bin/bash
#Copyright (C) 2007  Paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
############################
#Language
############################
MOBILE=no
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
source /opt/karoshi/web_controls/version
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/server_network/domain_information/domain_name
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<META HTTP-EQUIV="refresh" CONTENT="300; URL=/cgi-bin/blank.cgi">
  <title>'$"Access Denied"'</title>
<link href="/css/'"$STYLESHEET"'" rel="stylesheet" type="text/css">'

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

echo '</head>
<body><div id="pagecontainer">'

if [ "$MOBILE" = no ]
then
	echo '<div id="header"><img src="/images/small_logo.png" alt="logo" align="top"> <font style="font-weight: bold;" size="+2">Web Management '"$SCHOOL_NAME"'</font> <small><small>
	'"$VERSIONMSG"' : '"$VERSION"'
	</small></small>
	'

	echo '</div><div id="navbar"><span class="preload1"></span>
	<span class="preload2"></span>

	<ul id="nav">
		<li class="top"><a href="/cgi-bin/menu.cgi" class="top_link"><span>Home</span></a></li>
	</ul></div>
	'

	echo '<div id="actionbox">
	<b>'"$ERRORMSG 401 - "$"Authentication required"'</b><br><br>
	'$"You are not allowed to view this page until you have supplied a correct username and password."'<br>
	</div>'
else
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'"$SHORTNAME"'</span>
        <a href="/cgi-bin/menu.cgi">'$"Home"'</a>
	<div class="a.current">
	<small><small>
	'$"Version"' : '"$VERSION"'
	</small></small>
	</div>
	</div>
	</div>
	<div id="mobileactionbox">
	<b>'"$ERRORMSG 401 - "$"Authentication required"'</b><br><br>
	'$"You are not allowed to view this page until you have supplied a correct username and password."'
	</div>'
fi
echo '</div></body></html>'
exit

