#!/bin/bash
#copy_files_select
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/copy_files ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/copy_files
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
  <title>'$TITLE2'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">
<form action="/cgi-bin/admin/copy_files_select.cgi" method="post"><span style="font-weight: bold;">
'$TITLE2'</span><br>
  <br>
  <br>
'
#Check to see if any files have been uploaded
if [ `ls -1 /var/www/karoshi/web_upload | wc -l` = 0 ]
then
echo '
'$ERRORMSG4'</div></body></html>
'
else
echo '
'$GROUPMSG'
  <br>
  <br>
        <select name="_GROUP_">
        <option>yr1999</option>
        <option>yr2000</option>
        <option>yr2001</option>
        <option>yr2002</option>
        <option>yr2003</option>
        <option>yr2004</option>
        <option>yr2005</option>
        <option>yr2006</option>
        <option>yr2007</option>
        <option>yr2008</option>
        <option>yr2009</option>
        <option>yr2010</option>
        <option>yr2011</option>
        <option>yr2012</option>
        <option>guests</option>
        <option>staff</option>
        <option>nonteachingstaff</option>
        <option>officestaff</option>
        <option>studentstaff</option>
        <option>tech</option>
        <option>itadmin</option>
        </select>
  <br>
  <br>
  <input value="'$SUBMITMSG'" type="submit">
</form>
</div>
</body>
</html>
'
fi
exit
