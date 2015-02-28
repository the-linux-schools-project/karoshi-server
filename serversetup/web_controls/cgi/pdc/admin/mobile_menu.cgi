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

#Expanding menu
#		/***********************************************
#		* Slashdot Menu script- By DimX
#		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
#		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
#		***********************************************/
##########################
#Section Control
##########################
source /opt/karoshi/server_network/menusettings
source /opt/karoshi/web_controls/version
source /opt/karoshi/server_network/domain_information/domain_name

############################
#Language
############################

STYLESHEET=defaultstyle.css

[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server


############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Web Management"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
	<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
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
        <a href="/cgi-bin/admin/helpdesk_view_fm.cgi">'$"View Requests"'</a>
        <a href="/cgi-bin/admin/helpdesk_add_fm.cgi">'$"Add Request"'</a>
        </div>     
	<div class="collapsed">
        <span>'$"Users and Groups"'</span>'
if [ $ADDUSERCTRL = yes ]
then
echo '        <a href="/cgi-bin/admin/add_user_fm.cgi">'$"Add User"'</a>
        <a href="/cgi-bin/admin/delete_user_fm.cgi">'$"Delete User"'</a>
	<a href="/cgi-bin/admin/change_username_fm.cgi">'$"Change Username"'</a>
'
fi
echo '	<a href="/cgi-bin/admin/change_password_fm.cgi">'$"Change Password"'</a>
	<a href="/cgi-bin/admin/group_membership_fm.cgi">'$"Group Membership"'</a>
      </div>
      <div class="collapsed">
        <span>'$"System"'</span>
        <a href="/cgi-bin/admin/file_manager.cgi">'$"File Manager"'</a>
        <a href="/cgi-bin/admin/server_info_fm.cgi">'$"Server Information"'</a>
        <a href="/cgi-bin/admin/update_servers_fm.cgi">'$"Update Servers"'</a>
        <a href="/cgi-bin/admin/update_servers_view_logs_fm.cgi">'$"Update logs"'</a>
        <a href="/cgi-bin/admin/update_karoshi_fm.cgi">'$"Update Web Management"'</a>
        <a href="/cgi-bin/admin/uptime_fm.cgi">'$"Uptime"'</a>
        <a href="/cgi-bin/admin/view_karoshi_web_management_logs.cgi">'$"Management Logs"'</a>
        <a href="/cgi-bin/admin/cron_view_fm.cgi">'$"Cron"'</a>
        <a href="/cgi-bin/admin/remote_management_change_language.cgi">'$"Change Language"'</a>
        <a href="/cgi-bin/admin/remote_management_change_theme.cgi">'$"Change Theme"'</a>
        <a href="/cgi-bin/admin/custom_command_fm.cgi">'$"Custom Command"'</a>
        <a href="/cgi-bin/admin/services_view_fm.cgi">'$"Control Services"'</a>
        <a href="/cgi-bin/admin/change_management_passwords_fm.cgi">'$"Management Passwords"'</a>
        <a href="/cgi-bin/admin/shutdown_fm.cgi">'$"Shutdown"'</a>
      </div>
	<div class="collapsed">
        <span>'$"Storage"'</span>
        <a href="/cgi-bin/admin/disk_information_fm.cgi">'$"Disk Information"'</a>
        <a href="/cgi-bin/admin/disk_usage_fm.cgi">'$"Disk Usage"'</a>
        <a href="/cgi-bin/admin/view_disk_usage_logs_fm.cgi">'$"Disk Usage Logs"'</a>
	<a href="/cgi-bin/admin/user_web_folders.cgi">'$"User Web Folders"'</a>
      </div>
      <div class="collapsed">
        <span>'$"Client"'</span>
	<a href="/cgi-bin/admin/client_boot_controls_fm.cgi">'$"Client Boot Controls"'</a>
	<a href="/cgi-bin/admin/client_wireless_settings_fm.cgi">'$"Client Wireless Settings"'</a>
	<a href="/cgi-bin/admin/client_shutdown_time.cgi">'$"Client Shutdown Time"'</a>'
	if [ $INTERNETCTRL = yes ]
	then
		echo '<a href="/cgi-bin/admin/package_cache_control.cgi">'$"Package Cache Control"'</a>'
	fi
echo '	<a href="/cgi-bin/admin/linux_client_choose_background_fm.cgi">'$"Linux Client Background"'</a>
	<a href="/cgi-bin/admin/linux_client_software_controls_fm.cgi">'$"Linux Client Software Controls"'</a>
	<a href="/cgi-bin/admin/linux_client_install_software_packages_fm.cgi">'$"Linux Client Software Packages"'</a>
      </div>

 <div class="collapsed">
        <span>'$"Infrastructure"'</span>
        <a href="/cgi-bin/admin/asset_register_view.cgi">'$"Asset Register"'</a>'
[ $DHCPCTRL = yes ] && echo '	<a href="/cgi-bin/admin/dhcp_reservations.cgi">'$"DHCP Reservations"'</a>'
[ $MONITORINGCTRL = yes ] && echo '	<a href="/cgi-bin/admin/mon_status.cgi">'$"Network Status"'</a>'
[ $RADIUSCTRL = yes ] && echo '	<a href="/cgi-bin/admin/radius_access_points.cgi">'$"Radius Access Points"'</a>'

echo '<a href="/cgi-bin/admin/dnsview_fm.cgi">'$"DNS"'</a>
</div>'


if [ $PRINTERCTRL = yes ]
then
echo '      <div class="collapsed">
        <span>'$"Printer"'</span>
        <a href="/cgi-bin/admin/printers.cgi">'$"Manage Print Queues"'</a>
        <a href="/cgi-bin/admin/printer_accounting_view_user_usage_fm.cgi">'$"User Printer Usage"'</a>
        <a href="/cgi-bin/admin/printer_accounting_view_group_usage_fm.cgi">'$"Group Printer Usage"'</a>
        <a href="/cgi-bin/admin/printer_accounting_add_user_limit_fm.cgi">'$"Add User Limit"'</a>
        <a href="/cgi-bin/admin/printer_accounting_user_limits_fm.cgi">'$"User Printer Limits"'</a>
        <a href="/cgi-bin/admin/printer_accounting_group_limits_fm.cgi">'$"Group Printer Limits"'</a>
        <a href="/cgi-bin/admin/printer_driver_gen.cgi">'$"Printer Driver Generation"'</a>
      </div>'
fi

if [ $EMAILCTRL = yes ]
then
echo '      <div class="collapsed">
        <span>E-Mail</span>
        <a href="/cgi-bin/admin/email_aliases.cgi">'$"Aliases"'</a>
	<a href="/cgi-bin/admin/email_whitelists.cgi">'$"Whitelists"'</a>
	<a href="/cgi-bin/admin/email_view_banned_domains_fm.cgi">'$"Banned E-Mail domains"'</a>
	<a href="/cgi-bin/admin/email_limits.cgi">'$"E-Mail limits"'</a>
	<a href="/cgi-bin/admin/email_show_queue_fm.cgi">'$"E-Mail queue"'</a>
	<a href="/cgi-bin/admin/email_statistics_fm.cgi">'$"E-Mail Statistics"'</a>
      </div>'
fi

if [ $INTERNETCTRL = yes ]
then
echo '      <div class="collapsed">
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

if [ $REVERSEPROXYCTRL = yes ]
then
echo '      <div class="collapsed">
        <span>Web</span>
        <a href="/cgi-bin/admin/reverse_proxy_view_fm.cgi">'$"Reverse Proxy Sites"'</a>
      </div>'
fi

echo '<div class="a.current">
<small><small>
'$"Version"' : '$VERSION'
</small></small>
</div>
</div></div></body></html>
'
exit
