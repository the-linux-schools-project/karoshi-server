#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/request_delete_users ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/request_delete_users
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
  <title>'$TITLE2'</title>
<link rel="stylesheet" href="/css/'$STYLESHEET'">
</head>
<script src="/all/stuHover.js" type="text/javascript"></script>
<body onLoad="start()">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">
<b>'$TITLE2'</b><br><br>'
if [ -d /opt/karoshi/user_requests/delete_users ]
then
if [ `ls -1 /opt/karoshi/user_requests/delete_users | wc -l` -gt 0  ]
then
echo '<table class="standard" style="text-align: left; width: 690px;" border="0" cellpadding="2" cellspacing="2"><tbody>'
echo '<tr><td style="vertical-align: top;">'$FORENAMEMSG'</td><td style="vertical-align: top;">'$SURNAMEMSG'</td><td style="vertical-align: top;">'$YEARGROUPMSG'</td><td style="vertical-align: top;">'$ADNOMSG'</td><td style="vertical-align: top;">'$REQUESTUSERMSG'</td><td style="vertical-align: top;">'$ACTIONMSG'</td><td style="vertical-align: top;">'$DELETEMSG'</td></tr>'
for DELETE_USER in /opt/karoshi/user_requests/delete_users/*
do
DELETE_USER_DATA=`sed -n 1,1p $DELETE_USER`
FORENAME=`echo $DELETE_USER_DATA | cut -d: -f1`
SURNAME=`echo $DELETE_USER_DATA | cut -d: -f2`
GROUP=`echo $DELETE_USER_DATA | cut -d: -f3`
ENROLLMENTNUMBER=`echo $DELETE_USER_DATA | cut -d: -f4`
REQUESTUSER=`echo $DELETE_USER_DATA | cut -d: -f5`
FILE=`basename $DELETE_USER`
echo '<tr><td style="vertical-align: top;">'$FORENAME'</td><td style="vertical-align: top;">'$SURNAME'</td><td style="vertical-align: top;">'$GROUP'</td><td style="vertical-align: top;">'$ENROLLMENTNUMBER'</td><td style="vertical-align: top;">'$REQUESTUSER'</td><td style="vertical-align: top;"><form action="/cgi-bin/admin/delete_user_fm.cgi" method="post"><input type="image" src="/images/submenus/user/delete_user.png" name="_ACTION_'$FILE'_" value=""></form></td><td style="vertical-align: top;"><form action="/cgi-bin/admin/request_delete_users_delete.cgi" method="post"><input type="image" src="/images/submenus/user/delete_user2.png" name="_ACTION_'$FILE'_" value=""></form></td></tr>'
done
echo '</tbody></table>'
else
echo $NOREQUESTSMSG'<br>'
fi
fi
echo '</div</body></html>'
exit
