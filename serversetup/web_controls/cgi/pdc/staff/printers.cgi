#!/bin/bash
#Copyright (C) 2007 Paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
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
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
############################
#Show page
############################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/karoshi/admin/printers.html";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Get data input
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><title>'$"Manage Print Queues"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
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
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')
#########################
#Assign data to variables
#########################
END_POINT=2
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
DATANAME=USERNAME
get_data
PRINTER="$DATAENTRY"

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

echo '<div id="'"$DIV_ID"'">'
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/staff/printers.cgi | cut -d' ' -f1`

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Manage Print Queues"'</span>'
	if [ -z "$PRINTER" ]
	then
		echo '<a href="/cgi-bin/staff/mobile_menu.cgi">'$"Menu"'</a>'
	else
		echo '<a href="/cgi-bin/staff/printers.cgi">'$"View Print Queues"'</a>'
	fi
	echo '</div></div>'
else
		echo '<div id="titlebox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top; height:30px"><div class="sectiontitle">'$"Manage Print Queues"'</div></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Manage_Print_Queues"><img class="images" alt="" src="/images/help/info.png"><span>'$"Click on the icons to control the printers in each queue."'</span></a></td>'

	if [ ! -z "$PRINTER" ]
	then
		echo '<td style="vertical-align: top;"><a href="printers.cgi"><input class="button" type="button" name="" value="'$"View Print Queues"'"></a></td>'
	fi

 echo '</tr></tbody></table></div><div id="infobox">
'
fi

sudo -H /opt/karoshi/web_controls/exec/printers_staff "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$PRINTER:"

[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
