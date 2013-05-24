#!/bin/bash
#Reset a user's password
#Copyright (C) 2007 Paul Sharrad
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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk

########################
#Required input variables
########################
#  _MYUSERNAME_  Staff username
#  _MYPASSWORD_  Staff password
#  _USERNAME_  Student username
#  _PASSWORD1_  New password for student
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/change_student_password ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/change_student_password
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################

SLEEPTIME=5

echo "Content-type: text/html"
echo ""
echo "<html><head><title>$TITLE2</title><meta http-equiv='"'REFRESH'"' content='"'0; URL='$HTTP_REFERER''"'><link rel="stylesheet" href="/css/$STYLESHEET"></head><body>"
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
#########################
#Assign data to variables
#########################
END_POINT=8

#Assign USERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
if [ `echo $DATA | cut -s -d'_' -f$COUNTER` = USERNAME ]
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
echo '</script>'
echo "</body></html>"
exit
}

#########################
#Check data
#########################
#Check to see that username is not blank
if [ $USERNAME'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that the member of staff is not restricted
if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
if [ `grep -c -w $MYUSERNAME /opt/karoshi/web_controls/staff_restrictions.txt` -gt 0 ]
then
sudo -H /opt/karoshi/web_controls/exec/record_staff_error $REMOTE_USER:$REMOTE_ADDR:$MYUSERNAME
sleep $SLEEPTIME
MESSAGE=$ERRORMSG10
show_status
fi
fi

#Check to see that the user exists
echo "$MD5SUM:$USERNAME" | sudo -H /opt/karoshi/web_controls/exec/existcheck_user
USEREXISTSTATUS=`echo $?`
if [ $USEREXISTSTATUS != 112 ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see if the user for password change is a student.
echo "$REMOTE_USER:$REMOTE_ADDR:$USERNAME" | sudo -H /opt/karoshi/web_controls/exec/check_student
STUDENTEXITSTATUS=`echo $?`
if [ $STUDENTEXITSTATUS != 111 ]
then
MESSAGE=$ERRORMSG9
show_status
fi

#Check view image tick box
if [ $VIEWIMAGE'check' = yescheck ]
then
echo '<body onload="submitForm()"><form action="/cgi-bin/staff/reset_student_password_fm.cgi" method="post" name="form">'
echo '<input name="_MYUSERNAME_" value="'$MYUSERNAME'" type="hidden">'
echo '<input name="_MYPASSWORD_" value="'$MYPASSWORD'" type="hidden">'
echo '<input name="_USERNAME_" value="'$USERNAME'" type="hidden"></form>'

echo '<SCRIPT LANGUAGE="JavaScript">
function submitForm(){
document.form.submit();
}
</SCRIPT></body></html>'
exit
fi

#Create random password for student
PASSWORD1=`echo $RANDOM`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/staff/reset_student_password.cgi | cut -d' ' -f1`
#Reset student password
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$PASSWORD1:" | sudo -H /opt/karoshi/web_controls/exec/change_student_password
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 0 ]
then
MESSAGE=`echo $USERNAME: $COMPLETEDMSG2 $PASSWORD1.`
else
MESSAGE=`echo $ERRORMSG5 $USERNAME.`
fi
show_status
