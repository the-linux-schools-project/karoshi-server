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
  <title>'$"Add Network Printer"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
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

echo '<div id="actionbox3"><div id ="titlebox">
<div class="sectiontitle">'$"Add Network Printer"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Add a network printer for your client computers."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/printers.cgi" name="printers" method="post">
			<button class="info" name="_ShowPrinters_" value="_">
				<img src="'"$ICON1"'" alt="'$"Show Printers"'">
				<span>'$"Show network printer queues."'</span><br>
				'$"Show Printers"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/printers_delete.cgi" name="printers" method="post">
			<button class="info" name="_DeletePrinters_" value="_">
				<img src="'"$ICON2"'" alt="'$"Delete Printers"'">
				<span>'$"Delete network printer queues."'</span><br>
				'$"Delete Printers"'
			</button>
		</form>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/locations.cgi" name="printers" method="post">
			<button class="info" name="_ViewLocations_" value="_">
				<img src="'"$ICON3"'" alt="'$"Locations"'">
				<span>'$"View locations."'</span><br>
				'$"Locations"'
			</button>
		</form>
	</td>

</tr></tbody></table><br>
'

echo '<form action="/cgi-bin/admin/printers_add.cgi" method="post">'
#Check that a print server has been assigned
if [ ! -f /opt/karoshi/server_network/printserver ]
then
	echo $"A print server has not yet been set up."
fi

echo '<table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"Printer Name"'</td>
        <td><input tabindex= "1" name="____PRINTERNAME____" maxlength="15" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxgfx.co.uk/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name that you want for this printer."'</span></a>
</td>
      </tr>
 <tr><td>'$"Printer Address"'</td><td><input tabindex= "2" name="____PRINTERADDRESS____" maxlength="15" style="width: 200px;" size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the tcpip number of the printer."'</span></a>
</td></tr>
<tr><td>'$"Queue - LPD only"'</td><td><input tabindex= "3" name="____PRINTERQUEUE____" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the network queue."'</span></a>
</td></tr>
<tr><td>'$"Description"'</td><td><input tabindex= "4" name="____PRINTERDESC____" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a description of the printer hardware."'</span></a>
</td></tr>
<tr><td>'$"Location"'</td><td>'

###############################
#Location
###############################
if [ -f /var/lib/samba/netlogon/locations.txt ]
then
	LOCATION_COUNT=$(wc -l < /var/lib/samba/netlogon/locations.txt)
else
	LOCATION_COUNT=0
fi
#Show current rooms
echo '<select tabindex= "5" name="____LOCATION____" style="width: 200px;">'
echo '<option label="defaultlocation" value="'"$NO_LOCATION"'">'"$NO_LOCATION"'</option>'
COUNTER=1
while [ "$COUNTER" -lt "$LOCATION_COUNT" ]
do
	LOCATION=$(sed -n "$COUNTER,$COUNTER""p" /var/lib/samba/netlogon/locations.txt)
	echo '<option value="'"$LOCATION"'">'"$LOCATION"'</option>'
	let COUNTER="$COUNTER"+1
done
echo '</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the location of this printer. Click on the add locations icon above to add locations."'</span></a>
</td></tr>
      <tr>
        <td>'$"Network Type"'</td>
        <td>
        <select tabindex= "6" name="____PRINTERTYPE____" style="width: 200px;">
        <option>'$"Network Printer TCP"'</option>
        <option>'$"Network Printer IPP"'</option>
        <option>'$"Remote LPD queue"'</option>
        </select></td></tr>
<tr><td>'$"Port"'</td><td>
        <select tabindex= "7" name="____PRINTERPORT____" style="width: 200px;">
        <option>9100</option>
        <option>9101</option>
        <option>9102</option>
        <option>631</option>
        </select>
        </td><td></td>
      </tr>
    </tbody>
  </table><br><br>
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</form>
</div></div></div></body></html>'
exit
