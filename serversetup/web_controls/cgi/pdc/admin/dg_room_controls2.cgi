#!/bin/bash
#Copyright (C) 2012  Paul Sharrad

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
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Client Internet Controls"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')
#########################
#Assign data to variables
#########################
END_POINT=19
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

#Assign LOCATION
DATANAME=LOCATION
get_data
LOCATION="$DATAENTRY"

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

#Assign ASSET
DATANAME=ASSET
get_data
ASSET="$DATAENTRY"

function show_status {
echo '<script>'
echo 'alert("'"$MESSAGE"'");'
echo 'window.location = "/cgi-bin/admin/dg_room_controls_fm.cgi;'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi

#########################
#Check data
#########################
#Check to see that location is not blank
if [ -z "$LOCATION" ]
then
	MESSAGE=$"You have not chosen a location."
	show_status
fi
#Check to see that ACTION is not blank
if [ -z "$ACTION" ]
then
	MESSAGE=$"You have not chosen an action."
	show_status
fi

#Check to see that ASSET is not blank
if [ -z "$ASSET" ]
then
	MESSAGE=$"You have not chosen an asset."
	show_status
fi

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/dg_room_controls2.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$LOCATION:$ACTION:$ASSET:" | sudo -H /opt/karoshi/web_controls/exec/dg_room_controls


#Redirect to room controls location page

echo '<form id="submit_form" action="dg_room_controls.cgi" method="POST">
<input type="hidden" name="_LOCATION_" value="'"$LOCATION"'">
</form>'

echo '<script>
document.getElementById("submit_form").submit();
</script>'


exit

