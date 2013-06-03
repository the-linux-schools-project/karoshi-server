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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/menus/menu ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/menus/menu
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
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'">
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
    <div style="float: left" id="my_menu" class="sdmenu">
	<div class="collapsed">
	<span>TLSP '$SCHOOL_NAME'</span>
<a href="/cgi-bin/menu.cgi">'$MAINMENUMSG'</a>
<a href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Main_Page">'$DOCUMENTATIONMSG'</a>
 	</div>
       <div class="collapsed">
        <span>'$HELPDESKSMSG'</span>
        <a href="/cgi-bin/admin/helpdesk_view_fm.cgi">'$HELPDESKVIEWMSG'</a>
        <a href="/cgi-bin/admin/helpdesk_add_fm.cgi">'$HELPDESKADDMSG'</a>
        </div>     
	<div class="collapsed">
        <span>'$USERMSG'</span>'
if [ $ADDUSERCTRL = yes ]
then
echo '        <a href="/cgi-bin/admin/add_user_fm.cgi">'$ADDUSERMSG'</a>
        <a href="/cgi-bin/admin/delete_user_fm.cgi">'$DELETEUSERMSG'</a>'
fi
echo '        <a href="/cgi-bin/admin/change_password_fm.cgi">'$CHANGEPASSMSG'</a>
      </div>
      <div class="collapsed">
        <span>'$SYSTEMMSG'</span>
        <a href="/cgi-bin/admin/file_manager.cgi">'$FILEMANAGER'</a>
        <a href="/cgi-bin/admin/server_info_fm.cgi">'$SERVERINFOMSG'</a>
        <a href="/cgi-bin/admin/update_karoshi_fm.cgi">'$UPDATEKAROSHIMSG'</a>
        <a href="/cgi-bin/admin/uptime_fm.cgi">'$UPTIMEMSG'</a>
        <a href="/cgi-bin/admin/view_karoshi_web_management_logs.cgi">'$WEBLOGSMSG'</a>
        <a href="/cgi-bin/admin/cron_view_fm.cgi">'$CRONCONTROLS'</a>
        <a href="/cgi-bin/admin/dnsview_fm.cgi">'$DNSCONTROLS'</a>
        <a href="/cgi-bin/admin/remote_management_change_language.cgi">'$CHANGELANG'</a>
        <a href="/cgi-bin/admin/remote_management_change_theme.cgi">'$CHANGETHEME'</a>
        <a href="/cgi-bin/admin/custom_command_fm.cgi">'$CUSTOMMSG'</a>
        <a href="/cgi-bin/admin/services_view_fm.cgi">'$SERVICESMSG'</a>
        <a href="/cgi-bin/admin/shutdown_fm.cgi">'$SHUTDOWNMSG'</a>
      </div>
	<div class="collapsed">
        <span>'$STORAGEMSG'</span>
        <a href="/cgi-bin/admin/disk_information_fm.cgi">'$DISKINFORMATION'</a>
        <a href="/cgi-bin/admin/disk_usage_fm.cgi">'$DISKUSAGE'</a>
        <a href="/cgi-bin/admin/view_disk_usage_logs_fm.cgi">'$DISKUSAGELOGS'</a>
      </div>
      <div class="collapsed">
        <span>'$CLIENTMSG'</span>
	<a href="/cgi-bin/admin/client_boot_controls_fm.cgi">'$CLIENTBOOTCONTROLS'</a>
      </div>

 <div class="collapsed">
        <span>'$INFRASTRUCTURESMSG'</span>
        <a href="/cgi-bin/admin/asset_register_view.cgi">'$ASSETREGISTER'</a>'
[ $MONITORINGCTRL = yes ] && echo '	<a href="/cgi-bin/admin/mon_status.cgi">'$SERVERSTATUSMSG'</a>'
       echo ' </div> '


if [ $PRINTERCTRL = yes ]
then
echo '      <div class="collapsed">
        <span>'$PRINTERMSG'</span>
        <a href="/cgi-bin/admin/printers.cgi">'$VIEWQUEUES'</a>
        <a href="/cgi-bin/admin/printer_accounting_view_user_usage_fm.cgi">'$USERPRINTERUSAGE'</a>
        <a href="/cgi-bin/admin/printer_accounting_view_group_usage_fm.cgi">'$GROUPPRINTERUSAGE'</a>
        <a href="/cgi-bin/admin/printer_accounting_add_user_limit_fm.cgi">'$ADDUSERPRINTERLIMIT'</a>
        <a href="/cgi-bin/admin/printer_accounting_user_limits_fm.cgi">'$USERPRINTERLIMITS'</a>
        <a href="/cgi-bin/admin/printer_accounting_group_limits_fm.cgi">'$ACCOUNTINGGROUPLIMITS'</a>
      </div>'
fi

if [ $INTERNETCTRL = yes ]
then
echo '      <div class="collapsed">
        <span>Internet</span>
        <a href="/cgi-bin/admin/dg_view_user_logs_fm.cgi">'$VIEWUSERLOGS'</a>
        <a href="/cgi-bin/admin/dg_view_site_logs_fm.cgi">'$VIEWSITELOGS'</a>
        <a href="/cgi-bin/admin/dg_view_computer_logs_fm.cgi">'$VIEWCOMPUTERLOGS'</a>
        <a href="/cgi-bin/admin/dg_ban_user.cgi">'$BANUSER'</a>
        <a href="/cgi-bin/admin/dg_banned_sites_fm.cgi">'$ADDBANNESITES'</a>
        <a href="/cgi-bin/admin/dg_part_banned_sites_fm.cgi">'$ADDPBANNEDSITES'</a>
        <a href="/cgi-bin/admin/dg_wildcard_ban_fm.cgi">'$WCARDBAN'</a>
        <a href="/cgi-bin/admin/dg_allowed_sites_fm.cgi">'$ADDALLOWEDSITES'</a>
        <a href="/cgi-bin/admin/dg_part_allowed_sites_fm.cgi">'$ADDPALLOWEDSITES'</a>
        <a href="/cgi-bin/admin/dg_room_controls_fm.cgi">'$ROOMCONTROLS'</a>
        <a href="/cgi-bin/admin/activate_internet_changes_fm.cgi">'$ACTIVATECHANGES'</a>
      </div>'
fi
echo '<div class="a.current">
<small><small>
'$VERSION' : 130603-1029
</small></small>
</span></div>
    </div>
</body></html>
'
exit
