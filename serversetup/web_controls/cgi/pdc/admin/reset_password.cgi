#!/bin/bash
#Reset a user's password
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

#Language
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/change_password ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/change_password
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
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
if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
then
let COUNTER=$COUNTER+1
USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/reset_password_fm.cgi"'
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
#Check to see that username is not blank
if [ $USERNAME'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Dont change passwords for certain users
if [ $USERNAME = karoshi ] || [ $USERNAME = root ]
then
MESSAGE=$ERRORMSG8
show_status
fi

#Check to see that the user exists
echo "$MD5SUM:$USERNAME" | sudo -H /opt/karoshi/web_controls/exec/existcheck_user
USEREXISTSTATUS=`echo $?`
if [ $USEREXISTSTATUS = 111 ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Check view image tick box
if [ $VIEWIMAGE'check' = yescheck ]
then
echo '<body onload="submitForm()"><div id="pagecontainer"><form action="/cgi-bin/admin/reset_password_fm.cgi" method="post" name="form">'
echo '<input name="_USERNAME_" value="'$USERNAME'" type="hidden">'
echo '<input name="_DOMAINPASSWORD_" value="'$DOMAINPASSWORD'" type="hidden"></form>'

echo '<SCRIPT LANGUAGE="JavaScript">
function submitForm(){
document.form.submit();
}
</SCRIPT></div></body></html>'
exit
fi

#Check to see that the user is not in acceptable use category
if [ -f /opt/karoshi/acceptable_use_authorisations/pending/$USERNAME ]
then
#Check to see how many days of trial are left
GRACE_TIME=`sed -n 1,1p /opt/karoshi/acceptable_use_authorisations/pending/$USERNAME | tr -cd 0-9`
[ $GRACE_TIME'null' = null ] && GRACE_TIME=0
if [ $GRACE_TIME = 0 ]
then
MESSAGE=`echo $USERNAME - $ERRORMSG12`
show_status
fi
fi

##########################
#Generate Password
##########################
PASSWORD1=`echo $RANDOM`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/reset_password.cgi | cut -d' ' -f1`
#reset password
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$PASSWORD1" | sudo -H /opt/karoshi/web_controls/exec/reset_password
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 0 ]
then
MESSAGE=`echo $USERNAME: $COMPLETEDMSG2 $PASSWORD1`
else
MESSAGE=`echo $ERRORMSG6 $USERNAME`
fi
if [ $EXEC_STATUS = 102 ]
then
MESSAGE=`echo $USERNAME - $ERRORMSG13.`
fi
show_status
exit
