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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

TABLECLASS=standard
if [ "$MOBILE" = yes ]
then
	TABLECLASS=mobilestandard
fi

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Schedule Wake on Lan"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script>
</head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/locations.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/wake_on_lan_add2.cgi" method="post"><div id="actionbox3"><div id="titlebox">
<table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: middle;"><b>'$"Schedule Wake on Lan"'</b></td>
<td><a href="wake_on_lan_view.cgi"><input class="button" type="button" name="" value="'$"View scheduled locations"'"></a></td>
<td><a href="wake_on_lan_now.cgi"><input class="button" type="button" name="" value="'$"Wake a location"'"></a></td>
<td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Wake_on_LAN"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will schedule all of the computers in your selected location to be turned on."'<br><br>'$"The computers have to be declared in the asset register with a valid mac address."'</span></a>
</td></tr></tbody></table><br>

'
#Time to wake location up
echo '<table class="'$TABLECLASS'" style="text-align: left; height: 60px;" >
    <tbody>
<tr><td style="width: 200px;"><b>'$"Time"'</b></td><td>'
echo '<input maxlength="2" size="2" name="_HOUR_" value="08"> : <input maxlength="2" size="2" name="_MINUTES_" value="15"> </td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Please enter in the time that you want the computers in your selected location to be turned on."'</span></a></td></tr><tr><td><b>'$"Location"'</b></td><td>'
#Show current rooms
LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
if [ $LOCATION_COUNT -gt 0 ]
then
	echo '<select name="_LOCATION_">'
	COUNTER=1
	while [ $COUNTER -le $LOCATION_COUNT ]
	do
		LOCATION=`sed -n $COUNTER,$COUNTER'p' /var/lib/samba/netlogon/locations.txt`
		echo '<option value="'$LOCATION'">'$LOCATION'</option>'
		let COUNTER=$COUNTER+1
		done
	echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Select the location that you want. All computers in this location will be turned on at the time you specify."'</span></a></td></tr></tbody></table>'
else
	MESSAGE=$"There are no locations to schedule."
	show_status
fi

echo '<br><br><input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div></form></div></div></body></html>'
exit
