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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/karoshi_servers_add_role ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/karoshi_servers_add_role
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
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

ICON=/images/warnings/server.png
ICON2=/images/warnings/server_no_config.png

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin


echo '<div id="actionbox3"><div id="titlebox">'


echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top;"><div class="sectiontitle">'$TITLE' - '$SERVERNAME'</div></td>
<td style="vertical-align: top;">
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Role"><img class="images" alt="" src="/images/help/info.png"><span>'$CHOOSEROLEHELP'</span></a>
</td></tr></tbody></table></div><div id="infobox">
<br>
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$DHCPSERVERMSG'</td>
<td style="vertical-align: top; width: 80px;">
'

if [ $SERVERNAME = `hostname-fqdn` ]
then
echo '<form action="/cgi-bin/admin/dhcp_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$DHCPSERVERHELPMSG'</span></a></form>'
else
echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$DHCPSERVERHELPMSG'<br><br>'$MAINSERVERDEPS'</span></a>'
fi

echo '</td><td style="vertical-align: top; width: 180px; height: 40px;">'$FILESERVERMSG'</td><td style="vertical-align: top;">'

if [ $SERVERNAME != `hostname-fqdn` ] && [ ! -f /opt/karoshi/server_network/slave_ldap_servers/$SERVERNAME ]
then
echo '<form action="/cgi-bin/admin/module_fileserver_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$FILESERVERHELPMSG'</span></a></form>'
else
echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$FILESERVERHELPMSG'<br><br>'$FILESERVERDEPS'</span></a>'
fi

echo '</td></tr>'

echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$PRINTSERVERMSG'</td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/module_printserver_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$PRINTERSERVERHELPMSG'</span></a></form></td>'


echo '<td style="vertical-align: top; height: 40px;">'$BACKUPSERVERMSG'</td><td style="vertical-align: top; height: 40px;">'

if [ $SERVERNAME != `hostname-fqdn` ]
then
echo '<form action="/cgi-bin/admin/module_backupserver_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$BACKUPSERVERHELPMSG'</span></a></form>
'
else
echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$BACKUPSERVERHELPMSG'<br><br>'$NEWSERVERDEPS'</span></a>'
fi

echo '</td></tr>'



if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/apacheserver ] && [ $SERVERNAME != `hostname-fqdn` ]
then
echo '<tr><td style="vertical-align: top; height: 40px;">'$REVERSEPROXYMSG'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_reverse_proxy_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$REVERSEPROXYHELPMSG'</span></a></form></td>'
else
echo '<tr><td style="vertical-align: top; height: 40px;">'$REVERSEPROXYMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$REVERSEPROXYHELPMSG'<br><br>'$NGINXDEPS'</span></a></td>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
echo '<td style="vertical-align: top; height: 40px;">'$SQUIDSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_squid_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$SQUIDSERVERHELPMSG'</span></a></form></td></tr>'
else
echo '<td style="vertical-align: top; height: 40px;">'$SQUIDSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$SQUIDSERVERHELPMSG'<br><br>'$APACHEDEPS'</span></a></td></tr>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
echo '<tr><td style="vertical-align: top; height: 40px;">'$EMAILSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_email_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$EMAILSERVERHELPMSG'</span></a></form></td>'
else
echo '<tr><td style="vertical-align: top; height: 40px;">'$EMAILSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$EMAILSERVERHELPMSG'<br><br>'$APACHEDEPS'</span></a></td>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
echo '<td style="vertical-align: top; height: 40px;">'$HOMEACCESSSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_smbwebclient_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$HOMEACCESSSERVERHELPMSG'</span></a></form></td></tr>'
else
echo '<td style="vertical-align: top; height: 40px;">'$HOMEACCESSSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$HOMEACCESSSERVERHELPMSG'<br><br>'$APACHEDEPS'</span></a></td></tr>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
echo '<tr><td style="vertical-align: top; height: 40px;">'$MOODLESERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_moodle_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$MOODLEHELPMSG'</span></a></form></td>'
else
echo '<tr><td style="vertical-align: top; height: 40px;">'$MOODLESERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$MOODLEHELPMSG'<br><br>'$APACHEDEPS'</span></a></td>'
fi

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
echo '<td style="vertical-align: top; height: 40px;">'$OCSSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_ocsinventory_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$OCSINVENTORYHELPMSG'</span></a></form></td></tr>'
else
echo '<td style="vertical-align: top; height: 40px;">'$OCSSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$OCSINVENTORYHELPMSG'<br><br>'$APACHEDEPS'</span></a></td></tr>'
fi

echo '<tr><td style="vertical-align: top; height: 40px;">'$RADIUSSERVERMSG'</td><td style="vertical-align: top; height: 40px;">'

if [ $SERVERNAME = `hostname-fqdn` ]
then

echo '<form action="/cgi-bin/admin/module_radius_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$RADIUSSERVERHELPMSG'</span></a></form>'
else
echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$RADIUSSERVERHELPMSG'<br><br>'$MAINSERVERDEPS'</span></a>'
fi
echo '</td>'

echo '<td style="vertical-align: top; height: 40px;">'$DISTRIBUTIONSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;">'

if [ -f /opt/karoshi/server_network/dhcpserver ]
then
echo '<form action="/cgi-bin/admin/module_distributionserver_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$DISTRIBUTIONSERVERHELPMSG'</span></a></form></td></tr>'
else
echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$DISTRIBUTIONSERVERHELPMSG'<br><br>'$DISRIBUTIONDEPS'</span></a>'
fi

echo '</td></tr><tr><td style="vertical-align: top; height: 40px;">'$RADIOSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_radioserver_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$RRADIOSSERVERHELPMSG'</span></a></form></td>'

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
echo '<td style="vertical-align: top; height: 40px;">'$JOOMLAMSG'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_joomla_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$JOOMLAHELPMSG'</span></a></form></td>
</tr>'
else
echo '<td style="vertical-align: top; height: 40px;">'$JOOMLAMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$JOOMLAHELPMSG'<br><br>'$APACHEDEPS'</span></a></td></tr>'
fi

echo '<tr><td style="vertical-align: top; height: 40px;">'$MONITORSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;">
'
if [ $SERVERNAME != `hostname-fqdn` ]
then
echo '<form action="/cgi-bin/admin/module_monitoring_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$MONITORSERVERHELPMSG'</span></a></form>'
else
echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$MONITORSERVERHELPMSG'<br><br>'$NEWSERVERDEPS'</span></a>'
fi

echo '</td>'

if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ] && [ -f /opt/karoshi/server_network/zones/internal/servers/$SERVERNAME ]
then
echo '<td style="vertical-align: top; height: 40px;">'$OWNCLOUDSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;">
<form action="/cgi-bin/admin/module_owncloud_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$OWNCLOUDSERVERHELPMSG'</span></a></form></td></tr>'
else
echo '<td style="vertical-align: top; height: 40px;">'$OWNCLOUDSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$OWNCLOUDSERVERHELPMSG'<br><br>'$APACHEDEPS'</span></a></td></tr>'
fi


if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
echo '<tr><td style="vertical-align: top; height: 40px;">'$XIBOSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><form action="/cgi-bin/admin/module_xibo_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$XIBOHELPMSG'</span></a></form></td></tr>'
else
echo '<tr><td style="vertical-align: top; height: 40px;">'$XIBOSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$XIBOHELPMSG'<br><br>'$APACHEDEPS'</span></a></td></tr>'
fi


echo '</tbody></table><br>'

#Advanced Modules
echo '<b>'$TITLE3' - '$SERVERNAME'</b><br><br><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$CUSTOMSERVERMSG'</td>
<td style="vertical-align: top; width: 80px;"><form action="/cgi-bin/admin/module_custom_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$CUSTOMSERVERHELPMSG'</span></a></form></td>'


if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/reverseproxyserver ]
then
echo '<td style="vertical-align: top; width: 180px; height: 40px;">'$WEBSERVERMSG'</td>
<td style="vertical-align: top; width: 80px;"><form action="/cgi-bin/admin/module_web_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$WEBSERVERHELPMSG'</span></a></form></td></tr>'
else
echo '<td style="vertical-align: top; width: 180px; height: 40px;">'$WEBSERVERMSG'</td>
<td style="vertical-align: top; height: 40px;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$WEBSERVERHELPMSG'<br><br>'$APACHEDEPS'</span></a></td></tr>'
fi

echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$SSHACCESSMSG'</td>
<td style="vertical-align: top; width: 80px;">
'

if [ $SERVERNAME = `hostname-fqdn` ]
then
echo '<form action="/cgi-bin/admin/module_ssh_access_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$SSHACCESSHELPMSG'</span></a></form>'
else
echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$SSHACCESSHELPMSG'</span></a>'
fi
#echo '</td><td style="vertical-align: top; width: 180px; height: 40px;">'$SHELLACCESSMSG'</td><td style="vertical-align: top; width: 80px;">'

#if [ $SERVERNAME = `hostname-fqdn` ]
#then
#echo '<form action="/cgi-bin/admin/module_ajaxterm_fm.cgi" method="post">
#<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$SHELLACCESSHELMSG'</span></a></form>'
#else
#echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$SHELLACCESSHELMSG'</span></a>'
#fi
#echo '</td>'

if [ -f /opt/karoshi/serversetup/variables/enable_federation_module ]
then
echo '<td style="vertical-align: top; width: 180px; height: 40px;">'$FEDERATIONCONTROLMSG'</td><td style="vertical-align: top; width: 80px;">'
if [ $SERVERNAME != `hostname-fqdn` ]
then
echo '<form action="/cgi-bin/admin/module_federation_control_fm.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_" value="_SERVERNAME_'$SERVERNAME'_" type="hidden"><a class="info" href="javascript:void(0)"><input name="_SERVERNAME_'$SERVERNAME'_" type="image" class="images" src="'$ICON'" value="_SERVERNAME_'$SERVERNAME'_"><span>'$FEDERATIONCONTROLHELPMSG'</span></a></form>'
else
echo '<a class="info" href="javascript:void(0)"><img class="images" alt="" src="'$ICON2'"><span>'$FEDERATIONCONTROLHELPMSG'<br><br>'$NEWSERVERDEPS'</span></a>'
fi
fi

echo '</td></tr></tbody></table></div></div></div></body></html>'
exit



