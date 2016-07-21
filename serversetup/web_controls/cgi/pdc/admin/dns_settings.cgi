#!/bin/bash
#Copyright (C) 2016  Paul Sharrad

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
  <title>'$"DNS Settings"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
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

DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+*'`
#CONVERT STAR
DATA=`echo "$DATA" | sed 's/*/%99/g'`
#echo $DATA"<br>"
#########################
#Assign data to variables
#########################
END_POINT=25
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

END_POINT=45

#Assign DNS1
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = DNS1check ]
	then
		let COUNTER=$COUNTER+1
		DNS1=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign DNS2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = DNS2check ]
	then
		let COUNTER=$COUNTER+1
		DNS2=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<script>
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/dns_settings.cgi";
</script></div></body></html>'
exit
}

#Check data
if [ -z "$ACTION" ]
then
	ACTION=view
fi

if [ "$ACTION" = reallyedit ]
then
	if [ -z "$SERVERNAME" ]
	then
		MESSAGE=$"The servername cannot be blank."
		show_status
	fi

	if [ -z "$DNS1" ]
	then
		MESSAGE=$"You have not entered in a DNS entry."
		show_status
	fi
	#Check that the tcpip number is valid.

	#Check dots and max number.
	if [ $(echo "$DNS1" | sed 's/\./\n /g'  | sed /^$/d | wc -l) != 4 ] || [ $(echo "$DNS1" | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p) -gt 255 ]
	then
		MESSAGE=$"You have entered in an incorrect DNS entry."
		show_status
	fi
	if [ ! -z "$DNS2" ]
	then
		if [ $(echo "$DNS2" | sed 's/\./\n /g'  | sed /^$/d | wc -l) != 4 ] || [ $(echo "$DNS1" | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p) -gt 255 ]
		then
			MESSAGE=$"You have entered in an incorrect DNS entry."
			show_status
		fi
	fi
fi

if [ -z "$SERVERNAME" ]
then
	SERVERNAME=notset
fi
if [ -z "$SERVERTYPE" ]
then
	SERVERTYPE=notset
fi

if [ $SERVERTYPE = federatedslave ]
then
	#Assign SERVERMASTER
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SERVERMASTERcheck ]
		then
			let COUNTER=$COUNTER+1
			SERVERMASTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

#########################
#Check data
#########################



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
		<span>'$"DNS Settings"' '$SERVER2'</span>'
	if [ $SERVERNAME != notset ]
	then
		echo '<a href="/cgi-bin/admin/dns_settings.cgi">'$"Select Server"'</a>'
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
	<td style="vertical-align: top;"><div class="sectiontitle">'$"DNS Settings"' '$SERVER2'</div></td>'

	if [ $SERVERNAME != notset ]
	then
		echo '
	<td style="vertical-align: top;">
	<form action="/cgi-bin/admin/dns_settings.cgi" method="post">
	<button class="button" name="_">'$"Choose Server"'</button>
	</form>
	</td>
	'
	else
		echo '<td style="vertical-align: top;">
	<form action="/cgi-bin/admin/dnsview_fm.cgi" method="post">
	<button class="button" name="_ViewDNSEntries_">'$"View DNS Entries"'</button>
	</form>
	</td>'
	fi
	echo '<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DNS_Settings"><img class="images" alt="" src="/images/help/info.png"><span>'$"View and edit the DNS settings for your servers."'</span></a></td></tr></tbody></table></div><div id="infobox">'
fi

echo '<form action="/cgi-bin/admin/dns_settings.cgi" method="post">'

if [ "$ACTION" = reallyedit ] || [ "$ACTION" = autogenerate ]
then
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/dns_settings.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$ACTION:$DNS1:$DNS2:" | sudo -H /opt/karoshi/web_controls/exec/dns_set_forwarder	
	ACTION=view
fi

if [ "$ACTION" = edit ]
then
	#Get DNS settings for the server
	DNSLIST=( $(sudo -H /opt/karoshi/web_controls/exec/get_dns_forwarders $SERVERNAME) )
	DNSLISTCOUNT=${#DNSLIST[*]} 

	FORMACTION=reallyedit
	[ $DNSLISTCOUNT -gt 1 ] && FORMACTION=autogenerate

	#Show form with the current dns servers on it


	echo '<input type="hidden" name="_SERVERNAME_'$SERVERNAME'_">
	<input type="hidden" name="_SERVERTYPE_'$SERVERTYPE'_">
	<input type="hidden" name="_SERVERMASTER_" value="'$SERVERMASTER'">
	<input type="hidden" name="_ACTION_" value="'$FORMACTION'">
	<table class="tablesorter" style="text-align: left;" ><tbody>
	<tr><td style="width: 220px;">'$"Servername"'</td><td style="width: 180px;">'$SERVERNAME'</td></tr>'

	COUNTER=0
	COUNTER1=1
	while [ $COUNTER -lt $DNSLISTCOUNT ]
	do
		echo '<tr><td>'$"DNS Server"' 1</td><td>'
		if [ "$FORMACTION" = reallyedit ]
		then
			echo '<input tabindex= "'$COUNTER1'" style="width: 120px;" name="_DNS'$COUNTER1'_" value="'${DNSLIST[$COUNTER]}'"  type="text">'
		else
			echo "${DNSLIST[$COUNTER]}"
		fi
	echo '</td></tr>'
		let COUNTER=$COUNTER+1
		let COUNTER1=$COUNTER1+1		
	done
	echo '</tbody></table>'
	[ "$FORMACTION" = autogenerate ] && echo ''$"This server uses your Domain Controllers for DNS."' '$"Press submit to auto regenerate the DNS settings."''
	echo '<br><br><input value="'$"Submit"'" class="button" type="submit">'
	[ "$FORMACTION" = reallyedit ] && echo ' <input value="'$"Reset"'" class="button" type="reset">'
fi

#Show list of servers
if [ "$ACTION" = view ]
then
	/opt/karoshi/web_controls/show_servers $MOBILE servers $"Set DNS Forwarder" "edit" "showdns"
fi

echo '</form>'
[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
