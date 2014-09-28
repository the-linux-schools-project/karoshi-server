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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Add Additional Network Share"'</title><META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE"><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
<body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
fi
echo '<form name="myform" action="/cgi-bin/admin/samba_add_share.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Add Additional Network Share"'</b></a></td></tr></tbody></table><br>'
else
echo '<div id="titlebox"><div class="sectiontitle">'$"Add Additional Network Share"'</div><br>'
fi

echo '
  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"Comment"'</td>
        <td><input tabindex= "1" name="_COMMENT_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Network_Shares"><img class="images" alt="" src="/images/help/info.png"><span>'$"This show as information for your clients when they look at the network share."'</span></a>
      </td></tr>
      <tr>
        <td>
'$"Folder Name"'</td>
        <td><input tabindex= "2"  name="_FOLDERNAME_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Network_Shares"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will create a folder in /home with the name that you specify."'</span></a>
      </td></tr>
      <tr>
        <td>
'$"Group"'</td>
        <td>'
/opt/karoshi/web_controls/group_dropdown_list

echo '</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Network_Shares"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name of the group that you want to allow access to the folder."'</span></a>
</td></tr>
<tr><td>'$"Group Permissions"'</td></tr>
<tr><td>'$"Read only"'</td><td><input name="_GROUPPERMS_" value="readonly" type="radio"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Network_Shares"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the permissions that you want to set for this group for the share."'</span></a></td></tr>
<tr><td>'$"Full Access"'</td><td><input name="_GROUPPERMS_" checked="checked" value="fullaccess" type="radio"></td></tr>
<tr><td>'$"Others Permissions"'</td></tr>
<tr><td>'$"No access"'</td><td><input name="_OTHERSPERMS_" value="none" type="radio"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Network_Shares"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the permissions that you want to allow for anyone else not in the group."'</span></a></td></tr>
<tr><td>'$"Read only"'</td><td><input name="_OTHERSPERMS_" checked="checked" value="readonly" type="radio"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Network_Shares"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the permissions that you want to allow for anyone else not in the group."'</span></a></td></tr>
<tr><td>'$"Full Access"'</td><td><input name="_OTHERSPERMS_" value="fullaccess" type="radio"></td></tr>
</tbody></table><br>'

[ $MOBILE = no ] && echo '</div><div id="infobox">'

#Show list of servers
/opt/karoshi/web_controls/show_servers $MOBILE servers $"Add share"

[ $MOBILE = no ] && echo '</div>'

echo '</div></form></div></body></html>'
exit

