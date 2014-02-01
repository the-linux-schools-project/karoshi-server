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
#  _JOBTITLE_
#  _FORENAME_
#  _SURNAME_
#  _USERNAME_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
#  _PRIMARYADMIN_
#  _TCPACCESS_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/remote_management_add ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/remote_management_add
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._: \-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%/+-'`
#########################
#Assign data to variables
#########################
END_POINT=16
#Assign JOBTITLE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = JOBTITLEcheck ]
then
let COUNTER=$COUNTER+1
JOBTITLE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign FORENAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = FORENAMEcheck ]
then
let COUNTER=$COUNTER+1
FORENAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Assign PRIMARYADMIN
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRIMARYADMINcheck ]
then
let COUNTER=$COUNTER+1
PRIMARYADMIN=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign TCPACCESS
#COUNTER=2
#while [ $COUNTER -le $END_POINT ]
#do
#if [ `echo $DATA | cut -s -d'_' -f$COUNTER` = TCPACCESS ]
#then
#let COUNTER=$COUNTER+1
#TCPACCESS=`echo $DATA | cut -s -d'_' -f$COUNTER`
#break
#fi
#let COUNTER=$COUNTER+1
#done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "remote_management_add_fm.cgi"'
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
#Check that password has been entered correctly
if [ $PASSWORD1 != $PASSWORD2 ]
then
MESSAGE=$ERRORMSG4
show_status
fi
# Check that PRIMARYADMIN is not blank
if [ $PRIMARYADMIN'null' = null ]
then
MESSAGE=$ERRORMSG8
show_status
fi
#Check that primary admin has the correct data
if [ $PRIMARYADMIN != 1 ] && [ $PRIMARYADMIN != 2 ] && [ $PRIMARYADMIN != 3 ]
then
MESSAGE=$ERRORMSG9
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo "<div id="actionbox">"
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/remote_management_add.cgi | cut -d' ' -f1`
#add remote management user
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$JOBTITLE:$FORENAME:$SURNAME:$USERNAME:$PASSWORD1:$PRIMARYADMIN:$TCPACCESS" | sudo -H /opt/karoshi/web_controls/exec/remote_management_add

EXEC_STATUS=`echo $?`
MESSAGE=`echo $USERNAME $COMPLETEDMSG`
if [ $EXEC_STATUS = 103 ]
then
MESSAGE=$ERRORMSG6
fi
if [ $EXEC_STATUS = 102 ]
then
MESSAGE=`echo $USERNAME: $ERRORMSG1`
fi
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $USERNAME: $ERRORMSG5`
fi
echo "</div>"
show_status
echo "</div></body></html>"
exit
