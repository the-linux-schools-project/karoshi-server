#!/bin/bash
#Copyright (C) 2012  Paul Sharrad

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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"E-Mail Access"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/script.js"></script>
<script type="text/javascript" src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script type="text/javascript" id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
	echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script type="text/javascript" src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
		***********************************************/
	</script>
	<script type="text/javascript">
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
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#echo $DATA"<br>"
#########################
#Assign data to variables
#########################
END_POINT=15
#Assign USERSELECT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = USERSELECTcheck ]
	then
		let COUNTER=$COUNTER+1
		USERSELECT=`echo $DATA | cut -s -d'_' -f$COUNTER`
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

#Assign ACCESSLEVEL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ACCESSLEVELcheck ]
	then
		let COUNTER=$COUNTER+1
		ACCESSLEVEL=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign GROUP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = GROUPcheck ]
	then
		let COUNTER=$COUNTER+1
		GROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

function show_status {
echo '<script type="text/javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/email_access.cgi";'
echo '</script>'
echo "</div></div></body></html>"
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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#Check that action is not blank
if [ -z "$ACTION" ]
then
	ACTION=getchoice
fi

if [ $ACTION = view ]
then
	if [ -z $USERSELECT ]
	then
		ACTION=getchoice
	fi
	#Check to see if the user or the group exists
	getent group "$USERSELECT" 1>/dev/null
	if [ $? != 0 ]
	then
		getent passwd "$USERSELECT" 1>/dev/null
		if [ $? != 0 ]
		then
			MESSAGE=$"The username or group you have chosen does not exist."
			show_status
		fi
	fi
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"E-Mail Access"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
	if [ "$ACTION" != viewrestrictionlist ]
	then
		echo '<form action="/cgi-bin/admin/email_access.cgi" method="post"><input name="_ACTION_viewrestrictionlist_" type="submit" class="button" value="'$"View Restriction List"'"></form>'
	fi
	if [ "$ACTION" != getchoice ]
	then
		echo '<a href="email_access.cgi"><input class="button" type="button" name="" value="'$"Choose User / group"'"></a>'
	fi
	echo '<br><br>'
else
	echo '<div id="'$DIV_ID'"><div id="titlebox"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr style="height: 30px;">
<td style="vertical-align: top;"><div class="sectiontitle">'$"E-Mail Access"'</div></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=E-Mail_Access_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows you to set the level of access for sending and receiving E-Mails for your users."'<br><br>'$"Full access - allow the user to send and receive E-mails to all domains."'<br><br>'$"Restricted - limit the user to sending and receiving E-Mails from domains on the restricted list. This list defaults to your domain."'<br><br>'$"No Access - the user will not be able to send or receive any E-Mails."'</span></a></td>'
	if [ "$ACTION" != viewrestrictionlist ]
	then
		echo '<td style="vertical-align: top;"><form action="/cgi-bin/admin/email_access.cgi" method="post"><input name="_ACTION_viewrestrictionlist_" type="submit" class="button" value="'$"View Restriction List"'"></form></td>'
	fi
	if [ "$ACTION" != getchoice ]
	then
		echo '<td style="vertical-align: top;"><a href="email_access.cgi"><input class="button" type="button" name="" value="'$"Choose User / group"'"></a></td>'
	fi
	echo '</tr></table><br></div><div id="infobox">'
fi



MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/email_access.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$USERSELECT:$ACCESSLEVEL:$GROUP:$MOBILE:email_access:" | sudo -H /opt/karoshi/web_controls/exec/email_access
[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit

