#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
	TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Enabled Printers"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body onLoad="start()"><div id="pagecontainer">'

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=menubox
fi
echo '<form name="myform" action="/cgi-bin/admin/printer_accounting_status.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<table class="standard" style="text-align: left;" >
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Enabled Printers"'</b></a></td></tr></tbody></table>'
else
	echo '<b>'$"Enabled Printers"'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Printer_Accounting#Enabled_Printers"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will allow you to track printing usage for all of your users."'</span></a><br><br>'
fi

echo '<table class="standard" style="text-align: left;" ><tbody>
<tr><td><b>'$"Printer Name"'</b></td><td><b>'$"Accounting Status"'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Printer_Accounting#Enabled_Printers"><img class="images" alt="" src="/images/help/info.png"><span>'$"You can choose to enable or disable accounting for each printer."'</span></a></td></tr>'
#Get list of of printers
PRINTERLIST=( `sudo -H /opt/karoshi/web_controls/exec/printers_list` )
PRINTERCOUNT=${#PRINTERLIST[@]}
COUNTER=0
while [ $COUNTER -lt $PRINTERCOUNT ]
do
	PRINTERNAME=${PRINTERLIST[$COUNTER]}
	STATUSMSG=''$PRINTERNAME' - '$"Enable accounting for this printer queue."''
	ACTION=enable
	PRINTER_ICON=/images/submenus/printer/accounting_disabled.png
	if [ -f /opt/karoshi/server_network/printer_accounting/accounting_status/$PRINTERNAME ]
	then
		PRINTER_ICON=/images/submenus/printer/accounting_enabled.png
		STATUSMSG=''$PRINTERNAME' - '$"Disable accounting for this printer queue."''
		ACTION=disable
	fi
	echo '<tr> <td style="width: 180px;">'$PRINTERNAME'</td><td>
	<button class="info" name="_DoAction_" value="_ACTION_'$ACTION'_PRINTER_'$PRINTERNAME'_">
	<img src="'$PRINTER_ICON'" alt="'$STATUSMSG'">
	<span>'$STATUSMSG'</span>
	</button>
	</td></tr>'
	let COUNTER=$COUNTER+1
done
       
echo '</tbody></table><br></div></form></div></body></html>'
exit

