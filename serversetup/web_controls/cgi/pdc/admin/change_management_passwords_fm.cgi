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
  <title>'$"Management Passwords"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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

echo '<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
</head><body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
if [ $MOBILE = no ]
then
	TOOLTIPCLASS="info"
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH1=192
	WIDTH2=200
	HEIGHT1=25
	HEIGHT2=25
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	TOOLTIPCLASS="info infoleft"
	DIV_ID=actionbox
	TABLECLASS=mobilestandard
	WIDTH1=140
	WIDTH2=140
	HEIGHT1=30
	HEIGHT2=30
fi

echo '<form action="/cgi-bin/admin/change_management_passwords.cgi" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'


#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Management Passwords"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
else
	echo '<b>'$"Management Passwords"'</b> <a class="'$TOOLTIPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Management_Passwords"><img class="images" alt="" src="/images/help/info.png"><span>'$"This is used to change important passwords on your system that are needed to access specific services."'</span></a>
<br><br>'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">System Password</td><td>
<select name="____USERACCOUNT____"  tabindex="1" style="width: '$WIDTH2'px; height: '$HEIGHT2'px;">
<option label="blank"></option>
<option>karoshi</option>
<option>Administrator</option>
<option>mysql</option>
'
#<option value="sambaroot">Samba Root</option>
echo '<option>root</option>
</select></td><td><a class="'$TOOLTIPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Management_Passwords"><img class="images" alt="" src="/images/help/info.png"><span><b>Karoshi</b> - '$"This is the account used to log in locally to the servers."'<br><br><b>administrator</b> - '$"This password is needed to join the clients to the domain."'<br><br><b>Root</b> - '$"You should not normally need to use this password."'</span></a>
</td></tr>
<tr><td>'$"New Password"'</td><td><input name="____PASSWORD1____"  tabindex="2" size="20" style="width: '$WIDTH1'px; height: '$HEIGHT1'px;" type="password"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Management_Passwords"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the pasword that you want to use."'<br><br><b>'$"Special Characters"'</b><br><br>'$CHARACTERHELP' space !	&quot;	# 	$	%	&amp; 	(	) 	*	+	, 	-	.	/ 	:
;	&lt;	=	&gt;	?	@ 	[	\	]	^	_	` 	{	|	}	~
</span></a>
</td></tr>
<tr><td>'$"Confirm Password"'</td><td><input name="____PASSWORD2____"  tabindex="3" size="20" style="width: '$WIDTH1'px; height: '$HEIGHT1'px;" type="password"></td><td></td></tr>
</tbody></table><br><br>'

[ $MOBILE = no ] && echo '</div><div id="infobox">'

#Show list of servers
/opt/karoshi/web_controls/show_servers $MOBILE all $"Change password" no no ____

[ $MOBILE = no ] && echo '</div>'

echo '</div></form></div></body></html>'
exit

