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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/exam_accounts_copy_data ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/exam_accounts_copy_data
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <title>'$TITLE2'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/exam_accounts_copy_data.cgi" method="post"><div id="actionbox">
<b>'$TITLE2'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$COPYDATAMSG'</span></a><br><br>'
#Check to see if any data has been uploaded
if [ `ls -1 /var/www/karoshi/exam_upload | wc -l` = 0 ]
then
echo '
'$ERRORMSG1'
</div></body></html>
'
else
echo '
  <br>
  <table class="standard" style="text-align: left; border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 180px;"><span style="font-weight: bold;">'$STARTACCOUNTMSG'</span></td><td>'$EXAMMSG'</td><td><input name="_EXAMSTART_" maxlength="3" size="3" value="1" type="text"></td></tr>
<tr><td><span style="font-weight: bold;">'$ENDACCOUNTMSG'</span></td><td>'$EXAMMSG'</td><td><input name="_EXAMEND_" maxlength="3" size="3" value="10" type="text"></td></tr>
<tr><td><span style="font-weight: bold;">'$ALLMSG'</span></td><td></td><td><input name="_ALL_" value="all" type="checkbox"></td></tr>
<tr><td><span style="font-weight: bold;">'$READONLYMSG'</span></td><td></td><td><input name="_READONLY_" value="readonly" type="checkbox"> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$UPLOADHELP2'</span></a></td></tr>
</tbody></table>
</div>
<div id="submitbox">
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div>
</form>
</body>
</html>
'
fi
exit
