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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Requested Users"'</title>
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">
<div class="sectiontitle">'$"Requested Users"'</div><br>'
if [ -d /opt/karoshi/user_requests/new_users ]
then
if [ `ls -1 /opt/karoshi/user_requests/new_users | wc -l` -gt 0  ]
then
echo '<table class="standard" style="text-align: left; width: 690px;" ><tbody>'
echo '<tr><td style="vertical-align: top;">'$"Forename"'</td><td style="vertical-align: top;">'$"Surname"'</td><td style="vertical-align: top;">'$"Primary Group"'</td><td style="vertical-align: top;">'$"Admission Number"'</td><td style="vertical-align: top;">'$"Requested by"'</td><td style="vertical-align: top;">'$"Add"'</td><td style="vertical-align: top;">'$"Remove"'</td></tr>'
for NEW_USER in /opt/karoshi/user_requests/new_users/*
do
NEW_USER_DATA=`sed -n 1,1p $NEW_USER`
FORENAME=`echo $NEW_USER_DATA | cut -d: -f1`
SURNAME=`echo $NEW_USER_DATA | cut -d: -f2`
GROUP=`echo $NEW_USER_DATA | cut -d: -f3`
ENROLLMENTNUMBER=`echo $NEW_USER_DATA | cut -d: -f4`
REQUESTUSER=`echo $NEW_USER_DATA | cut -d: -f5`
FILE=`basename $NEW_USER`
echo '<tr><td style="vertical-align: top;">'$FORENAME'</td><td style="vertical-align: top;">'$SURNAME'</td><td style="vertical-align: top;">'$GROUP'</td><td style="vertical-align: top;">'$ENROLLMENTNUMBER'</td><td style="vertical-align: top;">'$REQUESTUSER'</td><td style="vertical-align: top;"><form action="/cgi-bin/admin/add_user_fm.cgi" method="post"><input type="image" src="/images/submenus/user/adduser.png" name="_ACTION_'$FILE'_" value=""></form></td><td style="vertical-align: top;"><form action="/cgi-bin/admin/request_new_users_delete.cgi" method="post"><input type="image" src="/images/submenus/user/delete_user2.png" name="_ACTION_'$FILE'_" value=""></form></td></tr>'
done
echo '</tbody></table>'
else
echo $"All requested users have been dealt with."'<br>'
fi
fi
echo '</div></div></body></html>'
exit
