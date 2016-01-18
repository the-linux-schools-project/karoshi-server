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
  <title>'$"Add Windows Server"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script>
</head><body onLoad="start()"><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-' | sed 's/__/_ _/g'`
ASKIP=no


#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/windows_servers_add.cgi" method="post"><div id="actionbox"><b>'$"Add Windows Server"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will add the details required to remotely run commands on a windows server."'</span></a>
<br><br>
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">'$"Server name"'</td><td><input tabindex= "1" name="_SERVERNAME_" size="23" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name of the windows server you want to add."'</span></a></td></tr>
<tr><td style="width: 180px;">'$"TCPIP number"'</td><td><input tabindex= "2" maxlength="15" name="_TCPIPNUMBER_" size="23" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the tcpip number of the server you want to add."'</span></a></td></tr>
<tr><td>'$"Administrator user"'</td><td><input tabindex= "3" name="_ADMINUSER_" size="23" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the administrator password. If you change the password on the server you will need to change it here as well."'</span></a></td></tr>
<tr><td>'$"Administrator password"'</td><td><input tabindex= "4" name="_PASSWORD1_" size="23" type="password"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the administrator password. If you change the password on the server you will need to change it here as well."'</span></a></td></tr>
<tr><td>'$"Confirm"'</td><td><input tabindex= "5" name="_PASSWORD2_" size="23" type="password"></td></tr>
<tr><td>'$"Role"'</td><td><textarea  tabindex= "6" cols="50" rows="4" name="_ROLE_"></textarea></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a description of the role of the server."'</span></a></td></tr>
</tbody></table>
<br><br></div>
<div id="submitbox">
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
</form></div></body></html>'
exit

