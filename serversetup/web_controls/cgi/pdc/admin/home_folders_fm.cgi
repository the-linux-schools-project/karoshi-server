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
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
then
	TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Home Folders"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
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
</head>
<body onLoad="start()"><div id="pagecontainer">'



#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
WIDTH=100
ICON1=/images/submenus/system/gluster.png
ICON2=/images/submenus/system/network-server.png

echo '<form action="/cgi-bin/admin/home_folders.cgi" method="post"><div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"Home Folders"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Home_Folders"><img class="images" alt="" src="/images/help/info.png"><span>'$"This displays the server that hosts the home folders for each group."'</span></a></div>
<table class="tablesorter"><tbody><tr>'

#Check for gluster support
if [[ $(grep -c dfs /etc/samba/smb.conf) -gt 0 ]]
then
	echo '

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<button class="info infonavbutton" formaction="gluster_control.cgi" name="GlusterVolumeControl" value="_">
			<img src="'$ICON1'" alt="'$"Gluster Volumes"'">
			<span>'$"Configure gluster volumes"'</span><br>
			'$"Gluster Volumes"'
		</button>
	</td>
	'
fi


echo '

<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
	<button class="info infonavbutton" formaction="samba_shares.cgi" name="SambaShares" value="_">
		<img src="'$ICON2'" alt="'$"Network Shares"'">
		<span>'$"Configure network shares"'</span><br>
		'$"Network Shares"'
	</button>
</td>

</tr></tbody></table>

</div><div id="infobox">

<table id="myTable" class="tablesorter" style="text-align: left; height: 91px;" >
<thead><tr><th style="width: 140px;"><b>'$"Primary Group"'</b></th><th style="width: 180px;"><b>'$"Server"'</b></th><td style="width: 180px;"><b>'$"Change"'</b></td><th style="width: 140px;"><b>'$"Primary Group"'</b></th><th style="width: 180px;"><b>'$"Server"'</b></th><td><b>'$"Change"'</b></td></tr>
</thead><tbody>
'
START_LINE=yes
ICON3=/images/submenus/system/computermed.png
for PRI_GROUP in /opt/karoshi/server_network/group_information/*
do
	PRI_GROUP=$(basename "$PRI_GROUP")
	unset GLUSTERVOL
	source /opt/karoshi/server_network/group_information/"$PRI_GROUP"

	#Check for gluster volume
	[ -z "$GLUSTERVOL" ] && GLUSTERVOL=notset
	if [ -d /opt/karoshi/server_network/gluster-volumes/"$GLUSTERVOL" ]
	then
		ICON3=/images/submenus/system/glustermed.png
	else
		ICON3=/images/submenus/system/computermed.png
	fi

	if [ "$START_LINE" = yes ]
	then
		echo '<tr><td style="vertical-align: top;">'"$PRI_GROUP"'</td><td style="vertical-align: top;">'"${SERVER//,/<br>}"'</td><td style="vertical-align: top;">
		<button class="info" name="_ChangeServer_" value="_PRIGROUP_'"$PRI_GROUP"'_SERVER_'"$SERVER"'_">
		<img src="'"$ICON3"'" alt="'$"Rename"'">
		<span>'$"Change Server"'<br><br>'"$PRI_GROUP"'<br><br>'"${SERVER//,/<br>}"'</span>
		</button>
		</td>'
		START_LINE=no
	else
		echo '<td style="vertical-align: top;">'"$PRI_GROUP"'</td><td style="vertical-align: top;">'"${SERVER//,/<br>}"'</td><td style="vertical-align: top;">
		<button class="info infoleft" name="_ChangeServer_" value="_PRIGROUP_'"$PRI_GROUP"'_SERVER_'"$SERVER"'_">
		<img src="'"$ICON3"'" alt="'$"Rename"'">
		<span>'$"Change Server"'<br><br>'"$PRI_GROUP"'<br><br><br>'"${SERVER//,/<br>}"'</span>
		</button>
		</td></tr>'
	START_LINE=yes
	fi
done

echo '</tbody></table><br><br>
</div></div>
</form>
</div></body>
</html>'
exit

