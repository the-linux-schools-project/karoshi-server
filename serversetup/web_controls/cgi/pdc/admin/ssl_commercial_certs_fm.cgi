#!/bin/bash
#Copyright (C) 2014  Paul Sharrad

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

source /opt/karoshi/server_network/domain_information/domain_name
source /opt/karoshi/web_controls/version
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

<!DOCTYPE html>
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Commercial SSL Certificates"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
</head><body onLoad="start()"><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=8
#Assign SERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERcheck ]
then
let COUNTER=$COUNTER+1
SERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

[ $SERVER'null' = null ] && SERVER=notset

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

############################
#Stage 1 - Create server key and server.crt
############################

echo '
<form action="/cgi-bin/admin/ssl_commercial_certs.cgi" name="selectservers" method="post">
<div id="actionbox3"><div id="titlebox"><table class="standard" style="text-align: left;" ><tbody><tr>
<td style="vertical-align: top;"><div class="sectiontitle">'$"Create Commercial Certificate"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Commercial_SSL_Certificate"><img class="images" alt="" src="/images/help/info.png"><span>'$"This is a three stage process to create and install a commercial SSL certificate for your domain."'</span></a></td></tr></tbody></table>
<br></div><div id="infobox">'
MOBILE=no

#Show step 1

echo '<table class="standard" style="text-align: left;" >
<tbody>
<tr><td style="width: 180px;">'$"Step"' 1</td><td><input name="___SERVERNAME___'$REALM'___SERVERTYPE___network___SERVERMASTER___notset___ACTION___getcertdetails___" type="submit" class="button" value="'$"Create Certificate"'"></td></tr>
'

if [ -f /opt/karoshi/server_network/ssl/commercial_ssl_certs/$REALM ]
then
echo '
<tr><td style="width: 180px;">'$"Step"' 2</td><td><input name="___SERVERNAME___'$REALM'___SERVERTYPE___network___SERVERMASTER___notset___ACTION___copycertinfo___" type="submit" class="button" value="'$"Copy Certificate"'"></td></tr>
<tr><td style="width: 180px;">'$"Step"' 3</td><td>'$"Install certificate"'</td></tr>
'
fi

echo '</tbody></table><br><br>'

if [ -f /opt/karoshi/server_network/ssl/commercial_ssl_certs/$REALM ]
then
#Show list of servers
/opt/karoshi/web_controls/show_servers $MOBILE servers $"Install certificate" getinstallcertinfo no ___
fi

echo '</div></div></form></div></body></html>'
exit
