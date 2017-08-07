#!/bin/bash
#Change password
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
  <title>'$"Setup a VPN Server"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+')
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign SERVERNAME

COUNTER=2
while [ "$COUNTER" -le "$END_POINT" ]
do
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [ $(echo "$DATAHEADER"'check') = SERVERNAMEcheck ]
	then
		let COUNTER="$COUNTER"+1
		SERVERNAME=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
		break
	fi
	let COUNTER="$COUNTER"+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi"'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Check data
#########################
#Check to see that servername is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The servername cannot be blank."
	show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '
<form action="/cgi-bin/admin/module_vpn.cgi" method="post">
<div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" ><tr><td><div class="sectiontitle">'$"Setup a VPN Server"' - '"$SERVERNAME"'</div></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=OpenVPN_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will set up an OpenVPN server for your network."'</span></a>
</td></tr></tbody></table><br>
<input name="_SERVERNAME_" value="'"$SERVERNAME"'" type="hidden">
<b>'$"Description"'</b><br><br>
'$"This will set up an OpenVPN server for your network."' '$"This is useful for allowing client devices to connect to your network via the internet."' '$"Once you have added your VPN server you will be able to create client VPN certificates in the web management."'
<br>
<br>
<input value="'$"Submit"'" class="button" type="submit">
</div></div>
</form>
</div></body>
</html>
'
exit
