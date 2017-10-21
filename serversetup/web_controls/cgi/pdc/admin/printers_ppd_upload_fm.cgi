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
if [ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]
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
    <TITLE>'$"Upload PPD file"'</TITLE><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#Get printer details
if [ ! -f /var/www/karoshi/uploadppd ]
then
	MESSAGE=$"No Printer details found."
	show_status
fi
source /var/www/karoshi/uploadppd
source /opt/karoshi/web_controls/version

ICON1=/images/submenus/printer/view_print_queues.png
ICON2=/images/submenus/printer/delete_printer.png
ICON3=/images/submenus/file/folder.png

echo '<div id="actionbox3"><div id="titlebox">
<FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/printers_ppd_upload.cgi" METHOD="POST">

	<div class="sectiontitle">'$"Upload PPD file"' <a target="_blank" href="http://openprinting.org/printer_list.cgi"><img src="/images/help/info.png" border="0"></a></div>
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

	</tr></tbody></table>
	<br>
	<table class="standard" style="text-align: left;" ><tbody>
	<tr><td style="vertical-align: middle; width: 180px; height: 30px;">'$"Printer"'</td><td>'"$PRINTERNAME"'</td></tr>
	<tr><td style="vertical-align: middle; height: 30px;">'$"Default Page Size"'</td><td>'"$PAGESIZE"'</td></tr>
	<tr><td style="vertical-align: middle; height: 30px;">'$"Print in Colour?"'</td><td>'"$COLOUR"'</td></tr>
	<tr><td style="vertical-align: middle; height: 30px;">'$"Printer PPD"'</td><td style="vertical-align: middle;">
	<INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="25">
	<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"If you are using a Linux client with cups installed you can find ppd files in /usr/share/cups/models or /usr/share/ppd."'</span></a></td></tr>
	</tbody></table><br>
	<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</form>
</div>
</div>
</div>
</body>
</html>
'
exit
