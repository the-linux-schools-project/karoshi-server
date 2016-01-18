#!/bin/bash
#Copyright (C) 2008  Paul Sharrad

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
  <title>'$"Apply Quota Settings"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/quotas_set.cgi" name="selectservers" method="post"><b></b>
  <div id="actionbox"><b>'$"Apply Quota Settings"'</b>
  <br>
  <br>
<table class="standard" style="text-align: left;" border="0"
 cellpadding="2" cellspacing="2">
  <tbody>
 <tr>
      <td style="width: 180px;">'$"Username"'</td>
      <td style="width: 120px;"><input size="20" name="_USERNAME_" style="width: 200px;"></td><td>  <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the username that you want to apply these settings to."'<br><br>'$"Leave this field blank if you want to apply the settings to a whole group of users."'</span></a></td>
    </tr>
    <tr>
      <td style="width: 180px;">'$"Group"'</td>
      <td style="width: 120px;">'

#Show groups
/opt/karoshi/web_controls/group_dropdown_list

echo '</td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the group that you want to apply the quota settings to."'</span></a></td>
    </tr>

<tr><td>Unit</td><td>
<select name="_UNIT_" style="width: 200px;">
<option value="MB" selected="selected">MB</option> 
<option>GB</option>
<option>TB</option>
</select>
</td></tr>
<tr><td style="width: 180px;">'$"Size"'</td><td style="width: 120px;"><input maxlength="3" size="9" name="_SIZE_" style="width: 200px;" value="300"></td>
<td> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This is the maximum file size that users can have on the system."'<br><br>'$"Users who reach this limit will not be able to save any more files until they have deleted some files."'<br><br>'$"Setting this value to 0 will disable this option."'</span></a></td></tr>
<tr>
      <td style="width: 180px;">'$"Max Files"'</td>
      <td style="width: 120px;"><input maxlength="7" size="20" name="_MAXFILES_" style="width: 200px;"
 value="1000"></td><td>  <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This is the maximum number of files that a user can save on the system."'<br><br>'$"Users who reach this limit will not be able to save any more files until they have deleted some files."'<br><br>'$"Setting this value to 0 will disable this option."'</span></a></td>
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


<option value="allstudents">'$"All Students"'</option>
