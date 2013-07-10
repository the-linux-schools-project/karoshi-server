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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/internet_access_controls ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/internet_access_controls
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body>'
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
echo '                window.location = "/cgi-bin/admin/client_boot_controls_fm.cgi";'
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
MESSAGE=$ERRORMSG8
show_status
fi

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
fi
echo '<div id="'$DIV_ID'">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/client_boot_controls.cgi | cut -d' ' -f1`
echo '<form action="/cgi-bin/admin/internet_access_controls2.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then

ICON1=/images/submenus/internet/internet_banm.png
ICON2=/images/submenus/internet/internet_allowm.png

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/internet_access_controls_fm.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><b>'$LOCATION'</b> <a class="info" href="javascript:void(0)"><input name="_ACTION_banall_ASSET_none_TCPIP_none_MACADDRESS_none_" type="image" class="images" src="'$ICON1'" value=""><span>'$BAN_ALLMSG'</span></a> <a class="info" href="javascript:void(0)"><input name="_ACTION_allowall_ASSET_none_TCPIP_none_MACADDRESS_none_" type="image" class="images" src="'$ICON2'" value=""><span>'$ALLOWALLMSG'</span></a></td></tr></tbody></table>'
else

ICON1=/images/submenus/internet/internet_ban.png
ICON2=/images/submenus/internet/internet_allow.png

echo '<b>'$LOCATION'</b> <a class="info" href="javascript:void(0)"><a class="info" href="javascript:void(0)"><input name="_ACTION_banall_ASSET_none_TCPIP_none_MACADDRESS_none_" type="image" class="images" src="'$ICON1'" value=""><span>'$BAN_ALLMSG'</span></a> <a class="info" href="javascript:void(0)"><input name="_ACTION_allowall_ASSET_none_TCPIP_none_MACADDRESS_none_" type="image" class="images" src="'$ICON2'" value=""><span>'$ALLOWALLMSG'</span></a><br><br>'
fi
#Get location data
sudo -H /opt/karoshi/web_controls/exec/internet_access_controls $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$LOCATION:$MOBILE

echo '</form>'
echo "</div>"
echo "</body></html>"
exit
