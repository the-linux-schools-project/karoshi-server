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
  <title>'$"View Assigned Printers"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
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
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

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

WIDTH=100
ICON1=/images/submenus/printer/view_print_queues.png
ICON2=/images/submenus/printer/delete_printer.png
ICON3=/images/submenus/file/folder.png

echo '<form action="/cgi-bin/admin/printers_view_assigned.cgi" method="post"><div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"View Assigned Printers"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_Assigned_Printers"><img class="images" alt="" src="/images/help/info.png"><span>'$"This shows the printers that have been assigned to locations."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="/cgi-bin/admin/printers.cgi" class="info infonavbutton" name="_ShowPrinters_" value="_">
			<img src="'"$ICON1"'" alt="'$"Show Printers"'">
			<span>'$"Show network printer queues."'</span><br>
			'$"Show Printers"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="/cgi-bin/admin/printers_delete.cgi" class="info infonavbutton" name="_DeletePrinters_" value="_">
			<img src="'"$ICON2"'" alt="'$"Delete Printer"'">
			<span>'$"Delete network printer queues."'</span><br>
			'$"Delete Printer"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="/cgi-bin/admin/locations.cgi" class="info infonavbutton" name="_ViewLocations_" value="_">
			<img src="'"$ICON3"'" alt="'$"Locations"'">
			<span>'$"View locations."'</span><br>
			'$"Locations"'
		</button>
	</td>

</tr></tbody></table></div><div id="infobox">
'

#Check to see that locations.txt exists
if [ ! -f /var/lib/samba/netlogon/locations.txt ]
then
	echo $"No Printers have been assigned to a location."'<br>'
	echo '</div></body></html>'
	exit
fi
COUNTER=$(grep -n ^--start-- /var/lib/samba/netlogon/printers.txt | cut -d: -f1)
let COUNTER="$COUNTER"+1
NOOFLINES=$(wc -l < /var/lib/samba/netlogon/printers.txt)

#Create top of table
echo '<table id="myTable" class="tablesorter" style="text-align: left;"><thead><tr><th style="width: 200px; height: 20px;"><b>'$"Location"'</b></th><th style="width: 150px;"><b>'$"Assigned Printers"'</b></th><th style="width: 80px;">'$"Default"'</th><th style="width: 80px;">'$"Remove"'</th></tr></thead><tbody>'
#Show locations and printers
while [ "$COUNTER" -le "$NOOFLINES" ]
do
	DATAENTRY=$(sed -n "$COUNTER,$COUNTER""p" /var/lib/samba/netlogon/printers.txt)
	#Assign data entry to an array
	if [ ! -z "$DATAENTRY" ]
	then
		DATARRAY=( ${DATAENTRY//,/ } )
		ARRAYCOUNT="${#DATARRAY[@]}"
		let ARRAYCOUNT="$ARRAYCOUNT"-1
		DEFAULTPRINTER="${DATARRAY[$ARRAYCOUNT]}"
		#Show printers
		ARRAYCOUNTER=2
		while [ "$ARRAYCOUNTER" -lt "$ARRAYCOUNT" ]
		do
			#Show location 
			echo '<tr><td style="height: 35px;">'"${DATARRAY[0]}"'</td><td>'"${DATARRAY[$ARRAYCOUNTER]}"'</td>'
			#Show printer actions
			#Set default option
			if [ "${DATARRAY[$ARRAYCOUNTER]}" != "$DEFAULTPRINTER" ]
			then
				echo '<td style="text-align: center;">

			<button class="info" name="____SetDefault____" value="____PRINTACTION____default:'"${DATARRAY[0]}"':'"${DATARRAY[$ARRAYCOUNTER]}"'____">
			<img src="/images/help/printer_make_default.png" alt="'$"Set Default"'">
			<span>'$"Set Default"'</span>
			</button>
			</td>'
			else
				echo '<td style="text-align: center;">
			<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/printer_default.png"><span>'$"Default Printer"'</span></a>
			'
			fi

			#Delete option
			echo '<td>
			<button class="info" name="____RemovePrinter____" value="____PRINTACTION____delete:'"${DATARRAY[0]}"':'"${DATARRAY[$ARRAYCOUNTER]}"'____">
			<img src="/images/submenus/printer/remove_printer.png" alt="'$"Remove Printer"'">
			<span>'$"Remove Printer"'</span>
			</button>
			</td></tr>'
			let ARRAYCOUNTER="$ARRAYCOUNTER"+1
		done
		#Clear array
		unset DATARRAY
	fi
	let COUNTER="$COUNTER"+1
done
#End table
echo '</tbody></table></div></div></form></div></body></html>'
exit

