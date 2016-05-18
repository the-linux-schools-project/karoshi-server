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
  <title>'$"Firewall Rules"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	4: { sorter: false}
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

DATA=`cat | tr -cd 'A-Za-z0-9\._:&%\-+' | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g'`

#########################
#Assign data to variables
#########################
END_POINT=22
#Assign SERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
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

#Assign RULESET
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = RULESETcheck ]
	then
		let COUNTER=$COUNTER+1
		RULESET=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/+/-/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

if [ -z "$ACTION" ]
then
	ACTION=view
fi

if [ -z "$SERVERNAME" ]
then
	SERVERNAME=notset
else
	SERVERNAME2=$(echo $SERVERNAME | cut -d. -f1)
fi

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallyedit ]
then
	END_POINT=22
	#Assign FIREWALLACTION
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = FIREWALLACTIONcheck ]
		then
			let COUNTER=$COUNTER+1
			FIREWALLACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign PORTS
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = PORTScheck ]
		then
			let COUNTER=$COUNTER+1
			PORTS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3A/-/g' | sed 's/%2C/,/g' | tr -cd "0-9\-," | sed 's/,,/,/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign PROTOCOL
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = PROTOCOLcheck ]
		then
			let COUNTER=$COUNTER+1
			PROTOCOL=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%2C/,/g'`
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
			TCPIP=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH=180
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=mobileactionbox
	TABLECLASS=mobilestandard
	WIDTH=160
fi


function show_status {
echo '<script>
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/firewall.cgi";
</script></div></body></html>'
exit
}

if [ "$ACTION" = edit ] || [ "$ACTION" = delete ]
then
	if [ -z "$RULESET" ]
	then
		MESSAGE=$"The ruleset cannot be blank."
		show_status
	fi
fi

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallyedit ]
then

	if [ -z "$RULESET" ]
	then
		MESSAGE=$"You have not entered the name of the ruleset."
		show_status
	fi	

	if [ -z "$PORTS" ]
	then
		MESSAGE=$"You have not entered in any ports."
		show_status
	fi
	#Check to see that valid ports have been entered.

	for PORT in $(echo $PORTS | sed 's/,/ /g' | sed 's/-/ /g' )
	do
		#Check that the port is not blank
		if [ -z "$PORT" ]
		then
			MESSAGE=$"You have entered in a blank port."
			show_status
		fi 
		#Check that the port is within range
		if [ $PORT -gt 65535 ]
		then
			MESSAGE=$"You have entered in a port that is larger than the maximum port number."
			show_status
		fi
		if [ $PORT -le 0 ]
		then
			MESSAGE=$"You cannot have zero as a port number."
			show_status
		fi
	done
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"Firewall Rules"' '$SERVER2'</span>'
	if [ "$SERVERNAME" != notset ]
	then
		echo '<a href="/cgi-bin/admin/firewall.cgi">'$"Select Server"'</a>'
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
	<td style="height:30px;"><div class="sectiontitle">'$"Firewall Rules"' '$SERVERNAME2'</div></td>
	<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Firewall_Rules"><img class="images" alt="" src="/images/help/info.png"><span>'$"Firewall Rules"'</span></a></td>'

	if [ "$SERVERNAME" != notset ]
	then
		echo '
	<td>
	<form action="/cgi-bin/admin/firewall.cgi" method="post">
	<button class="button" name="_">'$"Choose Server"'</button>
	</form>
	</td>
	'
	fi

	if [ "$ACTION" = view ] || [ "$ACTION" = reallydelete ] || [ "$ACTION" = reallyedit ] || [ "$ACTION" = reallyadd ] && [ "$SERVERNAME" != notset ]
	then
		echo '
	<td>
	<form action="/cgi-bin/admin/firewall.cgi" method="post">
	<button class="button" name="___AddRule___" value="___ACTION___add___SERVERTYPE___'$SERVERTYPE'___SERVERMASTER___'$SERVERMASTER'___SERVERNAME___'$SERVERNAME'___">'$"Add Rule"'</button>
	</form>
	</td>
	'
	fi
	if [ "$ACTION" = add ] || [ "$ACTION" = edit ] || [ "$ACTION" = delete ]
	then
		echo '
	<td>
	<form action="/cgi-bin/admin/firewall.cgi" method="post">
	<button class="button" name="___ViewRules___" value="___ACTION___view___SERVERTYPE___'$SERVERTYPE'___SERVERMASTER___'$SERVERMASTER'___SERVERNAME___'$SERVERNAME'___">'$"View Rules"'</button>
	</form>
	</td>
	'
	fi


	echo '</tr></tbody></table></div><div id="infobox">'
fi

echo '<form action="/cgi-bin/admin/firewall.cgi" method="post">'

if [ "$SERVERNAME" = notset ]
then
	#Show list of servers
	/opt/karoshi/web_controls/show_servers $MOBILE servers $"View Rules" view "" "___"
else
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/firewall.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$ACTION:$RULESET:$FIREWALLACTION:$PROTOCOL:$PORTS:$TCPIP:" | sudo -H /opt/karoshi/web_controls/exec/firewall
fi

echo '</form>'
[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
