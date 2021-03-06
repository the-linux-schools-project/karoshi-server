#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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

#Language
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

HOUR=$(date +%H)
MINUTES=$(date +%M)
SECONDS=$(date +%S)

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Update Servers"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/calendar/ts_picker.js" type="text/javascript"></script>
<!-- Timestamp input popup (European Format) --><script src="/all/stuHover.js" type="text/javascript"></script>
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

echo '</head><body onLoad="start()"><div id="pagecontainer">'

#########################
#Get data input
#########################

DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%+')

END_POINT=9
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

#Assign _DAY_
DATANAME=DAY
get_data
DAY="$DATAENTRY"

#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
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

if [[ $(grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	TOOLTIPCLASS="info"
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH1=180
	WIDTH2=200
	WIDTH3=200
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	TOOLTIPCLASS="info infoleft"
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
	WIDTH1=90
	WIDTH2=120
	WIDTH3=120
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Update Servers"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
else
	WIDTH=100
	ICON1=/images/submenus/system/logs.png

	echo '
	<div class="sectiontitle">'$"Update Servers"' <a class="'"$TOOLTIPCLASS"'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows you to schedule updates for your servers."'</span></a></div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<form action="/cgi-bin/admin/update_servers_view_logs_fm.cgi" name="tstest" method="post">
				<button class="info infonavbutton" formaction="update_servers_view_logs_fm.cgi" name="_ViewUpdateLogs_" value="_">
					<img src="'$ICON1'" alt="'$"Update Logs"'">
					<span>'$"View the update logs for this server."'</span><br>
					'$"Update Logs"'
				</button>
			</form>
		</td>

	</tr></tbody></table></div><div id="infobox">
	'
fi

#Preselect day
if [ ! -z "$DAY" ]
then
	[ "$DAY" = 1 ] && OP1='selected="selected"'
	[ "$DAY" = 2 ] && OP2='selected="selected"'
	[ "$DAY" = 3 ] && OP3='selected="selected"'
	[ "$DAY" = 4 ] && OP4='selected="selected"'
	[ "$DAY" = 5 ] && OP5='selected="selected"'
	[ "$DAY" = 6 ] && OP6='selected="selected"'
	[ "$DAY" = 7 ] && OP7='selected="selected"'
	[ "$DAY" = 8 ] && OP8='selected="selected"'
fi

echo '<form action="/cgi-bin/admin/update_servers.cgi" name="tstest" method="post"><table class="'"$TABLECLASS"'" style="text-align: left;" ><tbody>
<tr><td style="width: '"$WIDTH1"'px;">'$"Day"'</td><td>
<select required="required" tabindex= "2" style="width: '"$WIDTH3"'px;" name="_DAY_">
<option label="blank" value=""></option>
<option value="never">'$"Never"'</option>
<option '"$OP1"' value="1">'$"Monday"'</option>
<option '"$OP2"' value="2">'$"Tuesday"'</option>
<option '"$OP3"' value="3">'$"Wednesday"'</option>
<option '"$OP4"' value="4">'$"Thursday"'</option>
<option '"$OP5"' value="5">'$"Friday"'</option>
<option '"$OP6"' value="6">'$"Saturday"'</option>
<option '"$OP7"' value="7">'$"Sunday"'</option>
<option '"$OP8"' value="8">'$"Every day"'</option>
</select>
</td><td><a class="'"$TOOLTIPCLASS"'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the day that you want your servers to update on."'</span></a></td></tr>
<tr><td>'$"Hour"'</td><td><input required="required" tabindex= "2" value="'"$HOUR"'" name="_HOURS_" style="width: '"$WIDTH2"'px;" size="3" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the time that you want your servers to update on."'</span></a></td></tr>
<tr><td>'$"Minutes"'</td><td><input required="required" tabindex= "3" value="'"$MINUTES"'" name="_MINUTES_" style="width: '"$WIDTH2"'px;" size="3" type="text"></td><td><a class="'"$TOOLTIPCLASS"'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the time that you want your servers to update on."'</span></a></td></tr>
<tr><td>'$"Force Reboot"'</td><td><input type="checkbox" name="_FORCEREBOOT_" value="yes"></td><td><a class="'"$TOOLTIPCLASS"'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$"Select this option only if you have a server that will not restart correctly if a reboot is required after system updates."'</span></a></td></tr>
</tbody></table><br>'

#Show list of servers
/opt/karoshi/web_controls/show_servers "$MOBILE" all $"Schedule Update" notset updateserver

echo '</form>'

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></div></body></html>'

exit

