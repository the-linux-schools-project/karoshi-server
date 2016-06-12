#!/bin/bash
#modify_groups
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
MOD_CODE=`echo ${RANDOM:0:3}`

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
  <title>'$"Bulk User Actions"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/modify_groups.cgi" method="post">
  <div id="actionbox">
  <b>'$"Bulk User Actions"'</b> 
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Bulk_User_Actions"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will affect a group of users."'</span></a>
<br><br>
  <table class="standard" style="text-align: left; left: 232px;" >
    <tbody>
<tr><td style="width: 180px;">
'$"Primary Group"'</td><td>'
/opt/karoshi/web_controls/group_dropdown_list
echo '</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Bulk_User_Actions"><img class="images" alt="" src="/images/help/info.png"><span>'$"All users in the group you select will be affected by the action you choose from this menu."'</span></a>
</td></tr>
<tr><td>'$"Option"'</td><td>
<select name="_OPTIONCHOICE_" style="width: 200px;">
<option value="enable">'$"Enable"'</option>
<option value="disable">'$"Disable"'</option>
<option value="deleteaccounts">'$"Delete accounts"'</option>
<option value="deleteaccounts2">'$"Archive and delete accounts"'</option>
<option value="resetpasswords">'$"Reset passwords"'</option>
<option value="changepassnextlogon">'$"Change password on next login"'</option>
<option value="passwordsneverexpire">'$"Passwords never expire"'</option>
<option value="passwordsexpire">'$"Passwords expire"'</option>
</select></td></tr>
<tr><td style="width: 180px;">
'$"Exceptions"'
</td><td>
<input tabindex= "1" name="_EXCEPTIONLIST_" style="width: 200px;" size="20" type="text">
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Bulk_User_Actions"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in any user accounts that you do not want to modify separated by spaces."'</span></a>
</td></tr>
<tr><td>'$"Modify Code"'</td><td style="vertical-align: top; text-align: left;"><b>'$MOD_CODE'</b></td></tr>
<tr><td>'$"Confirm"'</td><td style="vertical-align: top; text-align: left;"><input name="_MODCODE_" maxlength="3" size="3" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Modify_Groups"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the code displayed on the page to confirm this action."'</span></a>

</td></tr>
    </tbody>
  </table>
<input name="_FORMCODE_" value="'$MOD_CODE'" type="hidden">
  </div>
  <div id="submitbox">
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
  </div>
</form>
</div></body>
</html>
'
exit
