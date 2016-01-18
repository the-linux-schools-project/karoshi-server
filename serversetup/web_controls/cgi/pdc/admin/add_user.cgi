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
#  _FIRSTNAME_
#  _SURNAME_
# _USERNAMESTYLE_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
#  _GROUP_      This is the primary group for the new user eg yr2000, staff, officestaff.
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Add a New User"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=21
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
#Assign ENROLLMENTNUMBER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ENROLLMENTNUMBERcheck ]
	then
		let COUNTER=$COUNTER+1
		ENROLLMENTNUMBER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign password1
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PASSWORD1check ]
	then
		let COUNTER=$COUNTER+1
		PASSWORD1=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
	done
#Assign password2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PASSWORD2check ]
	then
		let COUNTER=$COUNTER+1
		PASSWORD2=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign group
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = GROUPcheck ]
	then
		let COUNTER=$COUNTER+1
		GROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign USERNAMESTYLE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = USERNAMESTYLEcheck ]
	then
		let COUNTER=$COUNTER+1
		USERNAMESTYLE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign USERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | tr 'A-Z' 'a-z'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign REQUESTFILE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = REQUESTFILEcheck ]
	then
		let COUNTER=$COUNTER+1
		REQUESTFILE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
	done

STARTCGI=add_user_fm.cgi
[ $REQUESTFILE'null' != null ] && STARTCGI=request_new_users_fm.cgi

function show_status {
echo '<script>
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/'$STARTCGI'";
</script>'
[ $MOBILE = no ] && echo '</div>'
echo '</div></body></html>'
exit
}

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=menubox
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Add a New User"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div>
'
else
	echo '<div id="'$DIV_ID'"><div class="sectiontitle">'$"Add a New User"'</div><br>'
fi

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
#Check to see that firstname is not blank
if [ -z "$FIRSTNAME" ]
then
	MESSAGE=$"The firstname must not be blank."
	show_status
fi
#Check to see that surname is not blank
if [ -z "$SURNAME" ]
then
	MESSAGE=$"The surname must not be blank."
	show_status
fi
#Check to see that password fields are not blank
if [ -z "$PASSWORD1" ]
then
	MESSAGE=$"The password must not be blank."
	show_status
fi
if [ -z "$PASSWORD2" ]
then
	MESSAGE=$"The password must not be blank."
	show_status
fi
if [ -z "$GROUP" ]
then
	MESSAGE=$"The group must not be blank."
	show_status
fi
#Check that password has been entered correctly
if [ "$PASSWORD1" != "$PASSWORD2" ]
then
	MESSAGE=$"The passwords do not match."
	show_status
fi
#Check that usernamestyle is not blank
if [ -z "$USERNAMESTYLE" ]
then
	MESSAGE=$"The username style must not be blank."
	show_status
fi
#Check that usernamestyle is the correct value
if [ $USERNAMESTYLE != userstyleS1 ] && [ $USERNAMESTYLE != userstyleS2 ] && [ $USERNAMESTYLE != userstyleS3 ] && [ $USERNAMESTYLE != userstyleS4 ] && [ $USERNAMESTYLE != userstyleS5 ] && [ $USERNAMESTYLE != userstyleS6 ] && [ $USERNAMESTYLE != userstyleS7 ] && [ $USERNAMESTYLE != userstyleS8 ] && [ $USERNAMESTYLE != userstyleS9 ] && [ $USERNAMESTYLE != userstyleS10 ]
then
	MESSAGE=$"Incorrect username style."
	show_status
fi
#Check that username is not blank for style 10
if [ $USERNAMESTYLE = userstyleS10 ]
then
	if [ -z "$USERNAME" ]
	then
		MESSAGE=$"The username must not be blank."
		show_status	
	fi
fi

COUNTER=""
#Create username
DUPLICATECHECK=0

function check_username {
NAMESTATUS=ok
id -u "$USERNAME" 1>/dev/null 2>/dev/null
if [ $? = 0 ]
then
	NAMESTATUS=error
fi
getent group "$USERNAME" 1>/dev/null 2>/dev/null
if [ $? = 0 ]
then
	NAMESTATUS=error
fi
}

function create_username {
source /opt/karoshi/server_network/group_information/$GROUP
if [ "$USERNAMESTYLE" = userstyleS1 ]
then
	USERNAME=`echo ${FIRSTNAME:0:1}$SURNAME$YEARSUFFIX$COUNTER`
fi
if [ "$USERNAMESTYLE" = userstyleS2 ]
then
	USERNAME=`echo $YEARSUFFIX$COUNTER${FIRSTNAME:0:1}$SURNAME`
fi
if [ "$USERNAMESTYLE" = userstyleS3 ]
then
	USERNAME=`echo $SURNAME${FIRSTNAME:0:1}$YEARSUFFIX$COUNTER`
fi
if [ "$USERNAMESTYLE" = userstyleS4 ]
then
	USERNAME=`echo $FIRSTNAME.$SURNAME$YEARSUFFIX$COUNTER`
fi
if [ "$USERNAMESTYLE" = userstyleS5 ]
then
	USERNAME=`echo $SURNAME.$FIRSTNAME$YEARSUFFIX$COUNTER`
fi
if [ "$USERNAMESTYLE" = userstyleS6 ]
then
	USERNAME=`echo $YEARSUFFIX$COUNTER$SURNAME${FIRSTNAME:0:1}`
fi
if [ "$USERNAMESTYLE" = userstyleS7 ]
then
	USERNAME=`echo $YEARSUFFIX$COUNTER$FIRSTNAME${SURNAME:0:1}`
fi
if [ "$USERNAMESTYLE" = userstyleS8 ]
then
	[ -z "$COUNTER" ] && COUNTER=1
	USERNAME=`echo $FIRSTNAME${SURNAME:0:$COUNTER}`
fi
if [ "$USERNAMESTYLE" = userstyleS9 ]
then
#Check to see that enrolment is not blank
	if [ -z "$ENROLLMENTNUMBER" ]
	then
		MESSAGE=$"The enrolment number must not be blank."
		show_status
	fi
	[ -z "$COUNTER" ] && COUNTER=1
	if [ $DUPLICATECHECK = 0 ]
	then
		USERNAME=`echo $ENROLLMENTNUMBER`
	else
		USERNAME=`echo $ENROLLMENTNUMBER.$COUNTER`
	fi
fi

if [ "$USERNAMESTYLE" = userstyleS10 ]
then
	[ -z "$COUNTER" ] && COUNTER=1
	USERNAME=`echo $USERNAME$COUNTER`
fi

USERNAME=`echo $USERNAME | tr 'A-Z' 'a-z'`
}

[ -z "$USERNAME" ] && create_username

#Correct new username if user already exists.
INITUSERNAME=$USERNAME
DUPLICATECHECK=1
ACTIONUSER=0

if [ $USERNAMESTYLE != userstyleS8 ]
then
	while [ $DUPLICATECHECK = 1 ]
	do
		check_username
		if [ $NAMESTATUS = error ]
		then
			[ -z "$COUNTER" ] && COUNTER=1
			#user exists
			create_username
			let COUNTER=$COUNTER+1
			ACTIONUSER=1
		else
			DUPLICATECHECK=0
		fi
	done
fi

if [ $USERNAMESTYLE = userstyleS8 ]
then
	while [ $DUPLICATECHECK = 1 ]
	do
		check_username
		if [ $NAMESTATUS = error ]
		then
			#user exists
			let COUNTER=$COUNTER+1
			create_username
			ACTIONUSER=1
		else
			DUPLICATECHECK=0
		fi
	done
fi

#Prompt to create user with revised username if username existed or create user.
if [ $ACTIONUSER = 1 ]
then
	echo '<form action="/cgi-bin/admin/add_user.cgi" method="post">
	<input name="____FIRSTNAME____" value="'$FIRSTNAME'" type="hidden">
	<input name="____SURNAME____" value="'$SURNAME'" type="hidden">
	<input name="____PASSWORD1____" value="'$PASSWORD1'" type="hidden">
	<input name="____PASSWORD2____" value="'$PASSWORD2'" type="hidden">
	<input name="____GROUP____" value="'$GROUP'" type="hidden">
	<input name="____USERNAMESTYLE____" value="'$USERNAMESTYLE'" type="hidden">
	<input name="____USERNAME____" value="'$USERNAME'" type="hidden">
	<input name="____ENROLLMENTNUMBER____" value="'$ENROLLMENTNUMBER'" type="hidden">
	'$INITUSERNAME' - '$"This user already exists."'<br><br>'$"Create user"' '$USERNAME'?<br><br>
	<input value="'$"Submit"'" class="button" type="submit">
	</form></div></div></body></html>'
	exit
else
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/add_user.cgi | cut -d' ' -f1`
	#Add user
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$FIRSTNAME:$SURNAME:$USERNAME:$PASSWORD1:$GROUP:$USERNAMESTYLE:$ENROLLMENTNUMBER:$REQUESTFILE::" | sudo -H /opt/karoshi/web_controls/exec/add_user
EXEC_STATUS=`echo $?`
MESSAGE=`echo $"Forename": "${FIRSTNAME^}"'\\n'$"Surname": "${SURNAME^}"'\\n'$"Username": $USERNAME'\\n'$"Created with primary group" $GROUP.`
	if [ $EXEC_STATUS = 101 ]
	then
		MESSAGE=`echo $"There was a problem with this action." $"Please check the karoshi web administration logs for more details."`
	fi

	if [ $EXEC_STATUS = 103 ]
	then
		MESSAGE=`echo "$MESSAGE" $"The enrolment number entered is already in use and has been left blank for this user."`
	fi

	if [ $EXEC_STATUS = 105 ]
	then
		MESSAGE=`echo $"A server required for this action was offline." $"Please check the karoshi web administration logs for more details."`
	fi

	if [[ $EXEC_STATUS -eq 106 ]]; then
		MESSAGE="$USERNAME - $"A group with the same name as this user already exists, not creating user""
	fi
	show_status
fi
exit
