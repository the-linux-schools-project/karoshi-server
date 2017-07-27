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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Wake on Lan - View"2'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'">
<script>
<!--
function SetAllCheckBoxes(FormName, FieldName, CheckValue)
{
	if(!document.forms[FormName])
		return;
	var objCheckBoxes = document.forms[FormName].elements[FieldName];
	if(!objCheckBoxes)
		return;
	var countCheckBoxes = objCheckBoxes.length;
	if(!countCheckBoxes)
		objCheckBoxes.checked = CheckValue;
	else
		// set the check value for all check boxes
		for(var i = 0; i < countCheckBoxes; i++)
			objCheckBoxes[i].checked = CheckValue;
}
// -->
</script><script src="/all/stuHover.js" type="text/javascript"></script>'
echo "</head><body><div id='pagecontainer'>"
#########################
#Get data input
#########################

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/locations.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [[ $(grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/client/wake_on_lan_add.png
ICON2=/images/submenus/client/wakeup.png

echo '<form action="/cgi-bin/admin/wake_on_lan_view2.cgi" name="selectwol" method="post"><div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"Wake on Lan - Scheduled Locations"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Wake_on_LAN"><img class="images" alt="" src="/images/help/info.png"><span>'$"The locations below are scheduled for wake on lan."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="wake_on_lan_add.cgi" class="info" name="_ScheduleWakeonLan_" value="_">
			<img src="'"$ICON1"'" alt="'$"Schedule a location"'">
			<span>'$"Schedule a location to wake on lan."'</span><br>
			'$"Schedule Location"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="wake_on_lan_now.cgi" class="info" name="_WakeALocation_" value="_">
			<img src="'"$ICON2"'" alt="'$"Wake a location"'">
			<span>'$"Wake a location."'</span><br>
			'$"Wake Location"'
		</button>
	</td>

</tr></tbody></table><br></div><div id="infobox">'
#Show scheduled wake on lan locations
MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/wake_on_lan_view.cgi | cut -d' ' -f1)
sudo -H /opt/karoshi/web_controls/exec/wake_on_lan_view "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:"
echo '</div></div></form></div></body></html>'
exit
