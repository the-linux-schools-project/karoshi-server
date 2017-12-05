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
<body>
'

DATA=$(echo "$QUERY_STRING" | tr -cd '0-9A-Za-z\-\n_')

END_POINT=6
function get_data {
COUNTER=2
DATAENTRY=""
while [[ $COUNTER -le $END_POINT ]]
do
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [[ "$DATAHEADER" = "$DATANAME" ]]
	then
		let COUNTER="$COUNTER"+1
		DATAENTRY=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
		break
	fi
	let COUNTER=$COUNTER+1
done
}

#Assign Username
DATANAME=username
get_data
Username="$DATAENTRY"

#Assign PrimaryGroup
DATANAME=primarygroup
get_data
PrimaryGroup="$DATAENTRY"

ImageFile=/images/blank_user_image.jpg
if [ ! -z "$Username" ] &&  [ ! -z "$PrimaryGroup" ]
then
	if [ -f /var/www/html_karoshi/images/user_images/"$PrimaryGroup/$Username".jpg ]
	then
		ImageFile=/images/user_images/"$PrimaryGroup/$Username".jpg
	fi
else
	#Show the user photo if one has been uploaded
	if [ -d "/var/www/karoshi/show_user_image/$REMOTE_USER" ]
	then

		ImageFile=$(find "/var/www/karoshi/show_user_image/$REMOTE_USER" -type f -iname "*.jpg" | sed -n 1,1p)
		ImageFile=$(basename "$ImageFile")
		if [ ! -z "$ImageFile" ]
		then
			ImageFile="/admin/show_user_image/$REMOTE_USER/$ImageFile"
		else
			ImageFile="/images/blank_user_image.jpg"
		fi
	fi	
fi
TimeStamp=$(date +%s)
echo '<div id="photobox" style="position: relative; top: 50%; transform: translateY(-50%);"><form enctype="multipart/form-data" action="/cgi-bin/admin/show_user_info_upload_image.cgi" method="post"><label for="fileButton"><img src="'"$ImageFile"'?'"$TimeStamp.$$"'" width="120" height="150" alt=""></label> 
<input accept=".jpg" onchange="this.form.submit()" name="file-to-upload-01" type="file" id="fileButton" style="display:none;"></form></div></body></html>'
