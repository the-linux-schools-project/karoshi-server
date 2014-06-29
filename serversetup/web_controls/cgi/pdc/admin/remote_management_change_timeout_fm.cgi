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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER

USER_TIMEOUT=$TIMEOUT

[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/remote_management_change_timeout ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/remote_management_change_timeout
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
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
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/remote_management_change_timeout.cgi" method="post">
<div id="actionbox"><div class="sectiontitle">'$TITLE'</div>
<br>
<table class="standard" style="text-align: left; height: 30px;" border="0" cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td style="width: 200px;">'$TIMEOUTMSG'</td>'
#Convert timeout to minutes
let USER_TIMEOUT=$USER_TIMEOUT/60
echo '
<td><input size="2" maxlength="2" name="_TIMEOUT_"value="'$USER_TIMEOUT'"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'<br><br>'$HELPMSG2'<br><br>'$HELPMSG3'</span></a></td>
</tr>
<tr><td>'$NOTIMEOUTMSG'</td>
<td><input size="15" maxlength="15" name="_NOTIMEOUT_"value="'$NOTIMEOUT'"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG4'<br><br>'$HELPMSG5'<br><br>'$HELPMSG6'</span></a></td>
</tbody></table></div>
  <div id="submitbox">
  <input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
  </div>
</form>
</div></body>
</html>
'
exit
