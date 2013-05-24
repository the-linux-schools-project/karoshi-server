#!/bin/bash
#Copyright (C) 2010  Paul Sharrad
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

##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/helpdesk ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/helpdesk
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo "<html><head><title>$TITLE</title>"
echo '<link rel="stylesheet" href="/css/'$STYLESHEET'"><meta http-equiv="REFRESH" content="0;url=helpdesk_view_fm.cgi"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\.%+_:\-'`
#########################
#Assign data to variables
#########################
END_POINT=11
#Assign FEEDBACK
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = FEEDBACKcheck ]
then
let COUNTER=$COUNTER+1
FEEDBACK=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PRIORITY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRIORITYcheck ]
then
let COUNTER=$COUNTER+1
PRIORITY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign ASSIGNED
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ASSIGNEDcheck ]
then
let COUNTER=$COUNTER+1
ASSIGNED=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign JOBNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = JOBNAMEcheck ]
then
let COUNTER=$COUNTER+1
JOBNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
then
let COUNTER=$COUNTER+1
ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/helpdesk_view_fm.cgi";'
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
#Check data
#########################
#Check that ACTION is not blank
if [ $ACTION'null' = null ]
then
MESSAGE=$ERRORMSG12
show_status
fi

if [ $ACTION = update ]
then
#Check to see that ASSIGNED is not blank
if [ $ASSIGNED'null' = null ]
then
MESSAGE=$ERRORMSG11
show_status
fi
#Check to see that PRIORITY is not blank
if [ $PRIORITY'null' = null ]
then
MESSAGE=$ERRORMSG10
show_status
fi

#Check that JOBNAME is not blank
if [ $JOBNAME'null' = null ]
then
MESSAGE=$ERRORMSG8
show_status
fi

#Convert special characters
ASSIGNED=`echo $ASSIGNED | sed 's/%0D%0A/ /g' | sed 's/+/ /g' | sed 's/%27//g'  | sed 's/%22//g'`
PRIORITY=`echo $PRIORITY | sed 's/%0D%0A/ /g' | sed 's/+/ /g' | sed 's/%27//g'  | sed 's/%22//g' | sed 's/%24/$/g'`
FEEDBACK=`echo $FEEDBACK | sed 's/%0D%0A/ /g' | sed 's/+/ /g' | sed 's/%27//g'  | sed 's/%22//g' | sed 's/%3F/?/g' | sed 's/%2C/,/g' | sed 's/%21/!/g'`
fi
[ ! -d /opt/karoshi/helpdesk/log ] && mkdir -p /opt/karoshi/helpdesk/log
LOG_DATE=`date +%F`

if [ $ACTION = update ]
then
echo `date`: Helpdesk - $JOBNAME updated by $REMOTE_USER from $REMOTE_ADDR >> /opt/karoshi/helpdesk/log/$LOG_DATE
#Update request
#Assigned
sed -i 9c\ASSIGNED="$ASSIGNED" /opt/karoshi/helpdesk/todo/$JOBNAME
#Priority
sed -i 10c\PRIORITY='"'"$PRIORITY"'"' /opt/karoshi/helpdesk/todo/$JOBNAME
#Feedback
sed -i 11c\FEEDBACK='"'"$FEEDBACK"'"' /opt/karoshi/helpdesk/todo/$JOBNAME
fi

if [ $ACTION = delete ]
then
echo `date`: Helpdesk - deleting $JOBNAME by $REMOTE_USER from $REMOTE_ADDR >> /opt/karoshi/helpdesk/log/$LOG_DATE
[ ! -d /opt/karoshi/helpdesk/deleted ] && mkdir -p /opt/karoshi/helpdesk/deleted
[ -f /opt/karoshi/helpdesk/todo/$JOBNAME ] && mv /opt/karoshi/helpdesk/todo/$JOBNAME /opt/karoshi/helpdesk/deleted/

fi

if [ $ACTION = completed ]
then
echo `date`: Helpdesk - $JOBNAME marked as complete by $REMOTE_USER from $REMOTE_ADDR >> /opt/karoshi/helpdesk/log/$LOG_DATE
[ ! -d /opt/karoshi/helpdesk/completed ] && mkdir -p /opt/karoshi/helpdesk/completed
[ -f /opt/karoshi/helpdesk/todo/$JOBNAME ] && mv /opt/karoshi/helpdesk/todo/$JOBNAME /opt/karoshi/helpdesk/completed/
#Add in completion dates
sed -i 12c\COMPLETEDDATE='"'`date +%d-%m-%y`'"' /opt/karoshi/helpdesk/completed/$JOBNAME
sed -i 13c\COMPLETEDDATE2='"'`date +%s`'"' /opt/karoshi/helpdesk/completed/$JOBNAME
fi

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:no:" | sudo -H /opt/karoshi/web_controls/exec/helpdesk_warning_message

exit



