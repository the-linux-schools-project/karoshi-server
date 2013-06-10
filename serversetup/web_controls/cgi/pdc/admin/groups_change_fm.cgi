#!/bin/bash
#groups_change
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/groups_change ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/groups_change
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/groups_change.cgi" method="post">
  <div id="actionbox"><b>'$TITLE'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Secondary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$EXPLMSG'</span></a><br>
  <br>
<table class="standard" style="text-align: left; left: 232px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 180px;">'$USERNAMEMSG'</td><td><input name="_USERNAME_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Secondary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$USERMSG'</span></a></td></tr>
<tr><td style="vertical-align: top;">'$GROUPSMSG'</td><td style="vertical-align: top;">'

#Get list
/opt/karoshi/web_controls/group_dropdown_list | sed 's/<select /<select multiple="multiple"/g'

echo '</td><td style="vertical-align: top;">
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Secondary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$OPENINGMSG'</span></a>

<br></td></tr>
<tr><td>'$OTHERGROUPMSG' 1</td><td><input name="_OTHERGROUP1_" style="width: 200px;" size="20" type="text"></td></tr>
<tr><td>'$OTHERGROUPMSG' 2</td><td><input name="_OTHERGROUP2_" style="width: 200px;" size="20" type="text"></td></tr>
<tr><td>'$OTHERGROUPMSG' 3</td><td><input name="_OTHERGROUP3_" style="width: 200px;" size="20" type="text"></td></tr>
<tr><td>'$OTHERGROUPMSG' 4</td><td><input name="_OTHERGROUP4_" style="width: 200px;" size="20" type="text"></td></tr>
</tbody></table>
  </div>
  <div id="submitbox">
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
  </div>
  </form>
</body>
</html>
'
exit
