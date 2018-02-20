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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/update_karoshi_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function completed {
echo '<SCRIPT language="Javascript">'
echo '                window.location = "/cgi-bin/admin/update_karoshi_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################

#Assign _PATCHNAME_

END_POINT=19
#Assign PATCHNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PATCHNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		PATCHNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Update Web Management"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>'
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
echo '<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body><div id="pagecontainer">'
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
#Check data
#########################
#Check to see that patchname is not blank
if [ -z "$PATCHNAME" ]
then
	MESSAGE=$"You need to choose an update."
	show_status
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Update Web Management"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div>
'
else
	echo '<div id="'$DIV_ID'"><div id="titlebox">'
fi

if [ "$PATCHNAME" = applyallpatches ]
then
	sudo -H /opt/karoshi/web_controls/exec/apply_all_karoshi_patches $MOBILE:
else
	Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/update_karoshi.cgi | cut -d' ' -f1`
	sudo -H /opt/karoshi/web_controls/exec/update_karoshi $REMOTE_USER:$REMOTE_ADDR:$Checksum:$PATCHNAME:$MOBILE:
fi
EXEC_STATUS=$?

[ $MOBILE = no ] && echo '</div></div>'

if [ $EXEC_STATUS = 102 ]
then
	MESSAGE=`echo $"The updates have been completed." $"Please check the karoshi web administration logs for more details."`
	show_status
	exit
fi

if [ $EXEC_STATUS = 103 ]
then
	echo '<br><b>'$"Showing available updates completed."'</b><br>'
	show_status
	exit
fi
completed


