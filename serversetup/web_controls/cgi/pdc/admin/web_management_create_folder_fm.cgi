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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/web/create_folder ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/web/create_folder
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
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">
<form action="/cgi-bin/admin/web_management_create_folder.cgi" method="post"><span style="font-weight: bold;">
'$TITLE'</span> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a><br>
  <br>
  <br>'

#Check that there are some web servers
if [ ! -d /opt/karoshi/server_network/webservers ]
then
MESSAGE=$ERRORMSG6
show_status
fi

#Check that there are some web servers
if [ `ls -1 /opt/karoshi/server_network/webservers | wc -l` = 0 ]
then
MESSAGE=$ERRORMSG6
show_status
fi

#Show list of ssh enabled web servers
SERVERLISTARRAY=( `ls -1 /opt/karoshi/server_network/webservers` )
SERVERLISTCOUNT=${#SERVERLISTARRAY[@]}
SERVERCOUNTER=0
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"


echo '<table class="standard" style="text-align: left; height: 20px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$FOLDERMSG'</td>
        <td><input tabindex= "1" name="___NEWFOLDER___" size="20" type="text"></td><td>

<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'<br><br>'$HELPMSG3'</span></a>
      </td></tr></tbody></table><br><br>'
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'

while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="___WEBSERVER___'$KAROSHISERVER'___" type="image" class="images" src="'$SERVERICON'" value="___WEBSERVER___'$KAROSHISERVER'___"><span>'$KAROSHISERVER'</span></a><br>'$KAROSHISERVER'</td>'
[ $SERVERCOUNTER = 5 ] && echo '</tr><tr>'
let SERVERCOUNTER=$SERVERCOUNTER+1
done
echo '</tr></tbody></table></div></body></html>
'
exit
