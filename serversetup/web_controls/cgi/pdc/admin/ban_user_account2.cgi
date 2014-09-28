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
#  _HOUR_
#  _MINUTES_
#  _DAY_
#  _MONTH_
#  _YEAR_
#  _STUDENTS_
#  _INCIDENT_
#  _ACTIONTAKEN_
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Ban User Account"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%/+-'`
#########################
#Assign data to variables
#########################
END_POINT=18
#Assign HOUR
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = HOURcheck ]
then
let COUNTER=$COUNTER+1
HOUR=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign MINUTES
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MINUTEScheck ]
then
let COUNTER=$COUNTER+1
MINUTES=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign DAY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DAYcheck ]
then
let COUNTER=$COUNTER+1
DAY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign MONTH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MONTHcheck ]
then
let COUNTER=$COUNTER+1
MONTH=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign YEAR
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = YEARcheck ]
then
let COUNTER=$COUNTER+1
YEAR=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign INCIDENT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = INCIDENTcheck ]
then
let COUNTER=$COUNTER+1
INCIDENT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign ACTIONTAKEN
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ACTIONTAKENcheck ]
then
let COUNTER=$COUNTER+1
ACTIONTAKEN=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign STUDENTS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = STUDENTScheck ]
then
let COUNTER=$COUNTER+1
STUDENTS=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign BANLENGTH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = BANLENGTHcheck ]
then
let COUNTER=$COUNTER+1
BANLENGTH=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/ban_user_account.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

function input_error {
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">'
echo '<b>'$MESSAGE'</b><br>'
echo '<form action="/cgi-bin/admin/ban_user_account.cgi" method="post">'
echo '<input type="hidden" id="_DAY_" name="_DAY_" value="'$DAY'" />'
echo '<input type="hidden" id="_MONTH_" name="_MONTH_" value="'$MONTH'" />'
echo '<input type="hidden" id="_YEAR_" name="_YEAR_" value="'$YEAR'" />'
echo '<input type="hidden" id="_HOUR_" name="_HOUR_" value="'$HOUR'" />'
echo '<input type="hidden" id="_MINUTES_" name="_MINUTES_" value="'$MINUTES'" />'
echo '<input type="hidden" id="_STUDENTS_" name="_STUDENTS_" value="'$STUDENTS'" />'
echo '<input type="hidden" id="_INCIDENT_" name="_INCIDENT_" value="'$INCIDENT'" />'
echo '<input type="hidden" id="_ACTIONTAKEN_" name="_ACTIONTAKEN_" value="'$"User account banned."'" />'
echo '<input type="hidden" id="_BANLENGTH_" name="_BANLENGTH_" value="'$BANLENGTH'" />'
echo '</div><div id="submitbox"> <input value='$Back' type="submit"></div></form></div></body></html>'
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
#Check to see that HOUR is not blank
if [ $HOUR'null' = null ]
then
MESSAGE=$"The time must not be blank."
input_error
fi
#Check to see that MINUTES is not blank
if [ $MINUTES'null' = null ]
then
MESSAGE=$"The time must not be blank."
input_error
fi
#Check to see that DAY is not blank
if [ $DAY'null' = null ]
then
MESSAGE=$"The date must not be blank."
input_error
fi
#Check to see that MONTH is not blank
if [ $MONTH'null' = null ]
then
MESSAGE=$"The date must not be blank."
input_error
fi
#Check to see that YEAR is not blank
if [ $YEAR'null' = null ]
then
MESSAGE=$"The date must not be blank."
input_error
fi
#Check to see that INCIDENT is not blank
if [ $INCIDENT'null' = null ]
then
MESSAGE=$"The incident must not be blank."
input_error
fi
#Check to see that ACTIONTAKEN is not blank
if [ $"User account banned."'null' = null ]
then
MESSAGE=$"The action taken must not be blank."
input_error
fi
#Check to see that STUDENTS is not blank
if [ $STUDENTS'null' = null ]
then
MESSAGE=$"You have not entered any students."
input_error
fi
#Check that HOUR has two digits
if [ `echo ${#HOUR}` != 2 ]
then
MESSAGE=$"The hour must have two digits."
HOUR="??"
input_error
fi
#Check that MINUTES has two digits
if [ `echo ${#MINUTES}` != 2 ]
then
MESSAGE=$"The minutes must have two digits."
MINUTES=""
input_error
fi
#Check that day has two digits
if [ `echo ${#DAY}` != 2 ]
then
MESSAGE=$"The day must have two digits."
DAY="??"
input_error
fi

#Check that month has two digits
if [ `echo ${#MONTH}` != 2 ]
then
MESSAGE=$"The month must have two digits."
MONTH="??"
input_error
fi
#Check that year has four digits
if [ `echo ${#YEAR}` != 4 ]
then
MESSAGE=$"The year must have four digits."
YEAR="????"
input_error
fi
#Check that ban length is a number
if [ $BANLENGTH'null' != null ]
then
BANLENGTH=`echo $BANLENGTH | tr -cd '0-9\n'`
if [ $BANLENGTH'null' = null ]
then
MESSAGE=$"The duration of the user ban must be a number."
BANLENGTH="??"
input_error
fi
#Check that ban length does not start with zero
if [ `echo ${BANLENGTH:0:1}` = 0 ]
then
BANLENGTH=`echo ${BANLENGTH:1}`
fi
fi

#Check that date and time does not have question marks in it!
if [ `echo $DAY$MONTH$YEAR$HOUR$MINUTES | grep -c ?` != 0 ]
then
MESSAGE=$"Please correct the date error."
input_error
fi
#Check that student usernames exist
STUDENT_ARRAY=( `echo $STUDENTS | sed 's/+/ /g'` )
STUDENT_ARRAY_COUNT=`echo ${#STUDENT_ARRAY[@]}`
COUNTER=0
while [ $COUNTER -lt $STUDENT_ARRAY_COUNT ]
do
STUDENT_USERNAME=`echo ${STUDENT_ARRAY[$COUNTER]}`
[ $STUDENT_USERNAME'null' = null ] && STUDENT_USERNAME=not_set
#Check to see that the user exists
echo "$MD5SUM:$STUDENT_USERNAME" | sudo -H /opt/karoshi/web_controls/exec/existcheck_user
USEREXISTSTATUS=`echo $?`
if [ $USEREXISTSTATUS = 111 ]
then
MESSAGE=$"This user does not exist."
show_status
fi
let COUNTER=$COUNTER+1
done
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/ban_user_account2.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$DAY:$MONTH:$YEAR:$HOUR:$MINUTES:$INCIDENT:$"User account banned.":$STUDENTS:$BANLENGTH" | sudo -H /opt/karoshi/web_controls/exec/ban_user_account
MESSAGE=$"Ban User account completed."
show_status
