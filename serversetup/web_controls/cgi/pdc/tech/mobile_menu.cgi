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
#		* Submitted to Dynamic Drive DHTML code library: www.dynamicdrive.com
#		* Visit Dynamic Drive at www.dynamicdrive.com for full source code
#		***********************************************/

##########################
#Section Control
##########################
source /opt/karoshi/server_network/web_controls/menusettings
source /opt/karoshi/web_controls/version
source /opt/karoshi/web_controls/version
source /opt/karoshi/web_controls/version
source /opt/karoshi/server_network/domain_information/domain_name
source /opt/karoshi/web_controls/version

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Web Management"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/tech/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
	<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css" />
	<script src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: www.dynamicdrive.com
		* Visit Dynamic Drive at www.dynamicdrive.com for full source code
		***********************************************/
	</script>
	<script>
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
<body><div id="pagecontainer">
    <div style="float: center" id="my_menu" class="sdmenu">
	<div class="collapsed">
	<span>'$SHORTNAME'</span>
		<a href="/cgi-bin/menu.cgi">'$"Main Menu"'</a>
		<a href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Main_Page" target="_blank">'$"Documentation"'</a>
		<a href="http://www.linuxschools.com/forum/" target="_blank">'$"Forum"'</a>
		<a href="irc_help.cgi" target="_blank">'$"IRC"'</a>
 	</div>
       <div class="collapsed">
        <span>'$"Helpdesk"'</span>
        <a href="/cgi-bin/tech/helpdesk_view_fm.cgi">'$"View Requests"'</a>
        <a href="/cgi-bin/tech/helpdesk_add_fm.cgi">'$"Add Request"'</a>
        </div> 
      <div class="collapsed">
        <span>'$"Users and Groups"'</span>
        <a href="/cgi-bin/tech/add_user_fm.cgi">'$"Add User"'</a>
        <a href="/cgi-bin/tech/change_password_fm.cgi">'$"Change Password"'</a>
	<a href="/cgi-bin/tech/lockout_reset_fm.cgi">'$"Reset User Lockout"'</a>
      </div>
      <div class="collapsed">
        <span>'$"Client"'</span>
	<a href="/cgi-bin/tech/client_boot_controls_fm.cgi">'$"Client Boot Controls"'</a>
      </div>
      <div class="collapsed">
        <span>'$"Infrastructure"'</span>
	<a href="/cgi-bin/tech/asset_register_view.cgi">'$"Asset Register"'</a>'
[ $MONITORINGCTRL = yes ] && echo '	<a href="/cgi-bin/tech/mon_status.cgi">'$"Network Status"'</a>'
echo 	'</div>'

if [ $PRINTERCTRL = yes ]
then
echo '       <div class="collapsed">
        <span>'$"Printer"'</span>
        <a href="/cgi-bin/tech/printers.cgi">'$"Manage Print Queues"'</a>
        <a href="/cgi-bin/tech/printer_accounting_view_user_usage_fm.cgi">'$"User Printer Usage"'</a>
        <a href="/cgi-bin/tech/printer_accounting_view_group_usage_fm.cgi">'$"Group Printer Usage"'</a>
        <a href="/cgi-bin/tech/printer_accounting_add_user_limit_fm.cgi">'$"Add User Limit"'</a>
        <a href="/cgi-bin/tech/printer_accounting_user_limits_fm.cgi">'$"User Printer Limits"'</a>
        <a href="/cgi-bin/tech/printer_accounting_group_limits_fm.cgi">'$"Group Printer Limits"'</a>
      </div>'
fi


if [ $INTERNETCTRL = yes ]
then
echo '  <div class="collapsed">
        <span>Internet</span>
        <a href="/cgi-bin/admin/dg_view_user_logs_fm.cgi">'$"User logs"'</a>
        <a href="/cgi-bin/admin/dg_view_site_logs_fm.cgi">'$"Site Logs"'</a>
        <a href="/cgi-bin/admin/dg_view_computer_logs_fm.cgi">'$"Computer Logs"'</a>
        <a href="/cgi-bin/admin/e2g_filtergroups.cgi">'$"Filter Management"'</a>
        <a href="/cgi-bin/admin/user_internet_access.cgi">'$"Ban User"'</a>
        <a href="/cgi-bin/admin/dg_room_controls_fm.cgi">'$"Room controls"'</a>
        <a href="/cgi-bin/admin/dg_bypass.cgi">'$"Client Bypass Controls"'</a>
      </div>'
fi

echo '
<div class="a.current">
<small><small>
'$"Version"' : '$VERSION'
</small></small>
</div></div></div></body></html>
'
exit
