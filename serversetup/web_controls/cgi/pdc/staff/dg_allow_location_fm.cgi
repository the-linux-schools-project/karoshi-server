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
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<html><head><title>'$"Allow Room"'</title><META HTTP-EQUIV="refresh" CONTENT="300; URL=/cgi-bin/blank.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_staff
echo '<form action="/cgi-bin/staff/dg_allow_location.cgi" method="post"><div id="actionbox"><b>'$"Allow Room"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will allow internet access for all student devices that are currently banned."'</span></a><br><br>'

#Show currently banned locations
echo '<table class="standard"><tbody>
<tr><td style="width: 180px;">'$"Location"'</td><td>'
echo '<select name="_LOCATION_">'
if [[ $(ls -1 /opt/karoshi/internet_controls/banned_locations | wc -l) != 0 ]]
then
	ls -1 /opt/karoshi/internet_controls/banned_locations | sed 's/^/<option>/g' | sed 's/$/<\/option>/g'
fi
echo '<option value="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;</option></select></td></tr></tbody></table></div>'
echo '<div id="submitbox"><input value="Submit" type="submit"> <input value="Reset" type="reset"></div>'
echo '</form></div></body></html>'
exit
