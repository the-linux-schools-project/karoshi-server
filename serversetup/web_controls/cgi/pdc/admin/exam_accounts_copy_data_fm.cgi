#!/bin/bash
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
<!DOCTYPE html>
<html>
<head>
  <title>'$"Exam Accounts - Copy Data"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/exam_accounts_copy_data.cgi" method="post"><div id="actionbox">
<b>'$"Exam Accounts - Copy Data"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Please select the exam accounts that you want to copy the data to."'</span></a><br><br>'
#Check to see if any data has been uploaded
if [ `ls -1 /var/www/karoshi/exam_upload | wc -l` = 0 ]
then
echo '
'$"No files have been uploaded to copy to the exam accounts."'
</div></div></body></html>
'
else
echo '
  <br>
  <table class="standard" style="text-align: left; >
    <tbody>
<tr><td style="width: 180px;"><span style="font-weight: bold;">'$"Start Account"'</span></td><td>'$"exam"'</td><td><input name="_EXAMSTART_" maxlength="3" size="3" value="1" type="text"></td></tr>
<tr><td><span style="font-weight: bold;">'$"End Account"'</span></td><td>'$"exam"'</td><td><input name="_EXAMEND_" maxlength="3" size="3" value="10" type="text"></td></tr>
<tr><td><span style="font-weight: bold;">'$"All"'</span></td><td></td><td><input name="_ALL_" value="all" type="checkbox"></td></tr>
<tr><td><span style="font-weight: bold;">'$"Read only"'</span></td><td></td><td><input name="_READONLY_" value="readonly" type="checkbox"> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will set the exam_files folder and the uploaded files to read only in each account. Students will need to copy the files out of the folder to use them."'</span></a></td></tr>
</tbody></table>
</div>
<div id="submitbox">
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
</form>
</div></body>
</html>
'
fi
exit
