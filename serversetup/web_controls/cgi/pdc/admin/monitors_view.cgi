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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Monitors"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">'
echo '<script>'
echo '<!--'
echo 'function SetAllCheckBoxes(FormName, FieldName, CheckValue)'
echo '{'
echo '	if(!document.forms[FormName])'
echo '		return;'
echo '	var objCheckBoxes = document.forms[FormName].elements[FieldName];'
echo '	if(!objCheckBoxes)'
echo '		return;'
echo '	var countCheckBoxes = objCheckBoxes.length;'
echo '	if(!countCheckBoxes)'
echo '		objCheckBoxes.checked = CheckValue;'
echo '	else'
echo '		// set the check value for all check boxes'
echo '		for(var i = 0; i < countCheckBoxes; i++)'
echo '			objCheckBoxes[i].checked = CheckValue;'
echo '}'
echo '// --></script><script src="/all/stuHover.js" type="text/javascript"></script>
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
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/monitors_add_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
	export MESSAGE=$"You must choose a monitor."
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

echo '<div id="actionbox3"><div id="titlebox"><table class="standard" style="text-align: left;" ><tbody><tr><td style="vertical-align: top; width: 110px;"><b>'$"View Monitors"'</b></td>
<td style="vertical-align: top;">
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Viewing_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"Deleting a monitor will stop the monitoring server from monitoring the monitor group."'</span></a></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/monitors_add_fm.cgi" name="monitors" method="post">
<button class="button" name="_AddMonitor_" value="_">
'$"Add Monitor"'
</button>
</form>
</td><td style="vertical-align: top;"><form action="/cgi-bin/admin/mon_status.cgi" name="monitors" method="post">
<button class="button" name="_NetworkStatus_" value="_">
'$"Network Status"'
</button>
</form></td></tr></tbody></table>
<br></div><div id="infobox">'

#Show monitors

if [ ! -d /opt/karoshi/server_network/mon/monitors ]
then
	MESSAGE=$"No monitors available."
	show_status
fi 

if [ `ls -1 /opt/karoshi/server_network/mon/monitors | wc -l` = 0 ] && [ `ls -1 /opt/karoshi/server_network/mon/monitors_disabled | wc -l` = 0 ]
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
	MONITORNAME=`basename $MONITORNAME`
	MONITORNAME2=`echo $MONITORNAME | sed 's/_/%%%%%/g'`
	MONITOR_SERVICES=`grep service /opt/karoshi/server_network/mon/monitors/$MONITORNAME | sed 's/service//g' |sed 's/$/<br>/g'`
	SERVICE_TCPIPS=`sed -n 4,4p /opt/karoshi/server_network/mon/monitors/$MONITORNAME | cut -d' ' -f3-`

	echo '<tr>

	<td style="vertical-align: top;">'$MONITORNAME'</td>
	<td style="vertical-align: top;">
		<form action="/cgi-bin/admin/monitors_enable_disable.cgi" name="monitors" method="post">
			<button class="button smallbutton" name="_Disable_" value="_MONITOR_'$MONITORNAME2'_">
			<span>'$"On"'</span>
			</button>
		</form>
	</td>
	<td style="vertical-align: top;">
		<form action="/cgi-bin/admin/monitors_add_fm.cgi" name="monitors" method="post">
			<button class="info" name="_Edit_" value="_MONITOR_'$MONITORNAME2'_">
			<img src="/images/submenus/system/edit.png" alt="'$"Edit"' - '$MONITORNAME'">
			<span>'$"Edit"' - '$MONITORNAME'</span>
			</button>
		</form>
	</td>
	<td style="vertical-align: top;">
		<form action="/cgi-bin/admin/monitors_delete.cgi" name="monitors" method="post">
			<button class="info" name="_Delete_" value="_MONITOR_'$MONITORNAME2'_">
			<img src="/images/submenus/system/delete.png" alt="'$"Delete"' - '$MONITORNAME'">
			<span>'$"Delete"' - '$MONITORNAME'</span>
			</button>
		</form>
	</td>
	<td style="vertical-align: top;">
		<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"TCPIP numbers monitored":'<br>'$SERVICE_TCPIPS'<br>'$"Services Monitored":'<br>'$MONITOR_SERVICES'</span></a>
	</td></tr>'
done

if [ -d /opt/karoshi/server_network/mon/monitors_disabled ]
then
	if [ `ls -1 /opt/karoshi/server_network/mon/monitors_disabled | wc -l` -gt 0 ]
	then
		for MONITORNAME in /opt/karoshi/server_network/mon/monitors_disabled/*
		do
			MONITORNAME=`basename $MONITORNAME`
			MONITORNAME2=`echo $MONITORNAME | sed 's/_/%%%%%/g'`
			MONITOR_SERVICES=`grep service /opt/karoshi/server_network/mon/monitors_disabled/$MONITORNAME | sed 's/service//g' |sed 's/$/<br>/g'`
			SERVICE_TCPIPS=`sed -n 4,4p /opt/karoshi/server_network/mon/monitors_disabled/$MONITORNAME | cut -d' ' -f3-`

			echo '<tr>

			<td style="vertical-align: top;">'$MONITORNAME'</td>
			<td style="vertical-align: top;">
				<form action="/cgi-bin/admin/monitors_enable_disable.cgi" name="monitors" method="post">
					<button class="button smallbutton" name="_Enable_" value="_MONITOR_'$MONITORNAME2'_">
					<span>'$"Off"'</span>
					</button>
				</form>
			</td>
			<td style="vertical-align: top;"></td>
			<td style="vertical-align: top;">
				<form action="/cgi-bin/admin/monitors_delete.cgi" name="monitors" method="post">
					<button class="info" name="_Delete_" value="_MONITOR_'$MONITORNAME2'_">
					<img src="/images/submenus/system/delete.png" alt="'$"Delete"' - '$MONITORNAME'">
					<span>'$"Delete"' - '$MONITORNAME'</span>
					</button>
				</form>
			</td>
			<td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"TCPIP numbers monitored":'<br>'$SERVICE_TCPIPS'<br>'$"Services Monitored":'<br>'$MONITOR_SERVICES'</span></a></td></tr>'
		done
	fi
fi

echo '</tbody></table></div></div></div></body></html>'
exit
