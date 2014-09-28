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
    <TITLE>'$"Update Moodle"'</TITLE><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</HEAD>
<BODY>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">
<b>'$"Update Moodle"'</b>
<br><br>'

########################
#Run checks on uploaded moodle archive
########################

#Check that a file has been uploaded
if [ `ls -1 /var/www/karoshi/moodle | wc -l` = 0 ]
then
MESSAGE=$"You have not uploaded a file."
show_status
fi

#Check that only one file has been uploaded
if [ `ls -1 /var/www/karoshi/moodle | wc -l` -gt 1 ]
then
MESSAGE=$"More than one file has been uploaded."
show_status
fi

#Get filename
MOODLEARCHIVE=`ls -1 /var/www/karoshi/moodle | sed -n 1,1p`

#Check that it has a .tgz file extension
if [ `echo "$MOODLEARCHIVE" | grep -c .tgz$` != 1 ]
then
MESSAGE=$"The file you have uploaded does not have a .tgz file extension."
show_status
fi

#Check archive
tar --list --file=/var/www/karoshi/moodle/"$MOODLEARCHIVE" > /var/www/karoshi/moodle_archive_list.txt 2>/dev/null
ARCHIVESTATUS=`echo $?`
if [ $ARCHIVESTATUS != 0 ]
then
MESSAGE=$"The archive you have uploaded is corrupt."
show_status
fi

if [ `grep -c moodle/config-dist.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $"This is not a correct moodle archive and is missing files" - config-dist.php`
show_status
fi

if [ `grep -c moodle/version.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $"This is not a correct moodle archive and is missing files" - version.php`
show_status
fi

if [ `grep -c moodle/install.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $"This is not a correct moodle archive and is missing files" - install.php`
show_status
fi

if [ `grep -c moodle/index.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $"This is not a correct moodle archive and is missing files" - index.php`
show_status
fi

if [ `grep -c moodle/backup/backup.php$ /var/www/karoshi/moodle_archive_list.txt` != 1 ]
then
MESSAGE=`echo $"This is not a correct moodle archive and is missing files" - backup.php`
show_status
fi

ARCHIVEMD5=`md5sum /var/www/karoshi/moodle/"$MOODLEARCHIVE" | cut -d' ' -f1`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/update_moodle_process1.cgi | cut -d' ' -f1`
#Do update
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ARCHIVEMD5:$MOODLEARCHIVE:" | sudo -H /opt/karoshi/web_controls/exec/update_moodle
EXITSTATUS=`echo $?`
if [ $EXITSTATUS = 102 ]
then
MESSAGE=$"Moodle is not installed."
show_status
fi
exit
