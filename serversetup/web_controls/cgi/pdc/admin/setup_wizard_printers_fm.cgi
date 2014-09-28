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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Setup Wizard"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
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
echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Setup Wizard"'</b></a></td></tr></tbody></table>'
else
echo '<b>'$"Setup Printers"'</b><br><br>'$"If you have not already done so you may want to add a printer server to your network so that you can control printing for your clients."'<br><br>'$"The show servers link below will show all available servers. Choose the server that you want to add the printer module to by clicking on the add role button."'<br><br><br><br>

<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr VALIGN=TOP><td style="width: 30px;">
<a href="karoshi_servers_view.cgi"><img src="/images/submenus/system/computer.png" width="16" height="16" border="0" /></a>
<br><br>
</td><td>
<a href="karoshi_servers_view.cgi">'$"Show Servers"'</a>
</td></tr>
<tr VALIGN=TOP><td>
<a href="printers_add_fm.cgi"><img src="/images/submenus/printer/add_printer.png" border="0" /></a>
<br><br>
</td><td>
<a href="printers_add_fm.cgi">'$"Add Printer"'</a>
</td></tr>
<tr VALIGN=TOP><td>
<a href="printers.cgi"><img src="/images/submenus/printer/view_print_queues.png" border="0" /></a>
<br><br>
</td><td>
<a href="printers.cgi">'$"Control Printers"'</a>
</td></tr>

</tbody></table>
'
fi


echo '
'$OPENINGMSG'
</div></div></body></html>
'
exit
