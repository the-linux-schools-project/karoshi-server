#!/bin/bash
#

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
##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_media_controls ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_media_controls
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
ERRORMSG1="NO VAL 1"
ERRORMSG2="NO VAL 2"
ERRORMSG3="NO VAL 3"
#########################
#Assign data to variables
#########################
END_POINT=9
#Assign MEDIAFILTER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MEDIAFILTERcheck ]
then
let COUNTER=$COUNTER+1
MEDIAFILTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign GROUP
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
#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
then
let COUNTER=$COUNTER+1
ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done



function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/dg_media_controls_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
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
#Check to see that MEDIAFILTER is not blank
if [ $MEDIAFILTER'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that GROUP is not blank
if [ $GROUP'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that ACTION is not blank
if [ $ACTION'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi


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
DIV_ID=navbar
/opt/karoshi/web_controls/generate_navbar_admin_mobile
fi

echo '<div id="'$DIV_ID'">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/dg_media_controls.cgi | cut -d' ' -f1`

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MEDIAFILTER:$GROUP:$ACTION" | sudo -H /opt/karoshi/web_controls/exec/dg_media_controls
EXEC_STATUS=`echo $?`
MESSAGE=`echo $USERNAME: $COMPLETEDMSG $GROUP.`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
fi

if [ $EXEC_STATUS = 103 ]
then
MESSAGE=`echo $MESSAGE $ENROLLMENTNUMBERERROR`
echo "ERROR"
fi

MESSAGE="Media status updated"
show_status
exit
