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
#  _NAME_
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Web Management Name"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+'`
#########################
#Assign data to variables
#########################
END_POINT=11
#Assign LONGNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = LONGNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		LONGNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign SHORTNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SHORTNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		SHORTNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
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



function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/remote_management_name_fm.cgi";'
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
#Check to see that longname is not blank
if [ -z "$LONGNAME" ]
then
	MESSAGE=$"The site name cannot be blank."
	show_status
fi
#Check to see that shortname is not blank
if [ -z "$SHORTNAME" ]
then
	MESSAGE=$"The short site name cannot be blank."
	show_status
fi
#Check to see that servername is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The servername cannot be blank."
	show_status
fi
#Check to see that servertype is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$"The servertype cannot be blank."
	show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/remote_management_name.cgi | cut -d' ' -f1`
#Add user
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SHORTNAME:$LONGNAME:$SERVERNAME:$SERVERTYPE" | sudo -H /opt/karoshi/web_controls/exec/remote_management_name
EXEC_STATUS="$?"
LONGNAME=$(echo $LONGNAME | sed 's/+/ /g')
MESSAGE=''$"The web management has been changed."'\n\n'$"Short Site Name"': '$SHORTNAME'\n\n'$"Site Name"': '$LONGNAME''
if [ $EXEC_STATUS = 101 ]
then
	MESSAGE=$"There was a problem with this action." $"Please check the karoshi web administration logs for more details."
fi
show_status
exit
