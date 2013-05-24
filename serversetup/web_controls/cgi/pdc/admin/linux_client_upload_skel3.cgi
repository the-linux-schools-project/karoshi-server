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
########################
#Required input variables
########################
#  _LINUXVERSION_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_upload_skel ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_upload_skel
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=9
#Assign username
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LINUXVERSIONcheck ]
then
let COUNTER=$COUNTER+1
LINUXVERSION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/linux_client_upload_skel_fm.cgi";'
echo '</script>'
echo "</body></html>"
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
#Check to see that LINUXVERSION is not blank
if [ $LINUXVERSION'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that the directory exists
if [ ! -d /var/www/karoshi/skel_upload/ ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that only one file exists
if [ `ls -1 /var/www/karoshi/skel_upload/ | wc -l` != 1 ]
then
MESSAGE=$ERRORMSG3
show_status
fi
SKELFILENAME=`ls -1 /var/www/karoshi/skel_upload/`
#Check to see that the file is a tar.gz
if [ `echo $SKELFILENAME | grep -c .tar.gz` != 1 ]
then
MESSAGE=$ERRORMSG4
show_status
fi
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/linux_client_upload_skel3.cgi | cut -d' ' -f1`
#Convert Spaces
SKELFILENAME=`echo $SKELFILENAME | sed 's/ /1234567890/g'`
#Upload Skel
sudo -H /opt/karoshi/web_controls/exec/linux_client_upload_skel $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$LINUXVERSION:$SKELFILENAME
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 0 ]
then
MESSAGE=`echo $LINUXVERSION: $COMPLETEDMSG`
else
MESSAGE=`echo $LINUXVERSION: $ERRORMSG5`
fi
show_status
exit
