#!/bin/bash
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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Manage Print Queues"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>
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
if [ $MOBILE = yes ]
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
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign PRINTER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PRINTERcheck ]
	then
		let COUNTER=$COUNTER+1
		PRINTER=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
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

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#Generate navigation bar
if [ $MOBILE = no ]
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

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
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
	echo '<div id="titlebox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top;"><b>'$"Manage Print Queues"'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Manage_Print_Queues"><img class="images" alt="" src="/images/help/info.png"><span>'$"Click on the icons to control the printers in each queue."'</span></a></td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/printers_add_fm.cgi" name="printers" method="post"><input name="ADDPRINTER" type="submit" class="button" value="'$"Add Printer"'"></form>
</td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers_delete.cgi" name="printers" method="post">
<input name="DELETEPRINTER" type="submit" class="button" value="'$"Delete Printer"'"></form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers_view_assigned_fm.cgi" name="printers" method="post">
<input name="VIEWASSIGNED" type="submit" class="button" value="'$"View Assigned Printers"'"></form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/locations.cgi" name="printers" method="post">
<input name="ADDLOCATION" type="submit" class="button" value="'$"Add Location"'"></form></td>
'


	if [ ! -z "$PRINTER" ]
	then
		echo '<td style="vertical-align: top;"><a href="printers.cgi"><input class="button" type="button" name="" value="'$"View Print Queues"'"></a></td>'
	fi

	echo '</tr></tbody></table></div>
'
fi

[ $MOBILE = no ] && echo '<div id="infobox">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/printers $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$PRINTER:
[ $MOBILE = no ] && echo '</div>'
echo "</div></div></body></html>"
exit
