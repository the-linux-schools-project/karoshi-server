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
########################
#Required input variables
########################
#  _FIRSTNAME_
#  _SURNAME_
# _USERNAMESTYLE_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
#  _GROUP_      This is the primary group for the new user eg yr2000, staff, officestaff.


##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER" ] && source "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--><title>Upload User Image</title></head>
<body id="photobox">'

ImageFile=/images/blank_user_image.jpg
#Show the user photo if one has been uploaded
if [ -d "/var/www/karoshi/add_user_image/$REMOTE_USER" ]
then

	ImageFile=$(find "/var/www/karoshi/add_user_image/$REMOTE_USER" -type f -iname "*.jpg" | sed -n 1,1p)
	ImageFile=$(basename "$ImageFile")
	if [ ! -z "$ImageFile" ]
	then
		ImageFile="/admin/add_user_image/$REMOTE_USER/$ImageFile"
	else
		ImageFile="/images/blank_user_image.jpg"
	fi
fi

echo '<form enctype="multipart/form-data" action="/cgi-bin/admin/add_user_upload_image.cgi" method="post"><label for="fileButton"><img src="'"$ImageFile"'" width="120" height="150" alt="photo"></label> 
<input accept=".jpg" onchange="this.form.submit()" name="file-to-upload-01" type="file" id="fileButton" style="display:none;"/></form>'

echo '</body></html>'

