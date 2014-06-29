#!/bin/bash
#Copyright (C) 2007  Paul Sharrad
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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/menus/internet ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/menus/internet
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head><title>Karoshi Web Application</title><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><link href="/css/'$STYLESHEET'?d='`date +%F`'" rel="stylesheet" type="text/css"></head>
<body><div id="pagecontainer"><table class="leftmenu" style="text-align: left; width: 222px; height: 426px;" border="0" cellpadding="6" cellspacing="0"><tbody><tr><td style="vertical-align: top;">
<a href="/cgi-bin/admin/dg_view_banned_users_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/internet/view_banned_users.png">'$VIEWMSG'</a><br>
<a href="/cgi-bin/admin/dg_banned_sites_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/internet/banned_sites.png">'$BANMSG'</a><br>
<a href="/cgi-bin/admin/dg_allowed_sites_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/internet/allowed_sites.png">'$ALLOWMSG'</a><br>
<a href="/cgi-bin/admin/dg_update_locations_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/internet/internet_update_data.png">'$UPDATELOCATIONS'</a><br>
<a href="/cgi-bin/admin/dg_import_location_data1.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/internet/internet_import_data.png">'$IMPORTLOCATIONDATA'</a><br>
<a href="/cgi-bin/admin/activate_internet_changes_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/internet/activate_changes.png">'$ACTIVATECHANGES'</a><br>
</div></body>
</td></tr></tbody></table></div></body></html>
'
exit
