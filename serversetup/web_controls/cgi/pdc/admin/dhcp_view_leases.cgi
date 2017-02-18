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

echo '<div id="actionbox3"><div id="titlebox"><form action="/cgi-bin/admin/dhcp_view_leases.cgi" method="post">

<table class="standard" style="text-align: left;" >
<tr><td style="width:180px"><div class="sectiontitle">'$"View DHCP Leases"'</div></td><td style="vertical-align: top;">
<button class="button" formaction="dhcp_fm.cgi" name="_ConfigureDHCP_" value="_">
'$"Configure DHCP"'
</button>
</td><td>
<button class="button" formaction="dhcp_reservations.cgi" name="_DHCPReservations_" value="_">
'$"DHCP Reservations"'
</button>
</td>
<td>
<button class="button" formaction="dhcp_bans.cgi" name="_DHCPBans_" value="_">
'$"DHCP bans"'
</button>
</td>
<td>
<input name="_OPTION_active_" type="submit" class="button" value="'$"Show Active Leases"'"></td>'

#Only show backup leases button if we have a secondary dhcp server
[ -d /opt/karoshi/server_network/dhcp_servers ] && echo '<td style="vertical-align: top;"><input name="_OPTION_backup_" type="submit" class="button" value="'$"Show Backup Leases"'"></td>'

echo '<td><input name="_OPTION_free_" type="submit" class="button" value="'$"Show Free Leases"'"></td>
</tr>
</tbody></table><br></form>
</div><div id="infobox">'

#Show lease information
/opt/karoshi/web_controls/leasecheck.pl $OPTION
echo '</div></div></div></body></html>'
exit

