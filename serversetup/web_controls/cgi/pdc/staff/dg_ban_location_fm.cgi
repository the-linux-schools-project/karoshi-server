#!/bin/bash
#Copyright (C) 2008 Paul Sharrad
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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
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
echo '<html><head><title>'$"Ban Room"'</title><META HTTP-EQUIV="refresh" CONTENT="300; URL=/cgi-bin/blank.cgi">'
echo "<link rel="stylesheet" href="/css/$STYLESHEET"><script src=\"/all/stuHover.js\" type=\"text/javascript\"></script>"
echo "</head><body><div id='pagecontainer'>"
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/staff/dg_ban_location_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_staff
echo '<form action="/cgi-bin/staff/dg_ban_location.cgi" method="post"><div id="actionbox"><b>'$"Ban Room"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will ban internet access for all student devices listed."'</span></a><br><br>'
###############################
#Location
###############################
if [ -f /var/lib/samba/netlogon/locations.txt ]
then
LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
else
LOCATION_COUNT=0
fi
#Show current rooms
echo '<table class="standard"><tbody>
<tr><td style="width: 180px;">'$"Location"'</td><td>'
if [ $LOCATION_COUNT -gt 0 ]
then
echo '<select name="_LOCATION_">'
cat /var/lib/samba/netlogon/locations.txt | sed 's/^/<option>/g' | sed 's/$/<\/option>/g'
echo '<option value="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;</option></select></td></tr></tbody></table>'
fi
echo "</div>"
echo '<div id="submitbox"><input value="Submit" type="submit"> <input value="Reset" type="reset"></div>'
echo '</form></div></body></html>'
exit
