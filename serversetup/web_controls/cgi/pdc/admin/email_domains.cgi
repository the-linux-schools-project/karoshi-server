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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"E-Mail Domains"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script type="text/javascript" id="js">
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
TCPIP_ADDR=$REMOTE_ADDR

DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`

#echo $DATA"<br>"
#########################
#Assign data to variables
#########################
END_POINT=15
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

function show_status {
echo '<script language="Javascript">
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/email_domains.cgi";
</script></div></body></html>'
exit
}

if [ -z "$ACTION" ]
then
	ACTION=view
fi

#########################
#Check data
#########################
if [ $ACTION != add ] && [ $ACTION != reallyadd ] && [ $ACTION != reallydelete ] && [ $ACTION != delete ] && [ $ACTION != view ]
then
	MESSAGE=$"You have not entered a correct action."
	show_status
fi

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ]
then
	#Make sure that the domain is not blank
	if [ -z "$DOMAIN" ]
	then
		MESSAGE=$"The domain must not be blank."
		show_status
	fi
fi

if [ "$ACTION" = reallyadd ]
then
	source /opt/karoshi/server_network/domain_information/domain_name
	#Make sure that the domain is not the real domain
	if [ "$DOMAIN" = "$REALM" ]
	then
		MESSAGE=$"You cannot add the main domain as a virtual domain."
		show_status
	fi
	
	#Check that a domain has been entered
	if [ $(echo "$DOMAIN" | grep -c "\.") = 0 ]
	then
		MESSAGE=$"You have not entered in a valid domain."
		show_status
	fi
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=mobileactionbox
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<form action="/cgi-bin/admin/file_manager.cgi" method="post"><div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"E-Mail Domains"'</span><a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a></div></div><div id="'$DIV_ID'">
	'
else
	echo '<div id="'$DIV_ID'"><div id="titlebox">
	<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
	<tr>
	<td style="vertical-align: top;"><div class="sectiontitle">'$"E-Mail Domains"'</div></td>
	<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=File_Manager"><img class="images" alt="" src="/images/help/info.png"><span>'$"E-Mail Domains"'</span></a></td>'

	if [ "$ACTION" != add ]
	then
		echo '<td><form action="/cgi-bin/admin/email_domains.cgi" method="post"><input name="_ACTION_add_" type="submit" class="button" value="'$"Add Domain"'"></form></td>'
	fi
	echo '</tr></tbody></table></div><div id="infobox">'
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/email_domains.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$ACTION:$DOMAIN:" | sudo -H /opt/karoshi/web_controls/exec/email_domains

[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
