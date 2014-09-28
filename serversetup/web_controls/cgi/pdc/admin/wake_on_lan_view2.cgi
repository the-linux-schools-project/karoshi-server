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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Banned Users"'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"<link rel="stylesheet" href="/css/$STYLESHEET"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA_ARRAY=( `echo $DATA | sed 's/_ENABLE_/_ENABLE_ /g' | sed 's/_DISABLE_/_DISABLE_ /g' | sed 's/_REMOVE_/_REMOVE_ /g'` )
END_POINT=`echo ${#DATA_ARRAY[@]}`
let END_POINT=$END_POINT*2
#Assign ENABLEARRAY
COUNTER=2
ARRAY_COUNT=0
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ENABLEcheck ]
then
let COUNTER=$COUNTER+1
ENABLEARRAY[$ARRAY_COUNT]=`echo $DATA | cut -s -d'_' -f$COUNTER`
let ARRAY_COUNT=$ARRAY_COUNT+1
fi
let COUNTER=$COUNTER+1
done

#Assign DISABLEARRAY
COUNTER=2
ARRAY_COUNT=0
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DISABLEcheck ]
then
let COUNTER=$COUNTER+1
DISABLEARRAY[$ARRAY_COUNT]=`echo $DATA | cut -s -d'_' -f$COUNTER`
let ARRAY_COUNT=$ARRAY_COUNT+1
fi
let COUNTER=$COUNTER+1
done

#Assign REMOVEARRAY
COUNTER=2
ARRAY_COUNT=0
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = REMOVEcheck ]
then
let COUNTER=$COUNTER+1
REMOVEARRAY[$ARRAY_COUNT]=`echo $DATA | cut -s -d'_' -f$COUNTER`
let ARRAY_COUNT=$ARRAY_COUNT+1
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/wake_on_lan_view.cgi";'
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

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/wake_on_lan_view2.cgi | cut -d' ' -f1`
if [ $ENABLEARRAY'null' != null ]
then
ACTION=enable
#ENABLE
sudo -H /opt/karoshi/web_controls/exec/wake_on_lan_view2 $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:`echo ${ENABLEARRAY[@]:0} | sed 's/ /:/g'`
fi

if [ $DISABLEARRAY'null' != null ]
then
#DISABLE
ACTION=disable
sudo -H /opt/karoshi/web_controls/exec/wake_on_lan_view2 $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:`echo ${DISABLEARRAY[@]:0} | sed 's/ /:/g'`
fi

if [ $REMOVEARRAY'null' != null ]
then
#REMOVE
ACTION=remove
sudo -H /opt/karoshi/web_controls/exec/wake_on_lan_view2 $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:`echo ${REMOVEARRAY[@]:0} | sed 's/ /:/g'`
fi
exit

