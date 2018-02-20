#!/bin/bash
#Copyright (C) 2007  The karoshi Team

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
#  _USERACTION_

#Language
TITLE="View Karoshi Remote Management Users"
DELETEDMSG="This remote management user has been deleted."
ERRORMSG1="The user action must not be blank."
ERRORMSG2="You cannot delete yourself."
HTTPS_ERROR="You must access this page via https."
ACCESS_ERROR1="You must be a Karoshi Management User to complete this action."

LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign username
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = USERACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		USERACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/remote_management_view.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
function view_users {
echo '<SCRIPT language="Javascript">'
echo '                window.location = "/cgi-bin/admin/remote_management_view.cgi";'
echo '</script>'
echo "</div></body></html>"
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
#Check to see that USERACTION is not blank
if [ -z "$USERACTION" ]
then
	MESSAGE=$ERRORMSG1
	show_status
fi
Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/remote_management_process.cgi | cut -d' ' -f1`
if [ `echo $USERACTION | grep -c deleteuser` = 1 ]
then
	USERNAME=`echo $USERACTION | sed 's/deleteuser//g'`
	if [ $USERNAME != $REMOTE_USER ]
	then
		sudo -H /opt/karoshi/web_controls/exec/remote_management_delete $REMOTE_USER:$REMOTE_ADDR:$Checksum:$USERNAME
		EXITSTATUS=`echo $?`
		view_users
	else
		MESSAGE=$ERRORMSG2
		show_status
	fi
fi

if [ `echo $USERACTION | grep -c edituser` = 1 ]
then
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
	echo '<div id="actionbox">'
	echo '<form action="/cgi-bin/admin/remote_management_edit.cgi" method="post">'
	USERNAME=`echo $USERACTION | sed 's/edituser//g'`
	sudo -H /opt/karoshi/web_controls/exec/remote_management_edit2 $REMOTE_USER:$REMOTE_ADDR:$Checksum:$USERNAME
	echo "</div>"
	echo '<div id="submitbox"><input value="Submit" type="submit"> <input value="Reset" type="reset"></div>'
	echo "</div></body></html>"
fi
exit
