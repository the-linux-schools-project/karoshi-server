#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
then
	TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Setup Wizard"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
<body onLoad="start()"><div id="pagecontainer">'

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=menubox
fi
echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<table class="standard" style="text-align: left;">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Setup Wizard"'</b></a></td></tr></tbody></table>'
else
	echo '<div class="sectiontitle">'$"Profiles"'</div><br><b>'$"Windows Clients"'</b><br><br>'$"By default windows clients use mandatory profiles."'<br>'$"New profiles are created using the profileuser account."'<br><br>'$"The profileuser account uses a roaming profile that you can customise. "'<br>'$"Copy the profileuser profile by right clicking on My Computer and using the profile management tools."'<br>'$"It is essential that the permissions are changed on the profile to allow all users to use it."'<br><br>'$"The copied profile can be zipped up and uploaded to the web management."'<br><br>
<a href="windows_client_profile_upload_fm.cgi"><img src="/images/submenus/client/upload_skel.png" border="0" alt="" />'$"Upload Windows Profile"'</a><br><br><br>
<b>'$"Karoshi Linux Clients"'</b><br><br>'$"The Karoshi Linux clients download an updated skel from the main server each time that the client is booted. "'<br>'$"Users logging onto the client then use the skel from the local machines."'<br><br>
<a href="linux_client_download_skel.cgi"><img src="/images/submenus/client/upload_skel.png" border="0" alt="" />'$"Download Karoshi Linux Profile"'</a><br><br>
<a href="linux_client_upload_skel_fm.cgi"><img src="/images/submenus/client/download_skel.png" border="0" alt="" />'$"Upload Karoshi Linux Profile"'</a><br><br>
'
fi


echo ''$OPENINGMSG'</div></div>'

[ "$MOBILE" = no ] && echo '</div>'

echo '</body></html>'
exit
