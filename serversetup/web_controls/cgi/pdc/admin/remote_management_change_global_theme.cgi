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
  <title>'$"Change Global Theme"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/remote_management_change_global_theme2.cgi" method="post"><div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" ><tbody><tr>
<td style="vertical-align: top;"><div class="sectiontitle">'$"Change Global Theme"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Web_Management_Themes"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the theme that you want for the Web Management."'<br><br>'$"This will affect all general web management pages."'</span></a></td></tr></tbody></table>
  <br></div><div id="infobox">
  <table class="standard" style="text-align: left;" ><tbody><tr>'

STYLESHEET=`echo $STYLESHEET | cut -d. -f1`
STYLECOUNT=1
for THEMES in /var/www/html_karoshi/images/theme_preview/*
do
	STYLESHEETCHOICE=`basename $THEMES | sed 's/.png//g'`

	echo '<td style="width: 90px; vertical-align: top; height: 160px; text-align: left;">
		<button class="info" name="_SetTheme_" value="_THEMECHOICE_'$STYLESHEETCHOICE'_">
		<img style="width: 330px;" src="/images/theme_preview/'$STYLESHEETCHOICE'.png" alt="'$STYLESHEETCHOICE'">
		<span>'$STYLESHEETCHOICE'</span>
		</button>
	`	</td>'
	let STYLECOUNT=$STYLECOUNT+1

	if [ $STYLECOUNT = 4 ]
	then
		echo '</tr><tr>'
		STYLECOUNT=1
	fi
done
[ $STYLECOUNT = 1 ] && echo "<td></td>"
echo '</tr></tbody></table><br></div></div></form></div></body></html>'
exit
