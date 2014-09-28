#!/bin/bash
#Change password
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
  <title>'$"View auto reset passwords"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/view_auto_reset_passwords.cgi" method="post">
<div id="actionbox"><span style="font-weight: bold;">
'$"View auto reset passwords"' </span> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_Auto_Reset_Passwords"><img class="images" alt="" src="/images/help/info.png"><span>'$"By default the following user account passwords are are reset every night."'<br><br>guest1 - guest 30<br>tech1 - tech4<br><br>'$"The guest accounts also have any files in the accounts deleted."'</span></a>
<br><br>
  <table class="standard" style="text-align: left;"
 border="0" cellpadding="2" cellspacing="2">
  <tbody>
    <tr>
      <td style="width: 201px;">'$"Guest Accounts"'</td>
      <td style="width: 31px;"><input checked="checked"
 name="_ACCOUNTTYPE_" value="guests" type="radio"></td>
      <td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_Auto_Reset_Passwords"><img class="images" alt="" src="/images/help/info.png"><span>'$"The guest accounts are for temporary visitors only."'</span></a>
</td>
    </tr>
    <tr>
      <td style="width: 201px;">'$"Tech Accounts"'</td>
      <td style="width: 31px;"><input
 name="_ACCOUNTTYPE_" value="tech" type="radio"></td>
      <td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_Auto_Reset_Passwords"><img class="images" alt="" src="/images/help/info.png"><span>'$"The tech accounts are used to gain admin status on windows clients."'</span></a>
</td>
    </tr>
  </tbody>
</table>
</div>
<div id="submitbox">
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
</form>
</div></body>
</html>
'
exit
