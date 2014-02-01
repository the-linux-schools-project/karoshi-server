#!/bin/bash
#Copyright (C) 2010 Paul Sharrad

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
#  _SERVER_
#  _CACERT_
#  _SSLCERT_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/ssl_certs ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/ssl_certs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:/\-%+' | sed 's/___/TRIPLESCORED/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLESCORED/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=12
#Assign SERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERcheck ]
then
let COUNTER=$COUNTER+1
SERVER=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign CERTTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CERTTYPEcheck ]
then
let COUNTER=$COUNTER+1
CERTTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign CACERT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CACERTcheck ]
then
let COUNTER=$COUNTER+1
CACERT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign SSLCERT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SSLCERTcheck ]
then
let COUNTER=$COUNTER+1
SSLCERT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done



function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/ssl_certs_commercial_fm.cgi";'
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
#Check to see that SERVER is not blank
if [ $SERVER'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Check to see that CERTTYPE is not blank
if [ $CERTTYPE'null' = null ]
then
MESSAGE=$ERRORMSG17
show_status
fi


#Check to see that CACERT is not blank
if [ $CACERT'null' = null ]
then
MESSAGE=$ERRORMSG15
show_status
fi

#Check to see that SSLCERT is not blank
if [ $SSLCERT'null' = null ]
then
MESSAGE=$ERRORMSG16
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/ssl_certs_commercial_install2.cgi | cut -d' ' -f1`

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">'

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVER:$CERTTYPE:$CACERT:$SSLCERT:" | sudo -H /opt/karoshi/web_controls/exec/ssl_certs_commercial_install

STATUS=`echo $?`
if [ $STATUS = 101 ]
then
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
show_status
fi
MESSAGE=`echo $SERVER - $COMPLETEDMSG`
show_status
exit
