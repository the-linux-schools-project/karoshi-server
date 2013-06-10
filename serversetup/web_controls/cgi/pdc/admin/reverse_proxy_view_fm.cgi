#!/bin/bash
#Copyright (C) 2010  Paul Sharrad
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/web/reverse_proxy_view ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/web/reverse_proxy_view
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

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "reverse_proxy_add_fm.cgi"'
echo '</script>'
echo "</body></html>"
exit
}

#Check to see if there are any proxy sites
if [ ! -d /opt/karoshi/server_network/reverseproxy/sites/ ]
then
MESSAGE=$ERRORMSG3
show_status
fi

if [ `ls -1 /opt/karoshi/server_network/reverseproxy/sites/ | wc -l` = 0 ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Get reverse proxy server
PROXYSERVER=`sed -n 1,1p /opt/karoshi/server_network/reverseproxyserver | sed 's/ //g'`

if [ $PROXYSERVER'null' = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi

echo '<form action="/cgi-bin/admin/reverse_proxy_view.cgi" method="post">
<div id="actionbox">
<b>'$TITLE' - '$PROXYSERVER'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$PROXYSERVER - $WEBHELP1'</span></a><br>
  <br>
      <tr><td style="vertical-align: top;">
  <table class="standard" style="text-align: left; height: 40px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr><td style="width: 120px;"><b>'$TARGETMSG'</b></td><td style="width: 300px;"><b>'$DESTINATIONMSG'</b></td><td><b>'$DELETETITLE'</b></td></tr>'

for SITES in /opt/karoshi/server_network/reverseproxy/sites/*
do
SITE=`basename $SITES`
SITE2=`echo $SITE | sed 's/%3A//g' | sed 's/%2F/\//g' | sed 's/\/\///g'`
REDIRECT=`sed -n 6,6p /opt/karoshi/server_network/reverseproxy/sites/$SITE | cut -d' ' -f2- | sed 's/;//g'`
echo '<tr><td>'$SITE2'</td><td>'$REDIRECT'</td><td><a class="info" href="javascript:void(0)"><input name="_ACTION_DELETE_FOLDER_'$SITE'_" type="image" class="images" src="/images/submenus/web/delete.png" value="_ACTION_DELETE_FOLDER_'$SITE'_"><span>'$DELETETITLE $SITE2'</span></a></td></tr>'
done

echo '</tbody></table>
</form>
</body>
</html>
'
exit
