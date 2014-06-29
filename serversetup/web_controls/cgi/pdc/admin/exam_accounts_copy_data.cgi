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
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/exam_accounts_copy_data ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/exam_accounts_copy_data
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><meta http-equiv="REFRESH" content="0; URL=/cgi-bin/admin/exam_accounts_upload_fm.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=9
#Assign EXAMSTART
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = EXAMSTARTcheck ]
then
let COUNTER=$COUNTER+1
EXAMSTART=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign EXAMEND
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = EXAMENDcheck ]
then
let COUNTER=$COUNTER+1
EXAMEND=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign ALL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ALLcheck ]
then
let COUNTER=$COUNTER+1
ALL=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign READONLY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = READONLYcheck ]
then
let COUNTER=$COUNTER+1
READONLY=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Check to see that all fields are not blank
if [ $EXAMSTART'null' = null ] || [ $EXAMEND'null' = null ]
then
if [ $ALL'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
fi
#Check that data is numbers
if [ `echo $EXAMSTART | grep -c [^0-9.' ']` != 0 ] || [ `echo $EXAMEND | grep -c [^0-9.' ']` != 0 ]
then
MESSAGE=$ERRORMSG4
show_status
fi
#Check that numbers are within range of exam accounts
if [ $ALL'check' != all'check' ]
then
if [ $EXAMSTART -gt $EXAMEND ] || [ $EXAMSTART -le 0 ]
then
MESSAGE=`echo $ERRORMSG6 $ERRORMSG7':' $EXAMACCOUNTS`
show_status
fi
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><div class="sectiontitle">'$TITLE2'</div><br>'
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/exam_accounts_copy_data.cgi | cut -d' ' -f1`
#Copy data to exam accounts

########################
#Check to see if any tar.gz or.zip files have been uploaded and extract them
########################

ZIPFILES=( `ls /var/www/karoshi/exam_upload/*.zip 2>/dev/null` )

ZIPFILECOUNT=${#ZIPFILES[@]}
COUNTER=0
while [ $COUNTER -lt $ZIPFILECOUNT ]
do
echo "<b>"$EXTRACTMSG ${ZIPFILES[$COUNTER]}"</b><br><br>"
cd /var/www/karoshi/exam_upload 
[ -f ${ZIPFILES[$COUNTER]} ] && unzip ${ZIPFILES[$COUNTER]} 1>/dev/null
[ -f ${ZIPFILES[$COUNTER]} ] && rm -f ${ZIPFILES[$COUNTER]}
let COUNTER=$COUNTER+1 
done

TARFILES=( `ls /var/www/karoshi/exam_upload/*.tar.gz 2>/dev/null` )

TARFILECOUNT=${#TARFILES[@]}

COUNTER=0
while [ $COUNTER -lt $TARFILECOUNT ]
do
echo "<b>"$EXTRACTMSG ${TARFILES[$COUNTER]}"</b><br><br>"
cd /var/www/karoshi/exam_upload 
[ -f ${TARFILES[$COUNTER]} ] && tar xzf ${TARFILES[$COUNTER]}
[ -f ${TARFILES[$COUNTER]} ] && rm -f ${TARFILES[$COUNTER]}
let COUNTER=$COUNTER+1 
done

sudo -H /opt/karoshi/web_controls/exec/exam_accounts_copy_data $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$EXAMSTART:$EXAMEND:$ALL:$READONLY:
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 0 ]
then
if [ $ALL'check' = all'check' ]
then
MESSAGE=`echo $COMPLETEDMSG1`
else
MESSAGE=`echo $COMPLETEDMSG2: exam$EXAMSTART - exam$EXAMEND`
fi
else
MESSAGE=`echo $ERRORMSG5`
fi
show_status
exit
