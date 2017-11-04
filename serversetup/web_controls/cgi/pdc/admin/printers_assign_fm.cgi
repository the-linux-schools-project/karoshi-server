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
  <title>'$"Assign Printers to Locations"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
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
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body onLoad="start()"><div id="pagecontainer">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

function no_locations {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/locations.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g')
#########################
#Assign data to variables
#########################
END_POINT=3
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

#Assign _PRINTERNAME_
DATANAME=PRINTERNAME
get_data
PRINTERNAME="${DATAENTRY//12345UNDERSCORE12345/_}"

#Check to see that PRINTER is not blank
if [ -z "$PRINTERNAME"	 ]
then
	MESSAGE=$"You have not chosen any printers."
	show_status
fi

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
fi

echo '<form action="/cgi-bin/admin/printers_assign.cgi" method="post"><div id="actionbox3"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<table class="standard" style="text-align: left;">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Assign Printers to Locations"'</b></a></td></tr></tbody></table>'
else

	WIDTH=100
	ICON1=/images/submenus/printer/view_print_queues.png
	ICON2=/images/submenus/printer/delete_printer.png
	ICON3=/images/submenus/printer/assign_ppd.png
	ICON4=/images/submenus/file/folder.png

	echo '


	<div class="sectiontitle">'$"Assign Printers to Locations"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Add a network printer for your client computers."'</span></a></div>
	<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="/cgi-bin/admin/printers.cgi" class="info" name="_ShowPrinters_" value="_">
			<img src="'"$ICON1"'" alt="'$"Show Printers"'">
			<span>'$"Show network printer queues."'</span><br>
			'$"Show Printers"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="/cgi-bin/admin/printers_delete.cgi" class="info" name="_DeletePrinters_" value="_">
			<img src="'"$ICON2"'" alt="'$"Delete Printer"'">
			<span>'$"Delete network printer queues."'</span><br>
			'$"Delete Printer"'
		</button>
	</td>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<button formaction="/cgi-bin/admin/printers_view_assigned_fm.cgi" class="info" name="_AssignedPrinter_" value="_">
				<img src="'"$ICON3"'" alt="'$"Assigned Printers"'">
				<span>'$"View Assigned Printers"'</span><br>
				'$"Assigned Printers"'
			</button>
		</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="/cgi-bin/admin/locations.cgi" class="info" name="_ViewLocations_" value="_">
			<img src="'"$ICON4"'" alt="'$"Locations"'">
			<span>'$"View locations."'</span><br>
			'$"Locations"'
		</button>
	</td>

	</tr></tbody></table></div><div id="infobox">'
fi

#Check to see that locations.txt exists
if [ ! -f /var/lib/samba/netlogon/locations.txt ]
then
	MESSAGE=$"No locations have been created."
	no_locations
	exit
fi

###############################
#Location
###############################
if [ -f /var/lib/samba/netlogon/locations.txt ]
then
	LOCATION_COUNT=$(wc -l < /var/lib/samba/netlogon/locations.txt)
else
	LOCATION_COUNT=0
fi

MAXCOLS=2
MAXHEADERS=1
if [ "$LOCATION_COUNT" -gt 10 ]
then
	MAXCOLS=4
	MAXHEADERS=2
fi

if [ "$LOCATION_COUNT" -gt 20 ]
then
	MAXCOLS=6
	MAXHEADERS=3
fi

if [ "$LOCATION_COUNT" -gt 30 ]
then
	MAXCOLS=8
	MAXHEADERS=4
fi

echo '<input type="hidden" name="____PRINTERNAME____" value="'"$PRINTERNAME"'"><table class="tablesorter" style="text-align: left;" ><tbody><tr><td style="width: 180px;">Printer</td><td style="width: 100px;">'"$PRINTERNAME"'</td></tr>
</tbody></table><br><table class="tablesorter" style="text-align: left;" ><thead><tr><th style="width: 180px; vertical-align: top;"><b>'$"Location"'</b></th><th style="width: 100px; vertical-align: top;"><b>'$"Assign"'</b></th>'


for (( i=1; i<MAXHEADERS; i++ ))
do
	echo '<th style="width: 140px; vertical-align: top;"><b>'$"Location"'</b></th><th style="width: 90px; vertical-align: top;"><b>'$"Assign"'</b></th>'
done

echo '</tr></thead><tbody>'

COUNTER=1
COLCOUNT=0

while [ "$COUNTER" -lt "$LOCATION_COUNT" ]
do
	LOCATION=$(sed -n "$COUNTER,$COUNTER""p" /var/lib/samba/netlogon/locations.txt)

	if [ "$COLCOUNT" = 0 ]
	then
 		 echo "<tr>"
	fi

	if [[ $(grep ^"$LOCATION," /var/lib/samba/netlogon/printers.txt | grep -c -w "$PRINTERNAME") -gt 0 ]]
	then
		echo '<td>'"$LOCATION"'</td><td><input type="checkbox" name="____LOCATION____" value="'"$LOCATION"'" checked></td>'
	else
		echo '<td>'"$LOCATION"'</td><td><input type="checkbox" name="____LOCATION____" value="'"$LOCATION"'"></td>'
	fi
	let COUNTER="$COUNTER"+1
	let COLCOUNT="$COLCOUNT"+2

	if [ "$COLCOUNT" = "$MAXCOLS" ]
	then
		echo "</tr>"
		COLCOUNT=0
	fi
done

if [ "$COLCOUNT" -lt "$MAXCOLS" ] && [ "$COLCOUNT" != 0 ]
then
	while [ "$COLCOUNT" -lt "$MAXCOLS" ]
	do
		echo "<td></td>"
		let COLCOUNT="$COLCOUNT"+1
	done
	echo "</tr>"
fi

echo '</tbody></table><br><br>'

echo '<input value="'$"Submit"'" class="button" type="submit"></div></div></form></div></body></html>'
exit
