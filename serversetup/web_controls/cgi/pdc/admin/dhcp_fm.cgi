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

DHCPCONFPATH=/etc/dhcpd.conf
[ -f /etc/dhcp3/dhcpd.conf ] && DHCPCONFPATH=/etc/dhcp3/dhcpd.conf

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
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
FILE=`echo $DATA | cut -s -d_ -f7`

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/dhcp.cgi" method="post"><div id="actionbox3"><div id="titlebox">

<table class="standard" style="text-align: left;" >
<tr><td style="vertical-align: top; width:180px"><div class="sectiontitle">'$"Configure DHCP"'</div></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Configure_DHCP"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the settings that you want to use for your client devices."'</span></a></td>
<td style="vertical-align: top;"><a href="dhcp_view_leases.cgi"><input class="button" type="button" name="" value="'$"View DHCP Leases"'"></a></td><td style="vertical-align: top;"><a href="dhcp_reservations.cgi"><input class="button" type="button" name="" value="'$"DHCP Reservations"'"></a></td>
</tr>
</tbody></table><br><br></div><div id="infobox">'

#Get current dhcp data

if [ -f /opt/karoshi/server_network/dhcp/dhcp_settings ]
then
	source /opt/karoshi/server_network/dhcp/dhcp_settings
else
	#Guess some useful numbers
	#Domain name server - use this server ip
	DOMAINNAMESERVER=`net lookup $HOSTNAME`
	#Use this server ip
	NETBIOSSERVER=$DOMAINNAMESERVER
	ROUTER=`grep gateway /etc/network/interfaces | sed -n 1,1p | cut -d' ' -f2`
	SUBNETMASK=`grep netmask /etc/network/interfaces | sed -n 1,1p | cut -d' ' -f2`
	SUBNET=`ipcalc -n $DOMAINNAMESERVER/$SUBNETMASK | grep ^Network: | sed 's/ * / /g' | cut -d' ' -f2 | cut -d"/" -f1`
	STARTADDRESS=
	ENDADDRESS=
	DEFAULTLEASETIME=21600
	MAXLEASETIME=43200
fi

#Check for a secondary dhcp server
SECONDARY_DHCP_SERVER=`[ -d /opt/karoshi/server_network/zones/internal/additional_domain_controllers/ ] && ls -1 /opt/karoshi/server_network/zones/internal/additional_domain_controllers/ | sed -n 1,1p`

echo '
  <table class="standard" style="text-align: left; height: 91px;" >
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"DNS Server IP"'</td>
        <td><input value="'$DOMAINNAMESERVER'" name="_DOMAINNAMESERVER_" tabindex= "1" size="20" type="text" readonly="readonly"></td><td>
      </td></tr>
	<tr>
        <td>
'$"Netbios Name Server"'</td>
        <td><input tabindex= "1" value="'$NETBIOSSERVER'" name="_NETBIOSSERVER_" size="20" type="text" readonly="readonly"></td><td>
      </td></tr>
      <tr>
        <td>
'$"Gateway"'</td>
        <td><input tabindex= "2" value="'$ROUTER'" name="_ROUTER_" size="20" type="text"></td><td>
      </td></tr>
	<tr>
        <td>
'$"Subnet"'</td>
        <td><input value="'$SUBNET'" name="_SUBNET_" size="20" tabindex= "3" type="text"></td><td>
      </td></tr>
      <tr>
        <td>
'$"Subnet Mask"'</td>
        <td><input value="'$SUBNETMASK'" name="_SUBNETMASK_" size="20" tabindex= "3" type="text"></td><td>
      </td></tr>
      <tr>
        <td>
'$"Start Address"'</td>
        <td><input tabindex= "4" value="'$STARTADDRESS'" name="_STARTADDRESS_" size="20" type="text"></td><td>
      </td></tr>
      <tr>
        <td>
'$"End Address"'</td>
        <td><input tabindex= "5" value="'$ENDADDRESS'" name="_ENDADDRESS_" size="20" type="text"></td><td>
      </td></tr>
      <tr>
        <td>
'$"Default Lease Time"'</td>
        <td><input tabindex= "6" value="'$DEFAULTLEASETIME'" name="_DEFAULTLEASETIME_" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Configure_DHCP"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the default lease time in seconds."'</span></a>
      </td></tr>
      <tr>
        <td>
'$"Max Lease Time"'</td>
        <td><input tabindex= "7" value="'$MAXLEASETIME'" name="_MAXLEASETIME_" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Configure_DHCP"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the maximum lease time in seconds."'</span></a>
      </td></tr>'

#Show secondary DHCP server
if [ ! -z "$SECONDARY_DHCP_SERVER" ]
then
	echo '<tr><td>'$"Secondary DHCP Server"'</td><td>'$SECONDARY_DHCP_SERVER'</td></tr>'
fi

echo '</tbody></table>'

if [ ! -z "$SECONDARY_DHCP_SERVER" ]
then
	echo '<input type="hidden" name="_SECONDARYSERVER_" value="'$SECONDARY_DHCP_SERVER'">'
fi

echo '<br><br><input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></div></form></div></body></html>'
exit

