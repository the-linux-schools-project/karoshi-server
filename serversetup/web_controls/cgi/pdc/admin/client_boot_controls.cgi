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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE6'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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

echo '</head><body><div id="pagecontainer">'
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

#Assign _SEARCH_
if [ $LOCATION'null' = SEARCHNOTVALIDnull ]
then
END_POINT=8

COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SEARCHcheck ]
then
let COUNTER=$COUNTER+1
SEARCH=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
fi

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/client_boot_controls_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
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
#########################
#Check data
#########################

#Check to see that LOCATION is not blank
if [ $LOCATION'null' = null ]
then
MESSAGE=$ERRORMSG7
show_status
fi

if [ $LOCATION'null' = SEARCHNOTVALIDnull ]
then
#Check to see that SEARCH is not blank
if [ $SEARCH'null' = null ]
then
MESSAGE=$ERRORMSG9
show_status
fi
LOCATION=$SEARCH
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
TABLECLASS=standard
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
fi

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE6'</span>
<a href="/cgi-bin/admin/client_boot_controls_fm.cgi">'$LOCATION'</a>
</div></div><div id="mobileactionbox">
'
ICON1=/images/submenus/client/activate_changesm.png
ICON2=/images/submenus/client/wakeupallm.png
ICON3=/images/submenus/client/reset_allm.png
ICON4=/images/assets/locationm.png

echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/client_boot_controls2.cgi" method="post">
<input name="_ACTION_activatechanges_LOCATION_'$LOCATION'_ASSET_none_TCPIP_none_MACADDRESS_none_" type="submit" class="button" value="'$ACTIVATECHANGESMSG'">
</form></td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/client_boot_controls2.cgi" method="post">
<input name="_ACTION_resetall_LOCATION_'$LOCATION'_ASSET_none_TCPIP_none_MACADDRESS_none_" type="submit" class="button" value="'$RESETALLMSG'">
</form></td>
</tr></tbody></table>'

else
ICON1=/images/submenus/client/activate_changes.png
ICON2=/images/submenus/client/wakeupall.png
ICON3=/images/submenus/client/reset_all.png
ICON4=/images/assets/location.png

echo '<b>'$TITLE6' - '$LOCATION'</b><br><br><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tr><td style="vertical-align: top;">
<form action="/cgi-bin/admin/client_boot_controls_fm.cgi" method="post">
<input name="_LOCATION_NOTSET_" type="submit" class="button" value="'$CHOOSELOCATIONMSG'">
</form></td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/client_boot_controls2.cgi" method="post">
<input name="_ACTION_activatechanges_LOCATION_'$LOCATION'_ASSET_none_TCPIP_none_MACADDRESS_none_" type="submit" class="button" value="'$ACTIVATECHANGESMSG'">
</form></td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/client_boot_controls2.cgi" method="post">
<input name="_ACTION_resetall_LOCATION_'$LOCATION'_ASSET_none_TCPIP_none_MACADDRESS_none_" type="submit" class="button" value="'$RESETALLMSG'">
</form></td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/client_boot_controls2.cgi" method="post">
<input name="_ACTION_wakeonlanall_LOCATION_'$LOCATION'_ASSET_none_TCPIP_none_MACADDRESS_none_" type="submit" class="button" value="'$WAKEONLANALLMSG'">
</form></td></tr></table>'
fi
[ $MOBILE = no ] && echo '</div><div id="infobox">'
echo '<form action="/cgi-bin/admin/client_boot_controls2.cgi" method="post">'
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/client_boot_controls.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/client_boot_controls $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$LOCATION:$SEARCH:$MOBILE:

echo '</form>'
[ $MOBILE = no ] && echo '</div>'
echo "</div></div></body></html>"
exit
