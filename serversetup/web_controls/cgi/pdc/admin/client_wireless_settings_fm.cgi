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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/client_wireless_settings ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/client_wireless_settings
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all

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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE"><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
<body onLoad="start()">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
FILE=`echo $DATA | cut -s -d_ -f3`

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
WIDTH1=180
WIDTH2=200
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=mobileactionbox
TABLECLASS=mobilestandard
WIDTH1=100
WIDTH2=140
fi
echo '<form name="myform" action="/cgi-bin/admin/client_wireless_settings.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$CLIENTMENUMSG'</a>
</div></div><div id="'$DIV_ID'">
'
else
echo '<div id="'$DIV_ID'"><b>'$TITLE'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Client_Wireless_Settings"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a><br><br>'
fi
[ -f /var/lib/samba/netlogon/domain_information/wifi_ssid ] && SSID=`sed -n 1,1p /var/lib/samba/netlogon/domain_information/wifi_ssid`
[ -f /var/lib/samba/netlogon/domain_information/wifi_key ] && KEY=`sed -n 1,1p /var/lib/samba/netlogon/domain_information/wifi_key`

echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: '$WIDTH1'px;">'$SSIDMSG'</td><td>
<input tabindex= "1" value="'$SSID'" name="_SSID_" style="width: '$WIDTH2'px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Client_Wireless_Settings"><img class="images" alt="" src="/images/help/info.png"><span>'$SIDHELP'</span></a></td></tr>
<tr><td style="width: 180px;">'$KEYMSG'</td><td>
<input tabindex= "1" value="'$KEY'" name="_KEY_" style="width: '$WIDTH2'px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Client_Wireless_Settings"><img class="images" alt="" src="/images/help/info.png"><span>'$KEYHELP'</span></a></td></tr></tbody></table><br>'

[ $MOBILE != yes ] && echo '</div><div id="submitbox">'

echo '<input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div></form></body></html>
'
exit

