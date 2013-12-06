#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_room_controls ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_room_controls
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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

echo '</head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\+-'`
#########################
#Assign data to variables
#########################
END_POINT=6

#Assign _LOCATION_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LOCATIONcheck ]
then
let COUNTER=$COUNTER+1
LOCATION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/dg_room_controls_fm.cgi";'
echo '</script>'
echo "</body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$ERRORMSG7
show_status
fi

#########################
#Check data
#########################

#Check to see that LOCATION is not blank
if [ $LOCATION'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi


#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
TABLECLASS=standard
WIDTH=60
WIDTH2=120
WIDTH3=120
TABLETITLE="$TITLE - $LOCATION"
ICON1=/images/submenus/internet/client_allowed.png
ICON2=/images/submenus/internet/client_denied.png
ICON3=/images/assets/location.png
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="'$DIV_ID'"><div id="titlebox"><b>'$TABLETITLE'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Room_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a><br>'
else
DIV_ID=menubox
TABLECLASS=mobilestandard
WIDTH=60
WIDTH2=90
WIDTH3=110
TABLETITLE="$LOCATION"
ICON1=/images/submenus/internet/client_allowedm.png
ICON2=/images/submenus/internet/client_deniedm.png
ICON3=/images/assets/locationm.png

echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/dg_room_controls_fm.cgi">'$LOCATION'</a>
</div></div><div id="mobileactionbox">
'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tr><td style="vertical-align: top;"><form action="/cgi-bin/admin/dg_room_controls_fm.cgi" method="post">
<input name="" type="submit" class="button" value="'$CHOOSELOCATIONMSG'">
</form></td>
<td valign=top>
<a href="dg_reset_room_controls_fm.cgi"><input class="button" type="button" name="" value="'$RESETTIMESMSG'"></a>
</td>'

[ $MOBILE = yes ] && echo '</tr><tr>'

echo '<td style="vertical-align: top;"><form action="/cgi-bin/admin/dg_room_controls2.cgi" method="post">
<input name="_LOCATION_'$LOCATION'_ACTION_allowall_ASSET_na_" type="submit" class="button" value="'$ALLOWALLMSG'">
</form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/dg_room_controls2.cgi" method="post">
<input name="_LOCATION_'$LOCATION'_ACTION_denyall_ASSET_na_" type="submit" class="button" value="'$DENYALLMSG'">
</form></td>
</tr></table><br>'

[ $MOBILE = no ] && echo '</div><div id="infobox">'

if [ -d /opt/karoshi/asset_register/locations/$LOCATION/ ]
then
if [ `ls -1 /opt/karoshi/asset_register/locations/$LOCATION/ | wc -l` -gt 0 ]
then
echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: '$WIDTH'px;"><b>'$ASSETMSG'</b></td>'

[ $MOBILE = no ] && echo '<td style="width: '$WIDTH2'px;"><b>'$MACADDRESSMSG'</b></td>'

echo '<td style="width: '$WIDTH3'px;"><b>'$TCPIPMSG'</b></td><td><b>'$ACTIONMSG'</b></td></tr>'

for ASSETS in "/opt/karoshi/asset_register/locations/$LOCATION/"*
do
ASSET=`basename $ASSETS`
source /opt/karoshi/asset_register/locations/$LOCATION/$ASSET
#Only show certain asset types
if [ $ASSETTYPE = 1 ] || [ $ASSETTYPE = 3 ] || [ $ASSETTYPE = 5 ] || [ $ASSETTYPE = 7 ] || [ $ASSETTYPE = 9 ]
then
CONTROLMSG=$DENYMSG
COLOUR=#11BE26
ACTION=deny
if [ -f /opt/karoshi/server_network/internet_room_controls/$LOCATION/$ASSET ]
then
CONTROLMSG=$ALLOWMSG
COLOUR=#FF0000
ACTION=allow
fi
echo '<tr><td valign="top"><font color="'$COLOUR'"><b>'$ASSET'</b></font></td>'

[ $MOBILE = no ] && echo '<td valign="top"><font color="'$COLOUR'"><b>'$MAC1'</b></font></td>'

echo '<td valign="top"><font color="'$COLOUR'"><b>'$TCPIP1'</b></font></td><td valign="top"><form action="/cgi-bin/admin/dg_room_controls2.cgi" method="post">
<input name="_ACTION_'$ACTION'_LOCATION_'$LOCATION'_ASSET_'$ASSET'_" type="submit" class="button" value="'$CONTROLMSG'"></form></td></tr>
'
fi
done
fi
fi

echo '</tbody></table></div>'
[ $MOBILE = no ] && echo '</div>'
echo '</body></html>'
exit
