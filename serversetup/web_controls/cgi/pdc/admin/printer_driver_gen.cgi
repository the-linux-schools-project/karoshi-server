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
<!DOCTYPE html>
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Windows Printer Drivers"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">

  
  <script>
<!--
function SetAllCheckBoxes(FormName, FieldName, CheckValue)
{
	if(!document.forms[FormName])
		return;
	var objCheckBoxes = document.forms[FormName].elements[FieldName];
	if(!objCheckBoxes)
		return;
	var countCheckBoxes = objCheckBoxes.length;
	if(!countCheckBoxes)
		objCheckBoxes.checked = CheckValue;
	else
		// set the check value for all check boxes
		for(var i = 0; i < countCheckBoxes; i++)
			objCheckBoxes[i].checked = CheckValue;
}
// -->
  </script>

<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>

<script src="/all/stuHover.js"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')
#########################
#Assign data to variables
#########################
END_POINT=7
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

#Assign action
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

#Assign queue
DATANAME=QUEUE
get_data
QUEUE="$DATAENTRY"

[ -z "$ACTION" ] && ACTION=view

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH=100
	ICON1=/images/submenus/printer/enable_printer.png
	ICON2=/images/submenus/printer/disable_printer.png
	ICON3=/images/submenus/printer/printer_assigned.png
	ICON4=/images/submenus/printer/view_print_queues.png
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
	WIDTH=145
	ICON1=/images/submenus/printer/enable_printerm.png
	ICON2=/images/submenus/printer/disable_printerm.png
	ICON3=/images/submenus/printer/printer_assignedm.png
	ICON4=/images/submenus/printer/view_print_queuesm.png
fi

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/printer_driver_gen.cgi";'
echo '</script>'
echo "</div></form></div></body></html>"
exit
}

echo '<form action="/cgi-bin/admin/printer_driver_gen.cgi" name="selectedsites" method="post"><b></b>'

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'


#Show back button for mobiles
if [ "$MOBILE" = yes ]
	then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Windows Printer Drivers"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
fi
if [ "$MOBILE" = no ]
then
	echo '
	<div class="sectiontitle">'$"Windows Printer Drivers"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Printer_Driver_Generation"><img class="images" alt="" src="/images/help/info.png"><span>'$"This is used to enable or disable automated Windows printer driver generation for your print queues."'</span></a></div>'
fi

echo '
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_EnableAll_" value="_ACTION_enableall_PRINTQUEUE_all_">
			<img src="'"$ICON1"'" alt="'$"Enable All"'">
			<span>'$"Enable auto generation for all printers."'</span><br>
			'$"Enable All"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_DisableAll_" value="_ACTION_disableall_PRINTQUEUE_all_">
			<img src="'"$ICON2"'" alt="'$"Disable all"'">
			<span>'$"Disable auto generation for all printers."'</span><br>
			'$"Disable all"'
		</button>
	</td>'

[ "$MOBILE" = yes ] && echo "</tr><tr>"

echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="_GenerateDrivers_" value="_ACTION_gendrivers_PRINTQUEUE_all_">
			<img src="'"$ICON3"'" alt="'$"Generate Drivers"'">
			<span>'$"Generate printer drivers for all enabled printers."'</span><br>
			'$"Generate Drivers"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button formaction="printers.cgi" class="info infonavbutton" name="_ShowPrinters_" value="_">
			<img src="'"$ICON4"'" alt="'$"Show Printers"'">
			<span>'$"Show network printer queues."'</span><br>
			'$"Show Printers"'
		</button>
	</td>

'

echo '</tr></tbody></table>'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/printer_driver_gen.cgi | cut -d' ' -f1)
if [ "$ACTION" = gendrivers ]
then
	sudo -H /opt/karoshi/web_controls/exec/printer_driver_gen2 "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:"
	EXEC_STATUS="$?"
	[ "$EXEC_STATUS" = 0 ] && MESSAGE=$"Windows printer driver generation completed."

	if [ "$EXEC_STATUS" = 102 ]
	then
		MESSAGE=$"The samba root password was incorrect."
	fi
	if [ "$EXEC_STATUS" = 103 ]
	then
		MESSAGE=$"The windows dll files needed to generate the windows printer drivers are missing. The dlls needed in /usr/share/cups/drivers/ are pscript5.dll, ps5ui.dll, pscript.hlp, pscript.ntf."
	fi
	show_status
else
	#Check that we have some printer queues
	COUNTER=$(grep -n ^--start-- /var/lib/samba/netlogon/printers.txt | cut -d: -f1)
	let COUNTER="$COUNTER"+1
	NOOFLINES=$(wc -l < /var/lib/samba/netlogon/printers.txt)
	if [ "$COUNTER" -lt "$NOOFLINES" ]
	then
		echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$QUEUE:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/printer_driver_gen
	else
		echo '<ul><li>'$"No Printers have been assigned"'</li></ul>'
	fi
fi
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></form></div></body></html>'
exit
