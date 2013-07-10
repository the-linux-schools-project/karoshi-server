#!/bin/bash
#backup_assign
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/restore_files ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/restore_files
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body onLoad="start()">'


function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi"'
echo '</script>'
echo "</body></html>"
exit
}


#Check to see that a backup server has been configured
if [ ! -d /opt/karoshi/server_network/backup_servers/backup_settings ]
then
MESSAGE=$ERRORMSG1
show_status
fi

if [ `ls -1 /opt/karoshi/server_network/backup_servers/backup_settings | wc -l` = 0 ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '
<form action="/cgi-bin/admin/file_manager.cgi" method="post">
<div id="actionbox">'

#############################
#Show list of servers to restore to
#############################
echo '<b>'$SYSTEMRESTOREMSG'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a><br><br>'
SERVERLISTARRAY=( `ls -1 /opt/karoshi/server_network/backup_servers/backup_settings/` )
SERVERLISTCOUNT=${#SERVERLISTARRAY[@]}
SERVERCOUNTER=0
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'

while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}

#Get backup path
BACKUPPATH=/home/backups/$KAROSHISERVER
#Get backup server
BACKUPSERVER=`sed -n 1,1p /opt/karoshi/server_network/backup_servers/backup_settings/$KAROSHISERVER/backupserver`

echo '<td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_network_ACTION_ENTER_SERVER_'$BACKUPSERVER'_LOCATION_'$BACKUPPATH'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$KAROSHISERVER'<br><br>'

cat /opt/karoshi/server_network/servers/$KAROSHISERVER/* | sed '/<a href/c'"&nbsp"

echo '</span></a><br>'$KAROSHISERVER'</td>'

[ $SERVERCOUNTER = 5 ] && echo '</tr><tr>'
let SERVERCOUNTER=$SERVERCOUNTER+1
done
echo '</tr></tbody></table><br>'

#############################
#Show list of primary groups to restore from.
#############################

echo '<b>'$USERRESTOREMSG'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a><br><br><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;"><b>'$PRIGROUPMSG'</b></td><td style="width: 90px;"><b>'$SERVERMSG'</b></td><td style="width: 180px;"><b>'$RESTOREMSG'</b></td><td style="width: 180px;"><b>'$PRIGROUPMSG'</b></td><td style="width: 90px;"><b>'$SERVERMSG'</b></td><td><b>'$RESTOREMSG'</b></td></tr>
'
START_LINE=yes
ICON1=/images/submenus/system/computer.png
for PRI_GROUP in /opt/karoshi/server_network/group_information/*
do
PRI_GROUP=`basename $PRI_GROUP`
source /opt/karoshi/server_network/group_information/$PRI_GROUP


if [ -d /opt/karoshi/server_network/backup_servers/backup_settings/$SERVER/ ]
then
#Get backup server
BACKUPSERVER=`sed -n 1,1p /opt/karoshi/server_network/backup_servers/backup_settings/$SERVER/backupserver`
#Get backup path
BACKUPPATH=/home/backups/$SERVER/$PRI_GROUP
if [ $START_LINE = yes ]
then
echo '<tr><td>'$PRI_GROUP'</td><td>'$SERVER'</td><td><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_network_ACTION_ENTER_SERVER_'$BACKUPSERVER'_LOCATION_'$BACKUPPATH'_" type="image" class="images" src="'$ICON1'" value="_PRIGROUP_'$PRI_GROUP'_SERVER_'$SERVER'_"><span>'$RESTOREMSG'<br>'$SERVER' - '$PRI_GROUP'</span></a></td>'
START_LINE=no
else
echo '<td>'$PRI_GROUP'</td><td>'$SERVER'</td><td><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_network_ACTION_ENTER_SERVER_'$BACKUPSERVER'_LOCATION_'$BACKUPPATH'_" type="image" class="images" src="'$ICON1'" value="_PRIGROUP_'$PRI_GROUP'_SERVER_'$SERVER'_"><span>'$RESTOREMSG'<br>'$SERVER' - '$PRI_GROUP'</span></a></td></tr>'
START_LINE=yes
fi
fi
done
echo '</tbody></table><br>'

echo '</div></form></body></html>'
exit

