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
#jsharrad@karoshi.org.uk

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

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Change a Username"'</title><meta http-equiv="REFRESH" content="0; URL=change_username_fm.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\--'`
#########################
#Assign data to variables
#########################
END_POINT=11
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
#Assign FIRSTNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = FIRSTNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		FIRSTNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign SURNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SURNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		SURNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Check to see that username is not blank
if [ -z "$USERNAME" ]
then
	MESSAGE=$"The username must not be blank."
	show_status
fi
#Check to see if the user exists
getent passwd $USERNAME 1>/dev/null
if [ $? != 0 ]
then
	MESSAGE=$"The username does not exist."
	show_status
fi
#Check to see that newusername is not blank
if [ -z "$NEWUSERNAME"  ]
then
	MESSAGE=$"The new username must not be blank."
	show_status
fi
#Check to see if the newusername exists
getent passwd $NEWUSERNAME 1>/dev/null
if [ $? = 0 ]
then
	MESSAGE=$"The new username is already in use."
	show_status
fi
#Check to see that firstname is not blank
if [ -z $FIRSTNAME ]
then
	MESSAGE=$"You have not entered in a forename."
	show_status
fi
#Check to see that surname is not blank
if [ -z "$SURNAME" ]
then
	MESSAGE=$"You have not entered in a surname."
	show_status
fi

#Don't change username for certain users
if [ $USERNAME = root ] || [ $USERNAME = karoshi ]
then
	MESSAGE=$"You cannot change that username."
	show_status
fi

#Check that the user is not a system user
USER_ID=`id -g $USERNAME`

if [ $USER_ID -lt 500 ]
then
	MESSAGE=$"You cannot change the name of a system user."
	show_status
	exit
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/change_username.cgi | cut -d' ' -f1`
#Change username
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$NEWUSERNAME:$FIRSTNAME:$SURNAME:" | sudo -H /opt/karoshi/web_controls/exec/change_username
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 0 ]
then
	MESSAGE=`echo $"Username changed": $USERNAME - $NEWUSERNAME`
else
	MESSAGE=`echo $"There was a problem changing the username." $USERNAME`
fi
show_status
