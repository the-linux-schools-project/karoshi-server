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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/add_user ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/add_user
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=19
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
USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
echo '<script type="text/javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/'$STARTCGI'";'
echo '</script>'
echo "</body></html>"
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
#Check to see that firstname is not blank
if [ $FIRSTNAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that surname is not blank
if [ $SURNAME'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that password fields are not blank
if [ $PASSWORD1'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
if [ $PASSWORD2'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
if [ $GROUP'null' = null ]
then
MESSAGE=$ERRORMSG6
show_status
fi
#Check that password has been entered correctly
if [ $PASSWORD1 != $PASSWORD2 ]
then
MESSAGE=$ERRORMSG4
show_status
fi
#Check that usernamestyle is not blank
if [ $USERNAMESTYLE'null' = null ]
then
MESSAGE=$ERRORMSG7
show_status
fi
#Check that usernamestyle is the correct value
if [ $USERNAMESTYLE != userstyleS1 ] && [ $USERNAMESTYLE != userstyleS2 ] && [ $USERNAMESTYLE != userstyleS3 ] && [ $USERNAMESTYLE != userstyleS4 ] && [ $USERNAMESTYLE != userstyleS5 ] && [ $USERNAMESTYLE != userstyleS6 ] && [ $USERNAMESTYLE != userstyleS7 ] && [ $USERNAMESTYLE != userstyleS8 ] && [ $USERNAMESTYLE != userstyleS9 ]
then
MESSAGE=$ERRORMSG8
show_status
fi
COUNTER=""
#Create username
DUPLICATECHECK=0
function create_username {
source /opt/karoshi/server_network/group_information/$GROUP
if [ $USERNAMESTYLE = userstyleS1 ]
then
USERNAME=`echo ${FIRSTNAME:0:1}$SURNAME$YEARSUFFIX$COUNTER`
fi
if [ $USERNAMESTYLE = userstyleS2 ]
then
USERNAME=`echo $YEARSUFFIX$COUNTER${FIRSTNAME:0:1}$SURNAME`
fi
if [ $USERNAMESTYLE = userstyleS3 ]
then
USERNAME=`echo $SURNAME${FIRSTNAME:0:1}$YEARSUFFIX$COUNTER`
fi
if [ $USERNAMESTYLE = userstyleS4 ]
then
USERNAME=`echo $FIRSTNAME.$SURNAME$YEARSUFFIX$COUNTER`
fi
if [ $USERNAMESTYLE = userstyleS5 ]
then
USERNAME=`echo $SURNAME.$FIRSTNAME$YEARSUFFIX$COUNTER`
fi
if [ $USERNAMESTYLE = userstyleS6 ]
then
USERNAME=`echo $YEARSUFFIX$COUNTER$SURNAME${FIRSTNAME:0:1}`
fi
if [ $USERNAMESTYLE = userstyleS7 ]
then
USERNAME=`echo $YEARSUFFIX$COUNTER$FIRSTNAME${SURNAME:0:1}`
fi
if [ $USERNAMESTYLE = userstyleS8 ]
then
[ $COUNTER'null' = null ] && COUNTER=1
USERNAME=`echo $FIRSTNAME${SURNAME:0:$COUNTER}`
fi
if [ $USERNAMESTYLE = userstyleS9 ]
then
#Check to see that enrolment is not blank
if [ $ENROLLMENTNUMBER'null' = null ]
then
MESSAGE=$ERRORMSG12
show_status
fi
[ $COUNTER'null' = null ] && COUNTER=1
if [ $DUPLICATECHECK = 0 ]
then
USERNAME=`echo $ENROLLMENTNUMBER`
else
USERNAME=`echo $ENROLLMENTNUMBER.$COUNTER`
fi
fi

USERNAME=`echo $USERNAME | tr 'A-Z' 'a-z'`
}

[ $USERNAME'null' = null ] && create_username

#Correct new username if user already exists.
INITUSERNAME=$USERNAME
DUPLICATECHECK=1
ACTIONUSER=0

if [ $USERNAMESTYLE != userstyleS8 ]
then
while [ $DUPLICATECHECK = 1 ]
do
id -u "$USERNAME" 1>/dev/null 2>/dev/null
if [ `echo $?` = 0 ]
then
[ $COUNTER'null' = null ] && COUNTER=1
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
id -u "$USERNAME" 1>/dev/null 2>/dev/null
if [ `echo $?` = 0 ]
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
echo '<form action="/cgi-bin/admin/add_user.cgi" method="post"><div id="'$DIV_ID'">
<input name="_FIRSTNAME_" value="'$FIRSTNAME'" type="hidden">
<input name="_SURNAME_" value="'$SURNAME'" type="hidden">
<input name="_PASSWORD1_" value="'$PASSWORD1'" type="hidden">
<input name="_PASSWORD2_" value="'$PASSWORD2'" type="hidden">
<input name="_GROUP_" value="'$GROUP'" type="hidden">
<input name="_USERNAMESTYLE_" value="'$USERNAMESTYLE'" type="hidden">
<input name="_USERNAME_" value="'$USERNAME'" type="hidden">
<input name="_ENROLLMENTNUMBER_" value="'$ENROLLMENTNUMBER'" type="hidden">

'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE'</b></a></td></tr></tbody></table>'
else
echo '<b>'$TITLE'</b><br><br>'
fi


echo $INITUSERNAME - $ERRORMSG10"<br><br>"$DUPLICATECREATE $USERNAME?
if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi
echo '<input value="'$SUBMITMSG'" type="submit">
</div></form></body></html>'
exit
else
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/add_user.cgi | cut -d' ' -f1`
#Add user
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$FIRSTNAME:$SURNAME:$USERNAME:$PASSWORD1:$GROUP:$USERNAMESTYLE:$ENROLLMENTNUMBER:$REQUESTFILE" | sudo -H /opt/karoshi/web_controls/exec/add_user
EXEC_STATUS=`echo $?`
MESSAGE=`echo $FIRSTNAMEMSG: $FIRSTNAME'\\n'$SURNAMEMSG: $SURNAME'\\n'$USERNAMEMSG: $USERNAME'\\n'$COMPLETEDMSG $GROUP.`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
fi

if [ $EXEC_STATUS = 103 ]
then
MESSAGE=`echo "$MESSAGE" $ENROLLMENTNUMBERERROR`
fi

if [ $EXEC_STATUS = 105 ]
then
MESSAGE=`echo $SERVERDOWNMSG $LOGMSG`
fi

show_status
fi


exit
