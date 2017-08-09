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
<!DOCTYPE html>
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Enable - Disable Network Backup"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
</head><body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Enable - Disable Network Backup"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Enable/Disable_Backup"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the server that you want to enable or disable the backup server for."'</span></a></td></tr></tbody></table><br>'

#Check if any backup servers have been enabled.
if [ ! -d /opt/karoshi/server_network/backup_servers/backup_settings/ ]
then
	echo $"No karoshi backup servers have been enabled."
	echo '</div></div></body></html>'
	exit
fi

echo '<form action="/cgi-bin/admin/backup_enable_disable.cgi" name="selectservers" method="post">'

#Get backup status for this server
BACKUPSTATUS="Disable Backup"
BACKUP_ICON=/images/submenus/system/backup_enabled.png

echo '<table id="myTable" class="tablesorter" style="text-align: left;" ><thead>'
echo '<tr><th style="width: 180px;"><b>'$"Server"'</b></th><th style="width: 180px;"><b>'$"Backup Server"'</b></th><th style="width: 60px;"><b>'$"Status"'</b></th></tr></thead><tbody>'

#Get backup status for the servers

if [ $(ls -1 /opt/karoshi/server_network/backup_servers/backup_settings/ | wc -l) = 0 ]
then
	echo $"No karoshi backup servers have been enabled."
	echo '</div></div></body></html>'
	exit
fi

for KAROSHI_SERVERS in /opt/karoshi/server_network/backup_servers/backup_settings/*
do
	KAROSHI_SERVER=$(basename "$KAROSHI_SERVERS")
	BACKUPSERVER=$(sed -n 1,1p /opt/karoshi/server_network/backup_servers/backup_settings/"$KAROSHI_SERVER"/backupserver)
	BACKUPSTATUS=$"Disable Backup"
	BACKUP_ICON=/images/submenus/system/backup_enabled.png
	if [ -f /opt/karoshi/server_network/backup_servers/backup_settings/"$KAROSHI_SERVER"/stop_backup ]
	then
		BACKUPSTATUS=$"Enable Backup"
		BACKUP_ICON=/images/submenus/system/backup_disabled.png
	fi
	echo '<tr><td>'"$KAROSHI_SERVER"'</td><td>'"$BACKUPSERVER"'</td><td>
	<button class="info" name="_'"$KAROSHI_SERVER"'_" value="_'"$KAROSHI_SERVER"'_">
	<img src="'"$BACKUP_ICON"'" alt="'"$BACKUPSTATUS"'">
	<span>'"$BACKUPSTATUS"'</span>
	</button>
	</td></tr>'

done
echo '</tbody></table><br></form></div></div></div></body></html>'
exit
