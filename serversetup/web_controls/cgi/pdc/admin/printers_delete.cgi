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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Delete a Network Printer"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
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

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

#Check that a print server has been declared
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$"A print server has not yet been set up."'")';
echo 'window.location = "karoshi_servers_view.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

[ ! -f /opt/karoshi/server_network/printserver ] && show_status

echo '<form action="/cgi-bin/admin/printers_delete2.cgi" method="post"><div id="actionbox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top;"><b>'$"Delete a Network Printer"'</b></td>
<td style="vertical-align: top;">
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$HELPMSG1"'</span></a></td>
<td style="vertical-align: top;">
<button class="button" formaction="/cgi-bin/admin/printers.cgi" name="_ShowPrinters_" value="_">
'$"Show Printers"'
</button>
</td>
<td style="vertical-align: top;">
<button class="button" formaction="/cgi-bin/admin/printers_add_fm.cg" name="_AddPrinter_" value="_">
'$"Add Printer"'
</button>
</td>
<td style="vertical-align: top;">
<button class="button" formaction="/cgi-bin/admin/locations.cgi" name="_AddLocation_" value="_">
'$"Add Location"'
</button>
</td>
</tr></tbody></table><br>
'

PRINTERLIST=( `sudo -H /opt/karoshi/web_controls/exec/printers_show_queues` )
PRINTERCOUNT=${#PRINTERLIST[@]}
if [ $PRINTERCOUNT = 0 ]
then
	echo $"There are no printer queues to delete."'<br>'
	echo '/div></div></body></html>'
	exit
fi
#Show printer list to choose from
echo '  <table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 180px;">'$"Printer"'</td><td>'
COUNTER=0
echo '<select name="_PRINTERNAME_" style="width: 200px;"><option label="blank" value=""></option>'
while [ $COUNTER -lt $PRINTERCOUNT ]
do
	#Get printer name
	PRINTERNAME=${PRINTERLIST[$COUNTER]}
	PRINTERNAME=`echo $PRINTERNAME | sed 's/_/123456789/g'`
	echo '<option value="'$PRINTERNAME'">'$PRINTERNAME'</option>'
	let COUNTER=$COUNTER+1
done
echo '</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Delete_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Please choose the printer you want to delete."'</span></a>
</td></tr></tbody></table></div><div id="submitbox"><input class="button" value="Submit" type="submit"></div>
</form></div></body></html>'
exit
