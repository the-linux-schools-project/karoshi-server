#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"E-Mail Domains"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
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
	WIDTH=90
	ICON1="/images/submenus/system/addm.png"
	ICON2="/images/submenus/email/domainm.png"
	ICON3="/images/submenus/email/alias_viewm.png"
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
else
	WIDTH=100
	ICON1="/images/submenus/system/add.png"
	ICON2="/images/submenus/email/domain.png"
	ICON3="/images/submenus/email/alias_view.png"	
fi
echo '</head><body onLoad="start()"><div id="pagecontainer">'

DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+')

#########################
#Assign data to variables
#########################
END_POINT=15
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

#Assign DOMAIN
DATANAME=DOMAIN
get_data
DOMAIN="$DATAENTRY"

function show_status {
echo '<script>
alert("'"$MESSAGE"'");
window.location = "/cgi-bin/admin/email_domains.cgi";
</script></div></body></html>'
exit
}

if [ -z "$ACTION" ]
then
	ACTION=view
fi

ALTACTION=add
ALTMESSAGE=$"Add Domain"
ALTMESSAGE2=$"Add a domain."
ICON="$ICON1"
if [ "$ACTION" = add ]
then
	ALTACTION=view
	ALTMESSAGE=$"Domains"
	ALTMESSAGE2=$"View the E-Mail domains."
	ICON="$ICON2"
fi

#########################
#Check data
#########################
if [ "$ACTION" != add ] && [ "$ACTION" != reallyadd ] && [ "$ACTION" != reallydelete ] && [ "$ACTION" != delete ] && [ "$ACTION" != view ]
then
	MESSAGE=$"You have not entered a correct action."
	show_status
fi

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ]
then
	#Make sure that the domain is not blank
	if [ -z "$DOMAIN" ]
	then
		MESSAGE=$"The domain must not be blank."
		show_status
	fi
fi

if [ "$ACTION" = reallyadd ]
then
	source /opt/karoshi/server_network/domain_information/domain_name
	#Make sure that the domain is not the real domain
	if [ "$DOMAIN" = "$REALM" ]
	then
		MESSAGE=$"You cannot add the main domain as a virtual domain."
		show_status
	fi
	
	#Check that a domain has been entered
	if [[ $(echo "$DOMAIN" | grep -c "\.") = 0 ]]
	then
		MESSAGE=$"You have not entered in a valid domain."
		show_status
	fi
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=mobileactionbox
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"E-Mail Domains"'</span><a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a></div></div><div id="'"$DIV_ID"'">'

else
	echo '<div id="'"$DIV_ID"'"><div id="titlebox">
	<div class="sectiontitle">'$"E-Mail Domains"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=E-Mail_Domains"><img class="images" alt="" src="/images/help/info.png"><span>'$"This shows any domains that you have set up for your E-Mail system."'</span></a></div>'
fi

echo '
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/email_domains.cgi" method="post">
			<button class="info infonavbutton" name="_DoAction_" value="_ACTION_'"$ALTACTION"'_">
				<img src="'"$ICON"'" alt="'"$ALTMESSAGE"'">
				<span>'"$ALTMESSAGE2"'</span><br>
				'"$ALTMESSAGE"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/email_aliases.cgi" method="post">
			<button class="info infonavbutton" name="_ViewAliases_" value="_">
				<img src="'"$ICON3"'" alt="'$"Aliases"'">
				<span>'$"View user aliases."'</span><br>
				'$"Aliases"'
			</button>
		</form>
	</td>

</tr></tbody></table>
'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/email_domains.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$ACTION:$DOMAIN:" | sudo -H /opt/karoshi/web_controls/exec/email_domains

[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
