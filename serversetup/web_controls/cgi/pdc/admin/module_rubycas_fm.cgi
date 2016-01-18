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
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

if [ -f /opt/karoshi/server_network/moodledomain ]
then
SUGGGESTDOMAIN=`sed -n 1,1p /opt/karoshi/server_network/moodledomain`
else
SUGGGESTDOMAIN=www.elearning.myschool.com
fi
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Set up Ruby CAS Authentication"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign SERVERNAME

COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
then
let COUNTER=$COUNTER+1
SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi"'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Check data
#########################
#Check to see that servername is not blank
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$"The server cannot be blank."
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/module_rubycas.cgi" method="post"><div id="actionbox"><b>'$"Set up Ruby CAS Authentication"' - '$SERVERNAME'</b><br><br>
<b>'$"Description"'</b><br><br>
'$"This will setup up the CAS single sign on solution."'<br><br>'$"WARNING - An internet connect is required to install this module."'<br><br>
<input name="_SERVERNAME_" value="'$SERVERNAME'" type="hidden">
'


SHOW_LDAP=yes
if [ $SERVERNAME = `hostname-fqdn` ]
then
SHOW_LDAP=no
fi
if [ -f /opt/karoshi/server_network/slave_ldap_servers/$SERVERNAME ]
then
SHOW_LDAP=no
fi
if [ -f /opt/karoshi/server_network/ldap_clients/$SERVERNAME ]
then
SHOW_LDAP=no
fi


if [ $SHOW_LDAP = yes ]
then
echo '<b>'$"Parameters"'</b><br><br>
<table class="standard" style="text-align: left; height: 15px;" ><tbody>
<tr><td style="width: 180px;">'$LDAPSERVERMSG1'</td><td>'
#Generate list of ldap servers for authentication
echo '<select name="_LDAPSERVER_">
<option value="">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </option>
<option value="'$HOSTNAME'">'$LDAPSERVERMSG2 : $HOSTNAME'</option>
<option value="slaveldapserver">'$LDAPSERVERMSG3'</option>
'

if [ -d /opt/karoshi/server_network/slave_ldap_servers ]
then
if [ `ls -1 /opt/karoshi/server_network/slave_ldap_servers | wc -l` -gt 0 ]
then
for LDAPSERVER in /opt/karoshi/server_network/slave_ldap_servers/*
do
LDAPSERVER=`basename $LDAPSERVER`
echo '<option>'$LDAPSERVER'</option>'
done
fi
fi
echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$LDAPSERVERHELP'</span></a></td></tr></tbody></table>'
else
echo '<input name="_LDAPSERVER_" value="noldap" type="hidden">'
fi

echo '<br><br></div><div id="submitbox"><input value="'$"Submit"'" class="button" type="submit"></div></form></div></body></html>'
exit
