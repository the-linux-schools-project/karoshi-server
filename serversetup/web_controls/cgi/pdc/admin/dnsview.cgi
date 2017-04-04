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
  <title>'$"DNS Controls"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
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

echo '</head><body><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+-'`
#########################
#Assign data to variables
#########################
END_POINT=19

#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SERVERTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERTYPEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
	done

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

#Assign NAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = NAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		NAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign DNSENTRY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = DNSENTRYcheck ]
	then
		let COUNTER=$COUNTER+1
		DNSENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign DNSTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = DNSTYPEcheck ]
	then
		let COUNTER=$COUNTER+1
		DNSTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign ZONE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ZONEcheck ]
	then
		let COUNTER=$COUNTER+1
		ZONE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/dnsview_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_dns {
echo "
<form action=\"/cgi-bin/admin/dnsview.cgi\" method=\"post\" id=\"showdns\">
<input type=\"hidden\" name=\"_SERVERNAME_$SERVERNAME"_"SERVERTYPE_$SERVERTYPE"_"ACTION_$ACTION"_"ZONE_$ZONE"_"\" value=''>
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
	MESSAGE=$"The servername cannot be blank."
	show_status
fi

#Check to see that SERVERTYPE is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$"The servertype cannot be blank."
	show_status
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

#Check to see if we have a monitoring server
MONITORSERVER=no
[ -f /opt/karoshi/server_network/monitoringserver ] && MONITORSERVER=yes


#Generate navigation bar
if [ $MOBILE = no ]
then
	WIDTH1=180
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	WIDTH1=100
	DIV_ID=actionbox2
fi

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'



TITLE=$"View DNS Entries"
ALTTITLE=$"View DNS Entries"
ICON=/images/submenus/system/dnsviewm.png
ACTION2=view

[ $ACTION = edit ] && TITLE=$"Edit a DNS Entry"
[ $ACTION = add ] && TITLE=$"Add DNS Entry"
[ $ACTION = viewdnszones ] && TITLE=$"View DNS Zones"
[ $ACTION = adddzone ] && TITLE=$"Add DNS Zone"
[ $ACTION = deletezone ] && TITLE=$"Delete DNS Zone"

if [ $ACTION = view ]
then
	ALTTITLE=$"Add DNS Entry"
	ACTION2=add
	ICON=/images/submenus/system/dnsaddm.png
fi

ACTION3=viewdnszones
ALTTITLE3=$"DNS Zones"
if [ $ACTION = viewdnszones ]
then
	ALTTITLE3=$"Add Zone"
	ACTION3=addzone
fi

SERVERNAME2=`echo "${SERVERNAME:0:9}" | cut -d. -f1`

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"View DNS Entries"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
<form action="/cgi-bin/admin/dnsview.cgi" method="post">
<input name="_SERVERNAME_'$SERVERNAME'_SERVERTYPE_'$SERVERTYPE'_ACTION_'$ACTION2'_" type="submit" class="button" value="'$ALTTITLE'">
</form>
<br>
'
else
	echo '<table class="standard" style="text-align: left;" >
<tr><td style="min-width: '$WIDTH1'px;"><div class="sectiontitle">'$TITLE'</div></td>
<td>
<form action="/cgi-bin/admin/dnsview.cgi" method="post">
<button class="button" name="_AltAction_" value="_SERVERNAME_'$SERVERNAME'_SERVERTYPE_'$SERVERTYPE'_ACTION_'$ACTION3'_ZONE_'$ZONE'_">
'$ALTTITLE3'
</button>
</form>
</td>
<td>
<form action="/cgi-bin/admin/dnsview.cgi" method="post">
<button class="button" name="_AltAction_" value="_SERVERNAME_'$SERVERNAME'_SERVERTYPE_'$SERVERTYPE'_ACTION_'$ACTION2'_ZONE_'$ZONE'_">
'$ALTTITLE'
</button>
</form>
</td>
<td>
<form action="/cgi-bin/admin/dns_settings.cgi" method="post">
<button class="button" name="_ViewDNSSettings_">'$"DNS Settings"'</button>
</form>
</td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DNS"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows you to view, edit, and delete the local dns entries on your system."'</span></a></td>
</tr></tbody></table>'
fi

[ $MOBILE = no ] && echo '</div><div id="infobox">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/dnsview.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$SERVERTYPE:$ACTION:$NAME:$DNSENTRY:$DNSTYPE:$ZONE:$MOBILE" | sudo -H /opt/karoshi/web_controls/exec/dnsview

if [ $ACTION = reallyedit ] || [ $ACTION = reallydelete ] || [ $ACTION = reallyadd ] || [ $ACTION = reallyaddzone ] || [ $ACTION = reallydeletezone ]
then
	if [ $ACTION = reallyaddzone ] || [ $ACTION = reallydeletezone ]
	then
		ACTION=viewdnszones
	else
		ACTION=view
	fi
	show_dns
fi

echo '</div></div></div></body></html>'
exit

