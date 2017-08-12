#!/bin/bash
#change_username
#Copyright (C) 2007  Paul Sharrad
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
  <title>'$"Change a Username"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\--')
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

#Assign USERNAME
DATANAME=USERNAME
get_data
USERNAME="$DATAENTRY"

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

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	TOOLTIPCLASS="info"
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH1=180
	WIDTH2=200
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	TOOLTIPCLASS="info infoleft"
	DIV_ID=mobileactionbox
	TABLECLASS=mobilestandard
	WIDTH1=130
	WIDTH2=150
fi


#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Change a Username"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="'"$DIV_ID"'">
'
else

	WIDTH=100
	ICON1=/images/submenus/user/edit_user_info.png
	ICON2=/images/submenus/user/groups.png

	echo '<div id="'"$DIV_ID"'"><div id="titlebox">
	<div class="sectiontitle">'$"Change a Username"'</div>
	<table class="tablesorter"><tbody><tr>
	'

	if [ ! -z "$USERNAME" ]
	then
		echo '
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/show_user_info.cgi" method="post">
				<button class="info infonavbutton" name="_ShowUserInfo_" value="_SERVERNAME_'"$(hostname-fqdn)"'_SERVERTYPE_network_SERVERMASTER_notset_ACTION_notset_USERNAME_'"$USERNAME"'">
					<img src="'"$ICON1"'" alt="'$"Edit User"'">
					<span>'$"Edit the user's information."'</span><br>
					'$"Edit User"'
				</button>
			</form>
		</td>
		'
	fi

	echo '
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<form action="/cgi-bin/admin/groups.cgi" method="post">
				<button class="info infonavbutton" name="____GroupManagement____" value="____GroupManagement____">
					<img src="'"$ICON2"'" alt="'$"Group Management"'">
					<span>'$"Group Management"'</span><br>
					'$"Group Management"'
				</button>
			</form>
		</td>

	</tr></tbody></table>
	<br>'
fi

echo '<form action="/cgi-bin/admin/change_username.cgi" method="post">'

if [ "$MOBILE" = no ]
then
	echo '<table class="'"$TABLECLASS"'" style="text-align: left; height: 30px;" >
	<tbody>
	<tr>
	<td style="width: '"$WIDTH1"'px;">
	'$"Current Username"'</td>
	<td><div id="suggestions"></div><input required="required" tabindex= "1" name="_USERNAME_" value="'"$USERNAME"'" size="20" style="width: '"$WIDTH2"'px;" type="text" id="inputString" onkeyup="lookup(this.value);"></td><td>
	<a class="'"$TOOLTIPCLASS"'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the username that you want to change."'</span></a>
	</td></tr>
	<tr><td>'$"New username"'</td><td><input required="required" tabindex= "2" name="_NEWUSERNAME_" size="20" style="width: '"$WIDTH2"'px;" type="text"></td><td>
	<a class="'"$TOOLTIPCLASS"'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new username for this user."'</span></a></td>
	</tr>
	<tr><td>'$"New forename"'</td><td><input required="required" tabindex= "3" name="_FIRSTNAME_" size="20"  style="width: '"$WIDTH2"'px;" type="text"></td><td>
	<a class="'"$TOOLTIPCLASS"'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new username for this user."'</span></a></td>
	      </tr>
	<tr><td>'$"New surname"'</td><td><input required="required" tabindex= "4" name="_SURNAME_" size="20"  style="width: '"$WIDTH2"'px;" type="text"></td><td>
	<a class="'"$TOOLTIPCLASS"'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new username for this user."'</span></a></td>
	</tr>
	</tbody>
	</table>
	<br>'
else
	echo '<div id="suggestions"></div>
	'$"Current username"'<br>
	<input required="required" tabindex= "1" style="width: 160px; height: 30px;" name="_USERNAME_" 
	 value="'"$USERNAME"'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"><br>
	'$"New username"'<br>
	<input required="required" tabindex= "2" style="width: 160px; height: 30px;" name="_NEWUSERNAME_" size="20" type="text"><br>
	'$"New forename"'<br>
	<input required="required" tabindex= "3" style="width: 160px; height: 30px;" name="_FIRSTNAME_" size="20" type="text"><br>
	'$"New surname"'<br>
	<input required="required" tabindex= "4" style="width: 160px; height: 30px;" name="_SURNAME_" size="20" type="text"><br>
	<br>'
fi

echo '<br>'

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></form>'

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></div></body></html>'
exit
