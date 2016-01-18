#!/bin/bash
#Copyright (C) 2014  Paul Sharrad

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Radius Access Points"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	1: { sorter: "ipAddress" },
	2: { sorter: false},
	3: { sorter: false}
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


echo '</head><body onLoad="start()"><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`

#########################
#Assign data to variables
#########################
END_POINT=10

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

#Assign TCPIP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = TCPIPcheck ]
	then
		let COUNTER=$COUNTER+1
		TCPIP=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9.%F' | sed 's/%2F/\//g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SHORTNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SHORTNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		SHORTNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign SECRETKEY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SECRETKEYcheck ]
	then
		let COUNTER=$COUNTER+1
		SECRETKEY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/radius_access_points.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	TABLECLASS=standard
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
	echo '<div id="'$DIV_ID'">'
else
	TABLECLASS=mobilestandard
fi

#Check data
if [ "$ACTION" = reallyadd ]
then
	#Check to see that TCPIP is not blank
	if [ -z "$TCPIP" ]
	then
		MESSAGE=$"The tcpip number cannot be blank."
		show_status
	fi
	#Check to see that SHORTNAME is not blank
	if [ -z "$SHORTNAME" ]
	then
		MESSAGE=$"The shortname cannot be blank."
		show_status
	fi
	#Check to see that SECRETKEY fields are not blank
	if [ -z "$SECRETKEY" ]
	then
		MESSAGE=$"The secret key cannot be blank."
		show_status
	fi

	#Check that we have some sort of useful ip address.
	if [ `ipcalc -n "$TCPIP" | grep -c INVALID` -gt 0 ]
	then
		MESSAGE=$"The TCPIP address is incorrect."
		show_status	
	fi

fi

echo '<form action="/cgi-bin/admin/radius_access_points.cgi" method="post">'

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = add ] || [ "$ACTION" = edit ]
then
	ACTION2=view
	BUTTONTXT=$"View Access Points"
	TITLETXT=$"Add Access Point"
fi

if [ "$ACTION" = view ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = delete ]
then
	ACTION2=add
	BUTTONTXT=$"Add Access Point"
	TITLETXT=$"View Access Points"
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLETXT'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
fi
echo '<table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: middle;"><b>'$TITLETXT'</b></td>
<td style="vertical-align: top;">
<input name="____ACTION____'$ACTION2'____" type="submit" class="button" value="'$BUTTONTXT'">
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Radius_Server#Viewing_Access_Points"><img class="images" alt="" src="/images/help/info.png"><span>'$"Access Points"'</span></a>
</td></tr></tbody></table><br>
'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/radius_access_points.cgi | cut -d' ' -f1`
#View access points
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$ACTION:$SHORTNAME:$SECRETKEY:$TCPIP:" | sudo -H /opt/karoshi/web_controls/exec/radius_access_points

echo '</div></form></div></body></html>'
exit
