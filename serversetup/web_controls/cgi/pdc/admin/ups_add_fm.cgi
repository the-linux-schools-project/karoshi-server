#!/bin/bash
#Copyright (C) 2010  Paul Sharrad

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

#Language
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

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Add a UPS"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script language="JavaScript" src="/all/calendar/ts_picker.js" type="text/javascript"></script>
<!-- Timestamp input popup (European Format) --><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
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
ICON1=/images/submenus/system/battery.png

echo '<form action="/cgi-bin/admin/ups_add.cgi" name="tstest" method="post"><div id="actionbox3"><div id="titlebox">
<div class="sectiontitle">'$"Add a UPS"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_a_UPS"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will configure a UPS device connected to a server."'</span></a></div>

	<table class="tablesorter"><tbody><tr>
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info" formaction="ups_status.cgi" name="_UPSStatus" value="_">
				<img src="'$ICON1'" alt="'$"UPS Status"'">
				<span>'$"UPS Status"'</span><br>
				'$"Status"'
			</button>
		</td>
	</tr></tbody></table>

<br></div><div id="infobox">'


echo '<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">'$"UPS Name"'</td>
        <td>'
#Generate list of UPC data
echo '<select name="_UPSDRIVER_" style="width: 200px;">'
UPSDATA_LENGTH=$(wc -l < /opt/karoshi/server_network/ups/ups-model-information.csv)

COUNTER=1
while [ "$COUNTER" -le "$UPSDATA_LENGTH" ]
do
	UPSDATA=$(sed -n "$COUNTER,$COUNTER"'p' /opt/karoshi/server_network/ups/ups-model-information.csv)
	UPSMAKE=$(echo "$UPSDATA" | cut -d, -f1,2 | sed 's/,/: /g')
	UPSMODEL=$(echo "$UPSDATA" | cut -d, -f2)
	UPSDRIVER=$(echo "$UPSDATA" | cut -d, -f3)
	echo '<option value="'"$UPSMODEL,$UPSDRIVER"'">'"$UPSMAKE"'</option>'
	let COUNTER="$COUNTER"+1
done

echo '</select></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_a_UPS"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose a UPS device from the list."'</span></a></td></tr>
<tr><td>'$"Port"'</td><td><select name="_UPSPORT_" style="width: 200px;"><option value="auto">auto</option><option value="/dev/ttyS0">/dev/ttyS0</option><option value="/dev/ttyS1">/dev/ttyS1</option></select></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_a_UPS"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose auto for UPS devices connected via usb."'</span></a></td></tr>
</tbody></table><br><br>'

#Show list of servers
/opt/karoshi/web_controls/show_servers no servers $"Add UPS"

echo '</div></div></form></div></body></html>'
exit

