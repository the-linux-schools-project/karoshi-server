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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Custom Spam Rules"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
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
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%'`
#########################
#Assign data to variables
#########################
END_POINT=15
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

#Check that action is not blank
if [ -z "$ACTION" ]
then
	ACTION=view
fi

if [ "$ACTION" = view ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ]
then
	ACTION2=add
	ACTIONTEXT=$"Add Rule"
else
	ACTION2=view
	ACTIONTEXT=$"View Rules"	
fi

#Assign RULEDATA
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = RULEDATA2check ]
	then
		let COUNTER=$COUNTER+1
		RULEDATA2=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign RULEDATA2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = RULEDATAcheck ]
	then
		let COUNTER=$COUNTER+1
		RULEDATA=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3F/?/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign RULESCORE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = RULESCOREcheck ]
	then
		let COUNTER=$COUNTER+1
		RULESCORE=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
echo '<script>'
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

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Custom E-Mail Spam Rules"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
<form action="/cgi-bin/admin/email_custom_spam_rules.cgi" method="post">
<button class="button" name="_Add_" value="_ACTION_'$ACTION2'_">
'$ACTIONTEXT'
</button>
</form>'
if [ -f /opt/karoshi/server_network/email/activate_spam_rule_changes ] && [ "$ACTION" != activatechanges ]
then
	echo '
	<form action="/cgi-bin/admin/email_custom_spam_rules.cgi" method="post">
	<button class="button" name="_Add_" value="_ACTION_activatechanges_">
	'$"Activate Changes"'
	</button>
	</form>
	' 
fi
else
	echo '<div id="'$DIV_ID'"><div id="titlebox"><table class="standard" style="text-align: left;" ><tbody>
<tr style="height: 30px;">
<td><div class="sectiontitle">'$"Custom Spam Rules"'</div></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=E-Mail_Custom_Spam_Rules"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows you to set custom spam rules for your E-Mail system."'</span></a></td>
<td>
<form action="/cgi-bin/admin/email_custom_spam_rules.cgi" method="post">
<button class="button" name="_Add_" value="_ACTION_'$ACTION2'_">
'$ACTIONTEXT'
</button>
</form>
</td>'
	if [ -f /opt/karoshi/server_network/email/activate_spam_rule_changes ] && [ "$ACTION" != activatechanges ]
	then
		echo '
		<td>
		<form action="/cgi-bin/admin/email_custom_spam_rules.cgi" method="post">
		<button class="button" name="_Add_" value="_ACTION_activatechanges_">
		'$"Activate Changes"'
		</button>
		</form>
		</td>
		' 
	fi
	echo '</tr></table><br></div><div id="infobox">'
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/email_custom_spam_rules.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$RULEDATA:$RULEDATA2:$RULESCORE:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/email_custom_spam_rules
[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit

