#!/bin/bash
#Wireless_add_zone
#Copyright (C) 2009 Paul Sharrad

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
#  _USERNAME_

#Language
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/wireless_add_zone ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/wireless_add_zone
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`

#########################
#Assign data to variables
#########################
END_POINT=7

#Assign CLIENTNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CLIENTNAMEcheck ]
then
let COUNTER=$COUNTER+1
CLIENTNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd 'A-Za-z0-9_\-+'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign TCPIP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPIPcheck ]
then
let COUNTER=$COUNTER+1
TCPIP=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9\./%'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign WPAKEY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = WPAKEYcheck ]
then
let COUNTER=$COUNTER+1
WPAKEY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/wireless_add_zone_fm.cgi"'
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

if [ $CLIENTNAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

if [ $TCPIP'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

##########################
#Generate Key if WPAKEY is blank
##########################
if [ $WPAKEY'null' = null ]
then
ALPHABET=( A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 )
ARRAYCOUNT=${#ALPHABET[@]}
COUNTER=0
while [ $COUNTER -lt 63 ]
do
RANDCOUNTER=$[ ( $RANDOM % $ARRAYCOUNT ) ]
CHOICE=${ALPHABET[$RANDCOUNTER]}
WPAKEY=`echo $WPAKEY$CHOICE`
let COUNTER=$COUNTER+1
done
fi

#Check key length
if [ `echo $WPAKEY | wc -c` -le 10 ]
then
MESSAGE=$ERRORMSG3
show_status
fi

if [ `echo $WPAKEY | wc -c` -gt 64 ]
then
MESSAGE=$ERRORMSG4
show_status
fi



#set wpakey
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/wireless_add_zone.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$CLIENTNAME:$TCPIP:$WPAKEY:" | sudo -H /opt/karoshi/web_controls/exec/wireless_add_zone
if [ `echo $?` = 101 ]
then
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
else
MESSAGE=`echo $WPAKEY '\n\n' $COMPLETEDMSG`
fi
show_status
exit
