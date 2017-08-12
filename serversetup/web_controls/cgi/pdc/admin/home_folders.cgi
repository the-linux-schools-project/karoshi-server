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
########################
#Required input variables
########################
#  _SERVER_
#  _PRIGROUP_
##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Change Home Server"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
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

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%')

#########################
#Generate navigation bar
#########################
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1="/images/submenus/file/folder.png"
ICON2="/images/submenus/system/gluster.png"

echo '<div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"Change Home Server"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Home_Folders"><img class="images" alt="" src="/images/help/info.png"><span>'$"Change the home server for this group of users."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<form action="home_folders_fm.cgi" method="post">
			<button class="info infonavbutton" name="ViewHomeFolders" value="_">
				<img src="'$ICON2'" alt="'$"Home Folders"'">
				<span>'$"Configure user home folders."'</span><br>
				'$"Home Folders"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<form action="gluster_control.cgi" method="post">
			<button class="info infonavbutton" name="GlusterVolumeControl" value="_">
				<img src="'$ICON2'" alt="'$"Gluster Volumes"'">
				<span>'$"Configure gluster volumes."'</span><br>
				'$"Gluster Volumes"'
			</button>
		</form>
	</td>

</tr></tbody></table>
'


#########################
#Assign data to variables
#########################
END_POINT=6
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

#Assign SERVER
DATANAME=SERVER
get_data
SERVER="${DATAENTRY//%2C/,}"

#Assign PRIGROUP
DATANAME=PRIGROUP
get_data
PRIGROUP="$DATAENTRY"

SHOW_STATUS_LOC=home_folders_fm.cgi

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/'"$SHOW_STATUS_LOC"'";'
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

if [[ $(grep -c ^"$REMOTE_USER": /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################
#Check to see that SERVER is not blank
if [ -z "$SERVER" ]
then
	MESSAGE=$"The home server cannot be blank."
	show_status
fi
#Check to see that PRIGROUP is not blank
if [ -z "$PRIGROUP" ]
then
	MESSAGE=$"The primary group cannot be blank."
	show_status
fi

#Check to see that there are other karoshi servers available
if [ ! -d /opt/karoshi/server_network/servers/ ]
then
	SHOW_STATUS_LOC=karoshi_servers_view.cgi
	MESSAGE=$"No other Karoshi servers have been set up."
	show_status
fi

if [[ $(ls -1 /opt/karoshi/server_network/servers/ | wc -l) = 0 ]]
then
	SHOW_STATUS_LOC=karoshi_servers_view.cgi
	MESSAGE=$"No other Karoshi servers have been set up."
	show_status
fi

FILESERVERCOUNT=0
for KAROSHI_SERVER in /opt/karoshi/server_network/servers/*
do
	KAROSHI_SERVER=$(basename "$KAROSHI_SERVER")
	if [ -f /opt/karoshi/server_network/servers/"$KAROSHI_SERVER"/fileserver ]
	then
		let FILESERVERCOUNT="$FILESERVERCOUNT"+1
	fi
done

if [ "$FILESERVERCOUNT" -le 1 ]
then
	SHOW_STATUS_LOC=karoshi_servers_view.cgi
	MESSAGE=$"No other Karoshi servers have been enabled as file servers. You will need to add the file server module to an additional server."
	show_status
fi

echo '<p><img height="16" width="16" alt="Warning" src="/images/warnings/warning.png"> '$"IMPORTANT - Please ensure that users are not logged to ensure that data is not lost."'</p><br>
<form action="/cgi-bin/admin/home_folders2.cgi" method="post">
<input name="_CURRENTSERVER_" value="'"$SERVER"'" type="hidden">
<input name="_PRIGROUP_" value="'"$PRIGROUP"'" type="hidden">
  <table class="standard" style="text-align: left;" ><tbody>

<tr><td style="width: 180px;">'$"Current Server"'</td><td>'"$SERVER"'</td></tr>
<tr><td>'$"Primary Group"'</td><td>'"$PRIGROUP"'</td></tr>
<tr><td>'$"Copy Home Areas"'</td><td><input name="_COPYHOMEAREAS_" value="yes" type="checkbox"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will copy any existing user home areas to the new server. This could take some time if there are a large amount of files to transfer."'</span></a></td></tr>
<tr><td style="height:50px"><b>'$"New Server"'</b></td></tr>
</tbody></table></div><div id="infobox">'

#Show list of file servers.
MOBILE=no
/opt/karoshi/web_controls/show_servers "$MOBILE" fileservers $"Select Server" notset "$SERVER"

echo '</form></div></div></div></body></html>'
exit

