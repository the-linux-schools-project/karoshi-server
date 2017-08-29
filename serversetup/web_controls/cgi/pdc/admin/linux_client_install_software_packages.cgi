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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Linux Client software packages"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
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
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/linux_client_install_software_packages_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
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

#########################
#Assign data to variables
#########################
END_POINT=6
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

#Assign VERSION
DATANAME=VERSION
get_data
VERSION="$DATAENTRY"

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH1=200
	WIDTH2=80
	HEIGHT1=24
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
	WIDTH1=160
	WIDTH2=50
	HEIGHT1=30
fi

#########################
#Check data
#########################
#Check to see that VERSION is not blank
if [ -z "$VERSION" ]
then
	MESSAGE=$"Blank version"
	show_status
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
<div class="expanded">
<span>'$"Linux Client software packages"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
else
	WIDTH=100
	ICON1=/images/submenus/client/software.png

	echo '<form action="/cgi-bin/admin/linux_client_software_controls.cgi" method="post"><input name="_VERSION_" value="'"$VERSION"'" type="hidden">

	<div class="sectiontitle">'$"Linux Client Software Packages"' - '"$VERSION"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Linux_Client_Software_Packages"><img class="images" alt="" src="/images/help/info.png"><span>'$"The software shown below will be installed by your linux client computers on boot."'</span></a></div>

	<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info infonavbutton" name="_UPLOAD_" value="_">
				<img src="'$ICON1'" alt="'$"Software Controls"'">
				<span>'$"View software controls."'</span><br>
				'$"Software Controls"'
			</button>
	</td>

	</tr></tbody></table>
	</form><br>'
fi

#Show a table of current software to install and remove
# install - /var/lib/samba/netlogon/linuxclient/version/install_list
# remove - /var/lib/samba/netlogon/linuxclient/version/remove_list

ICON3=/images/submenus/client/delete_software.png

#Show input box
echo '<form action="/cgi-bin/admin/linux_client_install_software_packages2.cgi" name="selectservers" method="post"><input name="___VERSION___" value="'"$VERSION"'" type="hidden">
<b>'$"Add software package"'</b><br><br>

<table class="'"$TABLECLASS"'" style="text-align: left;" ><tbody><tr><td style="width: '"$WIDTH1"'px;">'$"Location"'</td><td>'

#Show current rooms
echo '<select name="___LOCATION___" style="width: '"$WIDTH1"'px; height: '"$HEIGHT1"'px;">'
echo '<option value="all">'$"All locations"'</option>'
if [ -f /var/lib/samba/netlogon/locations.txt ]
then
	for LOCATION in $(cat /var/lib/samba/netlogon/locations.txt)
	do
		echo '<option value="'"$LOCATION"'">'"$LOCATION"'</option>'
	done
fi
echo '</select></td><td></td></tr>
<tr><td style="width: '"$WIDTH1"'px;">'$"Software Package"'</td><td><input style="width: '"$WIDTH1"'px; height: '"$HEIGHT1"'px;" tabindex= "1" name="___ACTION___add___SOFTWARE___"  size="20" type="text"></td></tr>
</tbody></table><br><br>

<button class="button" name="___Install___" value="___INSTALL___install___">
'$"Install"'
</button>
 
<button class="button" name="___Install___" value="___INSTALL___remove___">
'$"Remove"'
</button>

</form>'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

echo '<br><form action="/cgi-bin/admin/linux_client_install_software_packages2.cgi" name="selectservers" method="post"><input name="___VERSION___" value="'"$VERSION"'" type="hidden">'

function show_software {
if [ -d /var/lib/samba/netlogon/linuxclient/"$VERSION/software/$INSTALL"/ ]
then
	if [[ $(ls -1 /var/lib/samba/netlogon/linuxclient/"$VERSION/software/$INSTALL"/*_software 2>/dev/null | wc -l) != 0 ]]
	then
		if [ "$SHOW_TABLE_HEADER" = yes ]
		then
			echo '<table id="myTable" class="tablesorter" style="text-align: left;" ><thead>
		<tr><th style="width: '"$WIDTH1"'px;"><b>'$"Location"'</b></th><th style="width: '"$WIDTH1"'px;"><b>'$"Action"'</b></th><th style="width: '"$WIDTH1"'px;"><b>'$"Software Package"'</b></th><th style="width: '"$WIDTH2"'px;"><b>'$"Delete"'</b></th></tr></thead><tbody>'
			SHOW_TABLE_HEADER=no
			SHOW_TABLE_FOOTER=yes
		fi
		for LOCATIONS in $(ls -1 /var/lib/samba/netlogon/linuxclient/"$VERSION/software/$INSTALL"/*_software)
		do
			#Show install list
			LOCATION=$(basename "$LOCATIONS" | cut -d"_" -f1)
			if [[ $(wc -l < "/var/lib/samba/netlogon/linuxclient/$VERSION/software/$INSTALL/$LOCATION"_software) -gt 0 ]]
			then
				for SOFTWARE in $(cat /var/lib/samba/netlogon/linuxclient/"$VERSION/software/$INSTALL/$LOCATION"_software)
				do
					echo '<tr><td>'"$LOCATION"'</td><td>'"$INSTALL_LANG"'</td><td>'"$SOFTWARE"'</td><td>

					<button class="info" name="___Delete___" value="___ACTION___delete___INSTALL___'"$INSTALL"'___SOFTWARE___'"$SOFTWARE"'___LOCATION___'"$LOCATION"'___">
					<img src="'"$ICON3"'" alt="'$"Delete"'">
					<span>'$"Delete" "$SOFTWARE"'</span>
					</button>
					</td></tr>'
				done
			fi
		done
	fi
fi
}

SHOW_TABLE_HEADER=yes
SHOW_TABLE_FOOTER=no
INSTALL=install
INSTALL_LANG=$"Install"
show_software
INSTALL=remove
INSTALL_LANG=$"Remove"
show_software
if [ "$SHOW_TABLE_FOOTER" = yes ]
then
	echo '</tbody></table>'
fi

echo '<br></form>'
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit

