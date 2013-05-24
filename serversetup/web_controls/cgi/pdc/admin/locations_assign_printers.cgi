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

#Language
TITLE="Assign Printers to Locations"
HTTPS_ERROR="You must access this page via https."
ACCESS_ERROR1="You must be a Karoshi Management User to complete this action."

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/karoshi/style.css"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'
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

echo '<form action="/cgi-bin/admin/locations2.cgi" method="post"><div id="actionbox"><b>Locations</b><br><br>'
echo '<table class="standard" style="text-align: left; width: 334px; height: 91px;" border="0" cellpadding="2" cellspacing="2">'
echo '<tbody>'
echo '<tr><td>New location</td><td><input name="_NEWLOCATION_" size="30" type="text"></td></tr>'
echo '</tbody></table>'
echo '<table class="standard" style="text-align: left; width: 334px;" border="0" cellpadding="2" cellspacing="2">'
echo '<tbody>'
echo '<tr><td><b>Current Locations</b></td><td><b>Delete</b></td></tr>'
echo '</tbody></table><br>'

#Show list of printers


if [ -f /var/lib/samba/netlogon/locations.txt ]
then
LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
else
LOCATION_COUNT=0
fi
echo '<table class="standard" style="text-align: left; width: 334px;" border="0" cellpadding="2" cellspacing="2">'
echo '<tbody>'
COUNTER=1
while [ $COUNTER -le $LOCATION_COUNT ]
do
LOCATION=`sed -n $COUNTER,$COUNTER'p' /var/lib/samba/netlogon/locations.txt`
echo '<tr><td>'$LOCATION'</td><td><input type="radio" name="_DELETE_" value="'$LOCATION'"><br></td></tr>'
let COUNTER=$COUNTER+1
done
echo '</tbody></table>'
echo "</div>"
echo '<div id="submitbox"><input value="Submit" type="submit"></div>'
echo '<div id="resetbox"><input value="Reset" type="reset"></div>'
echo '</form></body></html>'
exit
