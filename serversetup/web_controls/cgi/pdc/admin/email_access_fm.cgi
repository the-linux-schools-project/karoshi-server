#!/bin/bash
#Copyright (C) 2012  Paul Sharrad

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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/email/email_access ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/email/email_access
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
echo '<div id="actionbox"><form action="/cgi-bin/admin/email_access.cgi" method="post"><b>'$TITLE'</b>
<a class="info" target="_blank" href="http://www.linuxgfx.co.uk/karoshi/documentation/wiki/index.php?title=E-Mail_Access_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>
<br><br>
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody>
<tr><td style="width: 180px;">'$USERNAMEMSG'</td><td><input tabindex= "1" name="_EMAILUSER_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxgfx.co.uk/karoshi/documentation/wiki/index.php?title=E-Mail_Access_Controls#Banning_and_Allowing_Users"><img class="images" alt="" src="/images/help/info.png"><span>'$USERHELP1'</span></a></td></tr>
<tr><td>Ban</td><td><input checked="checked" name="_ACTION_" value="deny" type="radio"></td></tr>
<tr><td>Allow</td><td><input name="_ACTION_" value="allow" type="radio"></td></tr></tbody></table><br><br>
<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
</form><br>
<form action="/cgi-bin/admin/email_access.cgi" method="post"><table class="standard" style="text-align: left" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;"><b>'$PRIGROUPMSG'</b></td><td style="width: 180px;"><b>'$CHANGEMSG'</b></td><td style="width: 180px;"><b>'$PRIGROUPMSG'</b></td><td><b>'$CHANGEMSG'</b></td></tr><tr>
'
COUNTER=0
ICON1=/images/submenus/email/email_allow.png
ICON2=/images/submenus/email/email_deny.png

for PRI_GROUP in /opt/karoshi/server_network/group_information/*
do
PRI_GROUP=`basename $PRI_GROUP`
source /opt/karoshi/server_network/group_information/$PRI_GROUP

if [ -f /opt/karoshi/server_network/email_restrictions/$PRI_GROUP ]
then
ICON=$ICON2
ACTION=allow
MESSAGE=`echo $PRI_GROUP: $DENYMSG`
else
ICON=$ICON1
ACTION=deny
MESSAGE=`echo $PRI_GROUP: $ALLOWMSG`
fi

echo '<td>'$PRI_GROUP'</td><td><a class="info" href="javascript:void(0)"><input name="_GROUP_'$PRI_GROUP'_ACTION_'$ACTION'_" type="image" class="images" src="'$ICON'" value="_PRIGROUP_'$PRI_GROUP'_SERVER_'$SERVER'_"><span>'$MESSAGE'</span></a></td>'
let COUNTER=$COUNTER+1

if [ $COUNTER -gt 1 ]
then
echo '</tr><tr>'
COUNTER=0
fi

done

echo '</tbody></table></form><br><br></div></body></html>'
exit

