#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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
  <title>'$"DNS Controls"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	2: { sorter: "ipAddress" }
    		}
		});
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

echo '</head><body><div id="pagecontainer">'

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-+-')
#########################
#Assign data to variables
#########################
END_POINT=19
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

#Assign SERVERTYPE
DATANAME=SERVERTYPE
get_data
SERVERTYPE="$DATAENTRY"

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

#Assign NAME
DATANAME=NAME
get_data
NAME="$DATAENTRY"

#Assign DNSENTRY
DATANAME=DNSENTRY
get_data
DNSENTRY="$DATAENTRY"

#Assign DNSTYPE
DATANAME=DNSTYPE
get_data
DNSTYPE="$DATAENTRY"

#Assign ZONE
DATANAME=ZONE
get_data
ZONE="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/dnsview_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_dns {
echo "
<form action=\"/cgi-bin/admin/dnsview.cgi\" method=\"post\" id=\"showdns\">
<input type=\"hidden\" name=\"_SERVERNAME_$SERVERNAME""_SERVERTYPE_$SERVERTYPE""_ACTION_$ACTION""_ZONE_$ZONE""_\" value=''>
</form>
<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('showdns').submit();
//-->
</script>
</div></div></body></html>
"
exit
}

#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	SERVERNAME=$(hostname-fqdn)
fi

#Check to see that SERVERTYPE is not blank
if [ -z "$SERVERTYPE" ]
then
	SERVERTYPE=network
fi

#Set a default zone
if [ -z "$ZONE" ]
then
	source /opt/karoshi/server_network/domain_information/domain_name
	ZONE="$REALM"
fi

#Check to see that action is not blank.
[ -z "$ACTION" ] && ACTION=view

#Check to see that linenumber is not blank.
[ -z "$LINENUMBER" ] && LINENUMBER=notset

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	WIDTH1=180
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	WIDTH1=120
	DIV_ID=actionbox2
fi

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'



TITLE=$"View Entries"
ALTTITLE=$"View Entries"
ALTDESC=$"View DNS Entries"
ACTION2=view
WIDTH=100
ICON1=/images/submenus/system/dns.png
ICON2=/images/submenus/system/dns.png

[ "$ACTION" = edit ] && TITLE=$"Edit an Entry"
[ "$ACTION" = add ] && TITLE=$"Add Entry"
[ "$ACTION" = viewdnszones ] && TITLE=$"View Zones"
[ "$ACTION" = adddzone ] && TITLE=$"Add Zone"
[ "$ACTION" = deletezone ] && TITLE=$"Delete Zone"

if [ "$ACTION" = view ]
then
	ALTTITLE=$"Add Entry"
	ALTDESC=$"Add a DNS Entry"
	ACTION2=add
	ICON2=/images/submenus/system/dnsadd.png
fi

ACTION3=viewdnszones
ICON3=/images/submenus/system/zones.png
ALTTITLE3=$"Zones"
ALTDESC3=$"View DNS Zones"
if [ "$ACTION" = viewdnszones ]
then
	ALTTITLE3=$"Add Zone"
	ALTDESC3=$"Add a DNS Zone"
	ACTION3=addzone
	ICON3=/images/submenus/system/add.png
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"View DNS Entries"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">

'
else
	echo '<div class="sectiontitle">'"$TITLE"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DNS"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows you to view, edit, and delete the local dns entries on your system."'</span></a></div>'
fi

echo '
<table class="tablesorter"><tbody><tr>

<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
	<form action="/cgi-bin/admin/dnsview.cgi" method="post">
		<button class="info infonavbutton" name="_AltAction_" value="_SERVERNAME_'"$SERVERNAME"'_SERVERTYPE_'"$SERVERTYPE"'_ACTION_'"$ACTION3"'_ZONE_'"$ZONE"'_">
			<img src="'$ICON3'" alt="'"$ALTTITLE3"'">
			<span>'"$ALTDESC3"'</span><br>
			'"$ALTTITLE3"'
		</button>
	</form>
</td>

<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
	<form action="/cgi-bin/admin/dnsview.cgi" method="post">
		<button class="info infonavbutton" name="_AltAction_" value="_SERVERNAME_'"$SERVERNAME"'_SERVERTYPE_'"$SERVERTYPE"'_ACTION_'"$ACTION2"'_ZONE_'"$ZONE"'_">
			<img src="'$ICON2'" alt="'"$ALTTITLE"'">
			<span>'"$ALTDESC"'</span><br>
			'"$ALTTITLE"'
		</button>
	</form>
</td>

<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
	<form action="/cgi-bin/admin/dns_settings.cgi" method="post">
		<button class="info infonavbutton" name="_ViewDNSSettings_" value="_">
			<img src="'$ICON1'" alt="'$"DNS Settings"'">
			<span>'$"View server DNS Settings"'</span><br>
			'$"DNS Settings"'
		</button>
	</form>
</td>

</tr></tbody></table>'


[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/dnsview.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$SERVERTYPE:$ACTION:$NAME:$DNSENTRY:$DNSTYPE:$ZONE:$MOBILE" | sudo -H /opt/karoshi/web_controls/exec/dnsview

if [ "$ACTION" = reallyedit ] || [ "$ACTION" = reallydelete ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallyaddzone ] || [ "$ACTION" = reallydeletezone ]
then
	if [ "$ACTION" = reallyaddzone ] || [ "$ACTION" = reallydeletezone ]
	then
		ACTION=viewdnszones
	else
		ACTION=view
	fi
	show_dns
fi

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></div></body></html>'
exit

