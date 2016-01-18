#!/bin/bash
#Change password
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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Find student files and folders"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
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

echo '<form action="/cgi-bin/admin/find_student_files.cgi" method="post"><div id="'$DIV_ID'">'

[ $MOBILE = no ] && echo '<div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Find student files and folders"'</b></a></td></tr></tbody></table><br>'
else
echo '<b>'$"Find student files and folders"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will search students home areas for files and folders."'</span></a><br><br>'
fi

if [ $MOBILE = yes ]
then
echo '
<div id="suggestions"></div>
'$"File / folder name"'<br>
<input tabindex= "1" style="width: 160px;" name="_FILENAME_" 
 value="'$USERNAME'" size="20" type="text"><br>
'
else
echo '<div id="suggestions"></div><table class="standard" style="text-align: left;" >
    <tbody>

<tr><td style="width: 180px;"><b>'$"File / folder name"'</b></td><td>
<input tabindex= "1" style="width: 200px;" name="_FILENAME_" 
 value="'$FILENAME'" size="20" type="text"></td><td style="text-align: center;">
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name of the file or folder you want to search for."'</span></a>
</td></tr>
<tr><td style="width: 180px;"><b>'$"Find"'</b></td><td></td><td style="text-align: center;"><input checked="checked" name="_OPTION_" value="find" type="radio"></td></tr>
<tr><td style="width: 180px;"><b>'$"Delete"'</b></td><td><span style="color: red;"><b>'$"Use with extreme care"'</b></span></td><td style="text-align: center;"><input name="_OPTION_" value="delete" type="radio"></td></tr>
</tbody></table><br>'
fi

[ $MOBILE = no ] && echo '</div><div id="infobox">'

#Show list of servers
/opt/karoshi/web_controls/show_servers $MOBILE servers $"Search server"

[ $MOBILE = no ] && echo '</div>'

echo '</div></form></div></body></html>'
exit
