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


#Select the default username style
if [ -f /opt/karoshi/server_network/default_username_style ]
then
source /opt/karoshi/server_network/default_username_style
[ $DEFAULTSTYLE = 1 ] && SELECT1='selected="selected"'
[ $DEFAULTSTYLE = 2 ] && SELECT2='selected="selected"'
[ $DEFAULTSTYLE = 3 ] && SELECT3='selected="selected"'
[ $DEFAULTSTYLE = 4 ] && SELECT4='selected="selected"'
[ $DEFAULTSTYLE = 5 ] && SELECT5='selected="selected"'
[ $DEFAULTSTYLE = 6 ] && SELECT6='selected="selected"'
[ $DEFAULTSTYLE = 7 ] && SELECT7='selected="selected"'
[ $DEFAULTSTYLE = 8 ] && SELECT8='selected="selected"'
[ $DEFAULTSTYLE = 9 ] && SELECT9='selected="selected"'
else
SELECT1='selected="selected"'
fi

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
  <title>'$"Bulk User Creation"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><form action="/cgi-bin/admin/bulk_user_creation_create.cgi" method="post"><div class="sectiontitle">'$"Bulk User Creation"'</div>
  <br>
'$"Please select the following options to create your users"':<br>
  <br>'

#Check that this server is not part of a federated setup
if [ -f /opt/karoshi/server_network/servers/$HOSTNAME/federated_server ]
then
echo $"This server is part of a federated system. Users must be created on the main federation server." '</div></div></body></html>'
exit
fi

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 150px;">
'$"Username"'</td><td>
<select name="_USERNAMESTYLE_" style="width: 200px;">
        <option value="userstyleS1" '$SELECT1'>'$"Style 1"': '$"astudent09"'</option>
        <option value="userstyleS2" '$SELECT2'>'$"Style 2"': '$"09astudent"'</option>
        <option value="userstyleS3" '$SELECT3'>'$"Style 3"': '$"studenta09"'</option>
        <option value="userstyleS4" '$SELECT4'>'$"Style 4"': '$"arnold.student09"'</option>
        <option value="userstyleS5" '$SELECT5'>'$"Style 5"': '$"student.arnold09"'</option>
        <option value="userstyleS6" '$SELECT6'>'$"Style 6"': '$"09studenta"'</option>
        <option value="userstyleS7" '$SELECT7'>'$"Style 7"': '$"09arnolds"'</option>
        <option value="userstyleS8" '$SELECT8'>'$"Style 8"': '$"arnolds"'</option>
        <option value="userstyleS9" '$SELECT9'>'$"Style 9"': '$"Enrollment number as username."'</option>
</select></td></tr>
<tr><td>'$"Primary Group"'</td>
</td><td>'
/opt/karoshi/web_controls/group_dropdown_list
echo '</td></tr></tbody></table>
</div>
<div id="submitbox">
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
</form>
</div></body>
</html>
'
exit

