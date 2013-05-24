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
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/search ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/search
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
<html>
<head>
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
</head>
<body>
<div id="menubox">
<iframe src="/cgi-bin/admin/menu.cgi" name="main" frameborder="0" width="950" height="150" scrolling="no" marginwidth="0" marginheight="0">
</iframe><br><br>
<form action="/cgi-bin/admin/search.cgi" method="post"><span style="font-weight: bold;">
'$TITLE' </span> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$SEARCHHELP'</span></a><br>
  <br>
  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 100px;">
'$SEARCHMSG'</td>
        <td><input tabindex= "1" name="_SEARCH_" size="20" type="text"> <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset"></td></tr>
    </tbody>
  </table>
</div>
</form>
</body>
</html>
'
exit
