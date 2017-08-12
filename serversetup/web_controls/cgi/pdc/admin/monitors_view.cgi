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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Monitors"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script>
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
// --></script><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
'
echo "</head><body><div id='pagecontainer'>"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/monitors_add_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You must choose a monitor."
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
ICON1=/images/submenus/system/add.png
ICON2=/images/submenus/system/monitor_status.png

echo '<div id="actionbox3"><div id="titlebox">
<div class="sectiontitle">'$"View Monitors"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Viewing_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"Deleting a monitor will stop the monitoring server from monitoring the monitor group."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<form action="/cgi-bin/admin/monitors_add_fm.cgi" method="post">
			<button class="info infonavbutton" name="_AddMonitor_" value="_">
				<img src="'$ICON1'" alt="'$"Add Monitor"'">
				<span>'$"Add a network monitor"'</span><br>
				'$"Add Monitor"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<form action="/cgi-bin/admin/mon_status.cgi" method="post">
			<button class="info infonavbutton" name="_NetworkStatus_" value="_">
				<img src="'$ICON2'" alt="'$"Network Status"'">
				<span>'$"Network Status"'</span><br>
				'$"Status"'
			</button>
		</form>
	</td>

</tr></tbody></table>
<br></div><div id="infobox">'

#Show monitors

if [ ! -d /opt/karoshi/server_network/mon/monitors ]
then
	MESSAGE=$"No monitors available."
	show_status
fi 

if [[ $(ls -1 /opt/karoshi/server_network/mon/monitors | wc -l) = 0 ]] && [[ $(ls -1 /opt/karoshi/server_network/mon/monitors_disabled | wc -l) = 0 ]]
then
	MESSAGE=$"No monitors available."
	show_status
fi

#Show table of sites
echo '<table id="myTable" class="tablesorter" style="text-align: left;" >'
echo "<thead>"
echo '<tr><th style="width: 180px;"><b>'$"Monitors"'</b></th><th style="width: 70px;"><b>'$"Status"'</b></th><th style="width: 70px;"><b>'$"Edit"'</b></th><th style="width: 70px;"><b>'$"Delete"'</b></th><th style="width: 70px;"><b>'$"Info"'</b></th></tr></thead><tbody>'

for MONITORNAME in /opt/karoshi/server_network/mon/monitors/*
do
	MONITORNAME=$(basename "$MONITORNAME")
	MONITORNAME2=$(echo "$MONITORNAME" | sed 's/_/%%%%%/g')
	MONITOR_SERVICES=$(grep service /opt/karoshi/server_network/mon/monitors/"$MONITORNAME" | sed 's/service//g' |sed 's/$/<br>/g')
	SERVICE_TCPIPS=$(sed -n 4,4p /opt/karoshi/server_network/mon/monitors/"$MONITORNAME" | cut -d' ' -f3-)

	echo '<tr>

	<td style="vertical-align: top;">'"$MONITORNAME"'</td>
	<td style="vertical-align: top;">
		<form action="/cgi-bin/admin/monitors_enable_disable.cgi" name="monitors" method="post">
			<button class="button smallbutton" name="_Disable_" value="_MONITOR_'"$MONITORNAME2"'_">
			<span>'$"On"'</span>
			</button>
		</form>
	</td>
	<td style="vertical-align: top;">
		<form action="/cgi-bin/admin/monitors_add_fm.cgi" name="monitors" method="post">
			<button class="info" name="_Edit_" value="_MONITOR_'"$MONITORNAME2"'_">
			<img src="/images/submenus/system/edit.png" alt="'$"Edit"' - '"$MONITORNAME"'">
			<span>'$"Edit"' - '"$MONITORNAME"'</span>
			</button>
		</form>
	</td>
	<td style="vertical-align: top;">
		<form action="/cgi-bin/admin/monitors_delete.cgi" name="monitors" method="post">
			<button class="info" name="_Delete_" value="_MONITOR_'"$MONITORNAME2"'_">
			<img src="/images/submenus/system/delete.png" alt="'$"Delete"' - '"$MONITORNAME"'">
			<span>'$"Delete"' - '"$MONITORNAME"'</span>
			</button>
		</form>
	</td>
	<td style="vertical-align: top;">
		<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"TCPIP numbers monitored":'<br>'"$SERVICE_TCPIPS"'<br>'$"Services Monitored":'<br>'"$MONITOR_SERVICES"'</span></a>
	</td></tr>'
done

if [ -d /opt/karoshi/server_network/mon/monitors_disabled ]
then
	if [[ $(ls -1 /opt/karoshi/server_network/mon/monitors_disabled | wc -l) -gt 0 ]]
	then
		for MONITORNAME in /opt/karoshi/server_network/mon/monitors_disabled/*
		do
			MONITORNAME=$(basename "$MONITORNAME")
			MONITORNAME2=$(echo "$MONITORNAME" | sed 's/_/%%%%%/g')
			MONITOR_SERVICES=$(grep service /opt/karoshi/server_network/mon/monitors_disabled/"$MONITORNAME" | sed 's/service//g' |sed 's/$/<br>/g')
			SERVICE_TCPIPS=$(sed -n 4,4p /opt/karoshi/server_network/mon/monitors_disabled/"$MONITORNAME" | cut -d' ' -f3-)

			echo '<tr>

			<td style="vertical-align: top;">'"$MONITORNAME"'</td>
			<td style="vertical-align: top;">
				<form action="/cgi-bin/admin/monitors_enable_disable.cgi" name="monitors" method="post">
					<button class="button smallbutton" name="_Enable_" value="_MONITOR_'"$MONITORNAME2"'_">
					<span>'$"Off"'</span>
					</button>
				</form>
			</td>
			<td style="vertical-align: top;"></td>
			<td style="vertical-align: top;">
				<form action="/cgi-bin/admin/monitors_delete.cgi" name="monitors" method="post">
					<button class="info" name="_Delete_" value="_MONITOR_'"$MONITORNAME2"'_">
					<img src="/images/submenus/system/delete.png" alt="'$"Delete"' - '"$MONITORNAME"'">
					<span>'$"Delete"' - '"$MONITORNAME"'</span>
					</button>
				</form>
			</td>
			<td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"TCPIP numbers monitored":'<br>'"$SERVICE_TCPIPS"'<br>'$"Services Monitored":'<br>'"$MONITOR_SERVICES"'</span></a></td></tr>'
		done
	fi
fi

echo '</tbody></table></div></div></div></body></html>'
exit
