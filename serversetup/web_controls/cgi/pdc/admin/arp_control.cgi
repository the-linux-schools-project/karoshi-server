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
echo '
<!DOCTYPE html><html><head><meta charset="UTF-8">
  <title>'$"ARP Controls"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	0: { sorter: "ipAddress" },
	1: { sorter: "MAC" }
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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\/*%+"-' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/QUADUNDERSCORE/_/g')
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

#Assign DEVICE
DATANAME=DEVICE
get_data
DEVICE="${DATAENTRY//UNDERSCORE/_}"

#Assign MACADDR
DATANAME=MACADDR
get_data
MACADDR="$DATAENTRY"

function show_status {
echo '<script>
alert("'"$MESSAGE"'");
window.location = "/cgi-bin/admin/arp_control.cgi";
</script></div></body></html>'
exit
}

if [ -z "$ACTION" ]
then
	ACTION=view
fi

#Check data

if [ "$ACTION" = static ] || [ "$ACTION" = dynamic ]
then
	if [ -z "$DEVICE" ]
	then
		MESSAGE=$"No TCPIP information has been received."
		show_status
	fi
	if [ -z "$MACADDR" ]
	then
		MESSAGE=$"No MAC address has been received."
		show_status
	fi

	#Check that tcpip number is correct
	#Check that we have 4 dots
	if [[ $(echo "$DEVICE" | sed 's/\./\n /g'  | sed /^$/d | wc -l) != 4 ]]
	then
		MESSAGE=$"The TCPIP number is not corrrect."
		show_status
	fi
	#Check that no number is greater than 255
	HIGHESTNUMBER=$(echo "$DEVICE" | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p)
	if [ "$HIGHESTNUMBER" -gt 255 ]
	then
		MESSAGE=$"The TCPIP number is not corrrect."
		show_status
	fi

	#Check that the mac address is correct
	#Check that we have 6 sets of data
	MACADDR2="${MACADDR//%3A/:}"

	if [[ $(echo "$MACADDR2" | sed 's/:/\n/g' | wc -l) != 6 ]]
	then
		echo "count is:"
		echo "$MACADDR2" | sed 's/:/\n/g' | wc -l
		echo "<br>"
		MESSAGE=''$"You have not entered in a valid mac address1."''
		show_status	
	fi
	#Check max chars
	for LINEDATA in ${MACADDR2//:/ }
	do
		if [[ $(echo "$LINEDATA" | wc -L) != 2 ]]
		then
			MESSAGE=''$"You have not entered in a valid mac address2."''
			show_status
		fi
	done
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
		<span>'$"ARP Controls"'</span>'
	if [ "$SERVERNAME" != notset ]
	then
		echo '<a href="/cgi-bin/admin/file_manager.cgi">'$"Select Server"'</a>'
	else
		echo '<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>'
	fi
	echo '</div></div>
	<div id="'"$DIV_ID"'">
	'

	else
		echo '<div id="'"$DIV_ID"'"><div id="titlebox">
	<table class="standard" style="text-align: left;" ><tbody>
	<tr>
	<td style="height:30px;"><div class="sectiontitle">'$"ARP Control"'</div></td>
	<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Arp_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows you to set static ARP entries for all of your servers to protect against ARP poisoning attacks."'</span></a></td></tr></tbody></table>
	<table class="standard" style="text-align: left;" ><tbody>
	<tr><td><img src="/images/help/warning.png" alt=""></td></tr>
	<tr><td>'$"Be careful using this feature."'</td></tr>
	<tr><td>'$"If you need to change a network card remove the mac address from your static arps first."'</td></tr>
	</tbody></table>
	</div><div id="infobox">'
fi

echo '<form action="/cgi-bin/admin/arp_control.cgi" method="post">'

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/arp_control.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$DEVICE:$MACADDR" | sudo -H /opt/karoshi/web_controls/exec/arp_control

echo '</form>'
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
