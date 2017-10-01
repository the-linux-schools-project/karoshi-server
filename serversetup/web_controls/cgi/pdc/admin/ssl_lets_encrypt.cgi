#!/bin/bash
#Copyright (C) 2016  Paul Sharrad

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>'$"Let's Encrypt SSL Certificates"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script>
<!--
function SetAllCheckBoxes(FormName, FieldName, CheckValue)
{
	if(!document.forms[FormName])
		return;
	var objCheckBoxes = document.forms[FormName].elements[FieldName];
	if(!objCheckBoxes)
		return;
	var countCheckBoxes = objCheckBoxes.length;
	if(!countCheckBoxes)
		objCheckBoxes.checked = CheckValue;
	else
		// set the check value for all check boxes
		for(var i = 0; i < countCheckBoxes; i++)
			objCheckBoxes[i].checked = CheckValue;
}
// -->
  </script>
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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-+')
#########################
#Assign data to variables
#########################
END_POINT=19
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

#Assign SERVERNAME
DATANAME=SERVERNAME
get_data
SERVERNAME="$DATAENTRY"

DATANAME=CUSTOMWEBADDRESS
get_data
CUSTOMWEBADDRESS="$DATAENTRY"

DATANAME=MODE
get_data
MODE="$DATAENTRY"

[ -z "$MODE" ] && MODE=auto

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/admin/ssl_lets_encrypt.cgi" name="selectservers" method="post">'

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Let's Encrypt SSL Certificates"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
else
	echo '<table class="standard" style="text-align: left;" ><tbody><tr>
<td style="height:30px;"><div class="sectiontitle">'$"Let's Encrypt SSL Certificates"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=SSL_Let%27s_Encrypt"><img class="images" alt="" src="/images/help/info.png"><span>'$"Apply a Let's Encrypt SSL certificate to a server."'</span></a></td></tr></tbody></table><br>
</div><div id="infobox">'
fi

if [ -z "$SERVERNAME" ]
then
	#Show custom alias box
	echo '
	<table class="standard" style="text-align: left;" ><tbody>
	<tr style="vertical-align:middle">
		<td style="width: 230px; height: 26px;">'$"Web Address Mode"'</td><td>'
		if [ "$MODE" = auto ]
		then
			echo '<input name="_MODE_manual_" type="submit" class="button" value='$"Auto"'>'
		else
			echo '<input name="_MODE_auto_" type="submit" class="button" value='$"Manual"'>'
		fi
	echo ' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=SSL_Let%27s_Encrypt"><img class="images" alt="" src="/images/help/info.png"><span>'$"In auto mode the web addresses of the server are automatically entered for the certificate based on the modules that have been applied to the server. Manual mode allows you to enter in custom web addresses for the certificate."'</span></a></td><td></td></tr>'
	if [ "$MODE" = auto ]
	then
		echo '<tr><td style="height: 26px;"></td><td></td><td></td></tr>'
	else
		echo '<tr>
		<td style="height: 26px;">'$"Custom Alias"'</td>
		<td><input tabindex="1" name="_CUSTOMWEBADDRESS_" size="20" type="text"></td><td style="vertical-align:bottom"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=SSL_Let%27s_Encrypt"><img class="images" alt="" src="/images/help/info.png"><span>'$"This field should normally be left blank to automtically create the certificate for the server. Enter in a web address if you want to override the default web addresses of the server."'</span></a></td>
	</tr>'
	fi
	echo '</tbody></table>'

	#Show list of servers
	/opt/karoshi/web_controls/show_servers "$MOBILE" servers $"Apply"
else
	#Show any assigned aliases for the server.
	#Show alias choice
	source /opt/karoshi/server_network/domain_information/domain_name
	if [ -f /opt/karoshi/server_network/webservers/"$SERVERNAME" ]
	then
		#Show any custom aliases that have been assigned
		echo "<ul><li>$SERVERNAME" - $"Creating an SSl certificate for the following domain entries""</li></ul>"

		if [ -z "$CUSTOMWEBADDRESS" ]
		then
			for CUSTOM_ALIAS in $(cat /opt/karoshi/server_network/aliases/"$SERVERNAME")
			do
				echo "<ul><li>$CUSTOM_ALIAS.$REALM</li></ul>"
				ALIASLIST="$ALIASLIST,$CUSTOM_ALIAS.$REALM"
			done
			ALIASLIST=$(echo "$ALIASLIST" | sed 's/^,//g')
		else
			ALIASLIST="${CUSTOMWEBADDRESS//+/ }"
			for CUSTOM_ALIAS in $ALIASLIST
			do
				echo "<ul><li>$CUSTOM_ALIAS</li></ul>"
			done
			ALIASLIST="${CUSTOMWEBADDRESS// /,}"
		fi
		ACTION=addcert
		MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/ssl_lets_encrypt.cgi | cut -d' ' -f1)
		echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$ALIASLIST:$ACTION:" | sudo -H /opt/karoshi/web_controls/exec/ssl_lets_encrypt
	else
		echo "<ul><li>$SERVERNAME: This server has not been set up as a web server</li></ul>"	
	fi
fi

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></form></div></body></html>'
exit
