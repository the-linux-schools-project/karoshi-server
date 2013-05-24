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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/bulk_user_creation ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/bulk_user_creation
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all

#Select the default username style
if [ -f /opt/karoshi/server_network/default_username_style ]
then
source /opt/karoshi/server_network/default_username_style
[ $DEFAULTSTYLE = 1 ] && SELECT1='selected="selected"'
[ $DEFAULTSTYLE = 2 ] && SELECT2='selected="selected"'
[ $DEFAULTSTYLE = 3 ] && SELECT3='selected="selected"'
[ $DEFAULTSTYLE = 4 ] && SELECT4='selected="selected"'
[ $DEFAULTSTYLE = 5 ] && SELECT5='selected="selected"'
[ $DEFAULTSTYLE = 6 ] && SELECT6='selected="selected"'
[ $DEFAULTSTYLE = 7 ] && SELECT7='selected="selected"'
[ $DEFAULTSTYLE = 8 ] && SELECT8='selected="selected"'
[ $DEFAULTSTYLE = 9 ] && SELECT9='selected="selected"'
else
SELECT1='selected="selected"'
fi

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
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><form action="/cgi-bin/admin/bulk_user_creation_create.cgi" method="post"><b>'$TITLE'</b><br>
  <br>
'$OPENINGMSG':<br>
  <br>'

#Check that this server is not part of a federated setup
if [ -f /opt/karoshi/server_network/servers/$HOSTNAME/federated_server ]
then
echo $ERRORMSG18 '</div></body></html>'
exit
fi

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 150px;">
'$USERNAMEMSG'</td><td>
<select name="_USERNAMESTYLE_" style="width: 200px;">
        <option value="userstyleS1" '$SELECT1'>'$STYLE1MSG': '$STYLE1MSGEX'</option>
        <option value="userstyleS2" '$SELECT2'>'$STYLE2MSG': '$STYLE2MSGEX'</option>
        <option value="userstyleS3" '$SELECT3'>'$STYLE3MSG': '$STYLE3MSGEX'</option>
        <option value="userstyleS4" '$SELECT4'>'$STYLE4MSG': '$STYLE4MSGEX'</option>
        <option value="userstyleS5" '$SELECT5'>'$STYLE5MSG': '$STYLE5MSGEX'</option>
        <option value="userstyleS6" '$SELECT6'>'$STYLE6MSG': '$STYLE6MSGEX'</option>
        <option value="userstyleS7" '$SELECT7'>'$STYLE7MSG': '$STYLE7MSGEX'</option>
        <option value="userstyleS8" '$SELECT8'>'$STYLE8MSG': '$STYLE8MSGEX'</option>
        <option value="userstyleS9" '$SELECT9'>'$STYLE9MSG': '$STYLE9MSGEX'</option>
</select></td></tr>
<tr><td>'$PRIGROUPMSG'</td>
</td><td>'
/opt/karoshi/web_controls/group_dropdown_list
echo '</td></tr></tbody></table>
</div>
<div id="submitbox">
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div>
</form>
</body>
</html>
'
exit

