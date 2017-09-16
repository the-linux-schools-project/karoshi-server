#!/bin/bash
#Copyright (C) 2017  Paul Sharrad

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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Radius Access Controls"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	2: { sorter: false}
    		}
		});
    }
);
</script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g')

#########################
#Assign data to variables
#########################
END_POINT=10
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

#Assign GROUP
DATANAME=GROUP
get_data
GROUP="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'");'
echo 'window.location = "/cgi-bin/admin/radius_access_controls.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	WIDTH=100
	WIDTH2=250
	WIDTH3=140
	ICON1=/images/submenus/system/wireless.png
	ICON2=/images/submenus/user/group_yes.png
	ICON3=/images/submenus/user/group_no.png
	ICON4=/images/submenus/system/reload.png
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
	echo '<div id="'"$DIV_ID"'"><div id="titlebox">'
else
	WIDTH=90
	WIDTH2=250
	WIDTH3=140
	ICON1=/images/submenus/system/wirelessm.png
	ICON2=/images/submenus/user/group_yes_m.png
	ICON3=/images/submenus/user/group_no_m.png
	ICON4=/images/submenus/system/reloadm.png
fi

#Check data
[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = allow ] || [ "$ACTION" = allowall ] || [ "$ACTION" = deny ] || [ "$ACTION" = denyall ] || [ "$ACTION" = activatechanges ] && [ ! -z "$GROUP" ]
then
	MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/radius_access_controls.cgi | cut -d' ' -f1)
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$ACTION:$GROUP:" | sudo -H /opt/karoshi/web_controls/exec/radius_access_controls	
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Radius Access Controls"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
else
	echo '<div class="sectiontitle">'$"Radius Access Controls"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Radius_Server#Viewing_Access_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$"Radius Access Controls"'</span></a></div>'
fi

echo '
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/radius_access_points.cgi" method="post">
			<button class="info infonavbutton" name="____RadiusAccessPoints____" value="____">
				<img src="'"$ICON1"'" alt="'$"Access Points"'">
				<span>'$"View Radius Access Points."'</span><br>
				'$"Access Points"'
			</button>
			</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/radius_access_controls.cgi" method="post">
			<button class="info infonavbutton" name="____RadiusAccessPoints____" value="____ACTION____allowall____GROUP____all____">
				<img src="'"$ICON2"'" alt="'$"Allow all"'">
				<span>'$"Allow all groups."'</span><br>
				'$"Allow all"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/radius_access_controls.cgi" method="post">
			<button class="info infonavbutton" name="____RadiusAccessPoints____" value="____ACTION____denyall____GROUP____all____">
				<img src="'"$ICON3"'" alt="'$"Allow all"'">
				<span>'$"Deny all groups."'</span><br>
				'$"Deny all"'
			</button>
		</form>
	</td>'

	if [ -f /opt/karoshi/server_network/radius/activate_changes ] 
	then
		echo '
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/radius_access_controls.cgi" method="post">
				<button class="info infonavbutton" name="____ActivateChanges____" value="____ACTION____activatechanges____GROUP____all____">
					<img src="'"$ICON4"'" alt="'$"Activate changes"'">
					<span>'$"Activate changes."'</span><br>
					'$"Activate changes"'
				</button>
			</form>
		</td>
		'
	fi

echo '</tr></tbody></table>'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

echo '<form action="/cgi-bin/admin/radius_access_controls.cgi" method="post">
'
#Show all primary groups
echo '<table id="myTable" class="tablesorter"><thead><tr><th style="width:'"$WIDTH2"'px"><b>'$"Group"'</b></th><th style="width:'"$WIDTH3"'px"><b>'$"Access"'</b></th><th></th></tr></thead><tbody>'

for PRI_GROUP in $(ls -1 /opt/karoshi/server_network/group_information)
do
	ACTION="deny"
	COLOUR="#6EDE60"
	STATUSICON="$ICON2"
	STATUSMSG=$"Allowed"
	LONGMSG=$"Deny access for this group of users."
	
	if [ -f /opt/karoshi/server_network/radius/denied_groups/"$PRI_GROUP" ]
	then
		ACTION="allow"
		COLOUR="#FF0004"
		STATUSICON="$ICON3"
		STATUSMSG=$"Denied"
		LONGMSG=$"Allow access for this group of users."
	fi
	
	echo '<tr><td>'"$PRI_GROUP"'</td><td style="color:'"$COLOUR"'"><b>'"$STATUSMSG"'</b></td><td>

		<button class="info infonavbutton" name="____DoAction____" value="____ACTION____'"$ACTION"'____GROUP____'"$PRI_GROUP"'____">
			<img src="'"$STATUSICON"'" alt="'"$STATUSMSG"'">
			<span>'"$LONGMSG"'</span>
		</button>

		</td></tr>'
done
echo '</tbody></table></form></div>'

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></body></html>'
exit
