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


#Select the default username style
if [ -f /opt/karoshi/server_network/default_username_style ]
then
	source /opt/karoshi/server_network/default_username_style
	[ "$DEFAULTSTYLE" = 1 ] && SELECT1='selected="selected"'
	[ "$DEFAULTSTYLE" = 2 ] && SELECT2='selected="selected"'
	[ "$DEFAULTSTYLE" = 3 ] && SELECT3='selected="selected"'
	[ "$DEFAULTSTYLE" = 4 ] && SELECT4='selected="selected"'
	[ "$DEFAULTSTYLE" = 5 ] && SELECT5='selected="selected"'
	[ "$DEFAULTSTYLE" = 6 ] && SELECT6='selected="selected"'
	[ "$DEFAULTSTYLE" = 7 ] && SELECT7='selected="selected"'
	[ "$DEFAULTSTYLE" = 8 ] && SELECT8='selected="selected"'
	[ "$DEFAULTSTYLE" = 9 ] && SELECT9='selected="selected"'
	[ "$DEFAULTSTYLE" = 10 ] && SELECT10='selected="selected"'
else
	SELECT1='selected="selected"'
fi

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
  <title>'$"Bulk User Creation"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/user/bulk_user_creation.png
ICON2=/images/submenus/user/users.png

echo '<div id="actionbox3"><div id="titlebox"><form action="/cgi-bin/admin/bulk_user_creation_create.cgi" method="post">

<div class="sectiontitle">'$"Bulk User Creation"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Upload_CSV#Username_Styles_and_Primary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the username style and primary group for the users you want to create."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" formaction="bulk_user_creation_upload_fm.cgi" name="_BulkUserCreation_" value="_">
			<img src="'"$ICON1"'" alt="'$"Bulk User Creation"'">
			<span>'$"Create user accounts from a CSV file."'</span><br>
			'$"Bulk User Creation"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" formaction="bulk_user_creation_import_enrollment_numbers_fm.cgi" name="_ImportEnrollmentNumbers_" value="_">
			<img src="'"$ICON2"'" alt="'$"Import Enrollment Numbers"'">
			<span>'$"Import enrollment numbers for your user accounts."'</span><br>
			'$"Import Enrollment Numbers"'
		</button>
	</td>

</tr></tbody></table><br>

'$"Select the following options to create your users"':<br>
  <br>'

#Check that this server is not part of a federated setup
if [ -f /opt/karoshi/server_network/servers/"$HOSTNAME"/federated_server ]
then
	echo $"This server is part of a federated system. Users must be created on the main federation server." '</div></div></body></html>'
	exit
fi

echo '<table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 150px;">
'$"Username"'</td><td>
<select name="_USERNAMESTYLE_" style="width: 200px;">
        <option value="userstyleS1" '"$SELECT1"'>'$"Style"' 1: '$"auser09"'</option>
        <option value="userstyleS2" '"$SELECT2"'>'$"Style"' 2: '$"09auser"'</option>
        <option value="userstyleS3" '"$SELECT3"'>'$"Style"' 3: '$"usera09"'</option>
        <option value="userstyleS4" '"$SELECT4"'>'$"Style"' 4: '$"arnold.user09"'</option>
        <option value="userstyleS5" '"$SELECT5"'>'$"Style"' 5: '$"user.arnold09"'</option>
        <option value="userstyleS6" '"$SELECT6"'>'$"Style"' 6: '$"09usera"'</option>
        <option value="userstyleS7" '"$SELECT7"'>'$"Style"' 7: '$"09arnoldu"'</option>
        <option value="userstyleS8" '"$SELECT8"'>'$"Style"' 8: '$"arnoldu"'</option>
        <option value="userstyleS9" '"$SELECT9"'>'$"Style"' 9: '$"Enrollment number as username"'</option>
	<option value="userstyleS10" '"$SELECT10"'>'$"Style"' 10: '$"Enter a username"'</option>
</select></td></tr>
<tr><td>'$"Primary Group"'</td><td>'
/opt/karoshi/web_controls/group_dropdown_list | sed 's/.*<option disabled selected value>.*/<option label="blank"><\/option><option value="getgroupfromcsv">'$"Primary group from CSV"'<\/option><option disabled value>-----------------<\/option>/g'
echo '</td></tr></tbody></table>
<br><br>
 <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</form>
</div></div></body>
</html>
'
exit

