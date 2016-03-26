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
  <title>'$"File Manager"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
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

DATA=`cat | tr -cd 'A-Za-z0-9\._:&%\-+*'`
#CONVERT STAR
DATA=`echo "$DATA" | sed 's/*/%99/g'`
#echo $DATA"<br>"
#########################
#Assign data to variables
#########################
END_POINT=45
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

#Assign LOCATION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = LOCATIONcheck ]
	then
		let COUNTER=$COUNTER+1
		LOCATION=`echo $DATA | cut -s -d'_' -f$COUNTER  | sed 's/%2F/\//g' | sed "s/Z%25%25%25%25%25Z/_/g"`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<script>
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/file_manager.cgi";
</script></div></body></html>'
exit
}

if [ -z "$ACTION" ]
then
	ACTION=notset
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
if [ $ACTION != ENTER ] && [ $ACTION != DELETE ] && [ $ACTION != REALLYDELETE ] && [ $ACTION != SETPERMS ] && [ $ACTION != REALLYSETPERMS ] && [ $ACTION != MOVE ] && [ $ACTION != REALLYMOVE ] && [ $ACTION != REALLYCOPY ] && [ $ACTION != CANCELCOPY ] && [ $ACTION != RENAME ] && [ $ACTION != REALLYRENAME ] && [ $ACTION != EDIT ] && [ $ACTION != REALLYEDIT ] && [ $ACTION != CREATEDIR ] && [ $ACTION != REALLYCREATEDIR ] && [ $ACTION != CREATEFILE ] && [ $ACTION != REALLYCREATEFILE ] && [ $ACTION != RESTORE ] && [ $ACTION != REALLYRESTORE ] && [ $ACTION != notset ]
then
	MESSAGE=$"You have not entered a correct action."
	show_status
fi

if [ "$ACTION" = REALLYEDIT ]
then
	END_POINT=32
	COUNTER=2
	#Assign TEXTDATA
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = TEXTDATAcheck ]
		then
			let COUNTER=$COUNTER+1
			TEXTDATA=`echo "$DATA" | cut -s -d'_' -f$COUNTER-`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

if [ "$ACTION" = REALLYCREATEDIR ] || [ "$ACTION" = REALLYCREATEFILE ]
then
	#Assign NEWFOLDER
	END_POINT=32
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = NEWFOLDERcheck ]
		then
			let COUNTER=$COUNTER+1
			NEWFOLDER=`echo "$DATA" | cut -s -d'_' -f$COUNTER- | cut -d'&' -f1`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

if [ "$ACTION" = REALLYRENAME ]
then
	#Assign NEWFOLDER
	END_POINT=32
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo "$DATAHEADER"'check'` = NEWFOLDERcheck ]
		then
			let COUNTER=$COUNTER+1
			NEWFOLDER=`echo "$DATA" | cut -s -d'_' -f$COUNTER- | cut -d'&' -f1`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi


if [ "$ACTION" = REALLYSETPERMS ]
then
	DATA=`echo "$DATA" | tr -cd 'A-Za-z0-9\._:%\-+*'`
	END_POINT=42
	#Assign OWNER
	COUNTER=2
	while [ "$COUNTER" -le "$END_POINT" ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = OWNERcheck ]
		then
			let COUNTER=$COUNTER+1
			OWNER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUP
	COUNTER=2
	while [ "$COUNTER" -le "$END_POINT" ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUPcheck ]
		then
			let COUNTER=$COUNTER+1
			GROUP=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign USERREAD
	COUNTER=2
	while [ "$COUNTER" -le "$END_POINT" ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = USERREADcheck ]
		then
			let COUNTER=$COUNTER+1
			USERREAD=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ "$USERREAD" = 1 ] && PERMISSIONS=USERREAD
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign USERWRITE
	COUNTER=2
	while [ "$COUNTER" -le "$END_POINT" ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = USERWRITEcheck ]
		then
			let COUNTER=$COUNTER+1
			USERWRITE=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $USERWRITE = 1 ] && PERMISSIONS="`echo $PERMISSIONS,USERWRITE`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign USEREXEC
	COUNTER=2
	while [ "$COUNTER" -le "$END_POINT" ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = USEREXECcheck ]
		then
			let COUNTER=$COUNTER+1
			USEREXEC=`echo $DATA | cut -s -d'_' -f$COUNTER`
			[ $USEREXEC = 1 ] && PERMISSIONS="`echo $PERMISSIONS,USEREXEC`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUPREAD
	COUNTER=2
	while [ "$COUNTER" -le "$END_POINT" ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUPREADcheck ]
		then
			let COUNTER=$COUNTER+1
			GROUPREAD=`echo $DATA | cut -s -d'_' -f$COUNTER`
			[ $GROUPREAD = 1 ] && PERMISSIONS="`echo $PERMISSIONS,GROUPREAD`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUPWRITE
	COUNTER=2
	while [ "$COUNTER" -le "$END_POINT" ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUPWRITEcheck ]
		then
			let COUNTER=$COUNTER+1
			GROUPWRITE=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $GROUPWRITE = 1 ] && PERMISSIONS="`echo $PERMISSIONS,GROUPWRITE`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUPEXEC
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUPEXECcheck ]
		then
			let COUNTER=$COUNTER+1
			GROUPEXEC=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $GROUPEXEC = 1 ] && PERMISSIONS="`echo $PERMISSIONS,GROUPEXEC`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign OTHERREAD
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = OTHERREADcheck ]
		then
			let COUNTER=$COUNTER+1
			OTHERREAD=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $OTHERREAD = 1 ] && PERMISSIONS="`echo $PERMISSIONS,OTHERREAD`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign OTHERWRITE
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = OTHERWRITEcheck ]
		then
			let COUNTER=$COUNTER+1
			OTHERWRITE=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $OTHERWRITE = 1 ] && PERMISSIONS="`echo $PERMISSIONS,OTHERWRITE`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign OTHEREXEC
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = OTHEREXECcheck ]
		then
			let COUNTER=$COUNTER+1
			OTHEREXEC=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $OTHEREXEC = 1 ] && PERMISSIONS="`echo $PERMISSIONS,OTHEREXEC`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign SETUID
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SETUIDcheck ]
		then
			let COUNTER=$COUNTER+1
			SETUID=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $SETUID = 1 ] && PERMISSIONS="`echo $PERMISSIONS,SETUID`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign SETGID
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SETGIDcheck ]
		then
			let COUNTER=$COUNTER+1
			SETGID=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $SETGID = 1 ] && PERMISSIONS="`echo $PERMISSIONS,SETGID`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign STICKY
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = STICKYcheck ]
		then
			let COUNTER=$COUNTER+1
			STICKY=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $STICKY = 1 ] && PERMISSIONS="`echo $PERMISSIONS,STICKY`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign RECURSIVE
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = RECURSIVEcheck ]
		then
			let COUNTER=$COUNTER+1
			RECURSIVE=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $RECURSIVE = 1 ] && PERMISSIONS="`echo $PERMISSIONS,RECURSIVE`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign EXECRECURSE
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = EXECRECURSEcheck ]
		then
			let COUNTER=$COUNTER+1
			EXECRECURSE=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
			[ $EXECRECURSE = 1 ] && PERMISSIONS="`echo $PERMISSIONS,EXECRECURSE`"
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Check to see that owner is not blank
	if [ -z "$OWNER" ]
	then
		MESSAGE=$"The owner cannot be blank."
		show_status
	fi

	#Check to see that group is not blank
	if [ -z "$GROUP" ]
	then
		MESSAGE=$"The group cannot be blank."
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

END_POINT=12
#Assign ITEMMOVE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ITEMMOVEcheck ]
	then
		let COUNTER=$COUNTER+1
		ITEMMOVE=`echo $DATA | cut -s -d'_' -f$COUNTER  | sed 's/%2F/\//g' | sed "s/Z%25%25%25%25%25Z/_/g"`
		break
	fi
	let COUNTER=$COUNTER+1
done

if [ "$ACTION" = notset ]
then
	SERVER2=""
	else
	if [ $MOBILE = yes ]
	then
		SERVER2=`echo "- ${SERVERNAME:0:9}" | cut -d. -f1`
	else
		SERVER2="- $SERVERNAME"
	fi
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"File Manager"' '$SERVER2'</span>'
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
	<td style="height:30px;"><div class="sectiontitle">'$"File Manager"' '$SERVER2'</div></td>
	<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=File_Manager"><img class="images" alt="" src="/images/help/info.png"><span>'$"File Manager"'</span></a></td>'

	if [ $SERVERNAME != notset ]
	then
		echo '
	<td>
	<form action="/cgi-bin/admin/file_manager.cgi" method="post">
	<button class="button" name="_">'$"Choose Server"'</button>
	</form>
	</td>
	'
	fi
	echo '</tr></tbody></table></div><div id="infobox">'
fi

echo '<form action="/cgi-bin/admin/file_manager.cgi" method="post">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/file_manager.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$LOCATION:$FILENAME:$ACTION:$PERMISSIONS:$OWNER:$GROUP:$ITEMMOVE:$NEWFOLDER:$TEXTDATA:" | sudo -H /opt/karoshi/web_controls/exec/file_manager

echo '</form>'
[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
