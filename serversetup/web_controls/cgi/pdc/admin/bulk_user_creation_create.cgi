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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Bulk User Creation"'</title></head><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><div class="sectiontitle">'$"Bulk User Creation"'</div><br>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign USERNAMESTYLE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = USERNAMESTYLEcheck ]
	then
		let COUNTER=$COUNTER+1
		USER_STYLE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign GROUP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = GROUPcheck ]
	then
		let COUNTER=$COUNTER+1
		PRI_GROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/bulk_user_creation_create.cgi | cut -d' ' -f1`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/bulk_user_creation_upload_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_status2 {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '</script>'
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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
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
#Check to see that user style is not blank
if [ -z "$USER_STYLE" ]
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
if [ $USER_STYLE != userstyleS1 ] && [ $USER_STYLE != userstyleS2 ] && [ $USER_STYLE != userstyleS3 ] && [ $USER_STYLE != userstyleS4 ] && [ $USER_STYLE != userstyleS5 ] && [ $USER_STYLE != userstyleS6 ] && [ $USER_STYLE != userstyleS7 ] && [ $USER_STYLE != userstyleS8 ] && [ $USER_STYLE != userstyleS9 ] && [ $USER_STYLE != userstyleS10 ]
then
	MESSAGE=$"Incorrect username style."
	show_status
fi

function datacheck {
CREATEUSER=yes
if [ -z "$FORENAME" ]
then
	echo $"Line": $COUNTER - $"Blank forename""<br>"
	CREATEUSER=no
fi
if [ -z "$SURNAME" ]
then
	echo $"Line": $COUNTER - $"Blank surname""<br>"
	CREATEUSER=no
fi
if [ $USER_STYLE = userstyleS9 ]
then
	if [ -z "$ENROLMENT_NO" ]
	then
		echo $"Line": $COUNTER - $"Blank enrolment number""<br>"
		CREATEUSER=no
	fi
fi
if [ $USER_STYLE = userstyleS10 ]
then
	if [ -z "$USERNAME" ]
	then
		echo $"Line": $COUNTER - $"Blank username""<br>"
		CREATEUSER=no
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
if [ `dir /var/www/karoshi/bulk_user_creation --format=single-column | wc -l` != 1 ]
then
	MESSAGE=$"File upload error."
	show_status
fi
CSVFILE=`ls /var/www/karoshi/bulk_user_creation`
echo >> /var/www/karoshi/bulk_user_creation/"$CSVFILE"
sed -i '/^$/d' /var/www/karoshi/bulk_user_creation/"$CSVFILE"
CSVFILE_LINES=`cat /var/www/karoshi/bulk_user_creation/"$CSVFILE" | wc -l`
[ -f /var/www/karoshi/bulk_user_creation/karoshi_web_user_create.csv ] && rm -f /var/www/karoshi/bulk_user_creation/karoshi_web_user_create.csv

#Convert Windows line returns
dos2unix /var/www/karoshi/bulk_user_creation/"$CSVFILE"

COUNTER=1
while [ $COUNTER -le $CSVFILE_LINES ]
do
	FORENAME=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f1 | tr -cd 'A-Za-z0-9,'`
	SURNAME=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f2 | tr -cd 'A-Za-z0-9,'`
	ENROLMENT_NO=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f3 | tr -cd 'A-Za-z0-9,-'`
	USERNAME=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f4 | tr -cd 'A-Za-z0-9,-'`
	PASSWORD=$(urlencode -m `sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f5-`)
	datacheck
	if [ $CREATEUSER = no ]
	then
		MESSAGE=`echo $"The CSV file you have chosen is not formatted correctly."`
		show_status
	fi
	echo "$FORENAME","$SURNAME","$PASSWORD","$ENROLMENT_NO","$USERNAME" >> /var/www/karoshi/bulk_user_creation/karoshi_web_user_create.csv
	let COUNTER=$COUNTER+1
done
rm -f /var/www/karoshi/bulk_user_creation/"$CSVFILE"

function create_username {
datacheck
if [ $CREATEUSER = no ]
then
	MESSAGE=`echo $"CSV file error."`
	show_status
fi

if [ $USER_STYLE = userstyleS2 ]
then
	USERNAME=$YEARSUFFIX$DUPLICATECOUNTER${FORENAME:0:1}$SURNAME
elif [ $USER_STYLE = userstyleS3 ]
then
	USERNAME=$SURNAME${FORENAME:0:1}$YEARSUFFIX$DUPLICATECOUNTER
elif [ $USER_STYLE = userstyleS4 ]
then
	USERNAME=$FORENAME.$SURNAME$YEARSUFFIX$DUPLICATECOUNTER
elif [ $USER_STYLE = userstyleS5 ]
then
	USERNAME=$SURNAME.$FORENAME$YEARSUFFIX$DUPLICATECOUNTER
elif [ $USER_STYLE = userstyleS6 ]
then
	USERNAME=$YEARSUFFIX$DUPLICATECOUNTER$SURNAME${FORENAME:0:1}
elif [ $USER_STYLE = userstyleS7 ]
then
	USERNAME=$YEARSUFFIX$DUPLICATECOUNTER$FORENAME${SURNAME:0:1}
elif [ $USER_STYLE = userstyleS8 ]
then
	SURNAMECOUNT=${#SURNAME}
	if [ $DUPLICATECOUNTER -le $SURNAMECOUNT ]
	then
		COUNTER2=""
		USERNAME=$FORENAME${SURNAME:0:$DUPLICATECOUNTER}
	else
		[ -z "$COUNTER2" ] && COUNTER2=1
		USERNAME=$FORENAME${SURNAME:0:$DUPLICATECOUNTER}$COUNTER2
		let COUNTER2=$COUNTER2+1
	fi
elif [ $USER_STYLE = userstyleS9 ]
then
	if [ $DUPLICATECOUNTER = 1 ]
	then
		USERNAME=$ENROLMENT_NO
	else
		USERNAME=$ENROLMENT_NO.$DUPLICATECOUNTER
	fi
elif [ $USER_STYLE = userstyleS10 ]
then
		USERNAME=$USERNAME$DUPLICATECOUNTER	
else
	USERNAME=${FORENAME:0:1}$SURNAME$YEARSUFFIX$DUPLICATECOUNTER
fi
USERNAME=`echo $USERNAME | tr '[A-Z]' '[a-z]'`
}

#Create CSVfile with information

source /opt/karoshi/server_network/group_information/$PRI_GROUP
CSVFILE=karoshi_web_user_create.csv
CSVFILE_LINES=`cat /var/www/karoshi/bulk_user_creation/"$CSVFILE" | wc -l`
COUNTER=1

tr -d '\r' < /var/www/karoshi/bulk_user_creation/"$CSVFILE" > /var/www/karoshi/bulk_user_creation/"$CSVFILE".$$
rm -f /var/www/karoshi/bulk_user_creation/"$CSVFILE"
mv /var/www/karoshi/bulk_user_creation/"$CSVFILE".$$ /var/www/karoshi/bulk_user_creation/"$CSVFILE"

#Show users to create

while [ $COUNTER -le $CSVFILE_LINES ]
do
	FORENAME=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f1 | sed 's/ //g'`
	SURNAME=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f2  | sed 's/ //g'`
	PASSWORD=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f3`
	ENROLMENT_NO=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f4 |  sed 's/ //g'`
	USERNAME=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation/"$CSVFILE" | cut -s -d, -f5 |  sed 's/ //g'`
	DUPLICATECOUNTER=""
	create_username
	DUPLICATE_CHECK=yes
	#Check that no duplicate usernames exist
	while [ $DUPLICATE_CHECK = yes ]
	do
		id -u "$USERNAME" 1>/dev/null 2>/dev/null
		if [ $? = 0 ]
		then
			[ -z "$DUPLICATECOUNTER" ] && DUPLICATECOUNTER=1
			echo $USERNAME - $"This username is already in use.""<br>"
			create_username
			let DUPLICATECOUNTER=$DUPLICATECOUNTER+1
		else
			DUPLICATE_CHECK=no
			break
		fi
		[ $DUPLICATECOUNTER = 50000 ] && break
	done


	if [ $DUPLICATE_CHECK = no ]
	then
		datacheck
		if [ $CREATEUSER = yes ]
		then
			echo $"Creating" "$USERNAME" - "$FORENAME" "$SURNAME"'<br><br>'
			[ -z "$PASSWORD" ] && PASSWORD="$RANDOM"
			echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$FORENAME:$SURNAME:$USERNAME:$PASSWORD:$PRI_GROUP:$USER_STYLE:$ENROLMENT_NO:$REQUESTFILE":bulkusercreation | sudo -H /opt/karoshi/web_controls/exec/add_user
		fi
	fi
	let COUNTER=$COUNTER+1
done
[ -f /var/www/karoshi/bulk_user_creation/"$CSVFILE" ] && rm -f /var/www/karoshi/bulk_user_creation/"$CSVFILE"
MESSAGE=$"Bulk user creation completed."
show_status
echo "</div>"
echo "</div></body></html>"
exit

