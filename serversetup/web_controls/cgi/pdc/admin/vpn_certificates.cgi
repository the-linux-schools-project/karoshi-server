#!/bin/bash
#Copyright (C) 2015 Paul Sharrad

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"VPN Certificates"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-+-')
#########################
#Assign data to variables
#########################
END_POINT=11
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

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

if [ -z "$ACTION" ]
then
	ACTION=view
fi

if [ "$ACTION" = view ]
then
	TITLEMSG=$"VPN Certificates"
	ACTION2=add
	ACTIONMSG=$"Add Certificate"
	ACTIONMSG2=$"Add"
	ICON1=/images/submenus/system/add.png
fi

if [ "$ACTION" = add ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = unrevoke ] || [ "$ACTION" = revoke ] || [ "$ACTION" = reallyunrevoke ]  || [ "$ACTION" = reallyrevoke ] || [ "$ACTION" = downloadcert ]
then
	ACTION2=view
	ACTIONMSG=$"View Certificates"
	ACTIONMSG2=$"View"
	ICON1=/images/submenus/system/vpn.png
fi

if [ "$ACTION" = add ] || [ "$ACTION" = reallyadd ]
then
	TITLEMSG=$"Create Client VPN Certificate"
fi

if [ "$ACTION" = revoke ] || [ "$ACTION" = reallyrevoke ]
then
	TITLEMSG=$"Revoke Client VPN Certificate"
fi

if [ "$ACTION" = unrevoke ] || [ "$ACTION" = reallyunrevoke ]
then
	TITLEMSG=$"Un-Revoke Client VPN Certificate"
fi


if [ "$ACTION" = downloadcert ]
then
	TITLEMSG=$"Download Client VPN Certificate"
fi

function show_status {
echo '<SCRIPT language="Javascript">
alert("'"$MESSAGE"'");
window.location = "/cgi-bin/admin/vpn_certificates.cgi"
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


#########################
#Check data
#########################

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallyrevoke ] || [ "$ACTION" = reallyunrevoke ]
then
	#Make sure that a username has been entered.
	if [ -z "$USERNAME" ]
	then
		MESSAGE=$"You must enter in a username."
		show_status
	fi

	if [ "$ACTION" = reallyadd ]
	then
		#Check that the username exists
		getent passwd "$USERNAME" 1>/dev/null 2>/dev/null
		if [ "$?" != 0 ]
		then
			MESSAGE=$"This username does not exist."
			show_status
		fi
	fi
fi

#Generate navigation bar
if [ $MOBILE = no ]
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
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"VPN Certificates"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox"><b>'"$USERNAME"'</b><br>
'
else
	WIDTH=100
	echo '<div id="'"$DIV_ID"'"><div id="titlebox">
	<div class="sectiontitle">'"$TITLEMSG"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=OpenVPN_Server#Creating_Client_Certificates"><img class="images" alt="" src="/images/help/info.png"><span>'"$ACTIONMSG"'</span></a></div>
	<table class="tablesorter"><tbody><tr>
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<form action="/cgi-bin/admin/vpn_certificates.cgi" method="post">
				<button class="info infonavbutton" name="_DoAction_" value="_ACTION_'$ACTION2'_">
					<img src="'$ICON1'" alt="'"$ACTIONMSG"'">
					<span>'"$ACTIONMSG"'</span><br>
					'"$ACTIONMSG2"'
				</button>
			</form>
		</td>
	</tbody></table>
	</div><div id="infobox">'
fi

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/vpn_certificates.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ACTION:$USERNAME:" | sudo -H /opt/karoshi/web_controls/exec/vpn_certificates
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit

