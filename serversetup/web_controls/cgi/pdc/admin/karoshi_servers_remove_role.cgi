#!/bin/bash
#Copyright (C) 2010  Paul Sharrad

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

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Add Server Role"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><meta http-equiv="REFRESH" content="0;url=/cgi-bin/admin/karoshi_servers_view.cgi"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=17
#Assign MODULE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MODULEcheck ]
then
let COUNTER=$COUNTER+1
MODULE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
then
let COUNTER=$COUNTER+1
SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign FORMCODE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = FORMCODEcheck ]
then
let COUNTER=$COUNTER+1
FORMCODE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign MODULECODE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MODULECODEcheck ]
then
let COUNTER=$COUNTER+1
MODULECODE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi";'
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
#Check to see that SERVERNAME is not blank
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$"The servername cannot be blank."
show_status
fi
#Check to see that MODULE is not blank
if [ $MODULE'null' = null ]
then
MESSAGE=$"The module cannot be blank."
show_status
fi
#Check to see that FORMCODE is not blank
if [ $FORMCODE'null' = null ]
then
MESSAGE=$"The code cannot be blank."
show_status
fi
if [ $MODULECODE'null' = null ]
then
MESSAGE=$"The code cannot be blank."
show_status
fi

if [ $MODULECODE != $FORMCODE ]
then
MESSAGE=$"The code did not match."
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><b>'$"Remove Server Role"' - '$SERVERNAME'</b><br><br>'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/karoshi_servers_remove_role.cgi | cut -d' ' -f1`
#Remove module
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$MODULE:" | sudo -H /opt/karoshi/web_controls/exec/karoshi_servers_remove_role
echo '</div></div></body></html>'

