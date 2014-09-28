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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Change My Password"'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
END_POINT=9
#Assign USERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
then
let COUNTER=$COUNTER+1
USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PASSWORD1
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
#Assign PASSWORD2
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
#Assign PASSWORD3
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PASSWORD3check ]
then
let COUNTER=$COUNTER+1
PASSWORD3=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">
alert("'$MESSAGE'");
</script>
</div></body></html>'
exit
}

#########################
#Check data
#########################
#Check to see that username is not blank
if [ $USERNAME'null' = null ]
then
MESSAGE=$"The username must not be blank."
show_status
fi
#Check to see that the user exists
getent passwd "$USERNAME" 1>/dev/null 2>/dev/null
USERSTATUS=`echo $?`
if [ $USERSTATUS != 0 ]
then
MESSAGE=$"This username does not exist."
show_status
fi
#Check to see that password fields are not blank
if [ $PASSWORD1'null' = null ] || [ $PASSWORD2'null' = null ] || [ $PASSWORD3'null' = null ]
then
MESSAGE=$"The password must not be blank."
show_status
fi
#Check that password has been entered correctly
if [ $PASSWORD2 != $PASSWORD3 ]
then
MESSAGE=$"The passwords do not match."
show_status
fi

#Check that the password is strong enough
USERPRIGROUP=`id -g -n $USERNAME`

#Get password strength settings
source /opt/karoshi/server_network/security/password_settings
if [ $USERPRIGROUP = staff ] || [ $USERPRIGROUP = staff2 ] || [ $USERPRIGROUP = staff3 ] || [ $USERPRIGROUP = staff4 ] || [ $USERPRIGROUP = officestaff ] || [ $USERPRIGROUP = itadmin ] || [ $USERPRIGROUP = tech ]
then
CHARS_AND_NUMBERS=$STAFF_CHARS_AND_NUMBERS
UPPER_AND_LOWER_CASE=$STAFF_UPPER_AND_LOWER_CASE
MINPASSLENGTH=$STAFF_MINPASSLENGTH
else
CHARS_AND_NUMBERS=$STUDENT_CHARS_AND_NUMBERS
UPPER_AND_LOWER_CASE=$STUDENT_UPPER_AND_LOWER_CASE
MINPASSLENGTH=$STUDENT_MINPASSLENGTH
fi

LENGTHCHECK=ok
CASECHECK=ok
CHARCHECK=ok
LENGTHCHECK2=$"Ok"
CASECHECK2=$"Ok"
CHARCHECK2=$"Ok"
[ $UPPER_AND_LOWER_CASE = no ] && CASECHECK2=$"N.A."
[ $CHARS_AND_NUMBERS = no ] && CHARCHECK2=$"N.A."

########################
#Convert special characters back for new password to check password strength
########################

NEW_PASSWORD=`echo "$PASSWORD2" | sed 's/+/ /g; s/%21/!/g; s/%3F/?/g; s/%2C/,/g; s/%3A/:/g; s/%7E/~/g; s/%40/@/g; s/%23/#/g; s/%24/$/g; s/%26/\&/g; s/%2B/+/g; s/%3D/=/g; s/%28/(/g; s/%29/)/g; s/%5E/^/g; s/%7B/{/g; s/%7D/}/g; s/%3C/</g; s/%3E/>/g; s/%5B/[/g; s/%5D/]/g; s/%7C/|/g; s/%22/"/g; s/%1123/*/g' | sed "s/%27/'/g" | sed 's/%3B/;/g' | sed 's/%60/\`/g' | sed 's/%5C/\\\/g' | sed 's/%2F/\//g' | sed 's/%25/%/g'`


PASSLENGTH=${#NEW_PASSWORD}

#Check to see that password has the required number of characters
if [ $PASSLENGTH -lt $MINPASSLENGTH ]
then
LENGTHCHECK=fail
LENGTHCHECK2=$"Failed"
fi

#Check that the password has a combination of characters and numbers
if [ $CHARS_AND_NUMBERS = yes ]
then
if [ `echo "$NEW_PASSWORD"'1' | tr -cd '0-9\n'` = 1 ]
then
CHARCHECK=fail
CHARCHECK2=$"Failed"
fi
if [ `echo "$NEW_PASSWORD"'A' | tr -cd 'A-Za-z\n'` = A ]
then
CHARCHECK=fail
CHARCHECK2=$"Failed"
fi
fi

#Check that a combination of upper case and lower case has been used
if [ $UPPER_AND_LOWER_CASE = yes ]
then
if [ `echo "$NEW_PASSWORD"'A' | tr -cd 'A-Z\n'` = A ]
then
CASECHECK=fail
CASECHECK2=$"Failed"
fi
if [ `echo "$NEW_PASSWORD"'a' | tr -cd 'a-z\n'` = a ]
then
CASECHECK=fail
CASECHECK2=$"Failed"
fi
fi

if [ $LENGTHCHECK = fail ] || [ $CASECHECK = fail ] || [ $CHARCHECK = fail ]
then
MESSAGE=''$"Your password length"': '$PASSLENGTH'\n'$"Required password length"': '$MINPASSLENGTH' - '$LENGTHCHECK2''

[ $CHARS_AND_NUMBERS = yes ] && MESSAGE=''$MESSAGE'\n'$"Characters and numbers required."' - '$CHARCHECK2''
[ $UPPER_AND_LOWER_CASE = yes ] && MESSAGE=''$MESSAGE'\n'$"Upper and lower case characters required."' - '$CASECHECK2''

show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/all/change_my_password.cgi | cut -d' ' -f1`
#Change password
echo "$REMOTE_ADDR:$MD5SUM:$USERNAME:$PASSWORD1:$PASSWORD2" | sudo -H /opt/karoshi/web_controls/exec/change_my_password
EXEC_STATUS=`echo $?`
MESSAGE=`echo $"Password changed for" $USERNAME.`
if [ $EXEC_STATUS = 102 ]
then
sleep 4
MESSAGE=`echo $"Incorrect username or password supplied for" $USERNAME.`
fi

show_status
