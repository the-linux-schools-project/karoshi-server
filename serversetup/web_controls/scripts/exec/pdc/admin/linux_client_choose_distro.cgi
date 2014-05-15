#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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

##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_upload_distro ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_upload_distro
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`echo $DATA | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=9
#Assign DISTROCHOICE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DISTROCHOICEcheck ]
then
let COUNTER=$COUNTER+1
DISTROCHOICE=`echo $DATA | cut -s -d'_' -f$COUNTER`
DISTROCHOICE=`echo $DISTROCHOICE | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign CONTROL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CONTROLcheck ]
then
let COUNTER=$COUNTER+1
CONTROL=`echo $DATA | cut -s -d'_' -f$COUNTER`
CONTROL=`echo $CONTROL | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<script type="text/javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/linux_client_choose_distro_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function completed {
echo '<script type="text/javascript">'
echo 'window.location = "/cgi-bin/admin/linux_client_choose_distro_fm.cgi";'
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
#Check to see that DISTROCHOICE is not blank
if [ $DISTROCHOICE'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">
<div class="sectiontitle">'$TITLE2'</div><br>'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/linux_client_choose_distro.cgi | cut -d' ' -f1`
#Copy iso
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$DISTROCHOICE:$CONTROL:" | sudo -H /opt/karoshi/web_controls/exec/linux_client_choose_distro2
EXEC_STATUS=`echo $?`

if [ $CONTROL = copy ]
then
MESSAGE="$COMPLETEDMSG2"
else
MESSAGE="$DISTROCHOICE - $DELETEDMSG"
fi

if [ $EXEC_STATUS != 0 ]
then
MESSAGE=`echo $ERRORMSG3`
fi

completed
echo "</div>/body></html>"
exit
