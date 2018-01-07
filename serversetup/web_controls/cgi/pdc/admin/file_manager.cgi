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
if [ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]
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
  <title>'$"File Manager"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
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

DATA=$(cat | tr -cd 'A-Za-z0-9\._:&%\-+*')
#CONVERT STAR
DATA=$(echo "$DATA" | sed 's/*/%99/g')
#echo $DATA"<br>"
#########################
#Assign data to variables
#########################
END_POINT=45
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

#Assign SERVER
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

#Assign LOCATION
DATANAME=LOCATION
get_data
LOCATION=$(echo "$DATAENTRY" |sed 's/%2F/\//g' | sed "s/Z%25%25%25%25%25Z/_/g")

function show_status {
echo '<script>
alert("'"$MESSAGE"'");
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
	DATANAME=SERVERMASTER
	get_data
	SERVERMASTER="$DATAENTRY"
fi

#########################
#Check data
#########################
if [ "$ACTION" != ENTER ] && [ "$ACTION" != DELETE ] && [ "$ACTION" != REALLYDELETE ] && [ "$ACTION" != SETPERMS ] && [ "$ACTION" != REALLYSETPERMS ] && [ "$ACTION" != MOVE ] && [ "$ACTION" != REALLYMOVE ] && [ "$ACTION" != REALLYCOPY ] && [ "$ACTION" != CANCELCOPY ] && [ "$ACTION" != RENAME ] && [ "$ACTION" != REALLYRENAME ] && [ "$ACTION" != EDIT ] && [ "$ACTION" != REALLYEDIT ] && [ "$ACTION" != CREATEDIR ] && [ "$ACTION" != REALLYCREATEDIR ] && [ "$ACTION" != CREATEFILE ] && [ "$ACTION" != REALLYCREATEFILE ] && [ "$ACTION" != RESTORE ] && [ "$ACTION" != REALLYRESTORE ] && [ "$ACTION" != SEARCHBACKUP ]  && [ "$ACTION" != REALLYSEARCHBACKUP ] && [ "$ACTION" != notset ] && [ "$ACTION" != DELETEACLPERMS ] && [ "$ACTION" != REALLYDELETEACLPERMS ] && [ "$ACTION" != ADDACLPERMS ] && [ "$ACTION" != REALLYADDACLPERMS ] && [ "$ACTION" != SQLRESTORE ]
then
	MESSAGE=$"You have not entered a correct action."
	show_status
fi

if [ "$ACTION" = REALLYSEARCHBACKUP ]
then
	END_POINT=32
	COUNTER=2
	#Assign SEARCH
	DATANAME=SEARCH
	get_data
	SEARCH="$DATAENTRY"
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

if [ "$ACTION" = REALLYADDACLPERMS ]
then
	END_POINT=50

	#Assign ACLOWNER
	DATANAME=ACLOWNER
	get_data
	ACLOWNER="$DATAENTRY"

	#Assign ACLPERMISSIONS
	DATANAME=ACLPERMISSIONS
	get_data
	ACLPERMISSIONS="$DATAENTRY"	
fi

if [ "$ACTION" = DELETEACLPERMS ] || [ "$ACTION" = REALLYDELETEACLPERMS ]
then
	END_POINT=50
	#Assign ACLOWNER
	DATANAME=ACLOWNER
	get_data
	ACLOWNER="$DATAENTRY"

	#Assign ACLGROUP
	DATANAME=ACLGROUP
	get_data
	ACLGROUP="$DATAENTRY"
fi

if [ "$ACTION" = SQLRESTORE ]
then
	#Assign DBNAME
	END_POINT=32
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo "$DATAHEADER"'check'` = DBNAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			DBNAME=`echo "$DATA" | cut -s -d'_' -f$COUNTER- | cut -d'&' -f1`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign DBUSERNAME
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo "$DATAHEADER"'check'` = DBUSERNAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			DBUSERNAME=`echo "$DATA" | cut -s -d'_' -f$COUNTER- | cut -d'&' -f1`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign  DBPASSWORD
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
		if [ `echo "$DATAHEADER"'check'` = DBPASSWORDcheck ]
		then
			let COUNTER=$COUNTER+1
			 DBPASSWORD=`echo "$DATA" | cut -s -d'_' -f$COUNTER- | cut -d'&' -f1`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

if [ "$ACTION" = REALLYSETPERMS ]
then
	DATA=$(echo "$DATA" | tr -cd 'A-Za-z0-9\._:%\-+*')
	END_POINT=42
	#Assign OWNER
	DATANAME=OWNER
	get_data
	OWNER="$DATAENTRY"

	#Assign GROUP
	DATANAME=GROUP
	get_data
	GROUP="$DATAENTRY"

	#Assign USERREAD
	DATANAME=USERREAD
	get_data
	USERREAD="$DATAENTRY"
	[ "$USERREAD" = 1 ] && PERMISSIONS=USERREAD

	#Assign USERWRITE
	DATANAME=USERWRITE
	get_data
	USERWRITE="$DATAENTRY"
	[ "$USERWRITE" = 1 ] && PERMISSIONS="$PERMISSIONS,USERWRITE"

	#Assign USEREXEC
	DATANAME=USEREXEC
	get_data
	USEREXEC="$DATAENTRY"
	[ "$USEREXEC" = 1 ] && PERMISSIONS="$PERMISSIONS,USEREXEC"

	#Assign GROUPREAD
	DATANAME=GROUPREAD
	get_data
	GROUPREAD="$DATAENTRY"
	[ "$GROUPREAD" = 1 ] && PERMISSIONS="$PERMISSIONS,GROUPREAD"

	#Assign GROUPWRITE
	DATANAME=GROUPWRITE
	get_data
	GROUPWRITE="$DATAENTRY"
	[ "$GROUPWRITE" = 1 ] && PERMISSIONS="$PERMISSIONS,GROUPWRITE"

	#Assign GROUPEXEC
	DATANAME=GROUPEXEC
	get_data
	GROUPEXEC="$DATAENTRY"
	[ "$GROUPEXEC" = 1 ] && PERMISSIONS="$PERMISSIONS,GROUPEXEC"

	#Assign OTHERREAD
	DATANAME=OTHERREAD
	get_data
	OTHERREAD="$DATAENTRY"
	[ "$OTHERREAD" = 1 ] && PERMISSIONS="$PERMISSIONS,OTHERREAD"

	#Assign OTHERWRITE
	DATANAME=OTHERWRITE
	get_data
	OTHERWRITE="$DATAENTRY"
	[ "$OTHERWRITE" = 1 ] && PERMISSIONS="$PERMISSIONS,OTHERWRITE"

	#Assign OTHEREXEC
	DATANAME=OTHEREXEC
	get_data
	OTHEREXEC="$DATAENTRY"
	[ "$OTHEREXEC" = 1 ] && PERMISSIONS="$PERMISSIONS,OTHEREXEC"

	#Assign SETUID
	DATANAME=SETUID
	get_data
	SETUID="$DATAENTRY"
	[ "$SETUID" = 1 ] && PERMISSIONS="$PERMISSIONS,SETUID"

	#Assign SETGID
	DATANAME=SETGID
	get_data
	SETGID="$DATAENTRY"
	[ "$SETGID" = 1 ] && PERMISSIONS="$PERMISSIONS,SETGID"

	#Assign STICKY
	DATANAME=STICKY
	get_data
	STICKY="$DATAENTRY"
	[ "$STICKY" = 1 ] && PERMISSIONS="$PERMISSIONS,STICKY"

	#Assign RECURSIVE
	DATANAME=RECURSIVE
	get_data
	RECURSIVE="$DATAENTRY"
	[ "$RECURSIVE" = 1 ] && PERMISSIONS="$PERMISSIONS,RECURSIVE"

	#Assign EXECRECURSE
	DATANAME=EXECRECURSE
	get_data
	EXECRECURSE="$DATAENTRY"
	[ "$EXECRECURSE" = 1 ] && PERMISSIONS="$PERMISSIONS,EXECRECURSE"

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
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [ $(echo "$DATAHEADER"'check') = ITEMMOVEcheck ]
	then
		let COUNTER="$COUNTER"+1
		ITEMMOVE=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER"  | sed 's/%2F/\//g' | sed "s/Z%25%25%25%25%25Z/_/g")
		break
	fi
	let COUNTER="$COUNTER"+1
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
echo '<form action="/cgi-bin/admin/file_manager.cgi" method="post">'

if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"File Manager"' '$SERVER2'</span>
		<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
		</div></div>
		<div id="'$DIV_ID'">'
else
	echo '<div id="'$DIV_ID'">'
fi


MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/file_manager.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$LOCATION:$FILENAME:$ACTION:$PERMISSIONS:$OWNER:$GROUP:$ITEMMOVE:$NEWFOLDER:$SEARCH:$TEXTDATA:$ACLOWNER:$ACLGROUP:$ACLPERMISSIONS:$DBNAME:$DBUSERNAME:$DBPASSWORD:" | sudo -H /opt/karoshi/web_controls/exec/file_manager

[ $MOBILE = no ] && echo '</div>'
echo '</div></form></div></body></html>'
exit
