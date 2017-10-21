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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Assign PPD File"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g')

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

#Assign PRINTERNAME
DATANAME=PRINTERNAME
get_data
PRINTERNAME="${DATAENTRY//12345UNDERSCORE12345/_}"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
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
#Check data
#########################
#Check to see that PRINTERNAME is not blank
if [ -z "$PRINTERNAME" ]
then
	MESSAGE=$"The printer name cannot be blank."
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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	WIDTH=100
	ICON1=/images/submenus/printer/view_print_queues.png
	ICON2=/images/submenus/printer/delete_printer.png
	ICON3=/images/submenus/file/folder.png
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=menubox
	WIDTH=90
	ICON1=/images/submenus/printer/view_print_queuesm.png
	ICON2=/images/submenus/printer/delete_printerm.png
	ICON3=/images/submenus/file/folderm.png
fi

echo '<form action="/cgi-bin/admin/printers_ppd_assign2.cgi" method="post"><div id="'"$DIV_ID"'"><div id="titlebox">

<div class="sectiontitle">'$"Assign PPD File"' <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"A PPD is a linux printer driver. You will need to assign a printer driver to every printer queue that you set up."'</span></a></div>
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
<br><input type="hidden" name="____PRINTERNAME____" value="'"$PRINTERNAME"'">
<table class="standard" style="text-align: left; height: 120px;" ><tbody><tr><td style="width: 180px;">'$"Printer"'</td><td>'"$PRINTERNAME"'</td><td></td></tr>'

#######################
#Guess default paper size
#######################
A4SELECTED='selected="selected"'
LETTERSELECTED=""

#Show list of page sizes
echo '
<tr><td>'$"Default Page Size"'</td><td>
<select style="width: 200px;" name="____PAGESIZE____">
<option value="A2">A2</option>
<option value="A3">A3</option>
<option value="Letter" '"$LETTERSELECTED"'>Letter</option>
<option value="A4" '"$A4SELECTED"'>A4</option>
<option value="A5" >A5</option>
<option value="A6">A6</option>
</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the default page size for this printer."'</span></a></td></tr>
<tr><td>'$"Print in Colour?"'</td><td>
<select style="width: 200px;" name="____COLOUR____">
<option value="yes">'$"yes"'</option>
<option value="no">'$"No"'</option>
</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This setting will only affect printers that can print in colour."'</span></a></td></tr>'

#Show printer manufacturer list to choose from
echo '<tr><td>'$"Printer Make"'</td><td><select style="width: 200px;" name="____PRINTERPPD____">'
echo '<option value="" label="blank"></option>'
echo '<option value="uploadppd">'$"Upload PPD File"'</option>'
#Get list of printer drivers
MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/printers_ppd_assign1.cgi | cut -d' ' -f1)
sudo -H /opt/karoshi/web_controls/exec/printers_show_drivers "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:"

echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the make of your printer from this list. If the printer make is not listed you will need to get a PPD from the internet and use the Upload PPD option."'</span></a></td></tr></tbody></table><br><input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">'

[ "$MOBILE" = no ] && echo '</div>' 

echo '</div></form></div></body></html>'
exit

