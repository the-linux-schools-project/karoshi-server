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

############################
#Language
############################

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version


STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/view_disk_usage_logs_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Get data input
#########################

DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')

#If we have not received any data via post then try and get it from query_string
if [ -z "$DATA" ]
then
	DATA=$(echo "$QUERY_STRING" | tr -cd 'A-Za-z0-9\_.-/-' | sed 's/\.\.\///g')
fi
#########################
#Assign data to variables
#########################
END_POINT=38
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

#Assign DATE
DATANAME=DATE
get_data
DATE="$DATAENTRY"

#Assign LOGVIEW
DATANAME=LOGVIEW
get_data
LOGVIEW="$DATAENTRY"

#Assign SERVERNAME
DATANAME=SERVERNAME
get_data
SERVER="$DATAENTRY"

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Disk Usage Logs"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
echo '</head><body><div id="pagecontainer">'
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

#Check to see that LOGVIEW is not blank
if [ -z "$LOGVIEW" ]
then
	MESSAGE=$"The logview cannot be blank."
	show_status
fi
#Check to see that DATE is not blank
if [ -z "$DATE" ]
then
	MESSAGE=$"The date cannot be blank."
	show_status
fi


#Check that date is valid
DAY=$(echo "$DATE" | cut -d- -f1)
MONTH=$(echo "$DATE" | cut -d- -f2)
YEAR=$(echo "$DATE" | cut -d- -f3)

#Check to see that MONTH is not blank
if [ -z "$MONTH" ]
then
	MESSAGE=$"The date cannot be blank."
	show_status
fi
#Check to see that YEAR is not blank
if [ -z "$YEAR" ]
then
	MESSAGE=$"The date cannot be blank."
	show_status
fi

if [ "$DAY" -gt 31 ]
then
	MESSAGE=$"Incorrect date format."
	show_status
fi

if [ "$MONTH" -gt 12 ]
then
	MESSAGE=$"Incorrect date format."
	show_status
fi

if [ "$YEAR" -lt 2006 ] || [ "$YEAR" -gt 3006 ]
then
	MESSAGE=$"Incorrect date format."
	show_status
fi

#Check to see that server is not blank
if [ -z "$SERVER" ]
then
	MESSAGE=$"You have not chosen any servers."
	show_status
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	SERVER2=$(echo "${SERVER:0:9}" | cut -d. -f1)
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Disk Usage Logs"' - '"$SERVER2"'</span>
<a href="/cgi-bin/admin/view_disk_usage_logs_fm.cgi">'$"Select Server"'</a>
</div></div>
<div id="mobileactionbox">
'

else
	WIDTH=100
	ICON1=/images/submenus/system/computer.png
	echo '
	<div class="sectiontitle">'$"View Disk Usage Logs"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Disk_Usage_Logs"><img class="images" alt="" src="/images/help/info.png"><span>'$"The disk usage logs show the overall usage for each partition on your server."'</span></a></div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<form action="view_disk_usage_logs_fm.cgi" name="selectservers" method="post">
				<button class="info" name="SelectServer" value="__">
					<img src="'$ICON1'" alt="'$"Select server"'">
					<span>'$"Select the server you want to view."'</span><br>
					'$"Select Server"'
				</button>
			</form>
		</td>

	</tr></tbody></table><br>
'
fi

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/view_disk_usage_logs.cgi | cut -d' ' -f1)
sudo -H /opt/karoshi/web_controls/exec/view_disk_usage_logs "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$LOGVIEW:$DAY:$MONTH:$YEAR:$SERVER:$MOBILE:"
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
