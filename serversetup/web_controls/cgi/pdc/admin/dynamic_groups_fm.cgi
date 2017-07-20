#!/bin/bash
#Copyright (C) 2015  Paul Sharrad

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
    <TITLE>'$"Dynamic Groups"'</TITLE><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</HEAD>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/user/groups.png

echo '<FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/dynamic_groups_upload.cgi" METHOD="POST"><div id="actionbox">

<div class="sectiontitle">'$"Dynamic Groups"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows you to create groups of users that change on a regular basis."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info" formaction="groups.cgi" name="_ViewNewPasswords_" value="_">
			<img src="'"$ICON1"'" alt="'$"Group Management"'">
			<span>'$"Manage groups."'</span><br>
			'$"Group Management"'
		</button>
	</td>

</tr></tbody></table>
<br>

<table class="standard">
<tr><td style="width: 180px;">'$"Upload CSV file"'</td><td>
<INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35"> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management"><img class="images" alt="" src="/images/help/info.png"><span>'$"CSV Format""<br>"$"username or enrolment number or staff code,group1,group2,group3..."'</span></a>
</td>
</tr>
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
