#!/bin/bash
#Copyright (C) 2010  Paul Sharrad
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
  <title>'$TITLE2'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
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
echo "</body></html>"
exit
}

#Check to see that servername is not blank
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

ICON=/images/warnings/server.png

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

function get_role_name {
ROLE_NAME=$ROLE_FILE
ROLE_NAME_STATUS=notset
CONSEQUENCES=""
if [ $ROLE_FILE = apachereverseproxyserver ]
then
ROLE_NAME=$REVERSEPROXYMSG
CONSEQUENCES=$REVERSEPROXY_REMOVAL
ROLE_NAME_STATUS=set
MODULES=yes
fi
if [ $ROLE_FILE = distributionserver ]
then
ROLE_NAME=$DISTRIBUTIONSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$DISTRIBUTIONSERVER_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = homeaccess ]
then
ROLE_NAME=$HOMEACCESSSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$HOMEACCESSSERVER_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = apacheserver ]
then
ROLE_NAME=$WEBSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$APACHESERVER_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = backupserver ]
then
ROLE_NAME=$BACKUPSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$BACKUPSERVER_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = dhcp_server ] && [ $SERVERNAME = $HOSTNAME ]
then
ROLE_NAME=$DHCPSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$DHCP_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = emailserver ]
then
ROLE_NAME=$EMAILSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$EMAILSERVER_REMOVAL
MODULES=yes
elif [ $SERVERNAME != $HOSTNAME ] && [ $ROLE_FILE = fileserver ]
then
ROLE_NAME=$FILESERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$FILESERVER_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = joomlaserver ]
then
ROLE_NAME=$JOOMLAMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$JOOMLA_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = moodleserver ]
then
ROLE_NAME=$MOODLESERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$MOODLE_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = ocsserver ]
then
ROLE_NAME=$OCSSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$OCS_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = printserver ]
then
ROLE_NAME=$PRINTSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$PRINSERVER_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = squid ]
then
ROLE_NAME=$SQUIDSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$SQUID_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = monitoring ]
then
ROLE_NAME=$MONITORSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$MONITORING_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = remote_ssh ]
then
ROLE_NAME=$SSHACCESSMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$SSHACCESS_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = casserver ]
then
ROLE_NAME=$CASSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$CASSERVER_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = radioserver ]
then
ROLE_NAME=$RADIOSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$RADIOSERVER_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = federated_server ] && [ $SERVERNAME != $HOSTNAME ]
then
ROLE_NAME=$FEDERATIONCONTROLMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$FEDERATIONCONTROL_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = ldapserver ] && [ $SERVERNAME != $HOSTNAME ]
then
ROLE_NAME=$SLAVELDAPSERVERMSG
ROLE_NAME_STATUS=set
CONSEQUENCES=$LDAP_REMOVAL
MODULES=yes
elif [ $ROLE_FILE = no_role ]
then
MODULES=yes
else
if [ $ROLE_FILE != 1pdc ] && [ $ROLE_FILE != ldapserver ] && [ $ROLE_FILE != fileserver ]
then
ROLE_NAME=`echo $ROLE_FILE | sed 's/+/ /g'`
ROLE_NAME_STATUS=set
CONSEQUENCES="$ROLE_NAME"
MODULES=yes
fi
fi
}

REMOVE_CODE=`echo ${RANDOM:0:3}`

echo '
<div id="actionbox">
<b>'$TITLE2' - '$SERVERNAME'</b><br><br><img alt="Warning" src="/images/warnings/warning.png"> <b>'$MODULEWARNINGMSG1'</b> - '$MODULEWARNINGMSG2'<br><br>
<form action="/cgi-bin/admin/karoshi_servers_remove_role.cgi" method="post">
<input name="___FORMCODE___" value="'$REMOVE_CODE'" type="hidden">
<input name="___SERVERNAME___" value="'$SERVERNAME'" type="hidden">
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>'

MODULES=no

if [ $SERVERNAME != $HOSTNAME ] && [ ! -d /opt/karoshi/server_network/federated_ldap_servers/$SERVERNAME ]
then
echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$REMOVE_SERVER_MSG'</td><td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><input name="___MODULE___REMOVESERVER___" type="image" class="images" src="'$ICON'" value=""><span>'$REMOVE_SERVER_CONSEQUENCES'</span></a></td></tr>'
fi

if [ -d /opt/karoshi/server_network/federated_ldap_servers/$SERVERNAME ]
then
ROLE_FILE=federated_server
get_role_name
if [ $ROLE_NAME_STATUS != notset ]
then
echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$ROLE_NAME'</td><td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><input name="___MODULE___'$ROLE_FILE'___" type="image" class="images" src="'$ICON'" value=""><span>'$CONSEQUENCES'</span></a></td></tr>'
fi
else
for ROLES in /opt/karoshi/server_network/servers/$SERVERNAME/*
do
ROLE_FILE=`basename $ROLES`
get_role_name

if [ $ROLE_NAME_STATUS != notset ]
then
echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$ROLE_NAME'</td><td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><input name="___MODULE___'$ROLE_FILE'___" type="image" class="images" src="'$ICON'" value=""><span>'$CONSEQUENCES'</span></a></td></tr>'
fi
done
fi
if [ $MODULES = yes ]
then
echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$CODEMSG'</td>
        <td style="vertical-align: top; text-align: left;"><b>'$REMOVE_CODE'</b></td></tr>
<tr><td style="vertical-align: top; width: 180px; height: 40px;">'$CONFIRMMSG'</td>
        <td style="vertical-align: top; text-align: left;"><input tabindex= "2" name="___MODULECODE___" maxlength="3" size="3" type="text"></td><td style="vertical-align: top;">
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$CODEHELPMSG'</span></a></td></tr>'
fi
echo '</tbody></table><br>'
if [ $MODULES != yes ]
then
echo $NO_MODULES_WARN
fi
echo '</form></div></body></html>'
exit
