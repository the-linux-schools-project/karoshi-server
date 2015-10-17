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

#Expanding menu
#		/***********************************************
#		* Slashdot Menu script- By DimX
#		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
#		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
#		***********************************************/


##########################
#Section Control
##########################
source /opt/karoshi/server_network/web_controls/menusettings

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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Web Management"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
	<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css" />
	<script type="text/javascript" src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
		***********************************************/
	</script>
	<script type="text/javascript">
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
<body>
    <div style="float: center" id="my_menu" class="sdmenu">
      <div class="collapsed">
        <span>'$"Users and Groups"'</span>
        <a href="/cgi-bin/staff/change_student_password_fm.cgi">'$"Change Password"'</a>
        <a href="/cgi-bin/staff/helpdesk_add_fm.cgi">'$"View Requests"'</a>
      </div>'

if [ $PRINTERCTRL = yes ]
then
echo '      <div class="collapsed">
        <span>'$"Printer"'</span>
        <a href="/cgi-bin/staff/printers.cgi">'$"Manage Print Queues"'</a>
      </div>'
fi

if [ $INTERNETCTRL = yes ]
then
echo  '     <div class="collapsed">
        <span>Internet</span>
        <a href="/cgi-bin/staff/dg_view_student_user_logs_fm.cgi">'$"User logs"'</a>
        <a href="/cgi-bin/admin/dg_room_controls_fm.cgi">'$"Room controls"'</a>
      </div>'
fi
echo '</div></div></body></html>'
exit
