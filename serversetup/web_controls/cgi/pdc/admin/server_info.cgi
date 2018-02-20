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
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/server_info_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')
#########################
#Assign data to variables
#########################
END_POINT=26
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

#Assign INFO
DATANAME=INFO
get_data
INFO="$DATAENTRY"

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

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Server Information"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
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

echo '</head><body><div id="pagecontainer">'

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
#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"You must choose a server."
	show_status
fi

#Check to see that INFO is not blank
if [ -z "$INFO" ]
then
	MESSAGE=$ERRORMSG8
	show_status
fi

#Check to see that SERVERTYPE is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$ERRORMSG9
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

if [ "$INFO" = cpu ]
then
	TITLE=$"CPU Usage"
elif [ "$INFO" = kernel ]
then
	TITLE=$"Kernel"
elif [ "$INFO" = samba ]
then
	TITLE=$"Samba information"
elif [ "$INFO" = harddrive ]
then
	TITLE=$"Hard disk usage"
fi


[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'
#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	SERVERNAME2=$(echo "${SERVERNAME:0:9}" | cut -d. -f1)
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Server Information"' - '"$SERVERNAME2"'</span>
<a href="/cgi-bin/admin/server_info_fm.cgi">'$"Select Server"'</a>
</div></div><div id="mobilecontent"><div id="mobileactionbox2">'
else

	WIDTH=100
	ICON1=/images/submenus/system/computer.png

	echo '

	<div class="sectiontitle">'$TITLE - "$SERVERNAME"'</div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form name="myform" action="server_info_fm.cgi" method="post">
				<button class="info infonavbutton" name="SelectServer" value="_">
					<img src="'"$ICON1"'" alt="'$"Select server"'">
					<span>'$"Select the server you want to view."'</span><br>
					'$"Select Server"'
				</button>
			</form>
		</td>

	</tr></tbody></table>

	</div><div id="infobox">'
fi

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/server_info.cgi | cut -d' ' -f1)
sudo -H /opt/karoshi/web_controls/exec/server_info "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$INFO:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$MOBILE:"
EXEC_STATUS="$?"

if [ "$EXEC_STATUS" = 102 ]
then
	MESSAGE="$COMPLETEDMSG "$"Please check the karoshi web administration logs for more details."
	show_status
fi

if [ "$EXEC_STATUS" = 103 ]
then
	echo '<br><b>'"$CHECKCOMPLETEDMSG"'</b><br>'
fi
echo "</div></div></div></body></html>"
exit
