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
#  _PRINTACTION_
##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_view_assigned ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_view_assigned
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\_\%-'`
#########################
#Assign data to variables
#########################
END_POINT=3
#Assign PRINTACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRINTACTIONcheck ]
then
let COUNTER=$COUNTER+1
PRINTACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Check to see that PRINTACTION is not blank
if [ $PRINTACTION'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
PRINTACTION=`echo $PRINTACTION | sed 's/%3A/:/g'`

ACTION=`echo $PRINTACTION | cut -d: -f1`
LOCATION=`echo $PRINTACTION | cut -d: -f2`
PRINTER=`echo $PRINTACTION | cut -d: -f3`
#Check to see that ACTION is not blank
if [ $ACTION'null' = null ]
then
MESSAGE=$ERRORMSG9
show_status
fi
#Check to see that LOCATION is not blank
if [ $LOCATION'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that PRINTER is not blank
if [ $PRINTER'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
#Check to see that ACTION is corect
if [ $ACTION != delete ] && [ $ACTION != default ]
then
MESSAGE=$ERRORMSG4
show_status
fi
#Check to see that location.txt exists
if [ ! -f /var/lib/samba/netlogon/locations.txt ]
then
MESSAGE=$ERRORMSG5
show_status
fi

#Check to see that LOCATION exists
if [ `grep -c $LOCATION /var/lib/samba/netlogon/locations.txt` = 0 ]
then
MESSAGE=$ERRORMSG6
show_status
fi

#Check to see that printer.txt exists
if [ ! -f /var/lib/samba/netlogon/printers.txt ]
then
MESSAGE=$ERRORMSG7
show_status
fi

#Check to see that PRINTER queue exits
if [ `grep -c ,$PRINTER,` /var/lib/samba/netlogon/printers.txt = 0 ]
then
MESSAGE=$ERRORMSG8
show_status
fi
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers_view_assigned.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/printers_view_assigned $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$LOCATION:$PRINTER
if [ `echo $?` = 101 ]
then
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
show_status
fi
exit
