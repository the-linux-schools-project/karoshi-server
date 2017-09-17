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
#  _OPTIONCHOICE_ enable,disable,changepasswords,resetpasswords,deleteaccounts
#  _GROUP_ All the users in this group will be affected

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Bulk user actions"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>
<SCRIPT language=JavaScript1.2>
//change 5 to another integer to alter the scroll speed. Greater is faster
var speed=1
var currentpos=-100,alt=1,curpos1=-100,curpos2=-1
function initialize(){
startit()
}
function scrollwindow(){
if (document.all &&
!document.getElementById)
temp=document.body.scrollTop
else
temp=window.pageYOffset
if (alt==0)
alt=2
else
alt=1
if (alt==0)
curpos1=temp
else
curpos2=temp
if (curpos1!=curpos2){
if (document.all)
currentpos=document.body.scrollTop+speed
else
currentpos=window.pageYOffset+speed
window.scroll(0,currentpos)
}
else{
currentpos=0
window.scroll(0,currentpos)
}
}
function startit(){
setInterval("scrollwindow()",30)
}
window.onload=initialize
</SCRIPT> 

</head><body><div id="pagecontainer">'



#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-+')
#########################
#Assign data to variables
#########################
END_POINT=15
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

#Assign OPTIONCHOICE
DATANAME=OPTIONCHOICE
get_data
OPTIONCHOICE="$DATAENTRY"

#Assign PASSWORD1
DATANAME=PASSWORD1
get_data
PASSWORD1="$DATAENTRY"

#Assign PASSWORD2
DATANAME=PASSWORD2
get_data
PASSWORD2="$DATAENTRY"

#Assign GROUP
DATANAME=GROUP
get_data
GROUP="$DATAENTRY"

#Assign NEWGROUP
DATANAME=NEWGROUP
get_data
NEWGROUP="$DATAENTRY"

#Assign MODCODE
DATANAME=MODCODE
get_data
MODCODE="$DATAENTRY"

#Assign FORMCODE
DATANAME=FORMCODE
get_data
FORMCODE="$DATAENTRY"

#Assign EXCEPTIONLIST
DATANAME=EXCEPTIONLIST
get_data
EXCEPTIONLIST="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/modify_groups_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
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

if [[ $(grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################
#Check to see that optionchoice is not blank
if [ -z "$OPTIONCHOICE" ]
then
	MESSAGE=$"The option choice must not be blank."
	show_status
fi
#Check to see that the group is not blank
if [ -z "$GROUP" ]
then
	MESSAGE=$"The group must not be blank."
	show_status
fi

#Check to see that the group exists
getent group "$GROUP" 1>/dev/null
if [ $? != 0 ]
then
	MESSAGE=$"This group does not exist."
	show_status
fi

#Check to see that the option choice is correct
if [ "$OPTIONCHOICE" != enable ] && [ "$OPTIONCHOICE" != disable ] && [ "$OPTIONCHOICE" != changepasswords ] && [ "$OPTIONCHOICE" != resetpasswords ] && [ "$OPTIONCHOICE" != deleteaccounts ] && [ "$OPTIONCHOICE" != deleteaccounts2 ] && [ "$OPTIONCHOICE" != changepassnextlogon ] && [ "$OPTIONCHOICE" != passwordsneverexpire ] && [ "$OPTIONCHOICE" != passwordsexpire ] && [ "$OPTIONCHOICE" != changeprigroup ]
then
	MESSAGE=$"Incorrect option chosen."
	show_status
fi

#Check to see that MODCODE is not blank
if [ -z "$MODCODE" ]
then
	MESSAGE=$"The modify code must not be blank."
	show_status
fi
#Check to see that FORMCODE is not blank
if [ -z "$FORMCODE" ]
then
	MESSAGE=$"The form code must not be blank."
	show_status
fi
#Make sure that FORMCODE and MODCODE matches
if [ "$FORMCODE" != "$MODCODE" ]
then
	MESSAGE=$"Incorrect modify code."
	show_status
fi

#Check to see that passwords have been entered and are correct
if [ "$OPTIONCHOICE" = changepasswords ]
then
	if [ -z "$PASSWORD1" ] || [ -z "$PASSWORD2" ]
	then
		MESSAGE=$"The passwords must not be blank."
		show_status
	fi
	if [ "$PASSWORD1" != "$PASSWORD2" ]
	then
		MESSAGE=$"The passwords do not match."
		show_status
	fi
fi

if [ "$OPTIONCHOICE" = enable ]
then
	MESSAGE=''$"Enable all users in group"' '"$GROUP"''
fi
if [ "$OPTIONCHOICE" = disable ]
then
	MESSAGE=''$"Disable all users in group"' '"$GROUP"''
fi
if [ "$OPTIONCHOICE" = changepasswords ]
then
	MESSAGE=''$"Change passwords for all users in group"' '"$GROUP"''
fi
if [ "$OPTIONCHOICE" = resetpasswords ]
then
	MESSAGE=''$"Reset passwords all users in group"' '"$GROUP"''
fi
if [ "$OPTIONCHOICE" = deleteaccounts ]
then
	MESSAGE=''$"Delete all users in group"' '"$GROUP"''
fi
if [ "$OPTIONCHOICE" = deleteaccounts2 ]
then
	MESSAGE=''$"Archive and delete all users in group"' '"$GROUP"''
fi
if [ "$OPTIONCHOICE" = changepassnextlogon ]
then
	MESSAGE=''$"Change password on next logon"' '"$GROUP"''
fi

if [ "$OPTIONCHOICE" = passwordsneverexpire ]
then
	MESSAGE=''$"Passwords never expire"' '"$GROUP"''
fi
if [ "$OPTIONCHOICE" = passwordsexpire ]
then
	MESSAGE=''$"Passwords expire"' '"$GROUP"''
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="infobox">'
MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/modify_groups.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$OPTIONCHOICE:$GROUP:$PASSWORD1:$EXCEPTIONLIST:$NEWGROUP:" | sudo -H /opt/karoshi/web_controls/exec/modify_groups
MODIFY_STATUS="$?"
if [ "$MODIFY_STATUS" = 102 ]
then
	MESSAGE=$"The form code must not be blank."
	show_status
fi

if [ "$OPTIONCHOICE" != resetpasswords ]
then
	MESSAGE=''$"Action completed for"' '"$GROUP"'.'
	show_status
else
	echo '<br><br>'$"Action completed for" "$GROUP"'<br>'
	echo "</div>"
fi
exit
