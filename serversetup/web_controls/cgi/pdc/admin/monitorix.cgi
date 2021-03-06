#!/bin/bash
#Copyright (C) 2014 Paul Sharrad

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

########################
#Required input variables
########################
#  _USERNAME_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

########################
#Language
########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Monitorix System Monitor"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g')
#########################
#Assign data to variables
#########################
END_POINT=12
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

#Assign SERVERNAME
DATANAME=SERVERNAME
get_data
SERVERNAME="$DATAENTRY"

#Assign INTERVAL
DATANAME=INTERVAL
get_data
INTERVAL="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">
alert("'"$MESSAGE"'");
window.location = "/cgi-bin/admin/monitorix_fm.cgi"
</script>
</div></body></html>'
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

#Check to see that username is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The servername cannot be blank."
	show_status
fi

if [ -z "$INTERVAL" ]
then
	MESSAGE=$"The interval cannot be blank."
	show_status
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	/opt/karoshi/web_controls/generate_navbar_admin
	WIDTH=100
	ICON1=/images/submenus/system/computer.png
else
	DIV_ID=actionbox2
	WIDTH=90
	ICON1=/images/submenus/system/computerm.png
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#echo HTTP_REFERER is $HTTP_REFERER"<br>"
ACCESSPORT=50001
[[ $(echo "$HTTP_REFERER" | grep -c ":50002") -gt 0 ]] && ACCESSPORT=50002
source /opt/karoshi/server_network/domain_information/domain_name
source /opt/karoshi/web_controls/version
echo '
<div class="sectiontitle">'$"Monitorix System Monitor"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=System_Monitoring"><img class="images" alt="" src="/images/help/info.png"><span>'$"Monitorix is a system monitoring tool."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form name="myform" action="/cgi-bin/admin/monitorix_fm.cgi" method="post">
			<button class="info infonavbutton" name="SelectServer" value="_">
				<img src="'"$ICON1"'" alt="'$"Select server"'">
				<span>'$"Select the server you want to view."'</span><br>
				'$"Select Server"'
			</button>
		</form>
	</td>

</tr></table><br></div><div id="infobox">'
#Show monitorix data

echo '<iframe src="https://manage.'"$REALM"':'"$ACCESSPORT"'/monitorix-'"$SERVERNAME"'/monitorix.cgi?mode=localhost&amp;graph=all&amp;when='"$INTERVAL"'&amp;color=white" frameborder="0" width="1000" height="3000" scrolling="no"></iframe>'


echo '</div></div></div></body></html>'
exit
