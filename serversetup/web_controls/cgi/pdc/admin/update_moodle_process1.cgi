#!/bin/bash
#Copyright (C) 2008  Paul Sharrad

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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/update_moodle ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/update_moodle
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/update_moodle_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <TITLE>'$TITLE'</TITLE><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</HEAD>
<BODY>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">
<b>'$TITLE'</b>
<br><br>'

########################
#Run checks on uploaded moodle archive
########################

#Check that a file has been uploaded
if [ `ls -1 /var/www/karoshi/moodle | wc -l` = 0 ]
then
MESSAGE=$UPLOADERROR1
show_status
fi

#Check that only one file has been uploaded
if [ `ls -1 /var/www/karoshi/moodle | wc -l` -gt 1 ]
then
MESSAGE=$UPLOADERROR2
show_status
fi

#Get filename
MOODLEARCHIVE=`ls -1 /var/www/karoshi/moodle | sed -n 1,1p`

#Check that it has a .tgz file extension
if [ `echo "$MOODLEARCHIVE" | grep -c .tgz$` != 1 ]
then
MESSAGE=$TGZERROR1
show_status
fi

#Check archive
tar --list --file=/var/www/karoshi/moodle/"$MOODLEARCHIVE" > /var/www/karoshi/moodle_archive_list.txt 2>/dev/null
ARCHIVESTATUS=`echo $?`
if [ $ARCHIVESTATUS != 0 ]
then
MESSAGE=$CORRUPTARCHIVEMSG
show_status
fi

if [ `grep -c moodle/config-dist.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $TGZERROR2 - config-dist.php`
show_status
fi

if [ `grep -c moodle/version.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $TGZERROR2 - version.php`
show_status
fi

if [ `grep -c moodle/install.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $TGZERROR2 - install.php`
show_status
fi

if [ `grep -c moodle/index.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $TGZERROR2 - index.php`
show_status
fi

if [ `grep -c moodle/backup/backup.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $TGZERROR2 - backup.php`
show_status
fi

ARCHIVEMD5=`md5sum /var/www/karoshi/moodle/"$MOODLEARCHIVE" | cut -d' ' -f1`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/update_moodle_process1.cgi | cut -d' ' -f1`
#Do update
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ARCHIVEMD5:$MOODLEARCHIVE:" | sudo -H /opt/karoshi/web_controls/exec/update_moodle
EXITSTATUS=`echo $?`
if [ $EXITSTATUS = 102 ]
then
MESSAGE=$NOTINSTALLEDMSG
show_status
fi
exit
