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

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"E-Mail Authentication"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	0: { sorter: "ipAddress" }
    		}
		});
    } 
);
</script>
'

HELPCLASS="info"

if [ $MOBILE = yes ]
then
	HELPCLASS="info infoleft"
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
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%+' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=16

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

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = delete ] || [ "$ACTION" = reallydelete ] || [ "$ACTION" = reallyadd ]
then
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

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = delete ]
then
	#Assign COMMENT
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = COMMENTcheck ]
		then
			let COUNTER=$COUNTER+1
			COMMENT=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi


function show_status {
echo '<script>'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/email_authentication.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
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

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ]
then
	#Check to see that TCPIP is not blank
	if [ -z "$TCPIP" ]
	then
		MESSAGE=$"You have not entered a TCPIP address."
		show_status
	fi
fi

if [ "$ACTION" = reallyadd ]
then
	#Check to see that COMMENT is not blank
	if [ -z "$COMMENT" ]
	then
		MESSAGE=$"You have not entered a comment for the TCPIP address."
		show_status
	fi

	#Check that we have some sort of useful ip address.
	if [ `ipcalc -n "$TCPIP" | grep -c INVALID` -gt 0 ]
	then
		MESSAGE=$"The TCPIP address is incorrect."
		show_status	
	fi
fi


#Generate navigation bar
if [ "$MOBILE" = no ]
then
	TABLECLASS=standard
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
	echo '<div id="'$DIV_ID'"><div id=titlebox>'
else
	TABLECLASS=mobilestandard
fi


if [ "$ACTION" = add ] || [ "$ACTION" = delete ]
then
	ACTION2=view
	BUTTONTXT=$"View TCPIP Addresses"
	TITLETXT=$"Add TCPIP Address"
	[ "$ACTION" = delete ] && TITLETXT=$"Delete TCPIP Address"
fi

if [ "$ACTION" = view ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ]
then
	ACTION2=add
	BUTTONTXT=$"Add TCPIP Address"
	TITLETXT=$"Bypass E-Mail Authentication"
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
echo '<form action="/cgi-bin/admin/email_authentication.cgi" method="post"><table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: middle;"><b>'$TITLETXT'</b></td>
<td style="vertical-align: top;">
<input name="____ACTION____'$ACTION2'____" type="submit" class="button" value="'$BUTTONTXT'">
</td>'
#echo '<td><a href="gluster_control.cgi"><input class="button" type="button" name="" value="'$"Gluster Volume Control"'"></a></td><td><a href="home_folders_fm.cgi"><input class="button" type="button" name="" value="'$"Home Folders"'"></a></td>'
echo '<td><a class="'$HELPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=E-Mail_Authentication"><img class="images" alt="" src="/images/help/info.png"><span>'$"By default all E-Mail clients have to authenticate to be able to send E-Mails."'<br><br>'$"Here you can allow TCPIP addresses that you want to be able to send E-Mail without having to authenticate."'</span></a>
</td></tr></tbody></table></form>
'
[ "$MOBILE" = no ] && echo '</div><div id="infobox">' 

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/email_authentication.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$TCPIP:$COMMENT:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/email_authentication
EXIT_STATUS=$?

if [ $EXIT_STATUS = 102 ]
then
	MESSAGE=$"A folder with this name already exists."
	show_status	
fi

if [ $EXIT_STATUS = 103 ]
then
	MESSAGE=$"This share already exits in samba."
	show_status	
fi

[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
