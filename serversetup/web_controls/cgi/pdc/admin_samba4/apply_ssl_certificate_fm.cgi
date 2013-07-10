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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/apply_ssl_certificate ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/apply_ssl_certificate
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi

SERVERICON="/images/submenus/system/computer.png"
source /opt/karoshi/server_network/domain_information/domain_name
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body onLoad="start()">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/apply_ssl_certificate.cgi" name="selectservers" method="post"><b></b>
  <div id="actionbox"><b>'$TITLE'</b>
  <br>
  <br><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 90px;"><b>Server</b></td><td style="width: 180px;"><b>Alias</b></td></tr>
<tr><td>'$HOSTNAME'</td><td>manage.'$REALM'</td><td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_ALIAS_manage_" type="image" class="images" src="'$SERVERICON'" value=""><span>Web Management</td></tr>'

#Show all aliases that have been setup

if [ -d /opt/karoshi/server_network/aliases ]
then
if [ `ls -1 /opt/karoshi/server_network/aliases | wc -l` -gt 0 ]
then
for ALIASES in /opt/karoshi/server_network/aliases/*
do
SERVER=`basename $ALIASES`
ALIAS=`sed -n 1,1p /opt/karoshi/server_network/aliases/$SERVER`

echo '<tr><td>'$SERVER'</td><td>'$ALIAS.$REALM'</td><td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVER_'$SERVER'_ALIAS_'$ALIAS'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$ALIAS.$REALM'</td></tr>'
done
echo '</tbody></table>'
fi
fi
exit

