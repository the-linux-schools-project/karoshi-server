#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Ban E-Mail Domain"'</title><META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE"><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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

echo '</head>
<body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
WIDTH1=200
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
TABLECLASS=mobilestandard
WIDTH1=160
fi
echo '<form name="myform" action="/cgi-bin/admin/email_ban_domain.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Ban E-Mail Domain"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox"><table class="mobilestandard" style="text-align: left;" ><tbody><tr><td style="vertical-align: middle; height: 20px;">
<td style="vertical-align: top;">
<a href="email_view_banned_domains_fm.cgi"><input class="button" type="button" name="" value="'$"Banned Domains"'"></a>
</td></tr>
</tbody></table><br>
'
else
echo '<div id="'$DIV_ID'">
<table class="standard" style="text-align: left;" ><tbody><tr><td style="vertical-align: middle; height: 20px;"><b>'$"Ban E-Mail Domain"'</b></td>
<td style="vertical-align: top;">
<a href="email_view_banned_domains_fm.cgi"><input class="button" type="button" name="" value="'$"Banned Domains"'"></a>
</td></tr>
</tbody></table><br>'
fi

echo '
<table class="'$TABLECLASS'" style="text-align: left;" >
<tbody><tr><td style="width: 180px;">'$"E-Mail Domain"'</td><td><input tabindex= "1" name="_EMAILDOMAIN_" style="width: '$WIDTH1'px;" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the E-mail domain that you want to ban."'<br><br>'$"This will stop emails from being delivered from the domain."'</span></a></td></tr>
<tr><td>'$"Reject"'</td><td><input type="radio" name="_DROPTYPE_" value="REJECT" checked></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This option will send a rejected message back to the sender."'</span></a></td></tr>
<tr><td>'$"Discard"'</td><td><input type="radio" name="_DROPTYPE_" value="DISCARD"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This option will silently drop messages without delivering them or notifying the sender."'</span></a></td></tr>
</tbody></table><br>'


if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi
echo '<input value="'$"Submit"'" class="button" type="submit">
</div></form></div></body></html>
'
exit

