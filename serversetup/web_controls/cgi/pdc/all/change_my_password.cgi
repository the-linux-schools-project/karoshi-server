#!/bin/bash
#Change my password
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
#  _PASSWORD1_  Current Password for the  user
#  _PASSWORD2_  New password.
#  _PASSWORD3_  Checked against PASSWORD2 for typos.
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Change My Password"'</title><meta http-equiv="REFRESH" content="0; URL='"$HTTP_REFERER"'"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g')
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

#Assign PASSWORD1
DATANAME=PASSWORD1
get_data
PASSWORD1="$DATAENTRY"

#Assign PASSWORD2
DATANAME=PASSWORD2
get_data
PASSWORD2="$DATAENTRY"

#Assign PASSWORD3
DATANAME=PASSWORD3
get_data
PASSWORD3="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">
alert("'"$MESSAGE"'");
</script>
</div></body></html>'
exit
}

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
	MESSAGE=$"This username does not exist."
	show_status
fi
#Check to see that password fields are not blank
if [ -z "$PASSWORD1" ] || [ -z "$PASSWORD2" ] || [ -z "$PASSWORD3" ]
then
	MESSAGE=$"The password must not be blank."
	show_status
fi
#Check that password has been entered correctly
if [ "$PASSWORD2" != "$PASSWORD3" ]
then
	MESSAGE=$"The passwords do not match."
	show_status
fi

#Check that the password is strong enough
USERPRIGROUP=$(id -g -n "$USERNAME")

#Get password strength settings
source /opt/karoshi/server_network/security/password_settings
source /opt/karoshi/web_controls/version
if [ "$USERPRIGROUP" = staff ] || [ "$USERPRIGROUP" = staff2 ] || [ "$USERPRIGROUP" = staff3 ] || [ "$USERPRIGROUP" = staff4 ] || [ "$USERPRIGROUP" = officestaff ] || [ "$USERPRIGROUP" = itadmin ] || [ "$USERPRIGROUP" = tech ]
then
	MINPASSLENGTH=$STAFF_MINPASSLENGTH
else
	MINPASSLENGTH=$STUDENT_MINPASSLENGTH
fi

CASECHECK=ok
CHARCHECK=ok

#Convert special characters back for new password to check password strength
NEW_PASSWORD=$(echo "$PASSWORD2" | sed 's/+/ /g; s/%21/!/g; s/%3F/?/g; s/%2C/,/g; s/%3A/:/g; s/%7E/~/g; s/%40/@/g; s/%23/#/g; s/%24/$/g; s/%26/\&/g; s/%2B/+/g; s/%3D/=/g; s/%28/(/g; s/%29/)/g; s/%5E/^/g; s/%7B/{/g; s/%7D/}/g; s/%3C/</g; s/%3E/>/g; s/%5B/[/g; s/%5D/]/g; s/%7C/|/g; s/%22/"/g; s/%1123/*/g' | sed "s/%27/'/g" | sed 's/%3B/;/g' | sed 's/%60/\`/g' | sed 's/%5C/\\/g' | sed 's/%2F/\//g' | sed 's/%25/%/g')

#Check password settings
source /opt/karoshi/server_network/security/password_settings

#Check to see that password has the required number of characters
PASSLENGTH="${#NEW_PASSWORD}"

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
	if [[ $(echo "$PASSWORD2"'1' | tr -cd '0-9\n') = 1 ]]
	then
		CHARCHECK=fail
	fi
	if [[ $(echo "$PASSWORD2"'A' | tr -cd 'A-Za-z\n') = A ]]
	then
		CHARCHECK=fail
	fi

	if [[ $(echo "$PASSWORD2"'A' | tr -cd 'A-Z\n') = A ]]
	then
		CASECHECK=fail
	fi
	if [[ $(echo "$PASSWORD2"'a' | tr -cd 'a-z\n') = a ]]
	then
		CASECHECK=fail
	fi

	if [ "$CASECHECK" = fail ] || [ "$CHARCHECK" = fail ]
	then
		MESSAGE=$"A combination of upper and lower case characters and numbers is required."
		show_status
	fi
fi

#Check to see that the user is not in acceptable use category
if [ -f /opt/karoshi/server_network/acceptable_use_authorisations/pending/"$USERNAME" ]
then
	#Check to see how many days of trial are left
	GRACE_TIME=$(sed -n 1,1p /opt/karoshi/server_network/acceptable_use_authorisations/pending/"$USERNAME" | cut -d, -f1 | tr -cd 0-9)
	[ -z "$GRACE_TIME" ] && GRACE_TIME=0
	if [ "$GRACE_TIME" = 0 ]
		then
		MESSAGE="$USERNAME - "$"This user has not signed an acceptable use policy and their account has now been suspended."
		show_status
	fi
fi

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/all/change_my_password.cgi | cut -d' ' -f1)
#Change password
echo "$REMOTE_ADDR:$MD5SUM:$USERNAME:$PASSWORD1:$PASSWORD2" | sudo -H /opt/karoshi/web_controls/exec/change_my_password
if [ "$?" = 102 ]
then
	sleep 4
	MESSAGE=$"Incorrect username or password supplied for"" $USERNAME."
else
	MESSAGE=$"Password changed for"" $USERNAME."
fi

show_status
