#!/bin/bash
#Copyright (C) 2007 Paul Sharrad
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_view_banned_users ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_view_banned_users
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"<link rel="stylesheet" href="/css/$STYLESHEET"></head><body>'
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

