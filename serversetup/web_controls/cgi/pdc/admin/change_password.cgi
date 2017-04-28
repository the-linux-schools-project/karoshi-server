#!/bin/bash
#Change a user's password
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
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.

########################
#Language
########################

STYLESHEET=defaultstyle.css
[ -f "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER" ] && source "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Change a User Password"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g')
#########################
#Assign data to variables
#########################
END_POINT=12
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

#Assign PASSWORD1
DATANAME=PASSWORD1
get_data
PASSWORD1="$DATAENTRY"

#Assign PASSWORD2
DATANAME=PASSWORD2
get_data
PASSWORD2="$DATAENTRY"

#Assign NEXTLOGON
DATANAME=NEXTLOGON
get_data
NEXTLOGON="$DATAENTRY"

#Assign VIEWIMAGE
DATANAME=VIEWIMAGE
get_data
VIEWIMAGE="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">
alert("'"$MESSAGE"'");
window.location = "/cgi-bin/admin/change_password_fm.cgi"
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
MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/change_password.cgi | cut -d' ' -f1)
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
USEREXISTSTATUS="$?"
if [ "$USEREXISTSTATUS" != 0 ]
then
	MESSAGE=$"This username does not exist."
	show_status
fi

#Dont change passwords for certain users
if [ "$USERNAME" = karoshi ] || [ "$USERNAME" = root ]
then
	MESSAGE=$"You can not change the password for this user."
	show_status
fi

#Check view image tick box
if [ "$VIEWIMAGE" = yes ]
then
echo '<body onload="submitForm()"><div id="pagecontainer"><form action="/cgi-bin/admin/change_password_fm.cgi" method="post" name="form">'
echo '<input name="_USERNAME_" value="'"$USERNAME"'" type="hidden">'
echo '<input name="_PASSWORD1_" value="'"$PASSWORD1"'" type="hidden">'
echo '<input name="_PASSWORD2_" value="'"$PASSWORD2"'" type="hidden"></form>'

echo '<SCRIPT LANGUAGE="JavaScript">
function submitForm(){
document.form.submit();
}
</SCRIPT></div></body></html>'
exit
fi

#Check to see that the user is not in acceptable use category
if [ -f "/opt/karoshi/server_network/acceptable_use_authorisations/pending/$USERNAME" ]
then
	#Check to see how many days of trial are left
	GRACE_TIME=$(sed -n 1,1p /opt/karoshi/server_network/acceptable_use_authorisations/pending/"$USERNAME" | cut -d, -f1 | tr -cd 0-9)
	[ -z "$GRACE_TIME" ] && GRACE_TIME=0
	if [ "$GRACE_TIME" = 0 ]
	then
		MESSAGE=''"$USERNAME"' - '$"This user has not signed an acceptable use policy and their account has now been suspended."''
		show_status
	fi
fi

#Check password settings
source /opt/karoshi/server_network/security/password_settings

SHOW_PASSWORD=no

#Create a random password if password1 has not been set to the minium password length set in default user settings
if [ -z "$PASSWORD1" ]
then
	if [ "$PASSWORDCOMPLEXITY" = on ]
	then
		PASSWORD1=$(openssl rand -base64 24 | head -c"$MINPASSWORDLENGTH" 2>/dev/null)
	else
		PASSWORD1=$(shuf -i 10000000000000-99999999999999 -n 1 | head -c"$MINPASSWORDLENGTH")
	fi
	SHOW_PASSWORD=yes
fi

if [ "$SHOW_PASSWORD" = no ]
then
	#Check to see that password fields match if they are not blank
	if [ -z "$PASSWORD2" ]
	then
		MESSAGE=$"You have not confirmed the password."
		show_status
	fi
	#Check that password has been entered correctly
	if [ "$PASSWORD1" != "$PASSWORD2" ]
	then
		MESSAGE=$"The passwords do not match."
		show_status
	fi
fi

#Convert special characters back for new password to check password strength
NEW_PASSWORD=$(echo "$PASSWORD1" | sed 's/+/ /g; s/%21/!/g; s/%3F/?/g; s/%2C/,/g; s/%3A/:/g; s/%7E/~/g; s/%40/@/g; s/%23/#/g; s/%24/$/g; s/%26/\&/g; s/%2B/+/g; s/%3D/=/g; s/%28/(/g; s/%29/)/g; s/%5E/^/g; s/%7B/{/g; s/%7D/}/g; s/%3C/</g; s/%3E/>/g; s/%5B/[/g; s/%5D/]/g; s/%7C/|/g; s/%22/"/g; s/%1123/*/g' | sed "s/%27/'/g" | sed 's/%3B/;/g' | sed 's/%60/\`/g' | sed 's/%5C/\\/g' | sed 's/%2F/\//g' | sed 's/%25/%/g')

PASSLENGTH=${#NEW_PASSWORD}

#Check to see that password has the required number of characters
if [ "$PASSLENGTH" -lt "$MINPASSLENGTH" ]
then
	MESSAGE=''$"Your password length"': '$PASSLENGTH'\n'$"Required password length"': '$MINPASSLENGTH''
	show_status
fi


if [ "$PASSWORDCOMPLEXITY" = on ]
then
	CASECHECK=ok
	CHARCHECK=ok

	#Check that the password has a combination of characters and numbers
	if [[ $(echo "$PASSWORD1"'1' | tr -cd '0-9\n') = 1 ]]
	then
		CHARCHECK=fail
	fi
	if [[ $(echo "$PASSWORD1"'A' | tr -cd 'A-Za-z\n') = A ]]
	then
		CHARCHECK=fail
	fi

	if [[ $(echo "$PASSWORD1"'A' | tr -cd 'A-Z\n') = A ]]
	then
		CASECHECK=fail
	fi
	if [[ $(echo "$PASSWORD1"'a' | tr -cd 'a-z\n') = a ]]
	then
		CASECHECK=fail
	fi

	if [ "$CASECHECK" = fail ] || [ "$CHARCHECK" = fail ]
	then
		MESSAGE=$"A combination of upper and lower case characters and numbers is required."
		show_status
	fi
fi

#Change password
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$PASSWORD1:$NEXTLOGON:" | sudo -H /opt/karoshi/web_controls/exec/change_password
EXEC_STATUS="$?"
if [ "$EXEC_STATUS" = 0 ]
then

	#Reset user lockout just in case
	MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/lockout_reset.cgi | cut -d' ' -f1)
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:" | sudo -H /opt/karoshi/web_controls/exec/lockout_reset

	MESSAGE=''$"Password changed for"' '"$USERNAME"'.'
	if [ "$SHOW_PASSWORD" = yes ]
	then
		MESSAGE=''"$MESSAGE"'\n\n'$"Password"': '"$PASSWORD1"''
	fi
else
	MESSAGE=''$"The password was not changed for"' '"$USERNAME".''
fi
if [ "$EXEC_STATUS" = 102 ]
then
	MESSAGE=''"$USERNAME"' - '$"This user account has been suspended."''
fi
show_status
exit
