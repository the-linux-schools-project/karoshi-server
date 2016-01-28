#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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
<!DOCTYPE html>
<html>
<head>
  <title>'$"Allowed Mime Types"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body onLoad="start()"><div id="pagecontainer">'

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
fi

echo '<form action="/cgi-bin/admin/dg_allowed_mime_types.cgi" name="selectedsites" method="post"><b></b>
  <div id="'$DIV_ID'">'


#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" >
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Allowed Mime Types"'</b></a></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$PARTBANMSG'<br><br>'$WWWWARNING'<br><br>'$EXAMPLEMSG'</span></a></td></tr></tbody></table><br>'
else
echo '<b>'$"Allowed Mime Types"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$PARTBANMSG'<br><br>'$WWWWARNING'<br><br>'$EXAMPLEMSG'</span></a>
<br><br>'
fi


#Check to see current state of mime types

source /opt/karoshi/server_network/dansguardian/mime_types


echo '
  <table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 100px;">'$STUDENTSMSG'</td>
        <td><input checked="checked" name="_FILTERGROUP_" value="Students" type="checkbox"></td>
      </tr>
      <tr>
        <td>'$STAFFMSG'</td>
        <td><input name="_FILTERGROUP_" value="Staff" type="checkbox"></td>
      </tr>
      <tr>
        <td>Site</td>
        <td><input name="_WEBADDRESS_" size="20"></td>
      </tr>
    </tbody>
  </table>
  <br>'

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"> <input type="button" onclick="SetAllCheckBoxes('\'selectedsites\'', '\'_FILTERGROUP_\'', true);" value="'$"Select all"'">
  </div></form></div></body></html>'
exit
