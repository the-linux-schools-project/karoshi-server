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

############################
#Language
############################

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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Linux Client software packages"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script type="text/javascript" src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
		***********************************************/
	</script>
	<script type="text/javascript">
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

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/linux_client_install_software_packages_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#########################
#Assign data to variables
#########################
END_POINT=6
#Assign VERSION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
	do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = VERSIONcheck ]
	then
		let COUNTER=$COUNTER+1
		VERSION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
	TABLECLASS=standard
	WIDTH=180
	WIDTH2=50
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
	WIDTH=160
	WIDTH2=50
fi

#########################
#Check data
#########################
#Check to see that VERSION is not blank
if [ -z $VERSION ]
then
	MESSAGE=$"Blank version"
	show_status
fi

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
<div class="expanded">
<span>'$"Linux Client software packages"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
else
	echo '<form action="/cgi-bin/admin/linux_client_software_controls.cgi"><input name="___VERSION___" value="'$VERSION'" type="hidden">
<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="0" cellspacing="0"><tbody><tr><td style="vertical-align: top;">
<b>'$"Linux Client Software Controls"' - '$VERSION'</b></td><td style="vertical-align: top;"><input type="submit" class="button" value="'$"Linux Client software controls"'"></td><td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Linux_Client_Software_Packages"><img class="images" alt="" src="/images/help/info.png"><span>'$"The software shown below will be installed by your linux client computers on boot."'</span></a></td></tr></tbody></table></form><br>'
fi

#Show a table of current software to install and remove
# install - /var/lib/samba/netlogon/linuxclient/version/install_list
# remove - /var/lib/samba/netlogon/linuxclient/version/remove_list

ICON1=/images/submenus/client/install_software.png
ICON2=/images/submenus/client/remove_software.png
ICON3=/images/submenus/client/delete_software.png

#Show input box
echo '<form action="/cgi-bin/admin/linux_client_install_software_packages2.cgi" name="selectservers" method="post"><input name="___VERSION___" value="'$VERSION'" type="hidden">
<b>'$"Add software package"'</b><br><br>'

if [ $MOBILE = no ]
then
	echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td style="width: '$WIDTH'px;">'$"Location"'</td><td>'

if [ -f /var/lib/samba/netlogon/locations.txt ]
then
	LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
else
	LOCATION_COUNT=0
fi
#Show current rooms
echo '<select name="___LOCATION___" style="width: 200px;">'
echo '<option value="all">'$"All locations"'</option>'
COUNTER=1
while [ $COUNTER -le $LOCATION_COUNT ]
do
	LOCATION=`sed -n $COUNTER,$COUNTER'p' /var/lib/samba/netlogon/locations.txt`
	echo '<option value="'$LOCATION'">'$LOCATION'</option>'
	let COUNTER=$COUNTER+1
done
echo '</select></td></tr><tr>
<td style="width: '$WIDTH'px;">'$"Software Package"'</td><td><input style="width: 200px;" tabindex= "1" name="___ACTION___add___SOFTWARE___" style="width: '$WIDTH'px;" size="20" type="text"></td>
<td><input type="submit" class="button" value="'$"Install"'"></td></tr>
</tbody></table>'
else
echo '
'$"Software Package"' <input tabindex= "1" name="___ACTION___add___SOFTWARE___" style="width: '$WIDTH'px;" size="20" type="text"><br>
<input type="submit" class="button" value="'$"Install"'"> <input type="submit" class="button" value="'$"Remove"'"><br><br>
'
fi
echo '<br></form><form action="/cgi-bin/admin/linux_client_install_software_packages2.cgi" name="selectservers" method="post"><input name="___VERSION___" value="'$VERSION'" type="hidden">'


for LOCATIONS in /var/lib/samba/netlogon/linuxclient/$VERSION/software/install/*
do
	#Show install list
	LOCATION=`basename $LOCATIONS`
	if [ `cat /var/lib/samba/netlogon/linuxclient/$VERSION/software/install/$LOCATION | wc -l` -gt 0 ]
	then
		echo '
		<b>'$"Location"' - '$LOCATION'</b><br><br><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
		<tr><td style="width: '$WIDTH'px;"><b>'$"Software Package"'</b></td><td style="width: '$WIDTH2'px;"><b>'$"Delete"'</b></td></tr>'
		for SOFTWARE in `cat /var/lib/samba/netlogon/linuxclient/$VERSION/software/install/$LOCATION`
		do
			echo '<tr><td>'$SOFTWARE'</td><td><a class="info" href="javascript:void(0)"><input name="___ACTION___delete___SOFTWARE___'$SOFTWARE'___LOCATION___'$LOCATION'___" type="image" class="images" src="'$ICON3'" value=""><span>'$"Delete" $SOFTWARE'</span></a></td></tr>'
		done
		echo '</tbody></table><br>'
	fi

done
echo '</form></div></div></body></html>'
exit

