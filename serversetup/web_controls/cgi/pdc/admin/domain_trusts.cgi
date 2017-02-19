#!/bin/bash
#Copyright (C) 2017  Paul Sharrad

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
if [ `echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT"` = 1 ]
then
	TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta charset="UTF-8">
  <title>'$"Domain Trusts"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	0: { sorter: "ipAddress" },
	1: { sorter: "MAC" }
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
echo '</head><body onLoad="start()"><div id="pagecontainer">'
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\/*%+"-' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/QUADUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=27
#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = add ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = remove ] || [ "$ACTION" = reallyremove ] || [ "$ACTION" = edit ] || [ "$ACTION" = reallyedit ]
then
	#Assign DOMAIN
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = DOMAINcheck ]
		then
			let COUNTER=$COUNTER+1
			DOMAIN=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallyremove ]
then
	#Assign USERNAME
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign PASSWORD
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = PASSWORDcheck ]
		then
			let COUNTER=$COUNTER+1
			PASSWORD=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

if [ "$ACTION" = reallyadd ]
then
	#Assign IPADDRESS1
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = IPADDRESS1check ]
		then
			let COUNTER=$COUNTER+1
			IPADDRESS1=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign IPADDRESS2
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = IPADDRESS2check ]
		then
			let COUNTER=$COUNTER+1
			IPADDRESS2=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi
function show_status {
echo '<script>
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/arp_control.cgi";
</script></div></body></html>'
exit
}

if [ -z "$ACTION" ]
then
	ACTION=view
fi

#Check data

if [ "$ACTION" = reallyadd2 ]
then
	if [ -z "$DEVICE" ]
	then
		MESSAGE=$"No TCPIP information has been received."
		show_status
	fi

	#Check that tcpip number is correct
	#Check that we have 4 dots
	if [ `echo $DEVICE | sed 's/\./\n /g'  | sed /^$/d | wc -l` != 4 ]
	then
		MESSAGE=$"The TCPIP number is not corrrect."
		show_status
	fi
	#Check that no number is greater than 255
	HIGHESTNUMBER=`echo $DEVICE | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p`
	if [ $HIGHESTNUMBER -gt 255 ]
	then
		MESSAGE=$"The TCPIP number is not corrrect."
		show_status
	fi
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=mobileactionbox
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"Domain Trusts"'</span>'
	if [ $SERVERNAME != notset ]
	then
		echo '<a href="/cgi-bin/admin/file_manager.cgi">'$"Select Server"'</a>'
	else
		echo '<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>'
	fi
	echo '</div></div>
	<div id="'$DIV_ID'">
	'

	else
		echo '<div id="'$DIV_ID'"><div id="titlebox">
	<table class="standard" style="text-align: left;" ><tbody>
	<tr>
	<td style="height:30px;"><div class="sectiontitle">'$"Domain Trusts"'</div></td>
	<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Domain_Trusts"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows you to add a domain trust so that users from other domains can log into this domain."'</span></a></td>

	<td>'
	if [ "$ACTION" = view ] || [ "$ACTION" = reallyadd ]
	then
		echo '<form action="/cgi-bin/admin/domain_trusts.cgi" method="post">
		<button class="button" name="____ACTION____add____">'$"Add a domain trust"'</button>
		</form>'
	else
		echo '<form action="/cgi-bin/admin/domain_trusts.cgi" method="post">
		<button class="button" name="____ACTION____view____">'$"View domain trusts"'</button>
		</form>'
	fi
	echo '</td>

	</tr></tbody></table>
	</div><div id="infobox">'
fi

echo '<form action="/cgi-bin/admin/domain_trusts.cgi" method="post">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/domain_trusts.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$DOMAIN:$USERNAME:$PASSWORD:$IPADDRESS1:$IPADDRESS2:" | sudo -H /opt/karoshi/web_controls/exec/domain_trusts

echo '</form>'
[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
