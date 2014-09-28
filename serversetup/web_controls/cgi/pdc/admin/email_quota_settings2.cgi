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

#  _ADMINEMAIL_
#  _SPOOLDIR_
#  _THRESHOLD1_
#  _THRESHOLD2_
#  _THRESHOLD3_
#  _THRESHOLD4_
#  _INTERVAL1_
#  _INTERVAL2_
#  _INTERVAL3_
#  _INTERVAL4_
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"E-Mail Quota Warning Settings"'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\%-'`
#########################
#Assign data to variables
#########################
END_POINT=20

#Assign ADMIN_EMAIL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ADMINEMAILcheck ]
then
let COUNTER=$COUNTER+1
ADMINEMAIL=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign THRESHOLD1
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = THRESHOLD1check ]
then
let COUNTER=$COUNTER+1
THRESHOLD1=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign THRESHOLD2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = THRESHOLD2check ]
then
let COUNTER=$COUNTER+1
THRESHOLD2=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign THRESHOLD3
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = THRESHOLD3check ]
then
let COUNTER=$COUNTER+1
THRESHOLD3=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign THRESHOLD4
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = THRESHOLD4check ]
then
let COUNTER=$COUNTER+1
THRESHOLD4=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign INTERVAL1
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = INTERVAL1check ]
then
let COUNTER=$COUNTER+1
INTERVAL1=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign INTERVAL2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = INTERVAL2check ]
then
let COUNTER=$COUNTER+1
INTERVAL2=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign INTERVAL3
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = INTERVAL3check ]
then
let COUNTER=$COUNTER+1
INTERVAL3=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign INTERVAL4
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = INTERVAL4check ]
then
let COUNTER=$COUNTER+1
INTERVAL4=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\n'`
break
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
#Check to see that ADMINEMAIL is not blank
if [ $ADMINEMAIL'null' = null ]
then
MESSAGE=$"The administrator account must not be blank."
show_status
fi
#Check to see that THRESHOLD1 is not blank
if [ $THRESHOLD1'null' = null ]
then
MESSAGE=$"Incorrect data entry for Level 1."
show_status
fi
#Check to see that THRESHOLD2 is not blank
if [ $THRESHOLD2'null' = null ]
then
MESSAGE=$"Incorrect data entry for Level 2."
show_status
fi
#Check to see that THRESHOLD3 is not blank
if [ $THRESHOLD3'null' = null ]
then
MESSAGE=$"Incorrect data entry for Level 3."
show_status
fi
#Check to see that THRESHOLD4 is not blank
if [ $THRESHOLD4'null' = null ]
then
MESSAGE=$"Incorrect data entry for Level 4."
show_status
fi
#Check to see that INTERVAL1 is not blank
if [ $INTERVAL1'null' = null ]
then
MESSAGE=$"Incorrect data entry for Interval 1."
show_status
fi
#Check to see that INTERVAL2 is not blank
if [ $INTERVAL2'null' = null ]
then
MESSAGE=$"Incorrect data entry for Interval 2."
show_status
fi
#Check to see that INTERVAL3 is not blank
if [ $INTERVAL3'null' = null ]
then
MESSAGE=$"Incorrect data entry for Interval 3."
show_status
fi
#Check to see that INTERVAL4 is not blank
if [ $INTERVAL4'null' = null ]
then
MESSAGE=$"Incorrect data entry for Interval 4."
show_status
fi

#Check to see that THRESHOLDs are in the correct order
if [ $THRESHOLD1 -gt $THRESHOLD2 ] || [ $THRESHOLD2 -gt $THRESHOLD3 ] || [ $THRESHOLD3 -gt $THRESHOLD4 ]
then
MESSAGE=$"The Levels must be in the correct order."
show_status
fi

#Check that the intervals are in the correct order
if [ $INTERVAL1 -lt $INTERVAL2 ] || [ $INTERVAL2 -lt $INTERVAL3 ] || [ $INTERVAL3 -lt $INTERVAL4 ]
then
MESSAGE=$"The warning intervals must be in the correct order."
show_status
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/email_quota_settings2.cgi | cut -d' ' -f1`
#Create config file
sudo -H /opt/karoshi/web_controls/exec/email_quota_settings_apply $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ADMINEMAIL:$THRESHOLD1:$THRESHOLD2:$THRESHOLD3:$THRESHOLD4:$INTERVAL1:$INTERVAL2:$INTERVAL3:$INTERVAL4
MESSAGE=$"E-mail quota warning settings have been applied."
show_status
exit
