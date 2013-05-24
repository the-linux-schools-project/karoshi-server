#!/bin/bash
#Change a user name
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
#  _USERNAME_
#  _NEWUSERNAME_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/change_username ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/change_username
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="0; URL=change_username_fm.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\--'`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign USERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
then
let COUNTER=$COUNTER+1
USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign NEWUSERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = NEWUSERNAMEcheck ]
then
let COUNTER=$COUNTER+1
NEWUSERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
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
#Check to see that username is not blank
if [ $USERNAME'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see if the user exists
echo "$MD5SUM:$USERNAME" | sudo -H /opt/karoshi/web_controls/exec/existcheck_user
USEREXISTSTATUS=`echo $?`
if [ $USEREXISTSTATUS != 112 ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that newusername is not blank
if [ $NEWUSERNAME'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
#Check to see if the newusername exists
echo "$MD5SUM:$NEWUSERNAME" | sudo -H /opt/karoshi/web_controls/exec/existcheck_user
USEREXISTSTATUS=`echo $?`
if [ $USEREXISTSTATUS = 112 ]
then
MESSAGE=`echo $NEWUSERNAME $ERRORMSG4`
show_status
fi
#Don't change username for certain users
if [ $USERNAME = root ] || [ $USERNAME = karoshi ]
then
MESSAGE=$ERRORMSG6
show_status
fi

#Check that the user is not a system user
USER_ID=`id -g $USERNAME`

if [ $USER_ID -lt 500 ]
then
MESSAGE=$ERRORMSG7
show_status
exit
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/change_username.cgi | cut -d' ' -f1`
#Change username
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$NEWUSERNAME" | sudo -H /opt/karoshi/web_controls/exec/change_username
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 0 ]
then
MESSAGE=`echo $COMPLETEDMSG: $USERNAME - $NEWUSERNAME`
else
MESSAGE=`echo $ERRORMSG5 $USERNAME`
fi
show_status
