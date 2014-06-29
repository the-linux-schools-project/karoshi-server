#!/bin/bash
#

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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_media_controls ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_media_controls
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
FILE=`echo $DATA | cut -s -d_ -f7`

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
DIV_ID=navbar
/opt/karoshi/web_controls/generate_navbar_admin_mobile
fi
echo '<form action="/cgi-bin/admin/dg_media_controls.cgi" method="post"><div id="'$DIV_ID'">'
echo ""

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_user_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><b>'$TITLE'</b></td></tr></tbody></table>'
else
echo '<div class="sectiontitle">'$TITLE'</div><br>'
fi

ICON1=/images/submenus/internet/allowed_sites.png
ACTION1=BAN
#Test
if [ -f /opt/karoshi/server_network/dansguardian/media_controls/no_student_flash ]
then
ICON1=/images/submenus/internet/banned_sites.png
ACTION1=ALLOW
fi

ICON2=/images/submenus/internet/allowed_sites.png
ACTION2=BAN
if [ -f /opt/karoshi/server_network/dansguardian/media_controls/no_staff_flash ]
then
ICON2=/images/submenus/internet/banned_sites.png
ACTION2=ALLOW
fi

echo '
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 180px;">
<b>'$MEDIATYPEMSG'</b></td><td><b>'$STUDENTSTITLE'</b></td><td><b>'$STAFFTITLE'</b></td></tr> 
<tr><td>Flash</td><td><a class="info" href="javascript:void(0)"><input name="_MEDIAFILTER_flash_GROUP_student_ACTION_'$ACTION1'_" type="image" class="images" src="'$ICON1'" value=""><span>'$HELPMSG1'</span></a></td>


<td><a class="info" href="javascript:void(0)"><input name="_MEDIAFILTER_flash__GROUP_staff_ACTION_'$ACTION2'_" type="image" class="images" src="'$ICON2'" value=""><span>'$HELPMSG2'</span></a></td></tr>

</tbody></table></div></form></div></body></html>'

exit

