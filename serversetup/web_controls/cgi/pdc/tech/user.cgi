#!/bin/bash
#user
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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/menus/user ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/menus/user
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head><title>Karoshi Web Application</title><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><link rel="stylesheet" href="/css/'$STYLESHEET'"></head>
<body><table class="leftmenu" style="text-align: left; width: 222px; height: 426px;" border="0" cellpadding="6" cellspacing="0">
<tbody><tr><td style="vertical-align: top;">
<a href="/cgi-bin/tech/change_password_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/password.png">'$CHANGEPASSMSG'</a><br>
<a href="/cgi-bin/tech/reset_password_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/reset_password.png">'$RESETPASSMSG'</a><br>
<a href="/cgi-bin/tech/add_user_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/adduser.png">'$ADDUSERMSG'</a><br>
<a href="/cgi-bin/admin/user_image_upload_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/user_images.png">'$USERIMAGEMSG'</a><br>
<a href="/cgi-bin/admin/lockout_reset_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/lockout_reset.png">'$LOCKOUTRESETMSG'</a><br>
<a href="/cgi-bin/tech/ban_user_account.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/ban_user.png">'$BANUSERMSG'</a><br>
<a href="/cgi-bin/tech/banned_users_view_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/view_banned_users.png">'$VIEWBANUSERMSG'</a><br>
<a href="/cgi-bin/tech/change_primary_group_fm.cgi" target="_top"><img style="border: 0px solid ; width: 17px; height: 17px;" alt="" src="/images/submenus/user/change_primary_group.png">'$CHANGEPRIGRPMSG'</a><br>
<a href="/cgi-bin/tech/groups_change_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/change_seconday_group.png">'$CHANGESECGRPMSG'</a><br>
<a href="/cgi-bin/tech/change_username_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/change_username.png">'$CHANGEUSERNAMEMSG'</a><br>
<a href="/cgi-bin/tech/incident_log_add.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/info.png">'$RECINCMSG'</a><br>
<a href="/cgi-bin/tech/incident_log_view_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/submenus/user/info.png">'$VIEWLOGSMSG'</a><br>
</td></tr></tbody></table></body></html>
'
exit
