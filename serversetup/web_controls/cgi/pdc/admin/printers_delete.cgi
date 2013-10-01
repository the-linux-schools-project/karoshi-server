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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_delete ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_delete
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'
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
echo "</body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

#Check that a print server has been declared
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$PRINTSERVERERRORMSG'")';
echo 'window.location = "karoshi_servers_view.cgi";'
echo '</script>'
echo "</body></html>"
exit
}

[ ! -f /opt/karoshi/server_network/printserver ] && show_status

echo '<div id="actionbox"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top;"><b>'$TITLE'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$HELPMSG1"'</span></a></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers.cgi" name="printers" method="post">
<input name="SHOWPRINTERS" type="submit" class="button" value="'$SHOWPRINTERSMSG'">
</form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers_add_fm.cgi" name="printers" method="post">
<input name="ADDPRINTER" type="submit" class="button" value="'$ADDPRINTERMSG'">
</form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/locations.cgi" name="printers" method="post">
<input name="ADDLOCATION" type="submit" class="button" value="'$ADDLOCATIONMSG'">
</form></td>
</tr></tbody></table><br>
'

echo '<form action="/cgi-bin/admin/printers_delete2.cgi" method="post">'
PRINTERLIST=( `sudo -H /opt/karoshi/web_controls/exec/printers_show_queues` )
PRINTERCOUNT=${#PRINTERLIST[@]}
if [ $PRINTERCOUNT = 0 ]
then
echo $NOPRINTERSMSG'<br>'
echo "</div>"
echo '</body></html>'
exit
fi
#Show printer list to choose from
echo '  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">'$PRINTERMSG'</td><td>'
COUNTER=0
echo '<select name="_PRINTERNAME_" style="width: 200px;"><option value=""></option>'
while [ $COUNTER -lt $PRINTERCOUNT ]
do
#Get printer name
PRINTERNAME=${PRINTERLIST[$COUNTER]}
PRINTERNAME=`echo $PRINTERNAME | sed 's/_/123456789/g'`
echo '<option value="'$PRINTERNAME'">'$PRINTERNAME'</option>'
let COUNTER=$COUNTER+1
done
echo '</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Delete_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$CHOOSEPRINTERMSG"'</span></a>
</td></tr></tbody</table></div><div id="submitbox"><input value="Submit" type="submit">'
echo '</form></div></body></html>'
exit
