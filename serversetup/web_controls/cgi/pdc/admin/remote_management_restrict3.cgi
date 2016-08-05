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
#  _TCPADDRESS_
#  _TCPCOMMENT_
#  _CURRENTTCPIP_
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Restrict access to Karoshi Remote Management"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\%+-'`
#########################
#Assign data to variables
#########################
END_POINT=10
#Assign _TCPADDRESS_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPADDRESScheck ]
then
let COUNTER=$COUNTER+1
TCPADDRESS=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _TCPCOMMENT_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPCOMMENTcheck ]
then
let COUNTER=$COUNTER+1
TCPCOMMENT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _CURRENTTCPIP_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CURRENTTCPIPcheck ]
then
let COUNTER=$COUNTER+1
CURRENTTCPIP=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _ADMINLEVEL_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ADMINLEVELcheck ]
then
let COUNTER=$COUNTER+1
ADMINLEVEL=`echo $DATA | cut -s -d'_' -f$COUNTER`
ADMINLEVEL=`echo $ADMINLEVEL | sed 's/%2B/+/g'`
break
fi
let COUNTER=$COUNTER+1
done

function view_tcpip {
echo '<SCRIPT language="Javascript">'
echo '                window.location = "/cgi-bin/admin/remote_management_restrict.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/remote_management_restrict.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
MESSAGE=$"You must access this page via https."
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
if [ $TCPADDRESS'null' = null ]
then
MESSAGE=$"The Action must not be blank."
show_status
fi
if [ $CURRENTTCPIP'null' = null ]
then
MESSAGE=$"The Action must not be blank."
show_status
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo "<div id="actionbox">"
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/remote_management_restrict3.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/remote_management_restrict $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:remove:$CURRENTTCPIP::$ADMINLEVEL
sudo -H /opt/karoshi/web_controls/exec/remote_management_restrict $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:add:$TCPADDRESS:$TCPCOMMENT:$ADMINLEVEL
echo "</div>"
view_tcpip
echo "</div></body></html>"
exit
