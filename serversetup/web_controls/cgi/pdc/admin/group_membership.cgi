#!/bin/bash
#Copyright (C) 2012 Paul Sharrad

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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Group Membership"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
'

if [ "$MOBILE" = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: www.dynamicdrive.com
		* Visit Dynamic Drive at www.dynamicdrive.com for full source code
		***********************************************/
	</script>
	<script>
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g')
#########################
#Assign data to variables
#########################
END_POINT=9
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

function show_status {
echo '<SCRIPT language="Javascript">
alert("'"$MESSAGE"'");
window.location = "/cgi-bin/admin/group_membership_fm.cgi"
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
MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/group_membership.cgi | cut -d' ' -f1)
#########################
#Check data
#########################
#Check to see that username is not blank
if [ -z "$USERNAME" ]
then
	MESSAGE=$"You have not entered in a username."
	show_status
fi
#Check to see that the user exists
getent passwd "$USERNAME" 1>/dev/null 2>/dev/null
if [ "$?" != 0 ]
then
	MESSAGE=$"This user does not exist."
	show_status
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	WIDTH=90
	ICON1=/images/submenus/user/adduserm.png
	ICON2=/images/submenus/user/edit_user_infom.png
	ICON3=/images/submenus/user/groupsm.png
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Group Membership"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="mobileactionbox"><b>'"$USERNAME"'</b><br>
'
else
	WIDTH=100
	ICON1=/images/submenus/user/adduser.png
	ICON2=/images/submenus/user/edit_user_info.png
	ICON3=/images/submenus/user/groups.png

	echo '<div id="'"$DIV_ID"'"><div id="titlebox">'
fi

echo '<div class="sectiontitle">'$"Group Membership"' - '"$USERNAME"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Membership"><img class="images" alt="" src="/images/help/info.png"><span>'$"This shows the groups that the user is a member of."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/group_membership_fm.cgi" method="post">
			<button class="info infonavbutton" name="_ChooseUser_" value="_">
				<img src="'"$ICON1"'" alt="'$"Choose User"'">
				<span>'$"Choose a user to view."'</span><br>
				'$"Choose User"'
			</button>
		</form>
	</td>

'

if [ ! -z "$USERNAME" ]
then
	echo '

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/show_user_info.cgi" method="post">
			<button class="info infonavbutton" name="_EditUser_" value="_SERVERNAME_'"$(hostname-fqdn)"'_SERVERTYPE_network_SERVERMASTER_notset_ACTION_notset_USERNAME_'"$USERNAME"'_">
				<img src="'"$ICON2"'" alt="'$"Edit User"'">
				<span>'$"Edit this user."'</span><br>
				'$"Edit User"'
			</button>
		</form>
	</td>
	'
fi

echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/groups.cgi" method="post">
			<button class="info infonavbutton" name="_GroupManagement_" value="_">
				<img src="'"$ICON3"'" alt="'$"Group Management"'">
				<span>'$"View all groups."'</span><br>
				'$"Group Management"'
			</button>
		</form>
	</td>

</tr></tbody></table>
'
[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/group_membership
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit

