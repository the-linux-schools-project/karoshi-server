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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/menus/menu ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/menus/menu
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
  <title>'$TITLE'</title>
<link href="/css/'$STYLESHEET'" rel="stylesheet" type="text/css">
</head>
<body>
<table class="menu" style="text-align: left; height: 90px;" border="0" cellpadding="2" cellspacing="2">
  <tbody>
    <tr>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/change_password_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/user.png"><br>
'$USERMSG'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/change_management_passwords_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/system.png"><br>
'$SYSTEMMSG'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/domain_information.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/client.png"><br>
'$CLIENTMSG'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/printers.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/printer.png"><br>
'$PRINTERMSG'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/file_manager.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/file.png"><br>
'$FILEMSG'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/email_add_alias_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/email.png"><br>
'$EMAILMSG'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/activate_internet_changes_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/internet.png"><br>
'$INTERNETMSG'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/web_management_upload_files_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/web.png"><br>
'$WEBMSG'</a></td>
    </tr>
  </tbody>
</table>

<div id="headerbar">
	<div id="headerbar1">
&nbsp;&nbsp;<a href="/cgi-bin/menu.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/home.png"></a>&nbsp;&nbsp;<a href="/cgi-bin/admin/search_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/search.png"></a>&nbsp;&nbsp;'$SCHOOL_NAME'&nbsp;&nbsp; - &nbsp;&nbsp;'$TITLE' <small><small>'$VERSION ':' 280509-0838'</small></small>
	</div>'

if [ -f /opt/karoshi/information ]
then
echo '
	<div id="headerbar2">
<a href="/cgi-bin/admin/information.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/info.png"></a>
	</div>'
fi
echo '</div>'
#Check for warning messages
if [ -f /opt/karoshi/web_controls/warnings/summary.txt ]
then
WARNINGS=`cat /opt/karoshi/web_controls/warnings/summary.txt`
if [ `echo $WARNINGS | wc -L` -gt 330 ]
then
echo '<div id="tickerbar"><marquee behavior="scroll" direction="left" scrollamount="2">'$WARNINGS'</marquee></div>'
else
echo '<div id="tickerbar">'$WARNINGS'</div>'
fi
fi
echo '</body></html>'
exit


