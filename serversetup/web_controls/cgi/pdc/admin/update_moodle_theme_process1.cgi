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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/update_moodle_theme ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/update_moodle_theme
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
echo 'window.location = "/cgi-bin/admin/update_moodle_theme_fm.cgi";'
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
</HEAD>
<BODY>
'

########################
#Run checks on uploaded moodle archive
########################

#Check that a file has been uploaded
if [ `ls -1 /var/www/karoshi/moodle_theme | wc -l` = 0 ]
then
MESSAGE=$UPLOADERROR1
show_status
fi

#Check that only one file has been uploaded
if [ `ls -1 /var/www/karoshi/moodle_theme | wc -l` -gt 1 ]
then
MESSAGE=$UPLOADERROR2
show_status
fi

#Get filename
MOODLETHEME=`ls -1 /var/www/karoshi/moodle_theme | sed -n 1,1p`

#Check that it has a .zip file extension
if [ `echo "$MOODLETHEME" | grep -c .zip$` != 1 ]
then
MESSAGE=$ZIPERROR1
show_status
fi

#Check archive
unzip -l /var/www/karoshi/moodle_theme/"$MOODLETHEME" > /var/www/karoshi/moodle_theme_list.txt 2>/dev/null
ARCHIVESTATUS=`echo $?`
if [ $ARCHIVESTATUS != 0 ]
then
MESSAGE=$CORRUPTARCHIVEMSG
show_status
fi

if [ `grep -c config.php$ /var/www/karoshi/moodle_theme_list.txt` = 0 ]
then
MESSAGE=`echo $ZIPERROR2 - config.php`
show_status
fi

if [ `grep -c styles.php$ /var/www/karoshi/moodle_theme_list.txt` = 0 ]
then
MESSAGE=`echo $ZIPERROR2 - styles.php`
show_status
fi

if [ `grep -c header.html$ /var/www/karoshi/moodle_theme_list.txt` = 0 ]
then
MESSAGE=`echo $ZIPERROR2 - header.html`
show_status
fi

if [ `grep -c footer.html$ /var/www/karoshi/moodle_theme_list.txt` = 0 ]
then
MESSAGE=`echo $ZIPERROR2 - footer.html`
show_status
fi

ARCHIVEMD5=`md5sum /var/www/karoshi/moodle_theme/"$MOODLETHEME" | cut -d' ' -f1`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/update_moodle_theme_process1.cgi | cut -d' ' -f1`
#Do update
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ARCHIVEMD5:$MOODLETHEME:" | sudo -H /opt/karoshi/web_controls/exec/update_moodle_theme
EXITSTATUS=`echo $?`
MESSAGE=`echo "$MOODLETHEME" : $COMPLETEDMSG`
if [ $EXITSTATUS = 102 ]
then
MESSAGE=$NOTINSTALLEDMSG
fi
show_status
exit
