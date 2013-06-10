#!/bin/bash
#Copyright (C) 2011  Paul Sharrad
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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/ksso ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/ksso
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE3'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body onLoad="start()">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR

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
DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/admin/ksso_delete.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE3'</b></a></td></tr></tbody></table><br>'
else
echo '<b>'$TITLE3'</b><br><br>'
fi

if [ $MOBILE = yes ]
then
echo '

'$LOGONPAGEMSG'<br>
<input tabindex= "1" style="width: 160px;" name="_LOGONPAGE_" 
 size="20" type="text"><br>
'
else
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 180px;"><b>'$ENTRYMSG'</b></td><td><b>'$DELETETITLE'</b></td></tr>'

#Show list of entries
ICON1=/images/submenus/file/delete.png
if [ -d /opt/karoshi/server_network/ksso/data/ ]
then
if [ `ls -1 /opt/karoshi/server_network/ksso/data/ | wc -l` -gt 0 ]
then
for ENTRIES in /opt/karoshi/server_network/ksso/data/*
do
ENTRY=`basename $ENTRIES`
echo '<tr><td>'$ENTRY'</td><td><a class="info" href="javascript:void(0)"><input name="_ENTRY_'$ENTRY'_" type="image" class="images" src="'$ICON1'" value=""><span>'$DELETETITLE - $ENTRY'</span></a></td></tr>'
done
fi
fi
echo '</tbody></table><br>'
fi
echo '</div></form></body></html>'
exit
