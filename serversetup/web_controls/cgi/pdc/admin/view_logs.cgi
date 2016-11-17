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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"View Event Logs"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	3: { sorter: false},
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

DATA=`echo $QUERY_STRING | tr -cd 'A-Za-z0-9\_.-/-' | sed 's/\.\.\///g'`

#If we have not received any data via get then try and get it from post
if [ -z "$DATA" ]
then
	DATA=`cat | tr -cd 'A-Za-z0-9\_.-/-%' | sed 's/\.\.\///g'`
fi

#########################
#Assign data to variables
#########################
END_POINT=45

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

#Assign SERVERNAME
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

#Assign LOGFILE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = LOGFILEcheck ]
	then
		let COUNTER=$COUNTER+1
		LOGFILE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign TAIL_LENGTH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = TAIL_LENGTHcheck ]
	then
		let COUNTER=$COUNTER+1
		TAIL_LENGTH=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done


function show_status {
echo '<script>
alert("'$MESSAGE'");
</script></div></body></html>'
exit
}

#Check data

if [ -z "$SERVERNAME" ]
then
	SERVERNAME=viewservers
	SERVERNAME2=""
else
	SERVERNAME2="$SERVERNAME"
fi

if [ $(ls -1 /opt/karoshi/server_network/servers/ | wc -l) = 1 ]
then
	SERVERNAME=$(hostname-fqdn)
	SERVERTYPE=network
	SERVERMASTER=notset	
fi

if [ -z "$LOGFILE" ]
then
	LOGFILE=viewlist
	LOGFILE2=""
	EVENT=""
else
	LOGFILE2=`echo "$LOGFILE" | sed 's/%3A/:/g'`
	#Get time, date and category of the event
	CATEGORY=$(echo $LOGFILE2= | cut -d"-" -f1)

	case "$CATEGORY" in
		syslog)
		    CATEGORY2=$"System Log"
		    ;;
		 
		backup)
		    CATEGORY2=$"Backup Log"
		    ;;
		 
		restore)
		     CATEGORY2=$"Restore Log"
		    ;;
	esac
	DAY=$(echo "$LOGFILE2" | cut -d"-" -f4)
	MONTH=$(echo "$LOGFILE2" | cut -d"-" -f3)
	YEAR=$(echo "$LOGFILE2" | cut -d"-" -f2)
	TIME=$(echo "$LOGFILE2" | cut -d"-" -f5)
	EVENT="$DAY-$MONTH-$YEAR $TIME"
fi

if [ "$ACTION" != viewevent ]
then
	EVENT=""
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
	SERVERNAME2=`echo $SERVERNAME | cut -d. -f1`
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"View Event Logs"' '$SERVERNAME2'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div>
	<div id="'$DIV_ID'">
	'
else
	echo '<div id="'$DIV_ID'"><div id="titlebox"><div class="sectiontitle">'$"View Event Logs"' '$SERVERNAME2' '$CATEGORY' '$EVENT'</div></div><div id="infobox">'
fi
if [ $SERVERNAME = viewservers ]
then
	#Show list of servers
	echo '<form action="/cgi-bin/admin/view_logs.cgi" method="post">'
	/opt/karoshi/web_controls/show_servers $MOBILE servers $"View Event Logs" viewlist
	echo '</form>'
else
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/view_logs.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$SERVERNAME:$ACTION:$LOGFILE:$TAIL_LENGTH:" | sudo -H /opt/karoshi/web_controls/exec/view_logs
fi

[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit

