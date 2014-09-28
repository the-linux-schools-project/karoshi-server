#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

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
#  _LINUXVERSION_
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Linux Client upload skel"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
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
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$"You must access this page via https."
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$"You must be a Karoshi Management User to complete this action."
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$"You must be a Karoshi Management User to complete this action."
show_status
fi
#########################
#Check data
#########################
#Check to see that LINUXVERSION is not blank
if [ $LINUXVERSION'null' = null ]
then
MESSAGE=$"The Linux Version must not be blank."
show_status
fi
#Check to see that the directory exists
if [ ! -d /var/www/karoshi/skel_upload/ ]
then
MESSAGE=$"The upload directory does not exist."
show_status
fi
#Check to see that only one file exists
if [ `ls -1 /var/www/karoshi/skel_upload/ | wc -l` != 1 ]
then
MESSAGE=$"Incorrect file count."
show_status
fi
SKELFILENAME=`ls -1 /var/www/karoshi/skel_upload/`
#Check to see that the file is a tar.gz
if [ `echo $SKELFILENAME | grep -c .tar.gz` != 1 ]
then
MESSAGE=$"You have not uploaded a tar.gz file."
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
MESSAGE=`echo $LINUXVERSION: $"Skel archive uploaded."`
else
MESSAGE=`echo $LINUXVERSION: $"There was a problem uploading the skel archive. Please check the Karoshi web management logs."`
fi
show_status
exit
