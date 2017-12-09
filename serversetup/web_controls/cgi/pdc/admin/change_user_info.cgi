#!/bin/bash
#Copyright (C) 2011 Paul Sharrad

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
#Language
########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Show User Information"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+')
#########################
#Assign data to variables
#########################
END_POINT=21
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

#Assign SN
DATANAME=SN
get_data
SN="$DATAENTRY"

#Assign GIVENNAME
DATANAME=GIVENNAME
get_data
GIVENNAME="$DATAENTRY"

#Assign EMPLOYEENUMBER
DATANAME=EMPLOYEENUMBER
get_data
EMPLOYEENUMBER="$DATAENTRY"

#Assign DISPLAYNAME
DATANAME=DISPLAYNAME
get_data
DISPLAYNAME="$DATAENTRY"

#Assign MAILLOCALADDRESS
DATANAME=MAILLOCALADDRESS
get_data
MAILLOCALADDRESS="$DATAENTRY"

#Assign _MAIL_
DATANAME=MAIL
get_data
MAIL="$DATAENTRY"

#Assign USERNAME
DATANAME=USERNAME
get_data
USERNAME="$DATAENTRY"

#Assign NEWUSERNAME
DATANAME=NEWUSERNAME
get_data
NEWUSERNAME="$DATAENTRY"

#Assign GROUP
DATANAME=GROUP
get_data
GROUP="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">
alert("'"$MESSAGE"'");
window.location = "/cgi-bin/admin/show_user_info.cgi"
</script>
</div></body></html>'
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
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [[ $(grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/change_user_info.cgi | cut -d' ' -f1)
#########################
#Check data
#########################

if [ -z "$SN" ]
then
	MESSAGE=$"The surname cannot be blank."
	show_status
fi
if [ -z "$GIVENNAME" ]
then
	MESSAGE=$"The given name cannot be blank."
	show_status
fi
if [ -z "$DISPLAYNAME" ]
then
	MESSAGE=$"The display name name cannot be blank."
	show_status
fi

if [ -z "$MAIL" ]
then
	MESSAGE=$"The mail address cannot be blank."
	show_status
fi
if [ -z "$USERNAME" ]
then
	MESSAGE=$"The username must not be blank."
	show_status
fi

if [ -z "$NEWUSERNAME" ]
then
	MESSAGE=$"The new username must not be blank."
	show_status
fi

#Change information
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$SN:$GIVENNAME:$DISPLAYNAME:$EMPLOYEENUMBER:$MAILLOCALADDRESS:$MAIL:$GROUP:$NEWUSERNAME" | sudo -H /opt/karoshi/web_controls/exec/change_user_info
SERVERNAME=$(hostname-fqdn)

echo '<form METHOD=POST ACTION="show_user_info.cgi" target="_top" name = "frm">
<input type="hidden" name="_UserInfo_" value="_USERNAME_'"$NEWUSERNAME"'_SERVERNAME_'"$SERVERNAME"'_SERVERTYPE_network_">
</form><script>document.frm.submit();</script><form>'

exit
