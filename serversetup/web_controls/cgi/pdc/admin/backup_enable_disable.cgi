#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

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

########################
#Required input variables
########################
#  _BACKUPACTION_ action to carry out. Either enable or disable
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/backup_enable_disable ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/backup_enable_disable
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo "<html><head><title>$TITLE</title>"
echo "<link rel="stylesheet" href="/css/$STYLESHEET"><script src=\"/all/stuHover.js\" type=\"text/javascript\"></script>"
echo '<meta http-equiv="REFRESH" content="0;url=/cgi-bin/admin/backup_enable_disable_fm.cgi">'
echo "</head>"
echo "<body><div id='pagecontainer'>"
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

#########################
#Assign data to variables
#########################
END_POINT=6
#Assign _KAROSHI_SERVER_
KAROSHI_SERVER=`echo $DATA | cut -d_ -f2`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/backup_enable_disable_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi
#########################
#Check data
#########################
#Check to see that the server is not blank
if [ $KAROSHI_SERVER'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><div class="sectiontitle">'$TITLE'</div><br>'
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/backup_enable_disable.cgi | cut -d' ' -f1`
#Enable - disable backup
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$KAROSHI_SERVER:" | sudo -H /opt/karoshi/web_controls/exec/backup_enable_disable
echo "</div>"
echo "</div></body></html>"
exit
