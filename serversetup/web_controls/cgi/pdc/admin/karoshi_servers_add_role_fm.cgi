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
  <title>'$"Add Server Role"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign SERVERNAME

COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#Check to see that servername is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The servername cannot be blank."
	show_status
fi

ICON=/images/warnings/server.png
ICON2=/images/warnings/server_no_config.png

#Get status of installed modules
DHCPSTATUS=""
[ -f /opt/karoshi/server_network/dhcp_servers/$SERVERNAME ] && DHCPSTATUS=$"Installed"
FILESERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/fileserver ] && FILESERVERSTATUS=$"Installed"
PRINTSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/printserver ] && PRINTSERVERSTATUS=$"Installed"
BACKUPSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/backupserver ] && BACKUPSERVERSTATUS=$"Installed"
REVERSEPROXYSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ] && REVERSEPROXYSERVERSTATUS=$"Installed"
SQUIDPROXYSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/squid ] && SQUIDPROXYSERVERSTATUS=$"Installed"
EMAILSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/emailserver ] && EMAILSERVERSTATUS=$"Installed"
HOMEACCESSSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/homeaccess ] && HOMEACCESSSTATUS=$"Installed"
MOODLESTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/moodle ] && MOODLESTATUS=$"Installed"
GITLABSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/gitlab ] && GITLABSTATUS=$"Installed"
OWNCLOUDSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/owncloud ] && OWNCLOUDSTATUS=$"Installed"
RADIUSSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/radiusserver ] && RADIUSSTATUS=$"Installed"
DISTROSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/distributionserver ] && DISTROSERVERSTATUS=$"Installed"
MONITORSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/monitoring ] && MONITORSERVERSTATUS=$"Installed"
JOOMLASTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/joomla ] && JOOMLASTATUS=$"Installed"
RADIOSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/radioserver ] && RADIOSTATUS=$"Installed"
XIBOSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/xibo ] && XIBOSTATUS=$"Installed"
KANBOARDSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/kanboard ] && KANBOARDSTATUS=$"Installed"
XERTESTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/xerte ] && XERTESTATUS=$"Installed"
WEBSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/apacheserver ] && WEBSERVERSTATUS=$"Installed"
SSHSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/remote_ssh ] && SSHSERVERSTATUS=$"Installed"
VPNSERVERSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/openvpn ] && VPNSERVERSTATUS=$"Installed"

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top;"><div class="sectiontitle">'$"Add Server Role"' - '$SERVERNAME'</div></td>
<td style="vertical-align: top;">
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Role"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the module that you want to add to the server."'</span></a>
</td></tr></tbody></table></div><div id="infobox">
<br>
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top; width: 160px; height: 40px;">'$"DHCP Server"'</td>
<td style="vertical-align: top; width: 60px;">'$DHCPSTATUS'</td>
<td style="vertical-align: top; width: 80px;">
'

if [ $SERVERNAME = `hostname-fqdn` ]
then
	echo '<form action="/cgi-bin/admin/dhcp_fm.cgi" method="post">
	<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will provide a DHCP server for your network."'</span></a></form>'
else
	echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will provide a DHCP server for your network."'<br><br>'$"This module can only be applied to the main server."'</span></a>'
fi

echo '</td><td style="vertical-align: top; width: 180px; height: 40px;">'$"File Server"'</td><td style="vertical-align: top; width: 60px;">'$FILESERVERSTATUS'</td><td style="vertical-align: top;">'

if [ $SERVERNAME != `hostname-fqdn` ] && [ ! -f /opt/karoshi/server_network/slave_ldap_servers/$SERVERNAME ]
then
	echo '<form action="/cgi-bin/admin/module_fileserver_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a server to provide home areas for selected groups of users. By default the primary domain controller provides home areas for all users."' '$"Using this feature will allow you to spread the server load in larger networks."'</span></a></form>'
else
	echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a server to provide home areas for selected groups of users. By default the primary domain controller provides home areas for all users."' '$"Using this feature will allow you to spread the server load in larger networks."'<br><br>'$"The main server already acts as a file server."'</span></a>'
fi

echo '</td></tr>'

echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$"Print Server"'</td><td style="vertical-align: top;">'$PRINTSERVERSTATUS'</td>
<td style="vertical-align: top;">'

if [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ]
then
	echo '<form action="/cgi-bin/admin/module_printserver_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a server to provide network print queues."'</span></a></form>'
else
	echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a server to provide network print queues."'<br><br>'$PRINTSERVERDEPS'</span></a>'
fi
echo '</td>'


echo '<td style="vertical-align: top; height: 40px;">'$"Backup Server"'</td><td style="vertical-align: top;">'$BACKUPSERVERSTATUS'</td><td style="vertical-align: top; height: 40px;">'

if [ $SERVERNAME != `hostname-fqdn` ]
then
	echo '<form action="/cgi-bin/admin/module_backupserver_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a backup server."'</span></a></form>
	'
else
	echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a backup server."'<br><br>'$"This module cannot be applied to your main server."'</span></a>'
fi

echo '</td></tr>'

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/apacheserver ] && [ $SERVERNAME != `hostname-fqdn` ]
then
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"Reverse Proxy Server"'</td><td style="vertical-align: top;">'$REVERSEPROXYSERVERSTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_reverse_proxy_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a reverse proxy server that allows incoming web traffic to be redirected to other servers on your network."' '$"The redirect is based on the trailing slash after the end of the domain of your site."'</span></a></form></td>'
else
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"Reverse Proxy Server"'</td><td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a reverse proxy server that allows incoming web traffic to be redirected to other servers on your network."' '$"The redirect is based on the trailing slash after the end of the domain of your site."'<br><br>'$"This module cannot be applied to a server running modules that use the apache web server."'</span></a></td>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td style="vertical-align: top; height: 40px;">'$"Squid Internet Proxy"'</td><td style="vertical-align: top;">'$SQUIDPROXYSERVERSTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_squid_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup squid and dansguardian to provide filtered internet access for the client computers."'</span></a></form></td></tr>'
else
	echo '<td style="vertical-align: top; height: 40px;">'$"Squid Internet Proxy"'</td><td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup squid and dansguardian to provide filtered internet access for the client computers."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td></tr>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"E-Mail Server"'</td><td style="vertical-align: top;">'$EMAILSERVERSTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_email_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a server to provide E-Mail services."'</span></a></form></td>'
else
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"E-Mail Server"'</td><td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a server to provide E-Mail services."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td style="vertical-align: top; height: 40px;">'$"Home Access Server"'</td><td style="vertical-align: top;">'$HOMEACCESSSTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_smbwebclient_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a server to provide web based access to home areas."'</span></a></form></td></tr>'
else
	echo '<td style="vertical-align: top; height: 40px;">'$"Home Access Server"'</td><td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a server to provide web based access to home areas."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td></tr>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"Moodle Server"'</td><td style="vertical-align: top;">'$MOODLESTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_moodle_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup the moodle E-Learning system."'</span></a></form></td>'
else
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"Moodle Server"'</td><td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup the moodle E-Learning system."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td>'
fi

if [ -f /opt/karoshi/server_network/servers/$SERVERNAME/apacheserver ]
then
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"Gitlab Server"'</td><td style="vertical-align: top;">'$GITLABSTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_gitlab_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup the Gitlab module."'</span></a></form></td>'
else
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"Gitlab Server"'</td><td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup the Gitlab Server."'<br><br>'$"This module cannot be applied to a server without the web server module."'</span></a></td>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ] && [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ]
then
	echo '<td style="vertical-align: top; height: 40px;">'$"Owncloud Server"'</td><td style="vertical-align: top;">'$OWNCLOUDSTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_owncloud_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will provide a cloud file storage system for web access to files."'</span></a></form></td></tr>'
else
	echo '<td style="vertical-align: top; height: 40px;">'$"Owncloud Server"'</td><td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will provide a cloud file storage system for web access to files."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td></tr>'
fi

echo '<tr><td style="vertical-align: top; height: 40px;">'$"Radius Server"'</td><td style="vertical-align: top;">'$RADIUSSTATUS'</td><td style="vertical-align: top; height: 40px;">'

if [ -f /opt/karoshi/server_network/servers/$SERVERNAME/1dc ]
then
	echo '<form action="/cgi-bin/admin/module_radius_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a radius server which can be used for your wireless access points."'</span></a></form>'
else
	echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a radius server which can be used for your wireless access points."'<br><br>'$"This module can only be applied to a domain controller."'</span></a>'
fi
echo '</td>'

echo '<td style="vertical-align: top; height: 40px;">'$"Distribution Server"'</td><td style="vertical-align: top;">'$DISTROSERVERSTATUS'</td>
<td style="vertical-align: top; height: 40px;">'

if [ -f /opt/karoshi/server_network/dhcpserver ]
then
	echo '<form action="/cgi-bin/admin/module_distributionserver_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a distribution server for centralised linux client installations."'</span></a></form></td></tr>'
else
	echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a distribution server for centralised linux client installations."'<br><br>'$"This module needs the DHCP module functioning to allow the clients to be able to network boot."'</span></a>'
fi

echo '</td></tr>'

echo '<tr><td style="vertical-align: top; height: 40px;">'$"Monitor Server"'</td><td style="vertical-align: top;">'$MONITORSERVERSTATUS'</td>
<td style="vertical-align: top; height: 40px;">
'
if [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ] && [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<form action="/cgi-bin/admin/module_monitoring_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will provide a monitoring server for you network that will alert you if there are any problems."'</span></a></form>'
else
	echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will provide a monitoring server for you network that will alert you if there are any problems."'<br><br>'$"This module cannot be applied to your main server."'</span></a>'
fi

echo '</td>'



if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td style="vertical-align: top; height: 40px;">'$"Joomla"'</td><td style="vertical-align: top;">'$JOOMLASTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_joomla_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a server to provide Joomla content management."'</span></a></form></td></tr>'
else
	echo '<td style="vertical-align: top; height: 40px;">'$"Joomla"'</td><td></td>
	<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a server to provide Joomla content management."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td></tr>'
fi

echo '<tr><td style="vertical-align: top; height: 40px;">'$"Internet Radio Server"'</td><td style="vertical-align: top;">'$RADIOSTATUS'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_radioserver_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will set up the server to act as an internet radio server using icecast."'</span></a></form></td>'


if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td style="vertical-align: top; height: 40px;">'$"Xibo Server"'</td><td style="vertical-align: top;">'$XIBOSTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_xibo_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup the Xibo Digital Signage system."'</span></a></form></td></tr>'
else
	echo '<td style="vertical-align: top; height: 40px;">'$"Xibo Server"'</td><td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup the Xibo Digital Signage system."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td></tr>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"Kanboard"'</td><td style="vertical-align: top;">'$KANBOARDSTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_kanboard_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup Kanboard which is a web based project management system."'</span></a></form></td>'
else
	echo '<tr><td style="vertical-align: top; height: 40px;">'$"Kanboard"'</td><td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup Kanboard which is a web based project management system."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td style="vertical-align: top; height: 40px;">'$"Xerte"'</td><td style="vertical-align: top;">'$XERTESTATUS'</td><td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_xerte_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup the Xerte E-Learning development environment for your users."'</span></a></form></td></tr>'
else
	echo '<td style="vertical-align: top; height: 40px;">'$"Xerte"'</td>td></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup the Xerte E-Learning development environment for your users."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td></tr>'
fi

#if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
#then
#echo '<td style="vertical-align: top; height: 40px;">'$"OCS Inventory"'</td>
#<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_ocsinventory_fm.cgi" method="post">
#<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This provides an automated inventory system for your client computers."'</span></a></form></td></tr>'
#else
#echo '<td style="vertical-align: top; height: 40px;">'$"OCS Inventory"'</td>
#<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This provides an automated inventory system for your client computers."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td></tr>'
#fi

echo '</tbody></table><br>'

#Advanced Modules
echo '<div class="sectiontitle">'$"Add Advanced Server Role"' - '$SERVERNAME'</div><br><table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$"Custom application"'</td><td style="vertical-align: top; width: 60px; height: 40px;"></td>
<td style="vertical-align: top; width: 80px;"><form action="/cgi-bin/admin/module_custom_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will add in a name of a non Karoshi application for your server."'</span></a></form></td>'


if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td style="vertical-align: top; width: 180px; height: 40px;">'$"Web Server"'</td><td style="vertical-align: top; width: 60px; height: 40px;">'$WEBSERVERSTATUS'</td><td style="vertical-align: top; width: 80px;"><form action="/cgi-bin/admin/module_web_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a server to provide LAMP web services with ftp access."'</span></a></form></td></tr>'
else
	echo '<td style="vertical-align: top; width: 180px; height: 40px;">'$"Web Server"'</td><td style="vertical-align: top; width: 60px; height: 40px;"></td><td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a server to provide LAMP web services with ftp access."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span></a></td></tr>'
fi

echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$"Remote SSH Access"'</td><td style="vertical-align: top;">'$SSHSERVERSTATUS'</td>
<td style="vertical-align: top; width: 80px;">
'

if [ $SERVERNAME = `hostname-fqdn` ]
then
	echo '<form action="/cgi-bin/admin/module_ssh_access_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will allow remote ssh access to your main server. This can also be used to join this server up to another karoshi system so that users created on the master server will also be created here."'</span></a></form></td>'
else
	echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will allow remote ssh access to your main server."' '$"This can also be used to join this server up to another karoshi system so that users created on the master server will also be created here."'</span></a></td>'
fi



#echo '</td><td style="vertical-align: top; width: 180px; height: 40px;">'$"Shell Access"'</td><td style="vertical-align: top; width: 80px;">'

#if [ $SERVERNAME = `hostname-fqdn` ]
#then
#echo '<form action="/cgi-bin/admin/module_ajaxterm_fm.cgi" method="post">
#<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup an embedded shell in the web management."'</span></a></form>'
#else
#echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup an embedded shell in the web management."'</span></a>'
#fi
#echo '</td>'

echo '<td style="vertical-align: top; width: 180px; height: 40px;">'$"VPN Server"'</td><td style="vertical-align: top;">'$VPNSERVERSTATUS'</td>
<td style="vertical-align: top; width: 80px;">
'

if [ $SERVERNAME != `hostname-fqdn` ] && [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ]
then
	echo '<form action="/cgi-bin/admin/module_vpn_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will setup a VPN server for client devices to connect to your network."'</span></a></form>'
else
	echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will setup a VPN server for client devices to connect to your network."'</span></a>'
fi


if [ -f /opt/karoshi/serversetup/variables/enable_federation_module ]
then
	echo '<td style="vertical-align: top; width: 180px; height: 40px;">'$"Federated Server"'</td><td style="vertical-align: top; width: 80px;">'
	if [ $SERVERNAME != `hostname-fqdn` ]
	then
		echo '<form action="/cgi-bin/admin/module_federation_control_fm.cgi" method="post"><input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$"This will modify a Karoshi main server to be part of a federation so that all users created on the main system are also created on the federated systems."' '$"This module can only be applied to a main server."'</span></a></form>'
	else
		echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$"This will modify a Karoshi main server to be part of a federation so that all users created on the main system are also created on the federated systems."' '$"This module can only be applied to a main server."'<br><br>'$"This module cannot be applied to your main server."'</span></a>'
	fi
fi

echo '</td></tr></tbody></table></div></div></div></body></html>'
exit
