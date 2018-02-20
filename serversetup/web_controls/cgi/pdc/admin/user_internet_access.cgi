#!/bin/bash
#Copyright (C) 2014  Paul Sharrad

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

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server


#Check if timout should be disabled
[[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]] && TIMEOUT=86400

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"User Internet Access"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
echo '<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
</head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-+%')
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

if [ ! -z "$ACTION" ]
then
	#Assign USERNAMES
	DATANAME=USERNAMES
	get_data
	USERNAMES="${DATAENTRY//%40/@}"

	if [ "$ACTION" = banusers ]
	then
		END_POINT=22
		#Assign HOUR
		DATANAME=HOUR
		get_data
		HOUR="$DATAENTRY"

		#Assign MINUTES
		DATANAME=MINUTES
		get_data
		MINUTES="$DATAENTRY"

		#Assign DAY
		DATANAME=DAY
		get_data
		DAY="$DATAENTRY"

		#Assign MONTH
		DATANAME=MONTH
		get_data
		MONTH="$DATAENTRY"

		#Assign YEAR
		DATANAME=YEAR
		get_data
		YEAR="$DATAENTRY"

		#Assign INCIDENT
		DATANAME=INCIDENT
		get_data
		INCIDENT="$DATAENTRY"

		#Assign ACTIONTAKEN
		DATANAME=ACTIONTAKEN
		get_data
		ACTIONTAKEN="$DATAENTRY"

		#Assign BANLENGTH
		DATANAME=BANLENGTH
		get_data
		BANLENGTH="$DATAENTRY"
	fi
fi



#########################
#Check data
#########################
[ -z "$ACTION" ] && ACTION=view 

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"User Internet Access"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="mobileactionbox">
'
else
	echo '<div id="'"$DIV_ID"'"><div id=titlebox>'
fi

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/user_internet_access.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ACTION:$USERNAMES:$HOUR:$MINUTES:$DAY:$MONTH:$YEAR:$BANLENGTH:$INCIDENT:$ACTIONTAKEN:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/user_internet_access

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></div></body></html>'
exit

