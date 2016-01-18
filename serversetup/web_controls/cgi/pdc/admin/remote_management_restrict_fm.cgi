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
  <title>'$"Restrict access to Karoshi Remote Management"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/remote_management_restrict.cgi" method="post">
  <div id="actionbox">
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top;"><div class="sectiontitle">'$"Restrict access to Karoshi Remote Management"'</div></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Access can be restricted by a complete tcpip number or by a partial number for a range."' '$"For example 172.30.4. will allow all computers from 172.30.4.1 to 172.30.4.254."'</span></a></td></tr></tbody></table>
  <br><br>
<input name="_ACTION_" value="add" type="hidden">
  <table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 180px;">'$"Allowed tcpip address"'</td>
        <td><input maxlength="15" name="_ADDTCPADDRESS_" size="15"></td></tr>
        <tr><td>'$"Comment"'</td>
        <td><input maxlength="30" name="_TCPCOMMENT_" size="15"></td></tr>
	<tr><td>'$"Admin Level"'</td>
	<td><select name="_PRIMARYADMIN_">
        <option>1 2</option>
        <option>3</option>
        </select>
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
