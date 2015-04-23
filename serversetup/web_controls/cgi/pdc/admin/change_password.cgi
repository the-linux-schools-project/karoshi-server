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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Change a User Password"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=12
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

#Assign _VIEWIMAGE_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = VIEWIMAGEcheck ]
	then
		let COUNTER=$COUNTER+1
		VIEWIMAGE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/change_password_fm.cgi"
</script>
</div></body></html>'
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
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/change_password.cgi | cut -d' ' -f1`
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
USEREXISTSTATUS=`echo $?`
if [ $USEREXISTSTATUS != 0 ]
then
	MESSAGE=$"This username does not exist."
	show_status
fi

#Dont change passwords for certain users
if [ $USERNAME = karoshi ] || [ $USERNAME = root ]
then
	MESSAGE=$"You can not change the password for this user."
	show_status
fi

#Check view image tick box
if [ $VIEWIMAGE'check' = yescheck ]
then
echo '<body onload="submitForm()"><div id="pagecontainer"><form action="/cgi-bin/admin/change_password_fm.cgi" method="post" name="form">'
echo '<input name="_USERNAME_" value="'$USERNAME'" type="hidden">'
echo '<input name="_PASSWORD1_" value="'$PASSWORD1'" type="hidden">'
echo '<input name="_PASSWORD2_" value="'$PASSWORD2'" type="hidden"></form>'

echo '<SCRIPT LANGUAGE="JavaScript">
function submitForm(){
document.form.submit();
}
</SCRIPT></div></body></html>'
exit
fi

#Check to see that the user is not in acceptable use category
if [ -f /opt/karoshi/server_network/acceptable_use_authorisations/pending/$USERNAME ]
then
	#Check to see how many days of trial are left
	GRACE_TIME=`sed -n 1,1p /opt/karoshi/server_network/acceptable_use_authorisations/pending/$USERNAME | cut -d, -f1 | tr -cd 0-9`
	[ -z "$GRACE_TIME" ] && GRACE_TIME=0
	if [ $GRACE_TIME = 0 ]
	then
		MESSAGE=`echo $USERNAME - $"This user has not signed an acceptable use policy and their account has now been suspended."`
		show_status
	fi
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
#Check that password has been entered correctly
if [ $PASSWORD1 != $PASSWORD2 ]
then
	MESSAGE=$"The passwords do not match."
	show_status
fi

#Check that there are no spaces in the password
#if [ `echo $PASSWORD1 | grep -c +` != 0 ]
#then
#MESSAGE=$"The password was not reset for"
#show_status
#fi

#Change password
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$PASSWORD1" | sudo -H /opt/karoshi/web_controls/exec/change_password
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 0 ]
then
	MESSAGE=`echo $"Password changed for" $USERNAME.`
else
	MESSAGE=`echo $"The password was not changed for" $USERNAME.`
fi
if [ $EXEC_STATUS = 102 ]
then
	MESSAGE=`echo $USERNAME - $"This user account has been suspended."`
fi
show_status
exit
