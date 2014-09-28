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
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Assign Printers to Locations"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><meta http-equiv="REFRESH" content="0;url=/cgi-bin/admin/printers.cgi"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
DATA=`echo $DATA | sed 's/_PRINTERNAME_//g' | sed 's/_LOCATION_/,/g'`
PRINTER=`echo $DATA | cut -d, -f1`
LOCATIONS=( `echo $DATA | cut -d, -f2- | sed 's/,/ /g'` )

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
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
export MESSAGE=$"No Printers are available."
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
#Check to see that LOCATION is not blank
if [ $LOCATIONS'null' = null ]
then
MESSAGE=$"You have not chosen a location."
show_status
fi
#Check to see that PRINTER is not blank
if [ $PRINTER'null' = null ]
then
MESSAGE=$"You have not chosen any printers."
show_status
fi
#Check to see that LOCATION exists
if [ ! -f /var/lib/samba/netlogon/locations.txt ]
then
MESSAGE=$"No Printers are available."
show_status
fi

COUNTER=0
LOCATIONCOUNT=${#LOCATIONS[*]}
while [ $COUNTER -lt $LOCATIONCOUNT ]
do
LOCATION=`echo ${LOCATIONS[$COUNTER]}`
if [ `grep -c "$LOCATION" /var/lib/samba/netlogon/locations.txt` = 0 ]
then
MESSAGE=$"No Printers are available."
show_status
fi
let COUNTER=$COUNTER+1
done

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers_assign.cgi | cut -d' ' -f1`
#Assign printers
sudo -H /opt/karoshi/web_controls/exec/printers_assign $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$PRINTER:`echo ${LOCATIONS[@]:0} | sed 's/ /:/g'`
echo "</div></body></html>"
exit
