#!/bin/bash
#Copyright (C) 2007 Paul Sharrad
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/asset_register ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/asset_register
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE6'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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

echo '</head><body onLoad="start()">'
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
echo "</body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
fi

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: left" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE6'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$CLIENTMENUMSG'</a>
</div></div><div id="mobileactionbox">
'
else
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tr><td style="vertical-align: top;"><b>'$TITLE6'</b></td></tr></tbody></table><br>'
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
ICON6=/images/assets/search.png
echo '<form action="/cgi-bin/admin/client_boot_controls.cgi" method="post"><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: '$WIDTH'px;">'$SEARCHMSG'</td><td><input tabindex= "1" name="_LOCATION_SEARCHNOTVALID_SEARCH_" style="width: 200px;" size="20" type="text"></td><td><a class="info" href="javascript:void(0)"><input name="_BUTTON_" type="image" class="images" src="'$ICON6'" value=""><span>'$SEARCHMSG'</span></a></td></tr></tbody></table></form><br><br>'


echo ''$CHOOSELOCATIONMSG'<br><form action="/cgi-bin/admin/client_boot_controls.cgi" method="post"><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
LOCCOUNTER=1
ICON1=/images/assets/location.png
for LOCATIONS in /opt/karoshi/asset_register/locations/*
do
LOCATION=`basename "$LOCATIONS"`

echo '<td style="width: '$WIDTH'px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_LOCATION_'$LOCATION'_" type="image" class="images" src="'$ICON1'" value=""><span>'$TITLE6'<br>'$LOCATION'</span></a><br>'$LOCATION'</td>'
[ $LOCCOUNTER = $ROWCOUNT ] && echo '</tr><tr>'
let LOCCOUNTER=$LOCCOUNTER+1
[ $LOCCOUNTER -gt $ROWCOUNT ] && LOCCOUNTER=1
done

echo "</tr></tbody></table></form><br>"
fi
else
echo $ERRORMSG18
fi
else
echo $ERRORMSG18
fi
echo '</div></body></html>'
exit
