#!/bin/bash
#delete_user
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
#  _USERNAME_
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Delete User"'</title><meta http-equiv="REFRESH" content="0; URL=delete_user_fm.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')

#########################
#Assign data to variables
#########################
END_POINT=9
function get_data {
COUNTER=2
DATAENTRY=""
while [[ $COUNTER -le $END_POINT ]]
do
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [[ "$DATAHEADER" = "$DATANAME" ]]
	then
		let COUNTER="$COUNTER"+1
		DATAENTRY=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
		break
	fi
	let COUNTER=$COUNTER+1
done
}

#Assign USERNAME
DATANAME=USERNAME
get_data
USERNAME="$DATAENTRY"



#Assign SHUTDOWNCODE
DATANAME=SHUTDOWNCODE
get_data
SHUTDOWNCODE="$DATAENTRY"

#Assign FORMCODE
DATANAME=FORMCODE
get_data
FORMCODE="$DATAENTRY"


#Assign VIEWIMAGE
DATANAME=VIEWIMAGE
get_data
VIEWIMAGE="$DATAENTRY"

#Assign REQUESTFILE
DATANAME=REQUESTFILE
get_data
REQUESTFILE="$DATAENTRY"

#Assign ARCHIVE
DATANAME=ARCHIVE
get_data
ARCHIVE="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">
alert("'"$MESSAGE"'");
</script>
</div></body></html>'
exit
}
#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [[ $(grep -c ^"$REMOTE_USER": /opt/karoshi/web_controls/web_access_admin) != 1 ]]
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
#Check to see that the user exists
getent passwd "$USERNAME" 1>/dev/null 2>/dev/null
if [ "$?" != 0 ]
then
	MESSAGE=$"This user does not exist."
	show_status
fi

#Check view image tick box
if [ "$VIEWIMAGE"'check' = yescheck ]
then
	echo '<body onload="submitForm()"><div id="pagecontainer"><form action="/cgi-bin/admin/delete_user_fm.cgi" method="post" name="form">'
	echo '<input name="_USERNAME_" value="'"$USERNAME"'" type="hidden">'
	echo '<input name="_DOMAINPASSWORD_" value="'"$DOMAINPASSWORD"'" type="hidden"></form>'

	echo '<SCRIPT LANGUAGE="JavaScript">
function submitForm(){
document.form.submit();
}
</SCRIPT></div></body></html>'
exit
fi

#Check to see that SHUTDOWNCODE is not blank
if [ -z "$SHUTDOWNCODE" ]
then
	MESSAGE=$"The delete code must not be blank."
	show_status
fi
#Check to see that FORMCODE is not blank
if [ -z "$FORMCODE" ]
then
	MESSAGE=$"The form code must not be blank."
	show_status
fi
#Make sure that FORMCODE and SHUTDOWNCODE matches
if [ "$FORMCODE" != "$SHUTDOWNCODE" ]
then
	MESSAGE=$"Incorrect delete code."
	show_status
fi
PRIMARYGROUP=$(id -G -n "$USERNAME" | cut -d' ' -f1)
Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/delete_user.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$USERNAME:$REQUESTFILE:$ARCHIVE:" | sudo -H /opt/karoshi/web_controls/exec/delete_user
EXEC_STATUS="$?"
if [ "$EXEC_STATUS" = 105 ]
then
	MESSAGE=''$"A server required for this action was offline."' '$"Please check the karoshi web administration logs for more details."''
	show_status
fi
if [ "$EXEC_STATUS" = 102 ]
then
	MESSAGE=$"Incorrect domain password."
	show_status
fi
if [ "$EXEC_STATUS" = 0 ]
then
	MESSAGE="$USERNAME: "$"This account has been deleted."
	[ "$ARCHIVE" = yes ] && MESSAGE="$MESSAGE\n\n"$"Archive path"" : /home/users/archive/$PRIMARYGROUP/$USERNAME"
else
	MESSAGE="$USERNAME: "$"The user was not deleted."
fi
show_status

