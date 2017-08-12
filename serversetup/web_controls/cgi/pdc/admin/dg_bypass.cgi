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
  <title>'$"Client Bypass Controls"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
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
        $("#myTable").tablesorter({
	headers: {
	0: { sorter: "ipAddress" }
    		}
		});
    } 
);
</script>
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

#Assign TCPIP
DATANAME=TCPIP
get_data
TCPIP="$DATAENTRY"

[ -z "$ACTION" ] && ACTION=view

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	WIDTH=100
	ICON1=/images/submenus/system/add.png
	ICON2=/images/submenus/system/computer.png
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	WIDTH=90
	ICON1=/images/submenus/system/addm.png
	ICON2=/images/submenus/system/computerm.png
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'


function passinfo {
MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/dg_bypass.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$TCPIP:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/dg_bypass
}


TITLE=$"Client Bypass Controls"
BUTTONACTION=add
BUTTONMSG=$"Add IP number"
ICON="$ICON1"
if [ $ACTION = add ]
then
	BUTTONACTION=view
	BUTTONMSG=$"View IP numbers"
	ICON="$ICON2"
	
fi
#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'"$TITLE"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
fi

echo '
<div class="sectiontitle">'"$TITLE"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Bypass_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$"This can be used for client devices to bypass the internet filtering."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<form action="/cgi-bin/admin/dg_bypass.cgi" name="selectedsites" method="post">
			<button class="info infonavbutton" name="_Add_" value="_ACTION_'"$BUTTONACTION"'_">
				<img src="'$ICON'" alt="'"$BUTTONMSG"'">
				<span>'"$BUTTONMSG"'</span><br>
				'"$BUTTONMSG"'
			</button>
		</form>
	</td>

</tr></tbody></table><br>'

if [ "$ACTION" = reallyadd ]
then
	passinfo
fi

if [ "$ACTION" = view ] || [ "$ACTION" = delete ]
then
	passinfo
fi

if [ "$ACTION" = add ]
then 
	echo '<form action="/cgi-bin/admin/dg_bypass.cgi" name="selectedsites" method="post"><input type="hidden" name="_ACTION_" value="reallyadd">'
	if [ "$MOBILE" = yes ]
	then
		echo '
	'$"TCPIP Number"'<br>
	<input name="_TCPIP_" style="width: 160px;" value="'"$TCPIP_ADDR"'" size="20"><br><br>
	'
	else
		echo '<table class="standard" style="text-align: left;" >
	    <tbody>
	      <tr>
		<td style="width: 200px;">'$"TCPIP Number"'</td>
		<td><input required="required" name="_TCPIP_" value="'"$TCPIP_ADDR"'" style="width: 200px;" size="20"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the tcpip number of the client computer that you want to set to bypass the filtering."'</span></a></td>
	      </tr>
	    </tbody>
	  </table>
	  <br><br>'
	fi
	echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></form>'
fi
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
