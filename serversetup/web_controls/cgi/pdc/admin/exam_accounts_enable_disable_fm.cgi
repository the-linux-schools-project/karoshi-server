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
  <title>'$"Enable - Disable all exam accounts"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/exam_accounts_enable_disable.cgi" method="post">
<div id="actionbox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Enable - Disable all exam accounts"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Enable/Disable_Exam_Accounts"><img class="images" alt="" src="/images/help/info.png"><span>'$"Use this option to allow or deny access to all of the exam accounts."'</span></a></td></tr></tbody></table><br>
  <table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"Enable"'</td>
        <td><input name="_EXAMSTATUS_" value="enable" checked="checked" type="radio">&nbsp;</td>
      </tr>
      <tr>
        <td>
'$"Disable"'</td>
        <td><input name="_EXAMSTATUS_" value="disable" type="radio">&nbsp;</td>
      </tr>
<tr><td>
'$"Exceptions"'
</td><td>
<input tabindex= "1" name="_EXCEPTIONLIST_" style="width: 200px;" size="20" type="text">
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Enable/Disable_Accounts"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in any exam accounts that you do not want to be enabled or disabled."'</span></a>
</td></tr>
    </tbody>
  </table>
</div>
<div id="submitbox">
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></form></div></body></html>'
exit
