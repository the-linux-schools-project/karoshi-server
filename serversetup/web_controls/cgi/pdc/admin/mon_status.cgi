#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

#Get defcon level
DEFCON=5
[ -f /opt/karoshi/server_network/mon/network_status ] && source /opt/karoshi/server_network/mon/network_status

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"System Status"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><META HTTP-EQUIV="refresh" CONTENT="120"><script src="/all/stuHover.js" type="text/javascript"></script>
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

HEIGHT=15
PADHEIGHT=6
if [ $MOBILE = yes ]
then
	HEIGHT=20
	PADHEIGHT=9
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

echo '
<style type="text/css">
 #hide1{height:'$HEIGHT'px !important; width:100px !important; padding-top:'$PADHEIGHT'px !important; color: #000 !important }
 #show1{height:'$HEIGHT'px !important; width:100px !important; padding-top:'$PADHEIGHT'px !important; color: #000 !important }
 #show1:hover{color: #fff !important }
 #hide1:hover{color: #fff !important } 

 .row { vertical-align: top; height:auto !important; }
 .list {display:none; }
 .show {display: none; }
 .hide:target + .show {display: inline-block; }
 .hide:target {display: none; }
 .hide:target ~ .list {display:inline; }
 @media print { .hide, .show { display: none; } }
 </style></head><body onLoad="start()"><div id="pagecontainer">'


#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/use_ssh_fm.cgi";'
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
	<span>'$"System Status"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
else
#Show title
echo '<table class="standard" style="text-align: left;" >
<tbody><tr><td style="vertical-align: top; width: 200px;"><div class="sectiontitle">'$"System Status"' Defcon '$DEFCON'</div></td><td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#System_Status"><img class="images" alt="" src="/images/help/info.png"><span>'$"Network Monitoring can be used to monitor any device connected to your network."'</span></a></td><td style="vertical-align: top;">
<form action="/cgi-bin/admin/monitors_add_fm.cgi" method="post">
	<button class="button" name="_AddMonitor_" value="_">
	'$"Add Monitor"'
	</button>
</form>
</td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/monitors_view.cgi" method="post">
	<button class="button" name="_ViewMonitors_" value="_">
	'$"View Monitors"'
	</button>
</form>
</td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/monitors_view_email_alerts_fm.cgi" method="post">
	<button class="button" name="_ViewEmailAlerts_" value="_">
	'$"E-Mail Alerts"'
	</button>
</form>
</td>
</tr></tbody></table></div><div id="infobox">'
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/mon_status.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/mon_status $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:
if [ $? = 102 ]
then
	echo '<br><br>'$"A monitoring server has not been setup."'<br>'
fi
[ $MOBILE = no ] && echo '</div>'
echo "</div></div></body></html>"
exit
