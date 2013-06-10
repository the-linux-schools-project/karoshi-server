#!/bin/bash
#Copyright (C) 2007  Paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1

DHCPCONFPATH=/etc/dhcpd.conf
[ -f /etc/dhcp3/dhcpd.conf ] && DHCPCONFPATH=/etc/dhcp3/dhcpd.conf

[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/dhcp ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/dhcp
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()">'
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
echo '<form action="/cgi-bin/admin/dhcp.cgi" method="post"><div id="actionbox"><b>'$TITLE'</b><br><br>'

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
SUBNET=`echo $DOMAINNAMESERVER | cut -d. -f1-2 | sed 's/$/.0.0/g'`
SUBNETMASK=`grep netmask /etc/network/interfaces | sed -n 1,1p | cut -d' ' -f2`
STARTADDRESS=
ENDADDRESS=
DEFAULTLEASETIME=21600
MAXLEASETIME=43200
fi

echo '
  <table class="standard" style="text-align: left; height: 91px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$DNSMSG'</td>
        <td><input value="'$DOMAINNAMESERVER'" name="_DOMAINNAMESERVER_" tabindex= "1" size="20" type="text"></td><td>
      </td></tr>
	<tr>
        <td>
'$NETBIOSMSG'</td>
        <td><input tabindex= "1" value="'$NETBIOSSERVER'" name="_NETBIOSSERVER_" size="20" type="text"></td><td>
      </td></tr>
      <tr>
        <td>
'$GATEWAYMSG'</td>
        <td><input tabindex= "2" value="'$ROUTER'" name="_ROUTER_" size="20" type="text"></td><td>
      </td></tr>
	<tr>
        <td>
'$SUBNETMSG'</td>
        <td><input value="'$SUBNET'" name="_SUBNET_" size="20" tabindex= "3" type="text"></td><td>
      </td></tr>
      <tr>
        <td>
'$SUBNETMASKMSG'</td>
        <td><input value="'$SUBNETMASK'" name="_SUBNETMASK_" size="20" tabindex= "3" type="text"></td><td>
      </td></tr>
      <tr>
        <td>
'$STARTADDRMSG'</td>
        <td><input tabindex= "4" value="'$STARTADDRESS'" name="_STARTADDRESS_" size="20" type="text"></td><td>
      </td></tr>
      <tr>
        <td>
'$ENDADDRMSG'</td>
        <td><input tabindex= "5" value="'$ENDADDRESS'" name="_ENDADDRESS_" size="20" type="text"></td><td>
      </td></tr>
      <tr>
        <td>
'$DEFAULTLEASEMSG'</td>
        <td><input tabindex= "6" value="'$DEFAULTLEASETIME'" name="_DEFAULTLEASETIME_" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$DEFAULTLEASEHELP'</span></a>
      </td></tr>
      <tr>
        <td>
'$MAXLEASEMSG'</td>
        <td><input tabindex= "7" value="'$MAXLEASETIME'" name="_MAXLEASETIME_" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$MAXLEASEHELP'</span></a>
      </td></tr>
    </tbody>
  </table><br><br>
</div>
<div id="submitbox">
<input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div>
</form>
</body>
</html>
'
exit

