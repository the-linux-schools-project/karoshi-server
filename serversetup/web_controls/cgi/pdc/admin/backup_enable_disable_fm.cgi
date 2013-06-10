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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/backup_enable_disable ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/backup_enable_disable
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script></head><body onLoad="start()">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><b>'$TITLE'</b><br><br>'

echo '<form action="/cgi-bin/admin/backup_enable_disable.cgi" name="selectservers" method="post">'

#Get backup status for this server
BACKUPSTATUS="Disable Backup"
BACKUP_ICON=/images/submenus/system/backup_enabled.png

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>'
echo '<tr><td style="width: 180px;"><b>Server</b></td><td><b>Status</b></td></tr>'

#Get backup status for the servers

if [ ! -d /opt/karoshi/server_network/backup_servers/backup_settings/ ]
then
echo $ERRORMSG1
echo '</div></body></html>'
exit
fi

if [ `ls -1 /opt/karoshi/server_network/backup_servers/backup_settings/ | wc -l` = 0 ]
then
echo $ERRORMSG1
echo '</div></body></html>'
exit
fi

for KAROSHI_SERVERS in /opt/karoshi/server_network/backup_servers/backup_settings/*
do
KAROSHI_SERVER=`basename $KAROSHI_SERVERS`
BACKUPSTATUS="Disable Backup"
BACKUP_ICON=/images/submenus/system/backup_enabled.png
if [ -f /opt/karoshi/server_network/backup_servers/stop_backup_$KAROSHI_SERVER ]
then
BACKUPSTATUS="Enable Backup"
BACKUP_ICON=/images/submenus/system/backup_disabled.png
fi
echo '<tr><td>'$KAROSHI_SERVER'</td><td><a class="info" href="javascript:void(0)"><input name="_'$KAROSHI_SERVER'_" type="image" class="images" src="'$BACKUP_ICON'" value="_'$KAROSHI_SERVER'_"><span>'$BACKUPSTATUS'</span></a></td></tr>'

done
echo '</tbody></table><br>
</div>
</form>
</div></body></html>'
exit
