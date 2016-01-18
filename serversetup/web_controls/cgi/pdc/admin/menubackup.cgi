#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

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
<!DOCTYPE html>
<html>
<head>
  <meta content="text/html; charset=UTF-8" http-equiv="content-type">
  <title>'$"Web Management"'</title>
<link href="/css/'$STYLESHEET'?d='`date +%F`'" rel="stylesheet" type="text/css">
</head>
<body>
<table class="menu" style="text-align: left; height: 90px;" >
  <tbody>
    <tr>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/change_password_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/user.png"><br>
'$"Users and Groups"'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/change_management_passwords_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/system.png"><br>
'$"System"'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/domain_information.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/client.png"><br>
'$"Client"'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/printers.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/printer.png"><br>
'$"Printer"'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/view_user_disk_usage_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/file.png"><br>
'$"File"'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/email_add_alias_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/email.png"><br>
'$"E-Mail"'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/dg_banned_sites_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/internet.png"><br>
'$"Internet"'</a></td>
      <td style="height: 90px; width: 110px; text-align: center;"><a href="/cgi-bin/admin/web_management_upload_files_fm.cgi" target="_top"><img style="border: 0px solid ; width: 48px; height: 48px;" alt="" src="/images/web.png"><br>
'$"Web"'</a></td>
    </tr>
  </tbody>
</table>

<div id="headerbar">
	<div id="headerbar1">
&nbsp;&nbsp;<a href="/cgi-bin/menu.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/home.png"></a>&nbsp;&nbsp;<a href="/cgi-bin/admin/search_fm.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/search.png"></a>&nbsp;&nbsp;'$"DE"'&nbsp;&nbsp; - &nbsp;&nbsp;'$"Web Management"' <small><small>'$VERSION ':' 120109-1210'</small></small>
	</div>
	<div id="headerbar2">
<a href="/cgi-bin/menu.cgi" target="_top"><img style="border: 0px solid ; width: 16px; height: 16px;" alt="" src="/images/info.png"></a>
	</div>
</div>
<div id="tickerbar">
'
#Check for warning messages
if [ -f /opt/karoshi/web_controls/warnings/summary.txt ]
then
WARNINGS=`cat /opt/karoshi/web_controls/warnings/summary.txt`
if [ `echo $WARNINGS | wc -L` -gt 300 ]
then
echo '<marquee behavior="scroll" direction="left">'$WARNINGS'</marquee>'
else
echo $WARNINGS
fi
fi
echo '</div></div></body></html>'
exit

