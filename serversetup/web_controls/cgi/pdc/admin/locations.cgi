#!/bin/bash
#Copyright (C) 2007 Paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/locations ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/locations
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
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
echo '                window.location = "/cgi-bin/admin/view_karoshi_web_admin_log.cgi";'
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

echo '<div id="actionbox"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top;"><b>'$TITLE'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$HELPMSG1"'</span></a></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers.cgi" name="printers" method="post"><a class="info" href="javascript:void(0)"><input name="SHOWPRINTERS" type="image" class="images" src="/images/submenus/printer/show_printers.png" value=""><span>'$SHOWPRINTERSMSG'</span></a></form></td>
</tr></tbody></table><br>
'

echo '<form action="/cgi-bin/admin/locations2.cgi" method="post"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">'
echo '<tbody>'
echo '<tr><td style="width: 180px;">'$NEWLOCATION'</td><td><input name="_NEWLOCATION_" size="15" type="text"> </td><td><input value="Submit" type="submit"></td></tr>'
echo '</tbody></table><br>'

if [ -f /var/lib/samba/netlogon/locations.txt ]
then
LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
else
LOCATION_COUNT=0
fi
#Show current rooms
if [ $LOCATION_COUNT -gt 0 ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">'
echo '<tbody>'
echo '<tr><td style="width: 180px;"><b>Current Locations</b></td><td><b>Delete</b></td></tr>'
echo '</tbody></table><br>'

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">'
echo '<tbody>'
COUNTER=1
while [ $COUNTER -lt $LOCATION_COUNT ]
do
LOCATION=`sed -n $COUNTER,$COUNTER'p' /var/lib/samba/netlogon/locations.txt`
echo '<tr><td style="width: 180px;">'$LOCATION'</td><td><a class="info" href="javascript:void(0)"><input name="_DELETE_'$LOCATION'_" type="image" class="images" src="/images/submenus/client/delete_location.png" value=""><span>Delete '$LOCATION'</span></a></td></tr>'
let COUNTER=$COUNTER+1
done
echo '</tbody></table><br>'
fi
echo '</form></div></body></html>'
exit
