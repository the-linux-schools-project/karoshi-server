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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
########################
#Required input variables
########################
#  _PRINTERNAME_
#  _LOCATION_
#  _PRINTERADDRESS_
#  _PRINTERQUEUE_
#  _PRINTERDESC_
#  _PRINTERTYPE_
#  _PRINTERPORT_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_ppd_upload ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_ppd_upload
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<html><head><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%/+-'`
#########################
#Assign data to variables
#########################
#Get printer details
if [ ! -f /var/www/karoshi/uploadppd ]
then
MESSAGE=$ERRORMSG7
show_status
fi
source /var/www/karoshi/uploadppd
rm -f /var/www/karoshi/uploadppd

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function view_printers {
echo '<SCRIPT language="Javascript">'
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
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

#Check input file
[ -d /var/www/karoshi/ppd_files ] || mkdir -p /var/www/karoshi/ppd_files
chmod 0700 /var/www/karoshi/
chmod 0700 /var/www/karoshi/ppd_files
if [ `dir /var/www/karoshi/ppd_files --format=single-column | wc -l` != 1 ]
then
MESSAGE=$ERRORMSG5
show_status
fi
PPDFILE=`ls /var/www/karoshi/ppd_files`
#Check file extension
if [ `echo $PPDFILE | grep -c .ppd` = 0 ]
then
MESSAGE=$ERRORMSG6
show_status
fi
#Create MD5 sum for the ppd file
touch /var/www/karoshi/ppd_files/ppdcheck.md5
chmod 0600 /var/www/karoshi/ppd_files/ppdcheck.md5
md5sum /var/www/karoshi/ppd_files/"$PPDFILE" > /var/www/karoshi/ppd_files/ppdcheck.md5

#########################
#Check data
#########################
#Check to see that PRINTERNAME is not blank
if [ $PRINTERNAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that PAGESIZE is not blank
if [ $PAGESIZE'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that Colour is not blank
if [ $COLOUR'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi

echo "<div id="actionbox">"
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers_ppd_upload3.cgi | cut -d' ' -f1`
#Add ppd file to printer
sudo -H /opt/karoshi/web_controls/exec/printers_ppd_add $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$PRINTERNAME:$PAGESIZE:$COLOUR
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $ERRORMSG4`
show_status
fi
MESSAGE=`echo $COMPLETEDMSG $PRINTERNAME`
show_status
echo "</div>"
echo "</div></body></html>"
exit
