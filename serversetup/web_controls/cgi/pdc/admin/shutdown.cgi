#!/bin/bash
#Shutdown
#Copyright (C) 2007 Paul Sharrad

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
#  _SHUTDOWN_  This can only have one of two values - shutdown or reboot.

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
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Shutdown-Reboot Server"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
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
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')
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

#Assign SHUTDOWN_OPTION
DATANAME=SHUTDOWN
get_data
SHUTDOWN_OPTION="$DATAENTRY"

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

#Assign SHUTDOWNCODE
DATANAME=SHUTDOWNCODE
get_data
SHUTDOWNCODE="$DATAENTRY"

#Assign FORMCODE
DATANAME=FORMCODE
get_data
FORMCODE="$DATAENTRY"

#Assign FORCE
DATANAME=FORCE
get_data
FORCE="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/shutdown_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
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

if [[ $(grep -c ^"$REMOTE_USER": /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################
#Check to see that shutdown option is not blank
if [ -z "$SHUTDOWN_OPTION" ]
then
	MESSAGE=$"No shutdown option."
	show_status
fi

#Only allow shutdown and reboot.
if [ "$SHUTDOWN_OPTION" != shutdown ] && [ "$SHUTDOWN_OPTION" != reboot ] && [ "$SHUTDOWN_OPTION" != wakeonlan ]
then
	MESSAGE=$"You must only choose shutdown or reboot."
	show_status
fi
#Check to see that a server has been picked to shut down
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"You must choose a server to shut down."
	show_status
fi
#Check to see that a server type is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$"The server type cannot be blank."
	show_status
fi


#Check to see that SHUTDOWNCODE is not blank
if [ -z "$SHUTDOWNCODE" ]
then
	MESSAGE=$"The shutdown code must not be blank."
	show_status
fi
#Check to see that FORMCODE is not blank
if [ -z "$FORMCODE" ]
then
	MESSAGE=$"The form code must not be blank."
	show_status
fi
#Make sure that FORMCODE and SHUTDOWNCODE matches
if [ "$FORMCODE" != "$SHUTDOWNCODE" ]
then
	MESSAGE=$"Incorrect shutdown code."
	show_status
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox3
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Shutdown-Reboot Server"'</span>
<a href="/cgi-bin/admin/shutdown_fm.cgi">'"$SERVERNAME"'</a>
</div></div><div id="mobileactionbox">'
else
	echo '<div class="sectiontitle">'$"Shutdown-Reboot Server"'</div><div id="infobox">'
fi

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/shutdown.cgi | cut -d' ' -f1)
#Shutdown server
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SHUTDOWN_OPTION:$FORCE:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/shutdown
if [ "$?" = 102 ]
then
	MESSAGE=$"The form code must not be blank."
	show_status
fi

[ "$MOBILE" = no ] && echo '</div>'

echo "</div>"
echo "</div></body></html>"
exit
