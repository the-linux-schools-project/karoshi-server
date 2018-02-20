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
[ -f "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER" ] && source "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER"
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
  <title>'$"DHCP Reservations"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	1: { sorter: "MAC" },
	2: { sorter: "ipAddress" },
	3: { sorter: false},
	4: { sorter: false}
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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+')

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

#Assign CLIENTHOSTNAME
DATANAME=CLIENTHOSTNAME
get_data
CLIENTHOSTNAME="$DATAENTRY"

#Assign MACADDRESS
DATANAME=MACADDRESS
get_data
MACADDRESS=${DATAENTRY//%3A/:}

#Assign TCPIPADDRESS
DATANAME=TCPIPADDRESS
get_data
TCPIPADDRESS="$DATAENTRY"

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

[ -z "$ACTION" ] && ACTION=view

function show_warnings {
echo '<script>
alert("'"$MESSAGE"'");
window.location = "/cgi-bin/admin/dhcp_reservations.cgi";
</script>'

exit
}

function checkIpNotInRange {
source /opt/karoshi/server_network/dhcp/dhcp_settings

	function convert_ip_to_int {
	IFS=. read -r a b c d <<< "$ip"
	printf '%s%d\n' "$((a * 256 ** 3 + b * 256 ** 2 + c * 256 + d))"
	}


ip="$STARTADDRESS"
int_range_start=$(convert_ip_to_int)

ip="$ENDADDRESS"
int_range_end=$(convert_ip_to_int)

ip="$TCPIPADDRESS"
int_ip_num=$(convert_ip_to_int)

#Check if ip is inside the range

if [ "$int_ip_num" -ge "$int_range_start" ] && [ "$int_ip_num" -le "$int_range_end" ]
then
	if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallyedit ]
	then
		ACTION=view
		MESSAGE=$"This TCPIP address is inside the DHCP reservation range."
		show_warnings
	fi
	if [ "$ACTION" = edit ] || [ "$ACTION" = add ]
	then
		TCPIPADDRESS=""
	fi
fi
}

#Check data

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallyedit ] || [ "$ACTION" = delete ]
then
	#Check that clienthostname is not blank
	if [ -z "$CLIENTHOSTNAME" ]
	then
		ACTION=view
		MESSAGE=$"You have not entered in a client name."
		show_warnings
	fi
fi

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallyedit ]
then
	#Check that tcpip is not blank
	if [ -z "$TCPIPADDRESS" ]
	then
		ACTION=view
		MESSAGE=$"You have not entered in a TCPIP address."
		show_warnings
	else
		#Check that the tcpip number has been entered correctly
		#Check dots
		if [[ $(echo "$TCPIPADDRESS" | sed 's/\./\n /g'  | sed /^$/d | wc -l) != 4 ]]
		then
			ACTION=view
			MESSAGE=$"You have not entered in a correct tcpip address."
			show_warnings
		fi
		#Check that no number is greater than 255
		HIGHESTNUMBER=$(echo "$TCPIPADDRESS" | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p)
		if [ "$HIGHESTNUMBER" -gt 255 ]
		then
			ACTION=view
			MESSAGE=$"You have not entered in a correct tcpip address."
			show_warnings
		fi
		#Check to see that the tcpip number has not already been added
		if [[ $(grep -r -H -w "$TCPIPADDRESS" /opt/karoshi/server_network/dhcp/reservations/ | grep -v -w "$CLIENTHOSTNAME" | grep -c -w "$TCPIPADDRESS") -gt 0 ]]
		then
				ACTION=view
				MESSAGE=$"This TCPIP address is already in use."
				show_warnings
		fi
		#Check that tcpip number is not in the dhcp reservation range
		checkIpNotInRange


	fi
	#Check that mac address is not blank
	if [ -z "$MACADDRESS" ]
	then
		ACTION=view
		MESSAGE=$"You have not entered a mac address."
		show_warnings
	else
		#Check that the mac address is formatted correctly
		#Check colons 00:13:77:b8:39:17
		if [[ $(echo "$MACADDRESS" | sed 's/:/\n/g' | wc -l) != 6 ]]
		then
			ACTION=view
			MESSAGE=$"You have not entered in a valid mac address."
			show_warnings	
		fi
		#Check max chars
		for LINEDATA in $(echo "$MACADDRESS" | sed 's/:/\n/g')
		do
			if [[ $(echo "$LINEDATA" | wc -L) != 2 ]]
			then
				ACTION=view
				MESSAGE=$"You have not entered in a valid mac address."
				show_warnings
			fi
		done
		#Check to see that the mac address has not already been added
		if [[ $(grep -r -H -w "$MACADDRESS" /opt/karoshi/server_network/dhcp/reservations/ | grep -v -w "$CLIENTHOSTNAME" | grep -c -w "$MACADDRESS") -gt 0 ]]
		then
				ACTION=view
				MESSAGE=$"This mac address is already in use."
				show_warnings
		fi
	fi
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	WIDTH=100
	WIDTH1=180
	WIDTH2=110
	WIDTH3=110
	WIDTH4=70	
	WIDTH5=200
	ICON1=/images/submenus/system/edit.png
	ICON2=/images/submenus/system/delete.png
	ICON3=/images/submenus/system/import.png
	ICON4=/images/submenus/system/add.png
	ICON5=/images/submenus/system/lock.png
	ICON6=/images/submenus/system/dhcp.png
	ICON7=/images/submenus/system/edit.png
	ICON8=/images/submenus/system/delete.png
	ICON9=/images/submenus/system/reload.png
	TABLECLASS=standard
	MACTITLE=$"Mac Address"
	TCPIPTITLE=$"TCP IP Address"

	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	WIDTH=90
	WIDTH1=80
	WIDTH2=100
	WIDTH3=80
	WIDTH4=70
	WIDTH5=150
	ICON1=/images/submenus/system/editm.png
	ICON2=/images/submenus/system/deletem.png
	ICON3=/images/submenus/system/import.png
	ICON4=/images/submenus/system/add.png
	ICON5=/images/submenus/system/lock.png
	ICON6=/images/submenus/system/dhcp.png
	ICON7=/images/submenus/system/edit.png
	ICON8=/images/submenus/system/delete.png
	ICON9=/images/submenus/system/reload.png
	TABLECLASS=mobilestandard
	MACTITLE=$"Mac"
	TCPIPTITLE=$"TCP IP"
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

echo '<form name="reservervationbuttons" action="/cgi-bin/admin/dhcp_reservations.cgi" method="post">'

if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"DHCP Reservations"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="mobileactionbox">
	<table class="tablesorter"><tbody><tr>
'
	if [ "$ACTION" = view ]
	then
		echo '
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info infonavbutton" name="_AddDHCPReservation_" value="_ACTION_add_reservation_">
				<img src="'$ICON4'" alt="'$"Add DHCP Reservation"'">
				<span>'$"Add DHCP Reservation"'</span><br>
				'$"Add"'
			</button>
		</td>
		'
	else
		echo '
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info infonavbutton" name="_ViewDHCPReservations_" value="_ACTION_view_">
				<img src="'$ICON5'" alt="'$"View DHCP Reservations"'">
				<span>'$"View DHCP Reservations"'</span><br>
				'$"View"'
			</button>
		</td>
		'
	fi
	echo '</tr></tbody></table></form>'
else

	echo '

	<div class="sectiontitle">'$"DHCP Reservations"'</div><table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<button class="info infonavbutton" formaction="dhcp_import_reservations_fm.cgi" name="_ImportDHCPReservations_" value="_">
			<img src="'$ICON3'" alt="'$"Import DHCP Reservations"'">
			<span>'$"Import DHCP Reservations"'</span><br>
			'$"Import"'
		</button>
	</td>

	'
	if [ "$ACTION" = view ]
	then
		echo '
			<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
				<button class="info infonavbutton" name="_AddDHCPReservation_" value="_ACTION_add_reservation_">
					<img src="'$ICON4'" alt="'$"Add DHCP Reservation"'">
					<span>'$"Add DHCP Reservation"'</span><br>
					'$"Add"'
				</button>
			</td>

		'
	else
		echo '
			<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
				<button class="info infonavbutton" name="_ViewDHCPReservations_" value="_ACTION_view_">
					<img src="'$ICON5'" alt="'$"View DHCP Reservations"'">
					<span>'$"View DHCP Reservations"'</span><br>
					'$"View"'
				</button>
			</td>

		'
	fi

	echo '

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info infonavbutton" formaction="dhcp_view_leases.cgi" name="_ViewDHCPleases_" value="_">
				<img src="'$ICON6'" alt="'$"View DHCP Leases"'">
				<span>'$"View DHCP Leases"'</span><br>
				'$"Leases"'
			</button>
		</td>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info infonavbutton" formaction="dhcp_fm.cgi" name="_ConfigureDHCP_" value="_">
				<img src="'$ICON7'" alt="'$"Configure DHCP"'">
				<span>'$"Configure DHCP"'</span><br>
				'$"Configure"'
			</button>
		</td>
	'
	if [ -d /opt/karoshi/server_network/dhcp/reservations_delete ]
	then
		echo '
			<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
				<button class="info infonavbutton" name="_DeleteAll_" value="_ACTION_reallydelete_">
					<img src="'$ICON8'" alt="'$"Delete DHCP reservations"'">
					<span>'$"Delete DHCP reservations"'</span><br>
					'$"Delete"'
				</button>
			</td>

		'

	fi
	if [ -f /opt/karoshi/server_network/dhcp/restart_required ]
	then
		echo '
			<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
				<button class="info infonavbutton" name="_ActivateChanges_" value="_ACTION_restartdhcp_">
					<img src="'$ICON9'" alt="'$"Activate Changes"'">
					<span>'$"Activate Changes"'</span><br>
					'$"Activate Changes"'
				</button>
			</td>
		'
	fi
	echo '</tr></tbody></table></form></div><div id="infobox">
	'
fi

function view_reservations {

SHOWENTRIES=no
if [ -d /opt/karoshi/server_network/dhcp/reservations ]
then
	if [[ $(ls -1 /opt/karoshi/server_network/dhcp/reservations | wc -l) -gt 0 ]]
	then
		SHOWENTRIES=yes

		echo '<form id="reservervations" name="reservervations" action="/cgi-bin/admin/dhcp_reservations.cgi" method="post"><table id="myTable" class="tablesorter" style="text-align: left;" ><thead>
		<tr>'
		[ "$MOBILE" = no ] && echo '<th style="width: '"$WIDTH1"'px;"><b>'$"Host name"'</b></th>'
		echo '<th style="width: '"$WIDTH2"'px;"><b>'"$MACTITLE"'</b></th><th style="width:'"$WIDTH3"'px;"><b>'"$TCPIPTITLE"'</b></th><th style="width:'"$WIDTH4"'px;">'$"Edit"'</th><th style="width:'"$WIDTH4"'px;">'
		if [ ! -d /opt/karoshi/server_network/dhcp/reservations_delete/ ]
		then
			echo '<button class="button" name="_DeleteAll_" value="_ACTION_deleteall_CLIENTHOSTNAME_deleteall_">
			'$"Select all"'
			</button>'
		else
			echo '<button class="button" name="_DeleteAll_" value="_ACTION_clearall_CLIENTHOSTNAME_clearall_">
			'$"Clear all"'
			</button>'
		fi
		echo '</th></tr></thead><tbody>'

		for CLIENTHOSTNAMES in /opt/karoshi/server_network/dhcp/reservations/*
		do
			CLIENTHOSTNAME=$(basename "$CLIENTHOSTNAMES")
			ALTDELETEMSG=$"Delete reservation"
			DELETEACTION=delete
			DELETESTYLE=""
			if [ -f /opt/karoshi/server_network/dhcp/reservations_delete/"$CLIENTHOSTNAME" ]
			then
				ALTDELETEMSG=$"Cancel delete reservation"
				DELETEACTION=canceldelete
				DELETESTYLE='style="color: #FFF; background-color:#CA0D26"'
			fi
			#Get details
			source "$CLIENTHOSTNAMES"
			echo '<tr>'
			if [ "$MOBILE" = no ]
			then
				echo '<td id="'"$CLIENTHOSTNAME"'" '"$DELETESTYLE"'>'"$CLIENTHOSTNAME"'</td><td '"$DELETESTYLE"'>'"$MACADDRESS"'</td>'
			else
				echo '<td id="'"$CLIENTHOSTNAME"'" '"$DELETESTYLE"'>'"$MACADDRESS"'</td>'
			fi
			echo '<td '"$DELETESTYLE"'>'"$TCPIPADDRESS"'</td><td '"$DELETESTYLE"'>'
			if [ -z "$DELETESTYLE" ]
			then
				echo '<button class="info" name="_Edit_" value="_ACTION_edit_'"$CLIENTHOSTNAME"'_CLIENTHOSTNAME_'"$CLIENTHOSTNAME"'_MACADDRESS_'"$MACADDRESS"'_TCPIPADDRESS_'"$TCPIPADDRESS"'_">
			<img src="'"$ICON1"'" alt="'$"Edit reservation"'">
			<span>'$"Edit reservation"'</span>
			</button>'
			fi
			echo '</td><td '"$DELETESTYLE"'>
			<button class="info" name="_Delete_" value="_ACTION_'"$DELETEACTION"'_CLIENTHOSTNAME_'"$CLIENTHOSTNAME"'_">
			<img src="'"$ICON2"'" alt="'"$ALTDELETEMSG"'">
			<span>'"$ALTDELETEMSG"'</span>
			</button>
			</td></tr>'
		done
		echo '</tbody></table></form><br>'
	fi
fi

if [ "$SHOWENTRIES" = no ]
then
	echo $"There are no current dhcp reservations.""<br>"
fi
}


function add_reservation {
if [ "$ACTION" = add ]
then
	FORMACTION=reallyadd
else
	FORMACTION=reallyedit
fi

#Check that the ip address is outside of the dns reservation range
checkIpNotInRange
	MACTITLE=$"Mac"
	TCPIPTITLE=$"TCP IP"
echo '<form name="addreservervation" action="/cgi-bin/admin/dhcp_reservations.cgi" method="post"><input type="hidden" name="_ACTION_'"$FORMACTION"'_" value="English"><table class="'"$TABLECLASS"'" style="text-align: left;" ><tbody>
<tr><td style="width: '"$WIDTH1"'px;">'$"Host name"'</td>
<td><input required="required" tabindex= "1" style="width: '"$WIDTH5"'px;" name="_CLIENTHOSTNAME_" value="'"$CLIENTHOSTNAME"'" 
 size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Reservation"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the host name of the client computer or device that you want to give a static tcpip address to."'</span></a></td></tr>
<tr><td>'"$MACTITLE"'</td><td><input required="required" tabindex= "2" style="width: '"$WIDTH5"'px;" name="_MACADDRESS_" value="'"$MACADDRESS"'"
 size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Reservation"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the mac address of the client computer or device that you want to give a static tcpip address to."'</span></a></td></tr>
<tr><td>'"$TCPIPTITLE"'</td><td><input required="required" tabindex= "3" style="width: '"$WIDTH5"'px;" name="_TCPIPADDRESS_"  value="'"$TCPIPADDRESS"'"
 size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Reservation"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the tcpip address that you want the client computer or device to have."'</span></a></td></tr> 
</tbody></table><br>'

echo '<br>'

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></form>'
}

[ "$ACTION" = view ] && view_reservations
[ "$ACTION" = add ] && add_reservation
[ "$ACTION" = edit ] && add_reservation

if [ "$ACTION" = reallyedit ] || [ "$ACTION" = reallydelete ] || [ "$ACTION" = delete ] || [ "$ACTION" = canceldelete ] || [ "$ACTION" = deleteall ] || [ "$ACTION" = clearall ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = restartdhcp ]
then
	MACADDRESS=$(echo "$MACADDRESS" | sed 's/:/%3A/g')
	Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/dhcp_reservations.cgi | cut -d' ' -f1)
	echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ACTION:$CLIENTHOSTNAME:$MACADDRESS:$TCPIPADDRESS:" | sudo -H /opt/karoshi/web_controls/exec/dhcp_reservations
	#view_reservations
	FORMID=reservations
	if [ "$ACTION" = delete ] || [ "$ACTION" = canceldelete ]
	then
		FORMID="$CLIENTHOSTNAME"
	fi
	#Reload page
	echo '<form id="'"$FORMID"'" name="reservervations" action="/cgi-bin/admin/dhcp_reservations.cgi#'"$FORMID"'" method="post"><script>
	document.getElementById("'"$FORMID"'").submit();
	</script></form>'

fi
echo '</div></div></div></body></html>'
exit
