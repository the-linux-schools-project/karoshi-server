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
#  _LINUXVERSION_  version of client
#  _FILENAME_  Name of background
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Linux Background - Select"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "linux_client_background_upload_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_backgrounds {
echo '<SCRIPT language="Javascript">'
echo 'window.location = "linux_client_choose_background_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#Check to see if any files have been uploaded
FILECOUNT=0
if [ -d /var/www/karoshi/linux_background_upload/ ]
then
	FILECOUNT=$(ls -1 /var/www/karoshi/linux_background_upload/ | wc -l)
	FILENAME=$(ls -1 /var/www/karoshi/linux_background_upload/ | sed -n 1,1p)
fi

if [ "$FILECOUNT" != 1 ]
then
	MESSAGE=$"An incorrect number of files have been uploaded."
	show_status
	exit
fi

#Check to see that FILENAME is not blank
if [ -z "$FILENAME" ]
then
	MESSAGE=$"The filename cannot be blank."
	show_status
fi


#Check that file is a png
if [[ $(echo "$FILENAME" | grep -c .png$) = 0 ]]
then
	MESSAGE=$"You have not uploaded a png file."
	show_status
	exit
else
	FILENAME=$(ls -1 /var/www/karoshi/linux_background_upload/ | sed -n 1,1p)
	#replace spaces
	FILENAME2="${FILENAME// /-}"
	
	[ ! -f /var/www/karoshi/linux_background_upload/"$FILENAME2" ] && mv /var/www/karoshi/linux_background_upload/"$FILENAME" /var/www/karoshi/linux_background_upload/"$FILENAME2"
fi

#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [[ $(grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#Check that background with this filename exists
if [ ! -f /var/www/karoshi/linux_background_upload/"$FILENAME2" ]
then
	MESSAGE=$"You have not uploaded a png file."
	show_status
fi

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/linux_client_background_upload2.cgi | cut -d' ' -f1)

sudo -H /opt/karoshi/web_controls/exec/linux_client_background_upload2 "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$FILENAME2:"
if [ "$?" = 0 ]
then
	MESSAGE=''$"Uploaded file"': '$FILENAME'\n\n'$"The background has been uploaded."''
else
	MESSAGE=''$"There was a problem with this action."' '$"Please check the karoshi web administration logs for more details."''
fi
show_backgrounds
exit
