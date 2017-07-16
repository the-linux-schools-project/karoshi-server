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
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Configure DHCP"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	0: { sorter: "ipAddress" },
	3: { sorter: "MAC" }
    		}
		});
    } 
);
</script>
</head>
<body><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign OPTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = OPTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		OPTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
WIDTH=100
ICON1=/images/submenus/system/edit.png
ICON2=/images/submenus/system/lock.png
ICON3=/images/submenus/system/ban.png
ICON4=/images/submenus/system/dhcp.png
ICON5=/images/submenus/system/dhcp.png
ICON6=/images/submenus/system/dhcp.png

echo '<div id="actionbox3"><div id="titlebox"><form action="/cgi-bin/admin/dhcp_view_leases.cgi" method="post">

<div class="sectiontitle">'$"DHCP Leases"'</div><table class="tablesorter"><tbody><tr>

<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
	<button class="info" formaction="dhcp_fm.cgi" name="_ConfigureDHCP_" value="_">
		'$"Configure"'<br>
		<img src="'$ICON1'" alt="'$"Configure DHCP"'">
		<span>'$"View and edit the DHCP setttings"'</span>
	</button>
</td>

<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
	<button class="info" formaction="dhcp_reservations.cgi" name="_DoDHCPReservations_" value="_">
		'$"Reservations"'<br>
		<img src="'$ICON2'" alt="'$"DHCP Reservations"'">
		<span>'$"View and edit DHCP Reservations"'</span>
	</button>
</td>

<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
	<button class="info" formaction="dhcp_bans.cgi" name="_DHCPBans_" value="_">
		'$"Bans"'<br>
		<img src="'$ICON3'" alt="'$"DHCP bans"'">
		<span>'$"View and edit DHCP bans"'</span>
	</button>
</td>

<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
	<button class="info" name="_DHCPActiveLeases_" value="_OPTION_active_">
		'$"Active Leases"'<br>
		<img src="'$ICON4'" alt="'$"Show Active Leases"'">
		<span>'$"Show Active Leases"'</span>
	</button>
</td>

'

#Only show backup leases button if we have a secondary dhcp server
if [ -d /opt/karoshi/server_network/dhcp_servers ]
then
	echo '<td style="vertical-align: top; white-space: nowrap; height: 30px; width: '$WIDTH'px; text-align:center;">
		<button class="info" name="_DHCPBackupLeases_" value="_OPTION_backup_">
			'$"Backup Leases"'<br>
			<img src="'$ICON4'" alt="'$"Show Backup Leases"'">
			<span>'$"Show Backup Leases"'</span>
		</button>
		</td>'
fi

echo '
<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
	<button class="info" name="_DHCPFreeLeases_" value="_OPTION_free_">
		'$"Free Leases"'<br>
		<img src="'$ICON5'" alt="'$"Show Free Leases"'">
		<span>'$"Show Free Leases"'</span>
	</button>
</td>

'
if [ -f /opt/karoshi/server_network/dhcp/restart_required ]
then
	echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<button class="info" formaction="dhcp_bans.cgi" name="_DHCPRestart_" value="_OPTION_restartdhcp_">
			'$"Activate Changes"'<br>
			<img src="'$ICON6'" alt="'$"Activate Changes"'">
			<span>'$"Restart DHCP to activate changes"'</span>
		</button>
	</td>
'

fi

echo '</tbody></table></form></div><div id="infobox">'

if [ "$OPTION" = restartdhcp ]
then
	echo "$REMOTE_USER:$REMOTE_ADDR:" | sudo -H /opt/karoshi/web_controls/exec/dhcp_restart
	OPTION=""
	#Reload page
	echo '<form id="reloadpage" name="reservervations" action="/cgi-bin/admin/dhcp_view_leases.cgi" method="post"><script>
	document.getElementById("reloadpage").submit();
	</script></form>'
fi

#Show lease information
/opt/karoshi/web_controls/leasecheck.pl $OPTION
echo '</div></div></div></body></html>'
exit

