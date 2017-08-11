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
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
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
  <title>'$"Add Web Management User"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/user/groups.png

echo '
<form action="/cgi-bin/admin/remote_management_add.cgi" method="post">
  <div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"Add Web Management User"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_a_Remote_Admin"><img class="images" alt="" src="/images/help/info.png"><span>'$"These accounts are used by your technical staff to access the web managagement. The usernames and passwords used here are totally separate from normal network users."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<button class="info" formaction="remote_management_view.cgi" name="_ViewUsers_" value="_">
			<img src="'$ICON1'" alt="'$"View"'">
			<span>'$"View Web Management users."'</span><br>
			'$"View"'
		</button>
	</td>

</tr></tbody></table>

<br>
<table class="standard" style="text-align: left;" ><tbody>
<tr>
	<td style="width: 180px;">Job Title</td>
	<td><input name="_JOBTITLE_" tabindex="1" style="width: 200px;" size="20"></td><td></td>
</tr>
<tr>
	<td>Forename</td>
	<td><input name="_FORENAME_" tabindex="2" style="width: 200px;" size="20"></td><td></td>
</tr>
<tr>
	<td>Surname</td>
	<td><input name="_SURNAME_" tabindex="3" style="width: 200px;" size="20"></td><td></td>
</tr>
<tr>
	<td>'$"Username"'</td>
        <td><input required="required" tabindex="4" name="_USERNAME_" style="width: 200px;" size="20" type="text"></td>
	<td></td>
</tr>
<tr>
	<td>'$"Password"'</td>
	<td><input required="required" tabindex="5" name="_PASSWORD1_" style="width: 200px;" size="20" type="password"></td><td></td>
</tr>
<tr>
	<td>'$"Confirm"'</td>
	<td><input required="required" tabindex="6" name="_PASSWORD2_" style="width: 200px;" size="20" type="password"></td><td></td>
</tr>
<tr>
	<td>'$"Access Level"'</td><td>
	<select required="required" tabindex="7" name="_PRIMARYADMIN_" style="width: 200px;">
		<option label="blank" value=""></option>
		<option value="1">'$"Primary Admin"'</option>
		<option value="2">'$"Admin"'</option>
		<option value="3">'$"Technician"'</option>        
	</select>
	</td>
	<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_a_Remote_Admin"><img class="images" alt="" src="/images/help/info.png"><span>'$"Primary Admins have full control of the web management."'<br><br>'$"Admins have full control of the web management but cannot add or delete other admins."'<br><br>'$"Technicians can access a limited set of controls for day to day running of the system such as changing passwords."'</span></a></td>
</tr>
</tbody></table>
<br><br>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></div></form></div></body></html>
'
exit
