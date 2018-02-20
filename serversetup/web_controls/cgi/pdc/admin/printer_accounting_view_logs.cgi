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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server



#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign LOGTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LOGTYPEcheck ]
then
let COUNTER=$COUNTER+1
LOGTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done


##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Printer Quota Logs"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body><div id="pagecontainer">'


function show_status {
echo '<script>'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/printer_accounting_view_logs_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
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
#Check to see that LOGTYPE is not blank
if [ $LOGTYPE'null' = null ]
then
MESSAGE=$"The name cannot be blank."
show_status
fi


#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
fi
echo '<div id="'$DIV_ID'">'
echo '<b>'$"View Printer Quota Logs"'</b><br><br>'
Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/printer_accounting_view_logs.cgi | cut -d' ' -f1`
#View printer logs
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$LOGTYPE:" | sudo -H /opt/karoshi/web_controls/exec/printer_accounting_view_logs
echo '</div></div></body></html>'
exit
