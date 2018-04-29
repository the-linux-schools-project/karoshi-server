#!/bin/bash
#Copyright (C) 2018 Paul Sharrad

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

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/printers_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Airprint"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js1">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	3: { sorter: false},
	4: { sorter: false}
    		}
		});
    }
);
</script>
<script id="js2">
$(document).ready(function() 
    { 
        $("#myTable2").tablesorter(); 
    } 
);
</script>
<script id="js3">
$(document).ready(function() 
    { 
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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g')
#########################
#Assign data to variables
#########################
END_POINT=9
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

#Assign PRINTER
DATANAME=PRINTER
get_data
PRINTER="${DATAENTRY//12345UNDERSCORE12345/_}"

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="${DATAENTRY//12345UNDERSCORE12345/_}"

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

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

#Check that a print server has been declared
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$"A print server has not yet been set up."'")';
echo 'window.location = "karoshi_servers_view.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

[ ! -f /opt/karoshi/server_network/printserver ] && show_status
PRINTSERVER=$(sed -n 1,1p /opt/karoshi/server_network/printserver)

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then

	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Manage Print Queues"'</span>'
	if [ -z "$PRINTER" ]
	then
		echo '<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>'
	else
		echo '<a href="/cgi-bin/admin/printers.cgi">'$"View Print Queues"'</a>'
	fi
	echo '</div></div>'
else

	WIDTH=100
	ICON1=/images/submenus/printer/view_print_queues.png
	ICON2=/images/submenus/printer/add_printer.png
	ICON3=/images/submenus/printer/delete_printer.png
	ICON4=/images/submenus/printer/assign_ppd.png
	ICON5=/images/submenus/printer/edit_ppd.png
	ICON6=/images/submenus/printer/win_print_gen.png
	ICON7=/images/submenus/printer/savapage.png
	ICON8=/images/submenus/file/folder.png
	ICON9=/images/submenus/printer/view_print_queues.png

	echo '<div id="titlebox">
	<div class="sectiontitle">'$"Manage AirPrint"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Manage_AirPrint"><img class="images" alt="" src="/images/help/info.png"><span>'$"Click on the icons to control Airprint availability."'</span></a></div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/printers.cgi" name="ShowPrinters" method="post">
				<button class="info infonavbutton" name="_ShowPrinters_" value="_">
					<img src="'"$ICON1"'" alt="'$"Show Printers"'">
					<span>'$"Show network printer queues."'</span><br>
					'$"Show Printers"'
				</button>
			</form>
		</td>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/printers_add_fm.cgi" name="AddPrinters" method="post">
				<button class="info infonavbutton" name="_AddPrinter_" value="_">
					<img src="'"$ICON2"'" alt="'$"Add Printer"'">
					<span>'$"Add a new printer queue."'</span><br>
					'$"Add Printer"'
				</button>
			</form>
		</td>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/printers_delete.cgi" name="DeletePrinters" method="post">
				<button class="info infonavbutton" name="_DeletePrinter_" value="_">
					<img src="'"$ICON3"'" alt="'$"Delete Printer"'">
					<span>'$"Delete a new printer queue."'</span><br>
					'$"Delete Printer"'
				</button>
			</form>
		</td>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/printers_view_assigned_fm.cgi" name="AssignedPrinters" method="post">
				<button class="info infonavbutton" name="_AssignedPrinter_" value="_">
					<img src="'"$ICON4"'" alt="'$"Assigned Printers"'">
					<span>'$"View Assigned Printers."'</span><br>
					'$"Assigned Printers"'
				</button>
			</form>
		</td>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/file_manager.cgi" name="EditPPDs" method="post">
				<button class="info infonavbutton" name="_EditPPD_" value="_SERVERTYPE_network_ACTION_ENTER_SERVERNAME_'"$PRINTSERVER"'_LOCATION_/etc/cups/ppd_">
					<img src="'"$ICON5"'" alt="'$"Edit PPD"'">
					<span>'$"Edit a printer driver."'</span><br>
					'$"Edit PPD"'
				</button>
			</form>
		</td>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="printer_driver_gen.cgi" name="WindowsPrinterDrivers" method="post">
				<button class="info infonavbutton" name="_WindowsDriverGen_" value="_">
					<img src="'"$ICON6"'" alt="'$"Edit PPD"'">
					<span>'$"Windows printer drivers."'</span><br>
					'$"Windows Drivers"'
				</button>
			</form>
		</td>

	'


	if [ -f /opt/karoshi/server_network/servers/"$PRINTSERVER"/savapage ]
	then
		echo '
			<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
				<form action="http://savapage:8631/admin" name="Savapage" method="post">
					<button class="info infonavbutton" name="_Savapage_" value="_">
						<img src="'"$ICON7"'" alt="Savapage">
						<span>'$"Configure printing with Savapage."'</span><br>
						Savapage
					</button>
				</form>
			</td>

		'
	fi

	echo '
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/locations.cgi" name="PrinterLocations" method="post">
				<button class="info infonavbutton" name="_ViewLocations_" value="_">
					<img src="'"$ICON8"'" alt="'$"Locations"'">
					<span>'$"View locations."'</span><br>
					'$"Locations"'
				</button>
			</form>
		</td>

	'


	if [ ! -z "$PRINTER" ]
	then
		echo '
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/printers.cgi" name="ShowPrinters" method="post">
				<button class="info infonavbutton" name="_ShowPrinters_" value="_">
					<img src="'"$ICON9"'" alt="'$"Show Printers"'">
					<span>'$"Show network printer queues."'</span><br>
					'$"Show Printers"'
				</button>
			</form>
		</td>

		'
	fi

	echo '</tr></tbody></table></div>'
fi

[ "$MOBILE" = no ] && echo '<div id="infobox">'

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/printers_airprint.cgi | cut -d' ' -f1)
sudo -H /opt/karoshi/web_controls/exec/printers_airprint "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$MOBILE:$PRINTER:$ACTION:"
[ "$MOBILE" = no ] && echo '</div>'
echo "</div></div></body></html>"
exit
