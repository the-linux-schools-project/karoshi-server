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

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Server Update Logs"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">'
echo '<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script type="text/javascript" src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) --><link rel="stylesheet" href="/all/calendar2/calendar.css"><script src="/all/stuHover.js" type="text/javascript"></script>
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

DATE_INFO=$(date +%F)
DAY=$(echo "$DATE_INFO" | cut -d- -f3)
MONTH=$(echo "$DATE_INFO" | cut -d- -f2)
YEAR=$(echo "$DATE_INFO" | cut -d- -f1)


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
	DIV_ID=actionbox3
	WIDTH2=200
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=mobileactionbox
	WIDTH2=200
fi
echo '<form name="testform" action="/cgi-bin/admin/update_servers_view_logs.cgi" method="post">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"View Server Update Logs"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="'"$DIV_ID"'">
	'
else
	WIDTH=100
	ICON1=/images/submenus/system/computer.png

	echo '
	<div id="'"$DIV_ID"'"><div id="titlebox">
	<div class="sectiontitle">'$"View Server Update Logs"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Viewing_Update_Logs"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the date that you want to view the update logs for."'</span></a></div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info infonavbutton" formaction="update_servers_fm.cgi" name="_UpdateServers_" value="_">
				<img src="'$ICON1'" alt="'$"Update Servers"'">
				<span>'$"Schedule a server to update"'</span><br>
				'$"Update Servers"'
			</button>
		</td>

	</tr></tbody></table><br><br>
	'
fi



if [ "$MOBILE" = yes ]
then
echo ''$"Log date"'<br>'

echo "	<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\""$DAY-$MONTH-$YEAR"\" size=14 maxlength=10 name=\"_DATE_\">
	<script type=\"text/javascript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script><br>"

echo ''$"View logs by date"'<br>
<input checked="checked" name="_LOGVIEW_" value="today" type="radio"><br>
'$"View logs by month"'<br>
<input name="_LOGVIEW_" value="month" type="radio"><br><br>'

else
	echo '<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">'$"Log date"'</td><td>'
echo "	<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$DAY-$MONTH-$YEAR\" size=14 maxlength=10 name=\"_DATE_\" style=\"width: "$WIDTH2"px;\"></td><td style=\"vertical-align: top; text-align: center;\">
	<script type=\"text/javascript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script>"

echo '</td></tr><tr><td>'$"View logs by date"'</td><td></td><td style="vertical-align: top; text-align: center;"><input checked="checked" name="_LOGVIEW_" value="today" type="radio"></td></tr><tr><td>'$"View logs by month"'</td><td></td><td style="vertical-align: top; text-align: center;"><input name="_LOGVIEW_" value="month" type="radio"></td></tr></tbody></table><br><br>'
fi

[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

#Show list of servers
/opt/karoshi/web_controls/show_servers "$MOBILE" servers $"Show logs" notset updateserver

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></form></div></body></html>'
exit
