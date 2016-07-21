#!/bin/bash
#Copyright (C) 2011  Paul Sharrad
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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Set Default Page"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
<body><div id="pagecontainer">'

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=navbar
	/opt/karoshi/web_controls/generate_navbar_admin_mobile
fi
echo '<form action="/cgi-bin/admin/set_default_page.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<table class="standard" style="text-align: left;" >
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_user_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><b>'$"Set Default Page"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the default page that you want to have for this section of the web management."'</span></a></td></tr></tbody></table>'
else
	echo '<b>'$"Set Default Page"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the default page that you want to have for this section of the web management."'</span></a><br><br>'
fi

echo '

  <table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"Default Page"'</td>
        <td>

<select name="_DEFAULTPAGE_" style="width: 200px;">
	<option label="blank"></option>
        <option value="add_user_fm.cgi">'$"Add Users"'</option>
        <option value="change_password_fm.cgi">'$"Change User Passwords"'</option>
        <option value="show_user_info_fm.cgi">'$"Show User Information"'</option>
        <option value="lockout_reset_fm.cgi">'$"Reset User Lockout"'</option>
        <option value="incident_log_view_fm.cgi">'$"View Incident Logs"'</option>
        <option value="helpdesk_view_fm.cgi">'$"Help Desk Requests"'</option>
'




[ -f /opt/karoshi/server_network/printserver ] && echo '<option value="printers.cgi">'$"Printer Queues"'</option>'
[ -f /opt/karoshi/server_network/monitoring_server ] &&	echo '<option value="mon_status.cgi">'$"System Monitoring"'</option>'
[ -f /opt/karoshi/server_network/proxyserver ] && echo '<option value="dg_view_top_sites_fm.cgi">'$"Top User Internet Sites"'</option>'

echo '</select>
</td></tr></tbody></table>
'
if [ $MOBILE = no ]
then
	echo '</div><div id="submitbox">'
fi
echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></form></div></body></html>
'
exit
