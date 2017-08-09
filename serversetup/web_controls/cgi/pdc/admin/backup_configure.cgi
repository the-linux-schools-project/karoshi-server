#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

#This file is part of Karoshi SERVERNAME.
#
#Karoshi SERVERNAME is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Karoshi SERVERNAME is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Karoshi SERVERNAME.  If not, see <http://www.gnu.org/licenses/>.

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
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Configure Backup"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>
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
</head><body><div id="pagecontainer">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/backup_configure_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g')

#########################
#Assign data to variables
#########################
END_POINT=22
function get_data {
COUNTER=2
DATAENTRY=""
while [[ $COUNTER -le $END_POINT ]]
do
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [[ "$DATAHEADER" = "$DATANAME" ]]
	then
		let COUNTER="$COUNTER"+1
		DATAENTRY=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
		break
	fi
	let COUNTER=$COUNTER+1
done
}

#Assign SERVERNAME
DATANAME=SERVERNAME
get_data
SERVERNAME="$DATAENTRY"

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = delete ] || [ "$ACTION" = edit ] || [ "$ACTION" = reallyedit ] || [ "$ACTION" = reallydelete ]
then
	#Assign BACKUPNAME
	DATANAME=BACKUPNAME
	get_data
	BACKUPNAME="${DATAENTRY//12345UNDERSCORE12345/_}"

	if [ "$ACTION" = reallyedit ]
	then
		#Assign BACKUPFOLDER
		DATANAME=BACKUPFOLDER
		get_data
		BACKUPFOLDER="${DATAENTRY//12345UNDERSCORE12345/_}"

		#Assign DURATION
		DATANAME=DURATION
		get_data
		DURATION=$(echo "$DATAENTRY" | tr -cd '0-9')
	fi
fi

if [ "$ACTION" = reallyschedule ]
then
	#Assign HOURS
	DATANAME=HOURS
	get_data
	HOURS=$(echo "$DATAENTRY" | tr -cd '0-9')


	#Assign MINUTES
	DATANAME=MINUTES
	get_data
	MINUTES=$(echo "$DATAENTRY" | tr -cd '0-9')
fi

if [ "$ACTION" = assignbackupserver ]
then
	#Assign BACKUPSERVER
	DATANAME=BACKUPSERVER
	get_data
	BACKUPSERVER=$"${DATAENTRY//12345UNDERSCORE12345/_}"
fi

if [ "$ACTION" = setbackupstatus ]
then
	#Assign BACKUPSTATUS
	DATANAME=BACKUPSTATUS
	get_data
	BACKUPSTATUS="${DATAENTRY//12345UNDERSCORE12345/_}"
fi

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
#########################
#Check data
#########################
#Check to see that a SERVERNAME has been chosen
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"You must choose a server."
	show_status
fi

if [ "$ACTION" = delete ] || [ "$ACTION" = edit ] || [ "$ACTION" = reallyedit ] || [ "$ACTION" = reallydelete ]
then
	
	if [ -z "$BACKUPNAME" ]
	then
		MESSAGE=$"Blank backup name."
		show_status
	fi
	if [ "$ACTION" = reallyedit ]
	then
		if [ -z "$BACKUPFOLDER" ]
		then
			MESSAGE=$"Blank backup folder."
			show_status
		fi

		if [ -z "$DURATION" ]
		then
			MESSAGE=$"Blank duration."
			show_status
		fi
	fi
fi

if [ "$ACTION" = assignbackupserver ]
then
	if [ -z "$BACKUPSERVER" ]
	then
		MESSAGE=$"Blank backup servername."
		show_status
	fi
fi

if [ "$ACTION" = setbackupstatus ]
then
	if [ -z "$BACKUPSTATUS" ]
	then
		MESSAGE=$"Blank backup status."
		show_status
	fi
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/system/computer.png
ICON2=/images/submenus/system/backup/config.png

echo '<div id="actionbox3"><div id="titlebox">
<div class="sectiontitle">'$"Configure Backup"' - '"$SERVERNAME"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Configure_Backup"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the folders you want to backup."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/backup_configure_fm.cgi" method="post">
			<button class="info" name="SelectServer" value="_">
				<img src="'"$ICON1"'" alt="'$"Select server"'">
				<span>'$"Select the server you want to view."'</span><br>
				'$"Select Server"'
			</button>
		</form>
	</td>

'

if [ "$ACTION" = edit ] || [ "$ACTION" = add ] || [ "$ACTION" = schedule ]
then
	echo '


	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/backup_configure.cgi" name="testform" method="post">
			<button class="info" name="____ViewBackups____" value="____SERVERNAME____'"$SERVERNAME"'____">
				<img src="'"$ICON2"'" alt="'$"View Backups"'">
				<span>'$"View backups for this server."'</span><br>
				'$"View Backups"'
			</button>
		</form>
	</td>
	'
fi
echo '</tr></tbody></table></div><div id="infobox">'

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/backup_configure.cgi | cut -d' ' -f1)
#View logs
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$ACTION:$BACKUPNAME:$BACKUPFOLDER:$DURATION:$BACKUPSERVER:$BACKUPSTATUS:$HOURS:$MINUTES:" | sudo -H /opt/karoshi/web_controls/exec/backup_configure
echo "</div></div></div></body></html>"
exit
