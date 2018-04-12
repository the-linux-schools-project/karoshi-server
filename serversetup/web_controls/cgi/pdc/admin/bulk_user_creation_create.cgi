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
#  _USERNAMESTYLE_
#  _GROUP_      This is the primary group for the new user eg yr2000, staff, officestaff.
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Bulk User Creation"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox"><div class="sectiontitle">'$"Bulk User Creation"'</div></div><div id="infobox">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')
#########################
#Assign data to variables
#########################
END_POINT=7
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

#Assign USERNAMESTYLE
DATANAME=USERNAMESTYLE
get_data
USERNAMESTYLE="$DATAENTRY"

#Assign GROUP
DATANAME=GROUP
get_data
PRI_GROUP="$DATAENTRY"

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/bulk_user_creation_create.cgi | cut -d' ' -f1)

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/bulk_user_creation_upload_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_status2 {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '</script>'
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
#Check to see that user style is not blank
if [ -z "$USERNAMESTYLE" ]
then
	MESSAGE=$"The user style must not be blank."
	show_status
fi
#Check that primary group is not blank
if [ -z "$PRI_GROUP" ]
then
	MESSAGE=$"The primary group must not be blank."
	show_status
fi
#Check to see that userstyle is correct
if [ "$USERNAMESTYLE" != userstyleS1 ] && [ "$USERNAMESTYLE" != userstyleS2 ] && [ "$USERNAMESTYLE" != userstyleS3 ] && [ "$USERNAMESTYLE" != userstyleS4 ] && [ "$USERNAMESTYLE" != userstyleS5 ] && [ "$USERNAMESTYLE" != userstyleS6 ] && [ "$USERNAMESTYLE" != userstyleS7 ] && [ "$USERNAMESTYLE" != userstyleS8 ] && [ "$USERNAMESTYLE" != userstyleS9 ] && [ "$USERNAMESTYLE" != userstyleS10 ]
then
	MESSAGE=$"Incorrect username style."
	show_status
fi

function datacheck {
CREATEUSER=yes
if [ -z "$FORENAME" ]
then
	echo $"Line"": $COUNTER - "$"Blank forename""<br>"
	CREATEUSER=no
fi
if [ -z "$SURNAME" ]
then
	echo $"Line"": $COUNTER - "$"Blank surname""<br>"
	CREATEUSER=no
fi
if [ "$USERNAMESTYLE" = userstyleS9 ]
then
	if [ -z "$ENROLMENT_NO" ]
	then
		echo $"Line": $COUNTER - $"Blank enrolment number""<br>"
		CREATEUSER=no
	fi
fi
if [ "$USERNAMESTYLE" = userstyleS10 ]
then
	if [ -z "$USERNAME" ]
	then
		echo $"Line": $COUNTER - $"Blank username""<br>"
		CREATEUSER=no
	fi
fi

#Check that the username is 20 characters or less
USERNAMELENGTH="${#USERNAME}"  
if [ "$USERNAMELENGTH" -gt 20 ]
then
	echo $"Line"": $COUNTER - $USERNAME "$"The username is greater than 20 characters""<br>"
	CREATEUSER=no
fi


if [ "$PRI_GROUP" = getgroupfromcsv ]
then
	if [ -z "$USERPGROUP" ]
	then
		echo $"Line"": $COUNTER - "$"Blank Primary Group""<br>"
		CREATEUSER=no
	fi
fi

source /opt/karoshi/server_network/security/password_settings
#Create a new password if it is blank
if [ -z "$PASSWORD" ]
then
	if [ "$PASSWORDCOMPLEXITY" = on ]
	then
		PASSWORD=$(openssl rand -base64 24 | head -c"$MINPASSWORDLENGTH" 2>/dev/null)
		PASSWORD=$(urlencode -m "$PASSWORD")
	else
		PASSWORD=$(shuf -i 10000000000000-99999999999999 -n 1 | head -c"$MINPASSWORDLENGTH")
	fi
else
	#Check password length
	RAWPASSWORD=$(urlencode -d "$PASSWORD")
	PASSLENGTH=${#RAWPASSWORD}

	#Check to see that password has the required number of characters
	if [ "$PASSLENGTH" -lt "$MINPASSLENGTH" ]
	then
		echo $"Line": $COUNTER - $"Required password length""<br>"
		CREATEUSER=no
	fi

	#Check for upper and lower case characters and numbers
	if [ "$PASSWORDCOMPLEXITY" = on ]
	then
		CASECHECK=ok
		CHARCHECK=ok

		#Check that the password has a combination of characters and numbers
		if [[ $(echo "$RAWPASSWORD"'1' | tr -cd '0-9\n') = 1 ]]
		then
			CHARCHECK=fail
		fi
		if [[ $(echo "$RAWPASSWORD"'A' | tr -cd 'A-Za-z\n') = A ]]
		then
			CHARCHECK=fail
		fi

		if [[ $(echo "$RAWPASSWORD"'A' | tr -cd 'A-Z\n') = A ]]
		then
			CASECHECK=fail
		fi
		if [[ $(echo "$RAWPASSWORD"'a' | tr -cd 'a-z\n') = a ]]
		then
			CASECHECK=fail
		fi

		if [ "$CASECHECK" = fail ] || [ "$CHARCHECK" = fail ]
		then
			echo $"Line": $COUNTER - $"A combination of upper and lower case characters and numbers is required.""<br>"
			CREATEUSER=no
		fi
	fi
fi




}

#########################
#Check data
#########################
#Check input file
[ -d /var/www/karoshi/bulk_user_creation ] || mkdir -p /var/www/karoshi/bulk_user_creation
chmod 0700 /var/www/karoshi/
chmod 0700 /var/www/karoshi/bulk_user_creation
if [[ $(dir /var/www/karoshi/bulk_user_creation --format=single-column | wc -l) != 1 ]]
then
	MESSAGE=$"File upload error."
	show_status
fi
CSVFILE=$(ls /var/www/karoshi/bulk_user_creation)
echo >> /var/www/karoshi/bulk_user_creation/"$CSVFILE"
sed -i '/^$/d' /var/www/karoshi/bulk_user_creation/"$CSVFILE"
CSVFILE_LINES=$(wc -l < /var/www/karoshi/bulk_user_creation/"$CSVFILE")
[ -f /var/www/karoshi/bulk_user_creation/karoshi_web_user_create.csv ] && rm -f /var/www/karoshi/bulk_user_creation/karoshi_web_user_create.csv

#Convert Windows line returns
dos2unix /var/www/karoshi/bulk_user_creation/"$CSVFILE"

#Check if the first row contain column headers
#Possible headers are: forename, surname, enrolment-number, username, primary-group, secondary-groups, change-password-on-logon,room-number,telephone-number,fax-number,mobile-number,password
if [[ $(sed -n 1,1p  /var/www/karoshi/bulk_user_creation/"$CSVFILE" | grep -ic 'forename\|surname') -gt 0 ]]
then
	UseHeaders=yes
	HeaderData=$(sed -n 1,1p  /var/www/karoshi/bulk_user_creation/"$CSVFILE" | sed 's/,/\n/g')
	COUNTER=2
	ForenameCol=$(echo -e "$HeaderData" | grep -in forename | cut -d: -f1)
	SurnameCol=$(echo -e "$HeaderData" | grep -in surname | cut -d: -f1)
	EnrolmentCol=$(echo -e "$HeaderData" | grep -in enrolment-number | cut -d: -f1)
	UsernameCol=$(echo -e "$HeaderData" | grep -in username | cut -d: -f1)
	PrimaryGroupCol=$(echo -e "$HeaderData" | grep -in primary-group | cut -d: -f1)
	SecondaryGroupsCol=$(echo -e "$HeaderData" | grep -in secondary-groups | cut -d: -f1)
	ChangePasswordOnLogonCol=$(echo -e "$HeaderData" | grep -in change-password-on-logon | cut -d: -f1)
	RoomNumberCol=$(echo -e "$HeaderData" | grep -in room-number | cut -d: -f1)
	TelephoneNumberCol=$(echo -e "$HeaderData" | grep -in telephone-number | cut -d: -f1)
	FaxNumberCol=$(echo -e "$HeaderData" | grep -in fax-number | cut -d: -f1)
	MobileNumberCol=$(echo -e "$HeaderData" | grep -in mobile-number | cut -d: -f1)
	PasswordCol=$(echo -e "$HeaderData" | grep -in password | cut -d: -f1)


else
	UseHeaders=no
	COUNTER=1
	ForenameCol=1
	SurnameCol=2
	EnrolmentCol=3
	UsernameCol=4
	PrimaryGroupCol=5
	SecondaryGroupsCol=6
	ChangePasswordOnLogonCol=7
	RoomNumberCol=8
	TelephoneNumberCol=9
	FaxNumberCol=10
	MobileNumberCol=11
	PasswordCol=12
fi

while [ "$COUNTER" -le "$CSVFILE_LINES" ]
do
	FORENAME=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$ForenameCol" | tr -cd 'A-Za-z0-9,')
	SURNAME=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$SurnameCol" | tr -cd 'A-Za-z0-9,')
	[ ! -z "$EnrolmentCol" ] && ENROLMENT_NO=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$EnrolmentCol" | tr -cd 'A-Za-z0-9,-')
	[ ! -z "$UsernameCol" ] && USERNAME=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$UsernameCol" | tr -cd 'A-Za-z0-9,-')
	[ ! -z "$PrimaryGroupCol" ] && USERPGROUP=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$PrimaryGroupCol" | tr -cd 'A-Za-z0-9,-')
	[ ! -z "$SecondaryGroupsCol" ] && USERSGROUPS=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$SecondaryGroupsCol" | tr -cd 'A-Za-z0-9,:-')
	[ ! -z "$ChangePasswordOnLogonCol" ] && NEXTLOGON=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$ChangePasswordOnLogonCol" | tr -cd 'A-Za-z0-9,-')

	[ ! -z "$RoomNumberCol" ] && ROOMNUMBER=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$RoomNumberCol" | tr -cd 'A-Za-z0-9,-')
	[ ! -z "$TelephoneNumberCol" ] && TELEPHONENUMBER=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$TelephoneNumberCol" | tr -cd 'A-Za-z0-9,-')
	[ ! -z "$FaxNumberCol" ] && FAXNUMBER=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$FaxNumberCol" | tr -cd 'A-Za-z0-9,-')
	[ ! -z "$MobileNumberCol" ] && MOBILENUMBER=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$MobileNumberCol" | tr -cd 'A-Za-z0-9,-')


	if [ "$UseHeaders" = yes ]
	then
		[ ! -z "$PasswordCol" ] && PASSWORD=$(urlencode -m "$(sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$PasswordCol")")
	else
		[ ! -z "$PasswordCol" ] && PASSWORD=$(urlencode -m "$(sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f"$PasswordCol"-)")
	fi
	datacheck
	if [ "$CREATEUSER" = no ]
	then
		MESSAGE=$"The CSV file you have chosen is not formatted correctly."
		show_status
	fi
	echo "$FORENAME,$SURNAME,$PASSWORD,$ENROLMENT_NO,$USERNAME,$USERPGROUP,$USERSGROUPS,$NEXTLOGON,$ROOMNUMBER,$TELEPHONENUMBER,$FAXNUMBER,$MOBILENUMBER" >> /var/www/karoshi/bulk_user_creation/karoshi_web_user_create.csv
	let COUNTER="$COUNTER"+1
done
rm -f /var/www/karoshi/bulk_user_creation/"$CSVFILE"

function create_username {
datacheck
source /opt/karoshi/server_network/group_information/"$USERGROUP"
if [ "$CREATEUSER" = no ]
then
	MESSAGE=$"CSV file error."
	show_status
fi

if [ "$USERNAMESTYLE" = userstyleS2 ]
then
	USERNAME="$YEARSUFFIX$DUPLICATECOUNTER${FORENAME:0:1}$SURNAME"
elif [ "$USERNAMESTYLE" = userstyleS3 ]
then
	USERNAME="$SURNAME${FORENAME:0:1}$YEARSUFFIX$DUPLICATECOUNTER"
elif [ "$USERNAMESTYLE" = userstyleS4 ]
then
	USERNAME="$FORENAME.$SURNAME$YEARSUFFIX$DUPLICATECOUNTER"
elif [ "$USERNAMESTYLE" = userstyleS5 ]
then
	USERNAME=$SURNAME.$FORENAME$YEARSUFFIX$DUPLICATECOUNTER
elif [ "$USERNAMESTYLE" = userstyleS6 ]
then
	USERNAME="$YEARSUFFIX$DUPLICATECOUNTER$SURNAME${FORENAME:0:1}"
elif [ "$USERNAMESTYLE" = userstyleS7 ]
then
	USERNAME="$YEARSUFFIX$DUPLICATECOUNTER$FORENAME${SURNAME:0:1}"
elif [ "$USERNAMESTYLE" = userstyleS8 ]
then
	SURNAMECOUNT="${#SURNAME}"
	[ -z "$DUPLICATECOUNTER" ] && DUPLICATECOUNTER=1
	if [ "$DUPLICATECOUNTER" -le "$SURNAMECOUNT" ]
	then
		COUNTER2=""
		USERNAME=$FORENAME${SURNAME:0:$DUPLICATECOUNTER}
	else
		[ -z "$COUNTER2" ] && COUNTER2=1
		USERNAME="$FORENAME${SURNAME:0:$DUPLICATECOUNTER}$COUNTER2"
		let COUNTER2="$COUNTER2"+1
	fi
elif [ "$USERNAMESTYLE" = userstyleS9 ]
then
	if [ -z "$DUPLICATECOUNTER" ]
	then
		USERNAME="$ENROLMENT_NO"
	else
		USERNAME="$ENROLMENT_NO.$DUPLICATECOUNTER"
	fi
elif [ "$USERNAMESTYLE" = userstyleS10 ]
then
		USERNAME="$USERNAME$DUPLICATECOUNTER"
else
	USERNAME="${FORENAME:0:1}$SURNAME$YEARSUFFIX$DUPLICATECOUNTER"
fi
USERNAME=$(echo "$USERNAME" | tr '[:upper:]' '[:lower:]')
}

#Create CSVfile with information

source /opt/karoshi/web_controls/version
CSVFILE=karoshi_web_user_create.csv
CSVFILE_LINES=$(wc -l < /var/www/karoshi/bulk_user_creation/"$CSVFILE")
COUNTER=1

tr -d '\r' < /var/www/karoshi/bulk_user_creation/"$CSVFILE" > /var/www/karoshi/bulk_user_creation/"$CSVFILE.$$"
rm -f /var/www/karoshi/bulk_user_creation/"$CSVFILE"
mv /var/www/karoshi/bulk_user_creation/"$CSVFILE.$$" /var/www/karoshi/bulk_user_creation/"$CSVFILE"

#Show users to create
echo "<ul>"
while [ "$COUNTER" -le "$CSVFILE_LINES" ]
do
	FORENAME=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f1 | sed 's/ //g')
	SURNAME=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f2  | sed 's/ //g')
	PASSWORD=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f3)
	ENROLMENT_NO=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f4 |  sed 's/ //g')
	USERNAME=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f5 |  sed 's/ //g')
	USERPGROUP=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f6 |  sed 's/ //g')
	USERSGROUPS=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f7 |  sed 's/ //g')
	NEXTLOGON=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f8 |  sed 's/ //g')
	ROOMNUMBER=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f9 |  sed 's/ //g')
	TELEPHONENUMBER=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f10 |  sed 's/ //g')
	FAXNUMBER=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f11 |  sed 's/ //g')
	MOBILENUMBER=$(sed -n "$COUNTER","$COUNTER"'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f12 |  sed 's/ //g')

	DUPLICATECOUNTER=""

	if [ "$PRI_GROUP" = getgroupfromcsv ]
	then
		USERGROUP="$USERPGROUP"
	else
		USERGROUP="$PRI_GROUP"
	fi

	create_username
	DUPLICATE_CHECK=yes
	#Check that no duplicate usernames exist
	while [ "$DUPLICATE_CHECK" = yes ]
	do
		id -u "$USERNAME" 1>/dev/null 2>/dev/null
		if [ "$?" = 0 ]
		then
			[ -z "$DUPLICATECOUNTER" ] && DUPLICATECOUNTER=1
			echo "<li>$USERNAME - "$"This username is already in use.""</li>"
			create_username
			let DUPLICATECOUNTER="$DUPLICATECOUNTER"+1
		else
			DUPLICATE_CHECK=no
			break
		fi
		[ "$DUPLICATECOUNTER" = 50000 ] && break
	done


	if [ "$DUPLICATE_CHECK" = no ]
	then
		datacheck
		if [ "$CREATEUSER" = yes ]
		then
			echo "<li>"$"Creating" "$USERNAME - $FORENAME $SURNAME</li>"

			echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$FORENAME:$SURNAME:$USERNAME:$PASSWORD:$USERGROUP:$USERNAMESTYLE:$ENROLMENT_NO:$REQUESTFILE:bulkusercreation:$NEXTLOGON:$ROOMNUMBER:$TELEPHONENUMBER:$FAXNUMBER:$MOBILENUMBER:$USERSGROUPS:" | sudo -H /opt/karoshi/web_controls/exec/add_user
		fi
	fi
	let COUNTER="$COUNTER"+1
done
echo "</ul>"
[ -f /var/www/karoshi/bulk_user_creation/"$CSVFILE" ] && rm -f /var/www/karoshi/bulk_user_creation/"$CSVFILE"
MESSAGE=$"Bulk user creation completed."
show_status
echo "</div>"
echo "</div></body></html>"
exit

