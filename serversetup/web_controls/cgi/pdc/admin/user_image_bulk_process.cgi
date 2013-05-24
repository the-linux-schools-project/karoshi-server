#!/bin/bash
#Copyright (C) 2008 Paul Sharrad
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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/user_image_bulk_upload ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/user_image_bulk_upload
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#GROUP=`echo $DATA | cut -d'_' -f3`

function show_status {

echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/user_image_bulk_upload_fm.cgi"'
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
#Check input file
[ -d /var/www/karoshi/user_image_bulk_upload ] || mkdir -p /var/www/karoshi/user_image_bulk_upload
chmod 0700 /var/www/karoshi/
chmod 0700 /var/www/karoshi/user_image_bulk_upload
#Check to see that only one file has been uploaded
if [ `dir /var/www/karoshi/user_image_bulk_upload --format=single-column | wc -l` != 1 ]
then
MESSAGE=$ERRORMSG1
show_status
fi
COMPRESSEDFILE=`ls -1 /var/www/karoshi/user_image_bulk_upload | sed -n 1,1p`
#Check to see if file is a .tar.gz or a .zip
if [ `echo $COMPRESSEDFILE | grep -c .zip$` != 1 ] && [ `echo $COMPRESSEDFILE | grep -c .tar.gz$` != 1 ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Process compressed image file
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/user_image_bulk_process.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$COMPRESSEDFILE:" | sudo -H /opt/karoshi/web_controls/exec/user_image_bulk_upload

echo '</div></body></html>'
exit
