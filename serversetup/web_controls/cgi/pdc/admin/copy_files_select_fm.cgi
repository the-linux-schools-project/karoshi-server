#!/bin/bash
#copy_files_select
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
  <title>'$"Copy Files - Select"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">
<form action="/cgi-bin/admin/copy_files_select.cgi" method="post"><span style="font-weight: bold;">
'$"Copy Files - Select"'</span><br>
  <br>
  <br>
'
#Check to see if any files have been uploaded
if [ `ls -1 /var/www/karoshi/web_upload | wc -l` = 0 ]
then
echo '
'$"No files have been uploaded to copy to user accounts."'</div></div></body></html>
'
else
echo '<table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"Group"'</td><td>
'
/opt/karoshi/web_controls/group_dropdown_list
echo '<td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=copy_files"><img class="images" alt="" src="/images/help/info.png"><span>'$"Select the group that you want to copy the data to."'</span></a></td></tr>
</tbody></table>
<br>
<input value="'$"Submit"'" class="button" type="submit">
</form>
</div>
</div></body>
</html>
'
fi
exit
