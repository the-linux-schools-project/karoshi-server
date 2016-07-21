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
#  _GROUPNAME_ The name of the mon monitor group to add
#  _TCPIP_  IP numbers of the devices in the group to check
#   _INTERVAL_  The time interval between each check.
#  _DESCRIPTION_
#  _MONITORTYPES_ The type of monitors to use to check the services.
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Add Monitors"'</title><meta http-equiv="REFRESH" content="0; URL=monitors_view.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\+-'`
#########################
#Assign data to variables
#########################
END_POINT=40
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

#Assign ALERTAFTER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ALERTAFTERcheck ]
then
let COUNTER=$COUNTER+1
ALERTAFTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Check to see that GROUPNAME is not blank
if [ $GROUPNAME'null' = null ]
then
MESSAGE=$"The group name must not be blank."
show_status
fi

if [ $TCPIP'null' = null ]
then
MESSAGE=$"The TCPIP numbers cannot be blank."
show_status
fi
#Check to see that MONITORTYPES is not blank
if [ $MONITORTYPES'null' = null ]
then
MESSAGE=$"The monitor type cannot be blank."
show_status
fi

#Check to see that monitor interval is correct if not blank

if [ $HOURSTART'null' != null ] || [ $HOUREND'null' != null ]
then
#Check that all times are not blank
if [ $HOURSTART'null' = null ] || [ $HOUREND'null' = null ]
then
MESSAGE=$"You must fill in all of the time interval boxes if you do not want continuous monitoring."
show_status
fi
fi
#Convert INTERVAL to numbers
[ $INTERVAL'null' = null ] && INTERVAL=5
INTERVAL=`echo $INTERVAL | tr -cd '0-9\._:\n-'`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/monitors_add.cgi | cut -d' ' -f1`
#Add monitor
sudo -H /opt/karoshi/web_controls/exec/monitors_add $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$GROUPNAME:$TCPIP:$ALERTAFTER:$INTERVAL:$DAYSTART:$DAYEND:$HOURSTART:$HOUREND:`echo ${MONITORTYPES[@]:0} | sed 's/ /:/g'`
EXEC_STATUS=`echo $?`
GROUPNAME=`echo $GROUPNAME | sed 's/+/ /g'`
MESSAGE=`echo $GROUPNAME: $"Monitor added."`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=$"There was a problem adding this monitor. Please check the Karoshi Web administration Logs."
fi
if [ $EXEC_STATUS = 102 ]
then
MESSAGE=$"A monitor group already exists with this name."
fi
if [ $EXEC_STATUS = 103 ]
then
MESSAGE=$"A monitoring server has not been added to the network."
fi
show_status
exit
