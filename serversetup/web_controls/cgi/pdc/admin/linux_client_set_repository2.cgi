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
#  ___LINUXVERSION___
#  ___SOFTWARE___
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Linux Client set repository"'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\%+-'`
#Convert underscores
DATA=`echo $DATA | sed 's/___/tripleunderscore/g' | sed 's/_/underscore/g' | sed 's/tripleunderscore/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=10
#Assign LINUXVERSION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LINUXVERSIONcheck ]
then
let COUNTER=$COUNTER+1
LINUXVERSION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _URI_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = URIcheck ]
then
let COUNTER=$COUNTER+1
URI=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/underscore/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _DISTRIBUTION_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DISTRIBUTIONcheck ]
then
let COUNTER=$COUNTER+1
DISTRIBUTION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/underscore/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _SECTIONS_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SECTIONScheck ]
then
let COUNTER=$COUNTER+1
SECTIONS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/underscore/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _LINUXVERSION_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LINUXVERSIONcheck ]
then
let COUNTER=$COUNTER+1
LINUXVERSION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/underscore/_/g'`
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
#Check to see that LINUXVERSION is not blank
if [ $LINUXVERSION'null' = null ]
then
MESSAGE=$"The linux version must not be blank."
show_status
fi
URI
#Check to see that URI is not blank
if [ $URI'null' = null ]
then
MESSAGE=$"The URI cannot be blank."
show_status
fi
#Check to see that DISTRIBUTION is not blank
if [ $DISTRIBUTION'null' = null ]
then
MESSAGE=$"The distribution cannot be blank."
show_status
fi
#Check to see that SECTIONS is not blank
if [ $SECTIONS'null' = null ]
then
MESSAGE=$"There was a problem setting the repository. Please check the Karoshi web management logs."
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/linux_client_set_repository2.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/linux_client_set_repository $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$LINUXVERSION:$URI:$DISTRIBUTION:$SECTIONS
SOFTWARESTATUS=`echo $?`
MESSAGE=`echo $LINUXVERSION: $COMPLETEDMSG`
if [ $SOFTWARESTATUS = 101 ]
then
MESSAGE=$"There was a problem setting the repository. Please check the Karoshi web management logs."
fi
if [ $SOFTWARESTATUS = 102 ]
then
MESSAGE=$"There was a problem setting the repository. Please check the Karoshi web management logs."
fi
show_status
exit

