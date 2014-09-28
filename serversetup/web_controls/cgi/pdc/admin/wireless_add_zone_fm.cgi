#!/bin/bash
#wire_add_zone
#Copyright (C) 2009  Paul Sharrad

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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Add Wireless Zone"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/wireless_add_zone.cgi" method="post"><div id="actionbox"><b>'$"Add Wireless Zone"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows WPA II enterprise wireless access points to be used. This key will need to match the key supplied to the wireless access points."'<br><br>'$"The wireless access points will authenticate using usernames and passwords via a radius server and LDAP on the PDC."'</span></a><br>
  <br>
  <table class="standard" style="text-align: left; height: 10px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 180px;">'$"Access Name"'</td><td><input name="_CLIENTNAME_" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a name for your set of wireless access points."'</span></a></td></tr>
<tr><td style="width: 180px;">'$"TCPIP"'</td><td><input name="_TCPIP_" maxlength="20" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the tcpip number or range you require."'<br><br>'$"Example 172.30.0.0/16"'</span></a></td></tr>
<tr><td style="width: 180px;">'$"Secret Key"'</td><td><input name="_WPAKEY_" maxlength="63" size="63" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a WPA key or leave blank to auto generate a key."'<br><br>'$"The key must be between 20 and 63 characters long."'</span></a>
</td></tr></tbody></table>
  <br>
  <br>
</div>
<div id="submitbox">
  <input value="Submit" type="submit"> <input value="Reset" type="reset">
</div>
</form>
</div></body>
</html>
'
exit
