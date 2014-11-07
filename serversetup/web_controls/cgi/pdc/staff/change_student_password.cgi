#!/bin/bash
#Change a user's password
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
#jsharrad@karoshi.org.uk

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

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
############################
#Show page
############################

SLEEPTIME=5

echo "Content-type: text/html"
echo ""
echo '<html><head><title>'$"Change a Student's Password"'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+-'`
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
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '</script>'
echo "</div></body></html>"
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


#Check to see that the member of staff is not restricted
if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
	if [ `grep -c -w $MYUSERNAME /opt/karoshi/web_controls/staff_restrictions.txt` -gt 0 ]
	then
		sudo -H /opt/karoshi/web_controls/exec/record_staff_error $REMOTE_USER:$REMOTE_ADDR:$MYUSERNAME
		sleep $SLEEPTIME
		MESSAGE=$"Authentication failure."
		show_status
	fi
fi

#Check to see that the user exists
echo "$MD5SUM:$USERNAME" | sudo -H /opt/karoshi/web_controls/exec/existcheck_user
USEREXISTSTATUS=`echo $?`
if [ $USEREXISTSTATUS != 112 ]
then
	MESSAGE=$"The username does not exist."
	show_status
fi
#Check to see if the user for password change is a student.
echo "$REMOTE_USER:$REMOTE_ADDR:$USERNAME" | sudo -H /opt/karoshi/web_controls/exec/check_student
STUDENTEXITSTATUS=`echo $?`
if [ $STUDENTEXITSTATUS != 111 ]
then
	MESSAGE=$"You can only change passwords for students."
	show_status
fi

#Check view image tick box
if [ $VIEWIMAGE'check' = yescheck ]
then
	echo '<body onload="submitForm()"><div id="pagecontainer"><form action="/cgi-bin/staff/change_student_password_fm.cgi" method="post" name="form">'
	echo '<input name="_MYUSERNAME_" value="'$MYUSERNAME'" type="hidden">'
	echo '<input name="_MYPASSWORD_" value="'$MYPASSWORD'" type="hidden">'
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
if [ -f /opt/karoshi/acceptable_use_authorisations/pending/$USERNAME ]
then
	#Check to see how many days of trial are left
	GRACE_TIME=`sed -n 1,1p /opt/karoshi/acceptable_use_authorisations/pending/$USERNAME cut -d, -f1 | tr -cd 0-9`
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
if [ "$PASSWORD1" != "$PASSWORD2" ]
then
	MESSAGE=$"The passwords do not match."
	show_status
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/staff/change_student_password.cgi | cut -d' ' -f1`
#Change student password
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$PASSWORD1:" | sudo -H /opt/karoshi/web_controls/exec/change_student_password
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 0 ]
then
	MESSAGE=`echo $"Password changed for" $USERNAME.`
else
	MESSAGE=`echo $"The password was not changed for" $USERNAME.`
fi
show_status
exit
