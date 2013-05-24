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
#  _GROUPNAME_ The name of the mon monitor group to add
#  _TCPIP_  IP numbers of the devices in the group to check
#   _INTERVAL_  The time interval between each check.
#  _DESCRIPTION_
#  _MONITORTYPES_ The type of monitors to use to check the services.
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_add ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_add
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="0; URL=monitors_view.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\+-'`
#########################
#Assign data to variables
#########################
END_POINT=38
#Assign GROUPNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = GROUPNAMEcheck ]
then
let COUNTER=$COUNTER+1
GROUPNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign TCPIP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPIPcheck ]
then
let COUNTER=$COUNTER+1
TCPIP=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign INTERVAL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = INTERVALcheck ]
then
let COUNTER=$COUNTER+1
INTERVAL=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign DAYSTART
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DAYSTARTcheck ]
then
let COUNTER=$COUNTER+1
DAYSTART=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign DAYEND
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DAYENDcheck ]
then
let COUNTER=$COUNTER+1
DAYEND=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign HOURSTART
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = HOURSTARTcheck ]
then
let COUNTER=$COUNTER+1
HOURSTART=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign HOUREND
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = HOURENDcheck ]
then
let COUNTER=$COUNTER+1
HOUREND=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign MONITORTYPES
COUNTER=2
ARRAY_COUNT=0
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MONITORTYPEScheck ]
then
let COUNTER=$COUNTER+1
MONITORTYPES[$ARRAY_COUNT]=`echo $DATA | cut -s -d'_' -f$COUNTER`
let ARRAY_COUNT=$ARRAY_COUNT+1
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
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
#Check to see that GROUPNAME is not blank
if [ $GROUPNAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

if [ $TCPIP'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that MONITORTYPES is not blank
if [ $MONITORTYPES'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Check to see that monitor interval is correct if not blank

if [ $HOURSTART'null' != null ] || [ $HOUREND'null' != null ]
then
#Check that all times are not blank
if [ $HOURSTART'null' = null ] || [ $HOUREND'null' = null ]
then
MESSAGE=$ERRORMSG8
show_status
fi
fi
#Convert INTERVAL to numbers
[ $INTERVAL'null' = null ] && INTERVAL=5
INTERVAL=`echo $INTERVAL | tr -cd '0-9\._:\n-'`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/monitors_add.cgi | cut -d' ' -f1`
#Add monitor
sudo -H /opt/karoshi/web_controls/exec/monitors_add $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$GROUPNAME:$TCPIP:$INTERVAL:$DAYSTART:$DAYEND:$HOURSTART:$HOUREND:`echo ${MONITORTYPES[@]:0} | sed 's/ /:/g'`
EXEC_STATUS=`echo $?`
GROUPNAME=`echo $GROUPNAME | sed 's/+/ /g'`
MESSAGE=`echo $GROUPNAME: $COMPLETEDMSG`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=$ERRORMSG4
fi
if [ $EXEC_STATUS = 102 ]
then
MESSAGE=$ERRORMSG5
fi
if [ $EXEC_STATUS = 103 ]
then
MESSAGE=$ERRORMSG6
fi
show_status
exit
