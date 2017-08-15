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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Scheduled Jobs"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
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
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
'

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

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi


[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Scheduled Jobs"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div>
	</div><div id="mobileactionbox">
	<form action="/cgi-bin/admin/cron_add_fm.cgi" method="post">
	<input name="submit" type="submit" class="button" value="'$"Schedule Job"'">
	</form><br>
'
else
	WIDTH=100
	ICON1=/images/submenus/system/add.png

	echo '

	<div class="sectiontitle">'$"Scheduled Jobs"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_Scheduled_Jobs"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the servers you want to view the scheduled commands on."'</span></a></div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/cron_add_fm.cgi" method="post">
				<button class="info infonavbutton" name="_ScheduleJob_" value="_">
					<img src="'"$ICON1"'" alt="'$"Schedule Job"'">
					<span>'$"Schedule a job."'</span><br>
					'$"Schedule Job"'
				</button>
			</form>
		</td>

	</tr></table>
	<br></div><div id="infobox">'
fi

echo '<form action="/cgi-bin/admin/cron_view.cgi" id="foo" name="selectservers" method="post">'

#Redirect to show the services if there is only one server
if [[ $(ls -1 /opt/karoshi/server_network/servers/ | wc -l) = 1 ]]
then
	echo '
	<input name="_SERVERNAME_'"$(hostname-fqdn)"'_SERVERTYPE_network_SERVERMASTER_notset_MOBILE_'"$MOBILE"'_" value="" type="hidden">
	<script type="text/javascript">
	    function myfunc () {
		var frm = document.getElementById("foo");
		frm.submit();
	    }
	    window.onload = myfunc;
	</script>'
else
	#Show list of servers
	/opt/karoshi/web_controls/show_servers "$MOBILE" servers $"View Jobs"
fi
echo '</form>'

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></div></body></html>'

exit
