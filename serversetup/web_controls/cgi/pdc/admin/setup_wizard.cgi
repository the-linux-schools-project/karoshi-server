#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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
INSTALL_TYPE=$(sed -n 1,1p /opt/karoshi/server_network/install_type)

#Check if timout should be disabled
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
then
	TIMEOUT=86400
fi

#Change default page to stop recursion problem
if [ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ]
then
	sed -i 's/DEFAULTPAGE=setup_wizard.cgi/DEFAULTPAGE=change_password_fm.cgi/g' /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Setup Wizard"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
<body>'

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')
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

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

#Assign VIEWEDPAGES
DATANAME=VIEWEDPAGES
get_data
VIEWEDPAGES="$DATAENTRY"

IMAGE1=/images/submenus/system/computer.png
#Add server roles
IMAGE2=/images/submenus/system/computer.png
#Management users
IMAGE3=/images/submenus/system/adduser.png
#Label groups
IMAGE4=/images/submenus/system/edit.png
#Add a user
IMAGE5=/images/submenus/user/adduser.png
#Room locations
IMAGE6=/images/assets/location.png
#Join clients
IMAGE7=/images/assets/curriculum_computer.png
IMAGE8=/images/submenus/printer/assign_printer.png
#Add assets
IMAGE9=/images/assets/add_asset.png
#Setup printers
IMAGEa=/images/submenus/printer/assign_printer.png
#User settings
IMAGEb=/images/submenus/user/user_images.png
#Bulk user creation
IMAGEc=/images/submenus/user/groups.png
#Set default page
IMAGEd=/images/assets/curriculum_computer.png

[ -f /opt/karoshi/server_network/web_controls/setup_wizard ] && source /opt/karoshi/server_network/web_controls/setup_wizard

SITEURL=welcome.cgi
if [ ! -z "$ACTION" ]
then
[ "$ACTION" = 1 ] && SITEURL=karoshi_servers_add_fm.cgi
[ "$ACTION" = 2 ] && SITEURL=karoshi_servers_view.cgi
[ "$ACTION" = 3 ] && SITEURL=remote_management_add_fm.cgi
[ "$ACTION" = 4 ] && SITEURL=label_groups_fm.cgi
[ "$ACTION" = 5 ] && SITEURL=add_user_fm.cgi
[ "$ACTION" = 6 ] && SITEURL=locations.cgi
[ "$ACTION" = 7 ] && SITEURL=setup_wizard_clients_fm.cgi
[ "$ACTION" = 8 ] && SITEURL=setup_wizard_profiles_fm.cgi
[ "$ACTION" = 9 ] && SITEURL=asset_register_view.cgi
[ "$ACTION" = a ] && SITEURL=setup_wizard_printers_fm.cgi
[ "$ACTION" = b ] && SITEURL=default_user_settings_fm.cgi
[ "$ACTION" = c ] && SITEURL=bulk_user_creation_upload_fm.cgi
[ "$ACTION" = d ] && SITEURL=set_default_page_fm.cgi

VIEWEDPAGES="$VIEWEDPAGES$ACTION"

[[ $(echo "$VIEWEDPAGES" | grep -c 1) -gt 0 ]] && IMAGE1=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c 2) -gt 0 ]] && IMAGE2=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c 3) -gt 0 ]] && IMAGE3=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c 4) -gt 0 ]] && IMAGE4=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c 5) -gt 0 ]] && IMAGE5=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c 6) -gt 0 ]] && IMAGE6=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c 7) -gt 0 ]] && IMAGE7=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c 8) -gt 0 ]] && IMAGE8=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c 9) -gt 0 ]] && IMAGE9=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c a) -gt 0 ]] && IMAGEa=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c b) -gt 0 ]] && IMAGEb=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c c) -gt 0 ]] && IMAGEc=/images/submenus/system/complete.png
[[ $(echo "$VIEWEDPAGES" | grep -c d) -gt 0 ]] && IMAGEd=/images/submenus/system/complete.png

echo IMAGE1="$IMAGE1" > /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE2="$IMAGE2" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE3="$IMAGE3" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE4="$IMAGE4" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE5="$IMAGE5" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE6="$IMAGE6" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE7="$IMAGE7" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE8="$IMAGE8" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE9="$IMAGE9" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGEa="$IMAGEa" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGEb="$IMAGEb" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGEc="$IMAGEc" >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGEd="$IMAGEd" >> /opt/karoshi/server_network/web_controls/setup_wizard

fi



echo '<div id="wizard">
<form action="/cgi-bin/admin/setup_wizard.cgi" method="post">
<input type="hidden" id="age" name="_VIEWEDPAGES_'"$VIEWEDPAGES"'_" value="">

<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_2_">
			<img src="'"$IMAGE2"'" alt="'$"Add Server Roles"'">
			<br>
			'$"Add Server Roles"'
		</button>
	</td>

	</tr><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_3_">
			<img src="'"$IMAGE3"'" alt="'$"Management Users"'">
			<br>
			'$"Management Users"'
		</button>
	</td>

	</tr><tr>
	'

if [ "$INSTALL_TYPE" != home ]
then
	echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_4_">
			<img src="'"$IMAGE4"'" alt="'$"Label Groups"'">
			<br>
			'$"Label Groups"'
		</button>
	</td>

	</tr><tr>
	'
fi

echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_5_">
			<img src="'"$IMAGE5"'" alt="'$"Add a User"'">
			<br>
			'$"Add a User"'
		</button>
	</td>

	</tr><tr>
'

if [ "$INSTALL_TYPE" != home ]
then
	echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_6_">
			<img src="'"$IMAGE6"'" alt="'$"Room Locations"'">
			<br>
			'$"Room Locations"'
		</button>
	</td>

	</tr><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_7_">
			<img src="'"$IMAGE7"'" alt="'$"Join Clients"'">
			<br>
			'$"Join Clients"'
		</button>
	</td>

	</tr><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_8_">
			<img src="'$IMAGE8'" alt="'$"Profiles"'">
			<br>
			'$"Profiles"'
		</button>
	</td>

	</tr><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_9_">
			<img src="'"$IMAGE9"'" alt="'$"Add Assets"'">
			<br>
			'$"Add Assets"'
		</button>
	</td>

	</tr><tr>
	'
fi

echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_a_">
			<img src="'$IMAGEa'" alt="'$"Setup Printers"'">
			<br>
			'$"Setup Printers"'
		</button>
	</td>

	</tr><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_b_">
			<img src="'"$IMAGEb"'" alt="'$"User Settings"'">
			<br>
			'$"User Settings"'
		</button>
	</td>

	</tr><tr>
'

if [ "$INSTALL_TYPE" != home ]
then
	echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_c_">
			<img src="'"$IMAGEc"'" alt="'$"Bulk User Creation"'">
			<br>
			'$"Bulk User Creation"'
		</button>
	</td>

	</tr><tr>
	'
fi

echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DoAction_" value="_ACTION_d_">
			<img src="'"$IMAGEd"'" alt="'$"Set Default Page"'">
			<br>
			'$"Set Default Page"'
		</button>
	</td>
</tr></tbody></table>

</form></div>
<iframe src="'"$SITEURL"'" name="setupwizard" width="100%" height="100%" frameborder="0">
  <p>Your browser does not support iframes.</p>
</iframe>
</body></html>
'
exit


