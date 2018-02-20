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
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]
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
  <title>'$"Default User Settings"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

##########################
#Get current settings
##########################

echo '<form action="/cgi-bin/admin/default_user_settings.cgi" method="post"><div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Default User Settings"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Default_User_Settings"><img class="images" alt="" src="/images/help/info.png"><span>'$"Sets the default settings for user accounts."'</span></a></td></tr></tbody></table><br>'
#Get lockout settings
Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/default_user_settings_fm.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:GETDATA" | sudo -H /opt/karoshi/web_controls/exec/default_user_settings


echo '<br><br>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></div></form></div></body></html>'
exit
