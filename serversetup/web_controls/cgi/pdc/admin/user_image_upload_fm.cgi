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
    <TITLE>'$"Upload User Image"'</TITLE><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/user/bulk_user_creation.png
ICON2=/images/submenus/user/password.png
ICON3=/images/submenus/user/users.png
ICON4=/images/submenus/user/password.png

echo '<FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/user_image_upload.cgi" METHOD="POST"><div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"Import User Image"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=User_Images"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows you to upload user images that can be used to identify your users."'</span></a></div>

<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" formaction="bulk_user_creation_upload_fm.cgi" name="_BulkUserCreation_" value="_">
			<img src="'"$ICON1"'" alt="'$"Bulk User Creation"'">
			<span>'$"Create user accounts from a CSV file."'</span><br>
			'$"Bulk User Creation"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" formaction="bulk_user_creation_view_passwords_fm.cgi" name="_ViewNewPasswords_" value="_">
			<img src="'"$ICON2"'" alt="'$"View New Passwords"'">
			<span>'$"View the passwords set for newly created accounts."'</span><br>
			'$"View New Passwords"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" formaction="bulk_user_creation_import_enrollment_numbers_fm.cgi" name="_ImportEnrollmentNumbers_" value="_">
			<img src="'"$ICON3"'" alt="'$"Import Enrollment Numbers"'">
			<span>'$"Import enrollment numbers for your user accounts."'</span><br>
			'$"Import Enrollment Numbers"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" formaction="csv_set_passwords_fm.cgi" name="_SetUserPasswords_" value="_">
			<img src="'"$ICON4"'" alt="'$"Set User Passwords"'">
			<span>'$"Set User Passwords."'</span><br>
			'$"Set User Passwords"'
		</button>
	</td>

</tr></tbody></table><br>
        
        <table class="standard">
        <tr>
<td style="width: 200px;">
'$"User Image or compressed file"':
</td>
            <td>
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35">
            </td>
<td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=User_Images"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose a jpg image which corresponds to a user name or enrollment number or choose a zip or tar.gz file that contains multiple images."'<br><br>'$"Example"' - jjones.jpg - 10111.jpg.<br><br>'$"User images default to width 120px height 150px."'</span></a>

</td>
</tr>
</table>
<br><br>
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></div>
        </form>
</div></body>
</html>
'
exit
