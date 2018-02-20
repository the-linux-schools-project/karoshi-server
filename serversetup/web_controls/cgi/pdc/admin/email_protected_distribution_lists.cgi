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
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
then
	TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Protected Distribution Lists"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script></script><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
	$("#myTable2").tablesorter(); 
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

echo '</head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')
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

#Assign USERNAME
DATANAME=USERNAME
get_data
USERNAME="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/email_protected_distribution_lists.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"The action cannot be blank."
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
[ -z "$ACTION" ] && ACTION=view
if [ "$ACTION" = delete ] || [ "$ACTION" = reallyadd ]
then
	if [ -z "$GROUP" ]
	then
		MESSAGE=$"You have not entered a username."
		show_status
	fi
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	ICON2="/images/submenus/email/alias_add.png"
	ICON3="/images/submenus/email/alias_view.png"
	WIDTH=100
	DIV_ID=actionbox3
	TABLECLASS=standard
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	ICON2="/images/submenus/email/alias_addm.png"
	ICON3="/images/submenus/email/alias_viewm.png"
	WIDTH=90
	DIV_ID=actionbox
	TABLECLASS=mobilestandard
fi

if [ "$ACTION" = viewusers ] || [ "$ACTION" = adduser ]
then
	ACTION2=view
	ICON=$ICON3
	MESSAGE=$"Protected Distribution Lists"
	MESSAGE2=$"View the protected distribution lists."
	HELPMSG=$"Adding a protected domain restricts which internal users can send to it."
else
	ACTION2=viewusers
	ICON=$ICON2
	MESSAGE=$"Allowed Users"
	MESSAGE2=$"View allowed users."
	HELPMSG=$"Only users added to the list can send E-mails to these distribution lists."
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Protected Distribution Lists"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
else
	echo '<div id="'"$DIV_ID"'"><div id="titlebox"><div class="sectiontitle">'$"Protected Distribution Lists"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=E-Mail_Protected_Distribution_Lists"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG'</span></a></div>'
fi

echo '
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/email_protected_distribution_lists.cgi" method="post">
			<button class="info infonavbutton" name="_DoAction_" value="_ACTION_'"$ACTION2"'_">
				<img src="'"$ICON"'" alt="'"$MESSAGE"'">
				<span>'"$MESSAGE2"'</span><br>
				'"$MESSAGE"'
			</button>
		</form>
	</td>

</tr></tbody></table>
'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/email_protected_distribution_lists.cgi | cut -d' ' -f1)
#Show aliases
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ACTION:$USERNAME:$GROUP:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/email_protected_distribution_lists
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
