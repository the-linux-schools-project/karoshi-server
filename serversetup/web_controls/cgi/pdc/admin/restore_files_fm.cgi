#!/bin/bash
#Restore_files
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
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Restore Files"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script>
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


function show_status {
echo '<SCRIPT language="Javascript">
alert("'$MESSAGE'")
window.location = "/cgi-bin/admin/karoshi_servers_view.cgi"
</script>
</div></body></html>'
exit
}


#Check to see that a backup server has been configured
if [ ! -d /opt/karoshi/server_network/backup_servers/backup_settings ]
then
	MESSAGE=$"No backup servers have been configured."
	show_status
fi

if [ `ls -1 /opt/karoshi/server_network/backup_servers/backup_settings | wc -l` = 0 ]
then
	MESSAGE=$"No backup servers have been configured."
	show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '
<form action="/cgi-bin/admin/file_manager.cgi" method="post">
<div id="actionbox3"><div id="infobox">'

#############################
#Show list of servers to restore to
#############################
echo '<table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Restore system files and folders"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Restore_Files"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the server that you want to restore system files to."'</span></a></td></tr></tbody></table><br>'

SERVERLISTARRAY=( `ls -1 /opt/karoshi/server_network/backup_servers/backup_settings/` )
SERVERLISTCOUNT=${#SERVERLISTARRAY[@]}
SERVERCOUNTER=0
LINECOUNTER=1
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"
echo '<table class="tablesorter" style="text-align: left;" ><thead><tr><th style="width: 360px; vertical-align: top; text-align: left;"><b>'$"Server"'</b></th><th style="width: 120px; vertical-align: top; text-align: left;"><b>'$"View Folders"'</b></th>'
if [ "$SERVERLISTCOUNT" -gt 1 ]
then
	echo '<th style="width: 360px; vertical-align: top; text-align: left;"><b>'$"Server"'</b></th><th style="width: 120px; vertical-align: top; text-align: left;"><b>'$"View Folders"'</b></th>'
fi
echo '</tr></thead><tbody><tr>'

while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
	KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}

	#Get backup path
	BACKUPPATH=/home/backups/"$KAROSHISERVER"
	#Get backup server
	BACKUPSERVER=`sed -n 1,1p /opt/karoshi/server_network/backup_servers/backup_settings/"$KAROSHISERVER"/backupserver`

	echo '<td style="vertical-align: top; text-align: left;">'$KAROSHISERVER'</td><td style="vertical-align: top; text-align: left;">


	<button class="info" name="_GotoServer_" value="_SERVERTYPE_network_ACTION_ENTER_SERVERNAME_'$BACKUPSERVER'_LOCATION_'$BACKUPPATH'_">
	<img src="'$SERVERICON'" alt="'$"Show Backup Folders"'">
	<span>'$KAROSHISERVER'<br><br>'
	
	cat /opt/karoshi/server_network/servers/$KAROSHISERVER/* | sed '/<a href/c'"&nbsp"

	echo '</span></button></td>'

	let SERVERCOUNTER="$SERVERCOUNTER"+1
	let LINECOUNTER="$LINECOUNTER"+1

	if [ "$LINECOUNTER" = 3 ] && [ "$SERVERCOUNTER" -lt "$SERVERLISTCOUNT" ]
	then	
		echo '</tr><tr>'
		LINECOUNTER=1
	fi	

done
echo '</tr></tbody></table><br>'

#############################
#Show list of primary groups to restore from.
#############################

echo '
<table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Restore User Files and Folders"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Restore_Files"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the primary group that you want to restore user files to."'</span></a></td></tr></tbody></table>
<br><table id="myTable" class="tablesorter" style="text-align: left;" ><thead>
<tr><th style="width: 120px;"><b>'$"Primary Group"'</b></th><th style="width:230px;"><b>'$"Server"'</b></th><th style="width: 120px;"><b>'$"View Folders"'</b></th><th style="width: 120px;"><b>'$"Primary Group"'</b></th><th style="width: 230px;"><b>'$"Server"'</b></th><th style="width: 120px;"><b>'$"View Folders"'</b></th></tr></thead><tbody>
'
START_LINE=yes
ICON1=/images/submenus/system/computer.png
PRI_GROUP_COUNT=$(ls -1 /opt/karoshi/server_network/group_information/ | wc -l)
for PRI_GROUP in /opt/karoshi/server_network/group_information/*
do
	PRI_GROUP=`basename $PRI_GROUP`
	source /opt/karoshi/server_network/group_information/$PRI_GROUP


	if [ -d /opt/karoshi/server_network/backup_servers/backup_settings/$SERVER/ ]
	then
		#Get backup server
		BACKUPSERVER=`sed -n 1,1p /opt/karoshi/server_network/backup_servers/backup_settings/$SERVER/backupserver`
		#Get backup path
		[ $PRI_GROUP = itadmin ] && PRI_GROUP=itadminstaff
		BACKUPPATH=/home/backups/$SERVER/$PRI_GROUP
		if [ $START_LINE = yes ]
		then
			echo '<tr>'
		fi

		echo '<td>'$PRI_GROUP'</td><td>'$SERVER'</td><td>
		<button class="info" name="_Goto_" value="_SERVERTYPE_network_ACTION_ENTER_SERVERNAME_'$BACKUPSERVER'_LOCATION_'$BACKUPPATH'_">
		<img src="'$ICON1'" alt="'$"Rename"'">
		<span>'$"View Folders"'<br>'$SERVER' - '$PRI_GROUP'</span>
		</button>
		</td>'
		if [ $START_LINE = no ]
		then
			START_LINE=yes
			echo '</tr>'
		else
			START_LINE=no
		fi
	fi
done
echo '</tbody></table><br>
</div></div></form></div></body></html>'
exit

