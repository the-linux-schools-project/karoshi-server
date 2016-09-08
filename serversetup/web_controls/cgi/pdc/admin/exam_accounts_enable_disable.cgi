#!/bin/bash
#enable_disable_exam_accounts.cgi
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
#  _EXAMSTATUS_  Radio button - needs either enable or disable
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Enable - Disable all exam accounts"'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+'`

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox"><b>'$"Enable - Disable all exam accounts"'</b><br><br></div><div id="infobox">'
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign EXAMSTATUS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = EXAMSTATUScheck ]
	then
		let COUNTER=$COUNTER+1
		EXAMSTATUS=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign EXCEPTIONLIST
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = EXCEPTIONLISTcheck ]
	then
		let COUNTER=$COUNTER+1
		EXCEPTIONLIST=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/exam_accounts_enable_disable_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
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

#Check to see that examstatus is either enable or disable
if [ $EXAMSTATUS'user' != enableuser ] && [ $EXAMSTATUS'user' != disableuser ]
then
	MESSAGE=$"Incorrect option."
	show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/exam_accounts_enable_disable.cgi | cut -d' ' -f1`
#Enable or disable all exam accounts
sudo -H /opt/karoshi/web_controls/exec/exam_accounts_enable_disable $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$EXAMSTATUS:$EXCEPTIONLIST:
EXEC_STATUS=$?
if [ $EXEC_STATUS = 0 ]
then
	if [ $EXAMSTATUS = enable ]
	then
		MESSAGE=`echo $"Exam accounts": $"enabled"`
	else
		MESSAGE=`echo $"Exam accounts": $"disabled"`
	fi
else
	MESSAGE=`echo $"Exam accounts": $"Status not changed."`
fi
show_status
exit
