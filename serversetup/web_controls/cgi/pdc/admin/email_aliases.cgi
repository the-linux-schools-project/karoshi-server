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
if [ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]
then
	TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"E-Mail Aliases"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script></script><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
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

#Assign ALIAS
DATANAME=ALIAS
get_data
ALIAS="$DATAENTRY"

#Assign USERNAME
DATANAME=USERNAME
get_data
USERNAME="$DATAENTRY"

#Assign DOMAIN
DATANAME=DOMAIN
get_data
DOMAIN="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/email_aliases.cgi";'
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
	if [ -z "$ALIAS" ]
	then
		MESSAGE=$"You have not entered an alias."
		show_status
	fi
	if [ -z "$USERNAME" ]
	then
		MESSAGE=$"You have not entered a username."
		show_status
	fi
	#Check that the username exists
	getent passwd "$USERNAME" 1>/dev/null
	if [ "$?" != 0 ]
	then
		MESSAGE=$"The username does not exist."
		show_status
	fi
	#Check that the domain is not blank
	if [ -z "$DOMAIN" ]
	then
		MESSAGE=$"The domain cannot be blank."
		show_status
	fi
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	WIDTH=100
	ICON1="/images/submenus/system/add.png"
	ICON2="/images/submenus/email/alias_view.png"
	ICON3="/images/submenus/system/edit.png"
	DIV_ID=actionbox3
	TABLECLASS=standard
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	WIDTH=90
	ICON1="/images/submenus/system/addm.png"
	ICON2="/images/submenus/email/alias_viewm.png"
	ICON3="/images/submenus/system/editm.png"
	DIV_ID=actionbox
	TABLECLASS=mobilestandard
fi

if [ "$ACTION" = add ] || [ "$ACTION" = delete ]
then
	ACTION2=view
	ICON="$ICON2"
	MESSAGE=$"Aliases"
	MESSAGE2=$"View the current aliases."
	HELPMSG=$"Adding an alias will allow emails to be sent to the alias address rather than the actual username."
else
	ACTION2=add
	ICON="$ICON1"
	MESSAGE=$"Add Alias"
	MESSAGE2=$"Add an alias."
	HELPMSG=$"These are the email aliases that are currently active for your email system."
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"E-Mail Aliases"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
else
	echo '<div id="'$DIV_ID'"><div id="titlebox">
	<div class="sectiontitle">'$"E-Mail Aliases"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=E-Mail_Aliases"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG'</span></a></div>'
fi

echo '
<form action="/cgi-bin/admin/email_aliases.cgi" method="post">
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<button class="info infonavbutton" name="_DoAction_" value="_ACTION_'$ACTION2'_">
				<img src="'"$ICON"'" alt="'$MESSAGE'">
				<span>'$MESSAGE2'</span><br>
				'$MESSAGE'
			</button>
		</td>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<button class="info infonavbutton" formaction="email_domains.cgi" name="_AddDomain_" value="_">
				<img src="'"$ICON3"'" alt="'$"Domains"'">
				<span>'$"View the defailt domains."'</span><br>
				'$"Domains"'
			</button>
		</td>

	</tr></tbody></table>
</form><br>
'

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/email_aliases.cgi | cut -d' ' -f1)
#Show aliases
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$ALIAS:$USERNAME:$DOMAIN:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/email_aliases
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
