#!/bin/bash
#backup_assign
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Assign Backup Server"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>
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
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+')
#########################
#Assign data to variables
#########################
END_POINT=5
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
	MESSAGE=$"The server cannot be blank."
	show_status
fi

#Check to see that a backup server has been configured
if [ ! -d /opt/karoshi/server_network/backup_servers/servers ]
then
	MESSAGE=$"No backup servers have been configured."
	show_status
fi

if [[ $(ls -1 /opt/karoshi/server_network/backup_servers/servers | wc -l) = 0 ]]
then
	MESSAGE=$"No backup servers have been configured."
	show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/backup_assign.cgi" method="post">
<div id="actionbox">

<table class="standard" style="text-align: left;" ><tr><td style="vertical-align: top;"><div class="sectiontitle">'$"Assign Backup Server"' - '"$SERVERNAME"'</div></td><td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the server that you want to backup to."'</span></a></td></tr></tbody></table><br>

<input name="_SERVER_" value="'"$SERVERNAME"'" type="hidden">
'

if [ -d /opt/karoshi/server_network/backup_servers/backup_settings/"$SERVERNAME" ]
then
CURRENTBSERVER=$(sed -n 1,1p /opt/karoshi/server_network/backup_servers/backup_settings/"$SERVERNAME"/backupserver)

echo '<br><br><table class="standard" style="text-align: left;" >
<tbody>
<tr><td style="width: 200px; vertical-align: top; text-align: left;">'$"Current backup server"'</td><td style="width: 200px; vertical-align: top; text-align: left;">'"$CURRENTBSERVER"'</td><td style="vertical-align: top; text-align: left;">
<input name="_SERVERNAME_removebackupoption_" type="submit" class="button" value="'$"Un-assign"'">
</td></tr></tbody></table><br><br>'
fi

MOBILE=no
/opt/karoshi/web_controls/show_servers "$MOBILE" backupservers $"Select server" backupserver "$SERVERNAME"

echo '</div></form></div></body></html>'
exit
