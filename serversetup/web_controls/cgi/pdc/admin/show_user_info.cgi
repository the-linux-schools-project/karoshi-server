#!/bin/bash
#Change a user's password
#Copyright (C) 2007 Paul Sharrad

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
#  _USERNAME_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Show User Information"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js"></script></head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox3"><div id="titlebox">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+')
#########################
#Assign data to variables
#########################
END_POINT=12
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

#Assign USERNAME
DATANAME=USERNAME
get_data
USERNAME="$DATAENTRY"

#Assign SERVERNAME
DATANAME=SERVERNAME
get_data
SERVERNAME="$DATAENTRY"

#Assign SERVERTYPE
DATANAME=SERVERTYPE
get_data
SERVERTYPE="$DATAENTRY"

#Assign SERVERMASTER
DATANAME=SERVERMASTER
get_data
SERVERMASTER="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/show_user_info_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
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
#########################
#Check data
#########################
#Check to see that username is not blank
if [ -z "$USERNAME" ]
then
	MESSAGE=$"The username must not be blank."
	show_status
fi

#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The servername cannot be blank."
	show_status
fi

#Check to see that SERVERTYPE is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$"The servertype cannot be blank."
	show_status
fi

#Check to see that SERVERMASTER is not blank
if [ "$SERVERTYPE" = federatedslave ]
then
	if [ -z "$SERVERMASTER" ]
	then
		MESSAGE=$"The servermaster cannot be blank."
		show_status
	fi
fi

#Check to see that the user exists
echo "$MD5SUM:$USERNAME" | sudo -H /opt/karoshi/web_controls/exec/existcheck_user
if [ "$?" = 111 ]
then
	MESSAGE=$"This username does not exist."
	show_status
fi
#Check that there are no spaces in the password
#if [ `echo $PASSWORD1 | grep -c +` != 0 ]
#then
#MESSAGE=$"The display name name cannot be blank."
#show_status
#fi
MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/show_user_info.cgi | cut -d' ' -f1)
#Show User info

WIDTH=100
ICON1=/images/submenus/user/adduser.png
ICON2=/images/submenus/user/edit_user_info.png
ICON3=/images/submenus/user/change_primary_group.png
ICON4=/images/submenus/user/groups.png
ICON5=/images/submenus/user/preferences.png

echo '
<div class="sectiontitle">'$"User Information"'</div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/show_user_info_fm.cgi" method="post">
			<button class="info infonavbutton" name="_ChooseUser_" value="_">
				<img src="'"$ICON1"'" alt="'$"Select user"'">
				<span>'$"Select the user you want to view."'</span><br>
				'$"Select user"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/change_username_fm.cgi" method="post">
			<button class="info infonavbutton" name="_ChangeUsername_" value="_USERNAME_'"$USERNAME"'_">
				<img src="'"$ICON2"'" alt="'$"Change Username"'">
				<span>'$"Change the username for this user."'</span><br>
				'$"Change Username"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/change_primary_group_fm.cgi" method="post">
			<button class="info infonavbutton" name="_ChangePrimaryGroup_" value="_USERNAME_'"$USERNAME"'_">
				<img src="'"$ICON3"'" alt="'$"Change Primary Group"'">
				<span>'$"Change the primary group for this user."'</span><br>
				'$"Change Primary Group"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/group_membership.cgi" method="post">
			<button class="info infonavbutton" name="____GroupMembership____" value="____USERNAME____'"$USERNAME"'____">
				<img src="'"$ICON4"'" alt="'$"Group Membership"'">
				<span>'$"Change the groups that this user is a member of."'</span><br>
				'$"Group Membership"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/default_user_settings_fm.cgi" method="post">
			<button class="info infonavbutton" name="_DefaultUserSettings_" value="_">
				<img src="'"$ICON5"'" alt="'$"Default User Settings"'">
				<span>'$"The default user settings that affect all users."'</span><br>
				'$"Default Settings"'
			</button>
		</form>
	</td>

</tr></table></div><div id="infobox">'

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:" | sudo -H /opt/karoshi/web_controls/exec/show_user_info
echo "</div></div></div></body></html>"
exit
