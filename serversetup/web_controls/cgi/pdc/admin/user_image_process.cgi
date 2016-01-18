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
#  _USERNAME_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
#  _GROUP_      This is the primary group for the new user eg yr2000, staff, officestaff.
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Upload User Image"'</title><meta http-equiv="REFRESH" content="0; URL=/cgi-bin/admin/user_image_upload_fm.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox"><div class="sectiontitle">'$"Upload User Image"'</div><br></div><div id="infobox">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR

function show_status {

echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
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
#Check input file
[ -d /var/www/karoshi/user_image_upload ] || mkdir -p /var/www/karoshi/user_image_upload
chmod 0700 /var/www/karoshi/
chmod 0700 /var/www/karoshi/user_image_upload
#Check to see that only one file has been uploaded
if [ `dir /var/www/karoshi/user_image_upload --format=single-column | wc -l` != 1 ]
then
	MESSAGE=$"Upload image error."
	show_status
fi
IMAGEFILE=`ls -1 /var/www/karoshi/user_image_upload | sed -n 1,1p`
#Check to see if image is a .jpg / zip / tar.gz
if [ `echo $IMAGEFILE | grep -c .jpg$` != 1 ] && [ `echo $IMAGEFILE | grep -c .zip$` != 1 ] && [ `echo $IMAGEFILE | grep -c .tar.gz$` != 1 ]
then
	MESSAGE=$"The file you have uploaded does not have a suitable file extension."
	show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/user_image_process.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$IMAGEFILE:" | sudo -H /opt/karoshi/web_controls/exec/user_image_upload
STATUS=`echo $?`
MESSAGE=`echo $IMAGEFILE - $"User Image uploaded."`

if [ $STATUS = 101 ]
then
	MESSAGE=`echo $"There was a problem with this action." $"Please check the karoshi web administration logs for more details."`
fi
if [ $STATUS = 103 ]
then
	MESSAGE=`echo $IMAGEFILE - $"The name of this image does not match a username or enrollment number."`
fi
show_status
echo "</div></div></body></html>"
