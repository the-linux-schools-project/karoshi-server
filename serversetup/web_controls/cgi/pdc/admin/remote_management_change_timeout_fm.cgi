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
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server


USER_TIMEOUT=$TIMEOUT

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
  <title>'$"Change Timeout"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/remote_management_change_timeout.cgi" method="post">
<div id="actionbox"><div class="sectiontitle">'$"Change Timeout"'</div>
<br>
<table class="standard" style="text-align: left; height: 30px;" >
<tbody>
<tr>
<td style="width: 200px;">'$"Timeout"'</td>'
#Convert timeout to minutes
let USER_TIMEOUT=$USER_TIMEOUT/60
echo '
<td><input size="2" maxlength="2" name="_TIMEOUT_" value="'$USER_TIMEOUT'"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This is the time delay before you are logged out of the Karoshi Web Management system."'<br><br>'$"Enter a time in minutes between 1 and 99. This is a per user setting and will not affect other users."'<br><br>'$"The default value is 5 minutes."'</span></a></td>
</tr>
<tr><td>'$"Extend timeout from"'</td>
<td><input size="15" maxlength="15" name="_NOTIMEOUT_" value="'$NOTIMEOUT'"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose a tcpip number or range to extend the timeout from. The timeout setting will extend to 1 day for computers matching this value."'<br><br>'$"Example1 - 172.30.3.1 - individual computer"'<br><br>'$"Example2 - 172.30.3 - all computers in this range"'</span></a></td>
</tbody></table></div>
  <div id="submitbox">
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
  </div>
</form>
</div></body>
</html>
'
exit
