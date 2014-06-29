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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printer_accounting ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printer_accounting
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all

TYPE=group

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=9
#Assign NAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = NAMEcheck ]
then
let COUNTER=$COUNTER+1
NAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign TYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TYPEcheck ]
then
let COUNTER=$COUNTER+1
TYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign LIMIT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LIMITcheck ]
then
let COUNTER=$COUNTER+1
LIMIT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

[ $TYPE = group ] && STARTPAGE=printer_accounting_group_limits_fm.cgi
[ $TYPE = user ] && STARTPAGE=printer_accounting_user_limits_fm.cgi
[ $TYPE = userdelete ] && STARTPAGE=printer_accounting_user_limits_fm.cgi
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE3'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><meta http-equiv="REFRESH" content="0;url='$STARTPAGE'"></head><body><div id="pagecontainer">'


function show_status {
echo '<script type="text/javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/'$STARTPAGE'";'
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
#Check to see that NAME is not blank
if [ $NAME'null' = null ]
then
MESSAGE=$ERRORMSG7
show_status
fi
#Check to see that TYPE is not blank
if [ $TYPE'null' = null ]
then
MESSAGE=$ERRORMSG6
show_status
fi
#Check to see that LIMIT is not blank
if [ $LIMIT'null' = null ]
then
MESSAGE=$ERRORMSG5
show_status
fi


#Check that user exists
if [ $TYPE = user ]
then
getent passwd $NAME 1>/dev/null
if [ `echo $?` != 0 ]
then
MESSAGE=$ERRORMSG10
show_status
fi
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
DIV_ID=menubox
fi
echo '<div id="'$DIV_ID'">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printer_accounting_edit_limits.cgi | cut -d' ' -f1`
#Change Printer status
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$NAME:$TYPE:$LIMIT:" | sudo -H /opt/karoshi/web_controls/exec/printer_accounting_edit_limits
echo '</div></div></body></html>'
exit
