#!/bin/bash
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
#  _JOBTITLE_
#  _FORENAME_
#  _SURNAME_
#  _USERNAME_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
#  _PRIMARYADMIN_
#  _TCPACCESS_
########################
#Language
########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server


echo "Content-type: text/html"
echo ""
echo "<html><head><title>$"Karoshi Web Management - Edit a Karoshi Remote Management User"</title><meta http-equiv='"'REFRESH'"' content='"'0; URL='/cgi-bin/admin/remote_management_view.cgi''"'>"
echo '<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=16
#Assign JOBTITLE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = JOBTITLEcheck ]
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
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = FORENAMEcheck ]
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
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = SURNAMEcheck ]
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
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = USERNAMEcheck ]
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
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = PASSWORD1check ]
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
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = PASSWORD2check ]
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
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = PRIMARYADMINcheck ]
then
let COUNTER=$COUNTER+1
PRIMARYADMIN=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign TCPACCESS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = TCPACCESScheck ]
then
let COUNTER=$COUNTER+1
TCPACCESS=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Check to see that username is not blank
if [ $USERNAME'null' = null ]
then
MESSAGE=$"The username must not be blank."
show_status
fi

#Check to see that password fields are not blank
if [ $PASSWORD1'null' != null ] || [ $PASSWORD2'null' != null ]
then
if [ $PASSWORD1'check' != $PASSWORD2'check' ]
then
MESSAGE=$"The passwords do not match."
show_status
fi
fi

#Check that duplicate data has not been added
if [ $USERNAME'check' = $FORENAME'check' ] || [ $USERNAME'check' = $SURNAME'check' ] || [ $USERNAME'check' = $JOBTITLE'check' ]
then
MESSAGE=$"You have entered duplicate data."
show_status
fi
Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/remote_management_edit.cgi | cut -d' ' -f1`
#add remote management user
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$JOBTITLE:$FORENAME:$SURNAME:$USERNAME:$PASSWORD1:$PRIMARYADMIN:$TCPACCESS" | sudo -H /opt/karoshi/web_controls/exec/remote_management_edit
EXEC_STATUS=`echo $?`
MESSAGE=`echo $USERNAME $"has been edited."`
if [ $EXEC_STATUS = 103 ]
then
MESSAGE=$"You can only do this if you are a primary admin."
fi
if [ $EXEC_STATUS = 102 ]
then
MESSAGE=`echo $USERNAME: $"This user does not exist."`
fi
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $USERNAME: $"There was a problem editing the details for this user."`
fi
show_status
exit
