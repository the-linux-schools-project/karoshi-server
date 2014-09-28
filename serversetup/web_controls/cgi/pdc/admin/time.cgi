#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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
#  _FIRSTNAME_
#  _SURNAME_
# _USERNAMESTYLE_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
#  _GROUP_      This is the primary group for the new user eg yr2000, staff, officestaff.
##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Set Server Time"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
#########################
#Assign data to variables
#########################
END_POINT=24
#Assign DAY
DATA=`echo $DATA | sed 's/^timestamp//g' | sed 's/%3A/:/g'`
TIMESTAMP=`echo $DATA | cut -d_ -f1`

INPUTDATE=`echo $TIMESTAMP | cut -d'+' -f1`
INPUTTIME=`echo $TIMESTAMP | cut -d'+' -f2`

DAY=`echo $INPUTDATE | cut -d- -f1`
MONTH=`echo $INPUTDATE | cut -d- -f2`
YEAR=`echo $INPUTDATE | cut -d- -f3`

HOUR=`echo $INPUTTIME | cut -d: -f1`
MINUTES=`echo $INPUTTIME | cut -d: -f2`
SECS=`echo $INPUTTIME | cut -d: -f3`

#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
then
let COUNTER=$COUNTER+1
SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign SERVERTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERTYPEcheck ]
then
let COUNTER=$COUNTER+1
SERVERTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign SERVERMASTER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERMASTERcheck ]
then
let COUNTER=$COUNTER+1
SERVERMASTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo "<div id="actionbox">"'<div class="sectiontitle">'$"Set Server Time"'</div><br>'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/time_fm.cgi";'
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
#Check to see that hours is not blank
if [ $HOUR'null' = null ]
then
MESSAGE=$"You cannot leave the date or time blank."
show_status
fi
#Check to see that minutes is not blank
if [ $MINUTES'null' = null ]
then
MESSAGE=$"You cannot leave the date or time blank."
show_status
fi
#Check to see that SECS is not blank
if [ $SECS'null' = null ]
then
MESSAGE=$"You cannot leave the date or time blank."
show_status
fi
if [ $DAY'null' = null ]
then
MESSAGE=$"You cannot leave the date or time blank."
show_status
fi
if [ $MONTH'null' = null ]
then
MESSAGE=$"You cannot leave the date or time blank."
show_status
fi
if [ $YEAR'null' = null ]
then
MESSAGE=$"You cannot leave the date or time blank."
show_status
fi
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$"You must choose a server."
show_status
fi

#Check that the month is in range
if [ $MONTH -gt 12 ] || [ $MONTH -lt 1 ]
then
MESSAGE=$"You have not entered a correct month."
show_status
fi

#Check that the day is in range
if [ $DAY -gt 31 ] || [ $DAY -lt 1 ]
then
MESSAGE=$"You have not entered a correct day."
show_status
fi

#Check that the year is in range
if [ $YEAR -gt 2200 ] || [ $YEAR -lt 2009 ]
then
MESSAGE=$"You have not entered a correct year."
show_status
fi

#Check that the hour is in range
if [ $HOUR -gt 23 ] || [ $HOUR -lt 0 ]
then
MESSAGE=$"You have not entered a correct hour."
show_status
fi

#Check that the minutes is in range
if [ $MINUTES -gt 59 ] || [ $MINUTES -lt 0 ]
then
MESSAGE=$"You have not entered the correct minutes."
show_status
fi

#Check that the SECS is in range
if [ $SECS -gt 59 ] || [ $SECS -lt 0 ]
then
MESSAGE=$"You have not entered the correct seconds."
show_status
fi

#Extra day check
if [ $MONTH = 02 ] && [ $DAY -gt 28 ]
then
MESSAGE=$"You have not entered a correct day."
fi

if [ $MONTH = 04 ] && [ $DAY -gt 30 ]
then
MESSAGE=$"You have not entered a correct day."
fi

if [ $MONTH = 09 ] && [ $DAY -gt 30 ]
then
MESSAGE=$"You have not entered a correct day."
fi

if [ $MONTH = 11 ] && [ $DAY -gt 30 ]
then
MESSAGE=$"You have not entered a correct day."
fi

if [ `echo $MESSAGE'null' | sed 's/ //g'` != null ]
then
show_status
fi

#Check to see that SERVERNAME is not blank
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$"You cannot leave the date or time blank."
show_status
fi

#Check to see that SERVERTYPE is not blank
if [ $SERVERTYPE'null' = null ]
then
MESSAGE=$"You have not entered a correct day."
show_status
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/time.cgi | cut -d' ' -f1`
#set the time

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$DAY:$MONTH:$YEAR:$HOUR:$MINUTES:$SECS:$SERVERNAME:$SERVERTYPE:$SERVERMASTER" | sudo -H /opt/karoshi/web_controls/exec/time
exit
