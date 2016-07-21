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
UPDATECHOICE=updatelist.html

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
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
  <title>'$"Update Web Management"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>
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
</script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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

echo '</head><body onLoad="start()"><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
[ -z "$ACTION" ] && ACTION=UPDATES

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
TABLECLASS=standard
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
fi
[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

#Show update list choice
if [ $ACTION = ALL ]
then
	UPDATELIST=updatelist_all.html
	[ "$MOBILE" = yes ] && UPDATELIST=updatelist_all_mobile.html
	ICON=/images/submenus/system/updates.png
	ACTION=UPDATES
	MESSAGE=$"Available updates"
else
	UPDATELIST=updatelist.html
	[ "$MOBILE" = yes ] && UPDATELIST=updatelist_mobile.html
	ICON=/images/submenus/system/updates_all.png
	ACTION=ALL
	MESSAGE=$"Installed Updates"
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	MOBILEACTIONBOX=mobileactionbox2
	[ ! -f /opt/karoshi/updates/$UPDATELIST ] && MOBILEACTIONBOX=mobileactionbox
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"Update Web Management"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="mobilecontent"><div id="'$MOBILEACTIONBOX'">'
else
	echo '<table class="standard" style="text-align: left;" ><tbody><tr>
	<td style="vertical-align: top;"><div class="sectiontitle">'$"Update Web Management"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Linux_Schools_Server_System"><img class="images" alt="" src="/images/help/info.png"><span>'$"This shows any Karoshi Server patches that are available."'</span></a></td></tr></tbody></table><br>'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
<tr><td>
<form action="/cgi-bin/admin/update_karoshi_fm.cgi" name="selectservers" method="post">
<button class="button" name="Updates" value="_ACTION_'$ACTION'_">
'$MESSAGE'
</button>
</form></td><td>
<form action="/cgi-bin/admin/refresh_karoshi_update_list.cgi" name="selectservers" method="post">
<input name="RefreshList" type="submit" class="button" value="'$"Check for updates"'">
</form></td></tr></tbody></table>'

[ $MOBILE = no ] && echo '</div><div id="infobox">'

echo '<form action="/cgi-bin/admin/update_karoshi.cgi" name="selectservers" method="post">'

if [ -f /opt/karoshi/updates/$UPDATELIST ]
then
	cat /opt/karoshi/updates/$UPDATELIST
else
	echo '<br>'$"No updates are available."'<br>'
fi

echo '</form><br><br><br><br><br></div></div></div></body></html>'
exit
