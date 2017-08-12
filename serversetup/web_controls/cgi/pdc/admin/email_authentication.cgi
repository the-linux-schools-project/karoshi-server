#!/bin/bash
#Copyright (C) 2015  Paul Sharrad

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

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"E-Mail Authentication"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
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
'

HELPCLASS="info"

if [ "$MOBILE" = yes ]
then
	HELPCLASS="info infoleft"
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

echo '</head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%+' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g')
#########################
#Assign data to variables
#########################
END_POINT=16
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

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = delete ] || [ "$ACTION" = reallydelete ] || [ "$ACTION" = reallyadd ]
then
	#Assign TCPIP
	DATANAME=TCPIP
	get_data
	TCPIP="$DATAENTRY"
fi

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = delete ]
then
	#Assign COMMENT
	DATANAME=COMMENT
	get_data
	COMMENT="$DATAENTRY"
fi


function show_status {
echo '<script>'
echo 'alert("'"$MESSAGE"'");'
echo 'window.location = "/cgi-bin/admin/email_authentication.cgi";'
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
#Check data
#########################

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ]
then
	#Check to see that TCPIP is not blank
	if [ -z "$TCPIP" ]
	then
		MESSAGE=$"You have not entered a TCPIP address."
		show_status
	fi
fi

if [ "$ACTION" = reallyadd ]
then
	#Check to see that COMMENT is not blank
	if [ -z "$COMMENT" ]
	then
		MESSAGE=$"You have not entered a comment for the TCPIP address."
		show_status
	fi

	#Check that we have some sort of useful ip address.
	if [[ $(ipcalc -n "$TCPIP" | grep -c INVALID) -gt 0 ]]
	then
		MESSAGE=$"The TCPIP address is incorrect."
		show_status	
	fi
fi

if [ "$MOBILE" = no ]
then
	WIDTH=100
	ICON1=/images/submenus/system/edit.png
	ICON2=/images/submenus/system/add.png
	DIV_ID=actionbox3
else
	WIDTH=90
	ICON1=/images/submenus/system/editm.png
	ICON2=/images/submenus/system/addm.png
fi 

if [ "$ACTION" = add ] || [ "$ACTION" = delete ]
then
	ACTION2=view
	BUTTONTXT=$"View"
	BUTTONTXT2=$"View TCPIP addresses."
	TITLETXT=$"Add TCPIP Address"
	ICON="$ICON1"
	[ "$ACTION" = delete ] && TITLETXT=$"Delete TCPIP Address"
fi

if [ "$ACTION" = view ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ]
then
	ACTION2=add
	BUTTONTXT=$"Add"
	BUTTONTXT2=$"Add a TCPIP address."
	TITLETXT=$"Bypass E-Mail Authentication"
	ICON="$ICON2"
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
	echo '<div id="'"$DIV_ID"'"><div id=titlebox>
	<div class="sectiontitle">'"$TITLETXT"' <a class="'"$HELPCLASS"'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=E-Mail_Authentication"><img class="images" alt="" src="/images/help/info.png"><span>'$"By default all E-Mail clients have to authenticate to be able to send E-Mails."'<br><br>'$"Here you can allow TCPIP addresses that you want to be able to send E-Mail without having to authenticate."'</span></a></div>
	'
fi


#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'"$TITLETXT"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
fi
echo '<form action="/cgi-bin/admin/email_authentication.cgi" method="post">

<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" name="____DoAction____" value="____ACTION____'"$ACTION2"'____">
			<img src="'"$ICON"'" alt="'"$BUTTONTXT"'">
			<span>'"$BUTTONTXT2"'</span><br>
			'"$BUTTONTXT"'
		</button>
	</td>

</tr></tbody></table></form>'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">' 

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/email_authentication.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$TCPIP:$COMMENT:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/email_authentication
EXIT_STATUS="$?"

if [ "$EXIT_STATUS" = 102 ]
then
	MESSAGE=$"A folder with this name already exists."
	show_status	
fi

if [ "$EXIT_STATUS" = 103 ]
then
	MESSAGE=$"This share already exits in samba."
	show_status	
fi

[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
