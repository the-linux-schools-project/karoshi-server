#!/bin/bash
#Copyright (C) 2012  Paul Sharrad

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Reset Room Controls"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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

echo '<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
</head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox
	TABLECLASS=standard
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox
	TABLECLASS=mobilestandard
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Reset Room Controls"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
else
	WIDTH=100
	ICON1=/images/assets/curriculum_computer.png

	echo '<div id="'"$DIV_ID"'"><div id="titlebox">

	<div class="sectiontitle">'$"Reset Room Controls"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Room_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will schedule times when all internet room controls are reset to allow internet access."'</span></a></div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<form action="dg_room_controls_fm.cgi" method="post">
				<button class="info" name="_ViewRoomControls_" value="_">
					<img src="'$ICON1'" alt="'$"Room Controls"'">
					<span>'$"View room controls."'</span><br>
					'$"Room Controls"'
				</button>
			</form>
		</td>

	</tr></tbody></table><br>
'
fi

ICON2=/images/submenus/internet/reset_room_controls_delete.png
echo '<form action="/cgi-bin/admin/dg_reset_room_controls.cgi" method="post"><br>
<table class="'"$TABLECLASS"'" style="text-align: left;" >
    <tbody><tr>
        <td style="width: 60px;"><b>'$"Time"'</b></td>
        <td style="width: 120px;">
        <select name="_HOURS_" style="width: 50px;">
        <option value="00">00</option>
        <option value="01">01</option>
        <option value="02">02</option>
        <option value="03">03</option>
        <option value="04">04</option>
        <option value="05">05</option>
        <option value="06">06</option>
        <option value="07">07</option>
        <option value="08">08</option>
        <option value="09">09</option>
        <option value="10">10</option>
        <option value="11">11</option>
        <option value="12">12</option>
        <option value="13">13</option>
        <option value="14">14</option>
        <option value="15">15</option>
        <option value="16">16</option>
        <option value="17">17</option>
        <option value="18">18</option>
        <option value="19">19</option>
        <option value="20">20</option>
        <option value="21">21</option>
        <option value="22">22</option>
        <option value="23">23</option>
	</select> : 
        <select name="_MINUTES_" style="width: 50px;">
        <option value="00">00</option>
        <option value="05">05</option>
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        <option value="55">55</option>
	</select>
</td>
<td><input name="_ACTION_add_" type="submit" class="button" value="'$"Add reset time"'"></td></tr></tbody></table></form><br>'


#Show any existing reset times
if [ -d /opt/karoshi/server_network/internet_room_controls_reset ]
then
	if [[ $(ls -1 /opt/karoshi/server_network/internet_room_controls_reset | wc -l) -gt 0 ]]
	then
		echo '<table id="myTable" class="tablesorter" style="text-align: left;" ><thead><th style="width: 200px; vertical-align: top;"><b>'$"Reset times"'</b></th><th style="width: 70px; vertical-align: top;">'$"Delete"'</th></thead><tbody>'

		for RESETTIMES in /opt/karoshi/server_network/internet_room_controls_reset/*
		do
			RESETTIME=$(basename "$RESETTIMES")
			echo '<tr><td>'"$RESETTIME"'</td><td>
			<form action="/cgi-bin/admin/dg_reset_room_controls.cgi" method="post">
				<button class="info" name="_DeleteTime_" value="_ACTION_delete_TIME_'"$RESETTIME"'_">
				<img src="'"$ICON2"'" alt="'$"Delete"'">
				<span>'$"Delete time"' - '"$RESETTIME"'</span>
				</button>
			</form></td></tr>'
		done
		echo '</tbody></table>'
	fi
fi

echo '</div></div></body></html>'
exit

