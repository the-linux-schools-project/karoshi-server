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
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
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
SAVAPAGESTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/savapage ] && SAVAPAGESTATUS=$"Installed"
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
NEXTCLOUDSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/nextcloud ] && NEXTCLOUDSTATUS=$"Installed"
RICHDOCUMENTSSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/richdocuments ] && RICHDOCUMENTSSTATUS=$"Installed"
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
SHELLINABOXSTATUS=""
[ -f /opt/karoshi/server_network/servers/$SERVERNAME/shellserver ] && VPNSERVERSTATUS=$"Installed"
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top;"><div class="sectiontitle">'$"Add Server Role"' - '$SERVERNAME'</div></td>
<td style="vertical-align: top;">
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Role"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the module that you want to add to the server."'</span></a>
</td></tr></tbody></table></div><div id="infobox">
<table class="tablesorter" style="text-align: left;" ><thead>
<tr><th style="width: 200px;">'$"Module"'</th><th style="width: 100px;">'$"Status"'</th><th style="width: 100px;">'$"Install"'</th><th style="width: 200px;">'$"Module"'</th><th style="width: 100px;">'$"Status"'</th><th style="width: 100px;">'$"Install"'</th></tr></thead>
<tbody><tr>'

echo '<td>'$"Backup Server"'</td><td>'$BACKUPSERVERSTATUS'</td><td>'

if [ $SERVERNAME != `hostname-fqdn` ]
then
	echo '<form action="/cgi-bin/admin/module_backupserver_fm.cgi" method="post">
	<button class="info" name="_AddbackupServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Backup Server"'">
	<span>'$"This will setup a backup server."'</span>
	</button>
	</form>
	</td>
	'
else
	echo '
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddbackupServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"backup Server"'">
	<span>'$"This will setup a backup server."'<br><br>'$"This module cannot be applied to your main server."'</span>
	</button>
	</form>
	</td>
	'
fi

#Col2
echo '<td>'$"Monitor Server"'</td><td>'$MONITORSERVERSTATUS'</td><td>'
if [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ] && [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<form action="/cgi-bin/admin/module_monitoring_fm.cgi" method="post">
	<button class="info" name="_AddMonitoringServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Monitoring Server"'">
	<span>'$"This will provide a monitoring server for you network that will alert you if there are any problems."'</span>
	</button>
	</form></td>'
else
	echo '
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddMonitoringServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Monitoring Server"'">
	<span>'$"This will provide a monitoring server for you network that will alert you if there are any problems."'<br><br>'$"This module cannot be applied to your main server."'</span>
	</button>
	</form></td>
'
fi

echo '</tr><tr>'

echo '<td>'$"DHCP Server"'</td><td>'$DHCPSTATUS'</td><td>'

if [ $SERVERNAME = `hostname-fqdn` ] || [ -f /opt/karoshi/server_network/servers/$SERVERNAME/1dc ]
then
	echo '<form action="/cgi-bin/admin/dhcp_fm.cgi" method="post">
	<button class="info" name="_AddDHCPServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"This will provide a DHCP server for your network."'">
	<span>'$"This will provide a DHCP server for your network."'</span>
	</button>
	</form>
	</td>'
else
	echo '

	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddDHCPServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"DHCP Server"'">
	<span>'$"This will provide a DHCP server for your network."'<br><br>'$"This module can only be applied to the main server or an Additional Domain Controller."'</span>
	</button>
	</form>
	</td>
	'
fi

#Col2
if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"Moodle Server"'</td><td>'$MOODLESTATUS'</td><td><form action="/cgi-bin/admin/module_moodle_fm.cgi" method="post">
	<button class="info" name="_AddMoodleServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Moodle Server"'">
	<span>'$"This will setup the moodle E-Learning system."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"Moodle Server"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddMoodleServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Moodle Server"'">
	<span>'$"This will setup the moodle E-Learning system."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

echo '</tr><tr>'

echo '<td>'$"Distribution Server"'</td><td>'$DISTROSERVERSTATUS'</td><td>'

if [ -f /opt/karoshi/server_network/dhcpserver ]
then
	echo '<form action="/cgi-bin/admin/module_distributionserver_fm.cgi" method="post">
	<button class="info" name="_AddDistributionServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Distribution Server"'">
	<span>'$"This will setup a distribution server for centralised linux client installations."'</span>
	</button>
	</form></td>'
else
	echo '
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddDistributionServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Distribution Server"'">
	<span>'$"This will setup a distribution server for centralised linux client installations."'<br><br>'$"This module needs the DHCP module functioning to allow the clients to be able to network boot."'</span>
	</button>
	</form></td>
	'
fi

#Col2
if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ] && [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ]
then
	echo '<td>'$"Nextcloud Server"'</td><td>'$NEXTCLOUDSTATUS'</td><td><form action="/cgi-bin/admin/module_nextcloud_fm.cgi" method="post">
	<button class="info" name="_AddNextCloudServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Nextcloud Server"'">
	<span>'$"This will provide a cloud file storage system for web access to files."'</span>
	</button>
	</form></td>'
else
	echo '</tr><tr><td>'$"Nextcloud Server"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddownCloudServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Nextcloud Server"'">
	<span>'$"This will provide a cloud file storage system for web access to files."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

echo '</tr><tr>'

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"E-Mail Server"'</td><td>'$EMAILSERVERSTATUS'</td><td><form action="/cgi-bin/admin/module_email_fm.cgi" method="post">
	<button class="info" name="_AddEMailServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"E-Mail Server"'">
	<span>'$"This will setup a server to provide E-Mail services."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"E-Mail Server"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddEmailServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"E-MailServer"'">
	<span>'$"This will setup a server to provide E-Mail services."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

#Col2
echo '<td>'$"Print Server"'</td><td>'$PRINTSERVERSTATUS'</td><td>'

if [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ]
then
	echo '<form action="/cgi-bin/admin/module_printserver_fm.cgi" method="post">
	<button class="info" name="_AddPrintServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Print Server"'">
	<span>'$"This will setup a server to provide network print queues."'</span>
	</button>
	</form>
	</td>
	'
else
	echo '
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddPrintServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Print Server"'">
	<span>'$"This will setup a server to provide network print queues."'<br><br>'$PRINTSERVERDEPS'</span>
	</button>
	</form>
	</td>
	'
fi

echo '</tr><tr>'

echo '<td>'$"File Server"'</td><td>'$FILESERVERSTATUS'</td><td>'

if [ $SERVERNAME != `hostname-fqdn` ] && [ ! -f /opt/karoshi/server_network/slave_ldap_servers/$SERVERNAME ]
then
	echo '<form action="/cgi-bin/admin/module_fileserver_fm.cgi" method="post">
	<button class="info" name="_AddFileerver_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Add File Server."'">
	<span>'$"This will setup a server to provide home areas for selected groups of users. By default the primary domain controller provides home areas for all users."' '$"Using this feature will allow you to spread the server load in larger networks."'</span>
	</button>
	</form></td>'
else
	echo '
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddFileServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"File Server"'">
	<span>'$"This will setup a server to provide home areas for selected groups of users. By default the primary domain controller provides home areas for all users."' '$"Using this feature will allow you to spread the server load in larger networks."'<br><br>'$"The main server already acts as a file server."'</span>
	</button>
	</form></td>'
fi

#Col2
echo '<td>'$"Radius Server"'</td><td>'$RADIUSSTATUS'</td><td>'

if [ -f /opt/karoshi/server_network/servers/$SERVERNAME/1dc ]
then
	echo '<form action="/cgi-bin/admin/module_radius_fm.cgi" method="post">
	<button class="info" name="_AddRadiusServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Radius Server"'">
	<span>'$"This will setup a radius server which can be used for your wireless access points."'</span>
	</button>
	</form></td>'
else
	echo '
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddRadiusServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Radius Server"'">
	<span>'$"This will setup a radius server which can be used for your wireless access points."'<br><br>'$"This module can only be applied to a domain controller."'</span>
	</button>
	</form></td>'
fi

echo '</tr><tr>'

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"Gitlab Server"'</td><td>'$GITLABSTATUS'</td><td><form action="/cgi-bin/admin/module_gitlab_fm.cgi" method="post">
	<button class="info" name="_AddGitServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Git Server"'">
	<span>'$"This will setup the Gitlab module."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"Gitlab Server"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddGitlabServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Gitlab Server"'">
	<span>'$"This will setup the Gitlab Server."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

#Col2
if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/apacheserver ] && [ $SERVERNAME != `hostname-fqdn` ]
then
	echo '<td>'$"Reverse Proxy Server"'</td><td>'$REVERSEPROXYSERVERSTATUS'</td><td><form action="/cgi-bin/admin/module_reverse_proxy_fm.cgi" method="post">
	<button class="info" name="_AddReverseproxyServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Reverse Proxy Server"'">
	<span>'$"This will setup a reverse proxy server that allows incoming web traffic to be redirected to other servers on your network."' '$"The redirect is based on the trailing slash after the end of the domain of your site."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"Reverse Proxy Server"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddReverseproxyServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Reverse Proxy Server"'">
	<span>'$"This will setup a reverse proxy server that allows incoming web traffic to be redirected to other servers on your network."' '$"The redirect is based on the trailing slash after the end of the domain of your site."'<br><br>'$"This module cannot be applied to a server running modules that use the apache web server."'</span>
	</button>
	</form>
	</td>'
fi

echo '</tr><tr>'

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"Home Access Server"'</td><td>'$HOMEACCESSSTATUS'</td><td><form action="/cgi-bin/admin/module_smbwebclient_fm.cgi" method="post">
	<button class="info" name="_AddHomeAccessServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Home Access Server"'">
	<span>'$"This will setup a server to provide web based access to home areas."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"Home Access Server"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddHomeAccessServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Home Access Server"'">
	<span>'$"This will setup a server to provide web based access to home areas."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

#Col2
echo '<td>'$"Savapage"'</td><td>'$SAVAPAGESTATUS'</td><td>'

if [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ] && [ -f /opt/karoshi/server_network/printserver ] && [ "$SERVERNAME" = $(cat /opt/karoshi/server_network/printserver) ]
then
	echo '<form action="/cgi-bin/admin/module_savapage_fm.cgi" method="post">
	<button class="info" name="_AddSavapageServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Savapage"'">
	<span>'$"This will set up the Savapage Libre Print Management System allowing Web Printing from all devices."'</span>
	</button>
	</form>
	</td>
	'
else
	echo '
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddSavapageServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Savapage"'">
	<span>'$"This will set up the Savapage Libre Print Management System allowing Web Printing from all devices."'<br><br>'$"This module can only be applied to a server that already has the print server module applied."'</span>
	</button>
	</form>
	</td>
	'
fi

echo '</tr><tr>'

echo '<td>'$"Internet Radio Server"'</td><td>'$RADIOSTATUS'</td>
<td><form action="/cgi-bin/admin/module_radioserver_fm.cgi" method="post">
	<button class="info" name="_AddRadioServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Radio Server"'">
	<span>'$"This will set up the server to act as an internet radio server using icecast."'</span>
	</button>
	</form>
	</td>'

#Col2
if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"Squid Internet Proxy"'</td><td>'$SQUIDPROXYSERVERSTATUS'</td><td><form action="/cgi-bin/admin/module_squid_fm.cgi" method="post">
	<button class="info" name="_AddSquidProxyServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Squid Proxy Server"'">
	<span>'$"This will setup squid and dansguardian to provide filtered internet access for the client computers."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"Squid Internet Proxy"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddSquidProxyServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Squid Proxy Server"'">
	<span>'$"This will setup squid and dansguardian to provide filtered internet access for the client computers."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

echo '</tr><tr>'

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"Joomla"'</td><td>'$JOOMLASTATUS'</td><td><form action="/cgi-bin/admin/module_joomla_fm.cgi" method="post">
	<button class="info" name="_AddJoomlaServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Joomla Server"'">
	<span>'$"This will setup a server to provide Joomla content management."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"Joomla"'</td><td></td>
	<td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddJoomlaServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Joomla Server"'">
	<span>'$"This will setup a server to provide Joomla content management."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

#Col2
if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"Xerte"'</td><td>'$XERTESTATUS'</td><td><form action="/cgi-bin/admin/module_xerte_fm.cgi" method="post">
	<button class="info" name="_AddXerteServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Xerte Server"'">
	<span>'$"This will setup the Xerte E-Learning development environment for your users."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"Xerte"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddXerteServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Xerte Server"'">
	<span>'$"This will setup the Xerte E-Learning development environment for your users."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

echo '</tr><tr>'

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"Kanboard"'</td><td>'$KANBOARDSTATUS'</td><td><form action="/cgi-bin/admin/module_kanboard_fm.cgi" method="post">
	<button class="info" name="_AddKanboardServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Kanboard Server"'">
	<span>'$"This will setup Kanboard which is a web based project management system."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"Kanboard"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddKanboardServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Kanboard Server"'">
	<span>'$"This will setup Kanboard which is a web based project management system."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

#Col2
if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"Xibo Server"'</td><td>'$XIBOSTATUS'</td><td>
	<form action="/cgi-bin/admin/module_xibo_fm.cgi" method="post">
	<button class="info" name="_AddXiboServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Xibo Server"'">
	<span>'$"This will setup the Xibo Digital Signage system."'</span>
	</button>
	</form>
	</td>'
else
	echo '<td>'$"Xibo Server"'</td><td></td><td>
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddXiboServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"Xibo Server"'">
	<span>'$"This will setup the Xibo Digital Signage system."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

echo '</tr>'

#echo '<td></td><td></td><td></td></tr>'

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
echo '<div class="sectiontitle">'$"Add Advanced Server Role"' - '$SERVERNAME'</div><br><table class="tablesorter" style="text-align: left;" ><thead>
<tr><th style="width: 200px;">'$"Module"'</th><th style="width: 100px;">'$"Status"'</th><th style="width: 100px;">'$"Install"'</th><th style="width: 200px;">'$"Module"'</th><th style="width: 100px;">'$"Status"'</th><th style="width: 100px;">'$"Install"'</th></tr></thead>

<tbody>
	<tr><td>'$"Custom application"'</td><td></td>
	<td><form action="/cgi-bin/admin/module_custom_fm.cgi" method="post">
	<button class="info" name="_AddCustom_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Custom"'">
	<span>'$"This will add in a name of a non Karoshi application for your server."'</span>
	</button>
	</form></td>'

echo '<td>'$"VPN Server"'</td><td>'$VPNSERVERSTATUS'</td><td>'

if [ $SERVERNAME != `hostname-fqdn` ] && [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ]
then
	echo '<form action="/cgi-bin/admin/module_vpn_fm.cgi" method="post">
	<button class="info infoabove" name="_AddVPNServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"VPN Server"'">
	<span>'$"This will setup a VPN server for client devices to connect to your network."'</span>
	</button>
	</form>'
else
	echo '
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info infoabove" name="_AddVPNerver_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"VPN Server"'">
	<span>'$"You can only install a VPN server on an additional server."'</span>
	</button>
	</form>
	'
fi

echo '</tr><tr>'

echo '<td>'$"Remote SSH Access"'</td><td>'$SSHSERVERSTATUS'</td><td>'

if [ $SERVERNAME = `hostname-fqdn` ]
then
	echo '<form action="/cgi-bin/admin/module_ssh_access_fm.cgi" method="post">

	<button class="info infoabove" name="_AddSSHServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"SSH Server"'">
	<span>'$"This will allow remote ssh access to your main server. This can also be used to join this server up to another karoshi system so that users created on the master server will also be created here."'</span>
	</button>
	</form></td>'
else
	echo '
	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info infoabove" name="_AddSSHServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"SSH Server"'">
	<span>'$"This will allow remote ssh access to your main server."' '$"This can also be used to join this server up to another karoshi system so that users created on the master server will also be created here."'</span>
	</button>
	</form>
	</td>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
	echo '<td>'$"Web Server"'</td><td>'$WEBSERVERSTATUS'</td><td><form action="/cgi-bin/admin/module_web_fm.cgi" method="post">
	<button class="info" name="_AddLampServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"Lamp Server"'">
	<span>'$"This will setup a server to provide LAMP web services with ftp access."'</span>
	</button>
	</form></td>'
else
	echo '<td>'$"Web Server"'</td><td></td><td>

	<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info" name="_AddLAMPServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"LAMP Server"'">
	<span>'$"This will setup a server to provide LAMP web services with ftp access."'<br><br>'$"This module cannot be applied to a server running the reverse proxy module."'</span>
	</button>
	</form>
	</td>'
fi

if [ -f /opt/karoshi/serversetup/variables/enable_federation_module ]
then
	echo '<td>'$"Federated Server"'</td><td>'
	if [ $SERVERNAME != `hostname-fqdn` ]
	then
		echo '<form action="/cgi-bin/admin/module_federation_control_fm.cgi" method="post">
		<button class="info infoabove" name="_AddFederationServer_" value="_SERVERNAME_'$SERVERNAME'_">
		<img src="'$ICON'" alt="'$"Federation Server"'">
		<span>'$"This will modify a Karoshi main server to be part of a federation so that all users created on the main system are also created on the federated systems."' '$"This module can only be applied to a main server."'</span>
		</button>
		</form></td>'
	else
		echo '
		<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
		<button class="info infoabove" name="_AddFederatedServer_" value="_SERVERNAME_'$SERVERNAME'_">
		<img src="'$ICON2'" alt="'$"Federated Server"'">
		<span>'$"This will modify a Karoshi main server to be part of a federation so that all users created on the main system are also created on the federated systems."' '$"This module can only be applied to a main server."'<br><br>'$"This module cannot be applied to your main server."'</span>
		</button>
		</form></td>'
	fi




fi

echo '</tr><tr>'

echo '<td>'$"Shell Access"'</td><td>'$SHELLINABOXSTATUS'</td><td style="vertical-align: top; width: 80px;">'

if [ $SERVERNAME = `hostname-fqdn` ]
then
	echo '<form action="/cgi-bin/admin/module_shellinabox_fm.cgi" method="post">
	<button class="info infoabove" name="_AddShellServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON'" alt="'$"This will setup an embedded shell in the web management."'">
	<span>'$"This will setup an embedded shell in the web management."'</span>
	</button>
	</form>
	'
else
	echo '<form action="/cgi-bin/admin/karoshi_servers_add_role_fm.cgi" method="post">
	<button class="info infoabove" name="_AddShellServer_" value="_SERVERNAME_'$SERVERNAME'_">
	<img src="'$ICON2'" alt="'$"DHCP Server"'">
	<span>'$"This will setup an embedded shell in the web management."'<br><br>'$"This module can only be applied to the main server or an Additional Domain Controller."'</span>
	</button>
	</form>'
fi

echo '<td></td><td></td><td></td>'

echo '</tr>'

echo '</tbody></table></div></div></div></body></html>'
exit
