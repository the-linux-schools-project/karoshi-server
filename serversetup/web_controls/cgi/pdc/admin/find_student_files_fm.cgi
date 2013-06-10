#!/bin/bash
#Change password
#Copyright (C) 2011  Paul Sharrad
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/file/find_student_files ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/file/find_student_files
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
  <title>'$TITLE1'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body onLoad="start()">'

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
DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/admin/find_student_files.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE1'</b></a></td></tr></tbody></table><br>'
else
echo '<b>'$TITLE1'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a><br><br>'
fi

if [ $MOBILE = yes ]
then
echo '
<div id="suggestions"></div>
'$FILEMSG'<br>
<input tabindex= "1" style="width: 160px;" name="_FILENAME_" 
 value="'$USERNAME'" size="20" type="text"><br>
'
else
echo '<div id="suggestions"></div><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>

<tr><td style="width: 180px;"><b>'$FILEMSG'</b></td><td>
<input tabindex= "1" style="width: 200px;" name="_FILENAME_" 
 value="'$FILENAME'" size="20" type="text"></td><td style="text-align: center;">
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a>
</td></tr>
<tr><td style="width: 180px;"><b>'$FINDMSG'</b></td><td></td><td style="text-align: center;"><input checked="checked" name="_OPTION_" value="find" type="radio"></td></tr>
<tr><td style="width: 180px;"><b>'$DELETEMSG'</b></td><td><span style="color: red;"><b>'$CAREMSG'</b></span></td><td style="text-align: center;"><input name="_OPTION_" value="delete" type="radio"></td></tr>
</tbody></table><br>'
fi

#Show list of ssh enabled servers
SERVERCOUNTER=1
ROWCOUNT=6
[ $MOBILE = yes ] && ROWCOUNT=3
WIDTH=90
[ $MOBILE = yes ] && WIDTH=70
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"
if [ -f /opt/karoshi/server_network/info ]
then
source /opt/karoshi/server_network/info
LOCATION_NAME="- $LOCATION_NAME"
fi
echo '<b>'$MYSERVERSMSG' '$LOCATION_NAME'</b><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
for KAROSHI_SERVER in /opt/karoshi/server_network/servers/*
do
KAROSHISERVER=`basename $KAROSHI_SERVER`
echo '<td style="width: '$WIDTH'px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_network_SERVERNAME_'$KAROSHISERVER'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$KAROSHISERVER'<br><br>'
cat /opt/karoshi/server_network/servers/$KAROSHISERVER/* | sed '/<a href/c'"<br>"
echo '</span></a><br>'$KAROSHISERVER'</td>'
[ $SERVERCOUNTER = $ROWCOUNT ] && echo '</tr><tr>'
let SERVERCOUNTER=$SERVERCOUNTER+1
[ $SERVERCOUNTER -gt $ROWCOUNT ] && SERVERCOUNTER=1
done
echo '</tr></tbody></table><br>'


#Show list of federated servers
if [ -d /opt/karoshi/server_network/federated_ldap_servers/ ]
then
if [ `ls -1 /opt/karoshi/server_network/federated_ldap_servers/ | wc -l` -gt 0 ]
then
for FEDERATED_SERVERS in /opt/karoshi/server_network/federated_ldap_servers/*
do
FEDERATED_SERVER=`basename $FEDERATED_SERVERS`
if [ -f /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/info ]
then
source /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/info
LOCATION_NAME="- $LOCATION_NAME"
fi
echo '<b>'$FEDERATEDSERVERSMSG' '$LOCATION_NAME'</b><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
echo '<td style="width: '$WIDTH'px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_federated_SERVERNAME_'$FEDERATED_SERVER'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$FEDERATED_SERVER'<br><br>'
cat /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/servers/$FEDERATED_SERVER/* | sed '/<a href/c'"<br>"
echo '</span></a><br>'$FEDERATED_SERVER'</td>'

SERVERCOUNTER2=2
for FEDERATED_SLAVE_SERVERS in /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/servers/*
do
FEDERATED_SLAVE_SERVER=`basename $FEDERATED_SLAVE_SERVERS`
if [ $FEDERATED_SLAVE_SERVER != $FEDERATED_SERVER ]
then
echo '<td style="width: '$WIDTH'px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_federatedslave_SERVERMASTER_'$FEDERATED_SERVER'_SERVERNAME_'$FEDERATED_SLAVE_SERVER'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$FEDERATED_SLAVE_SERVER'<br><br>'
cat /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/servers/$FEDERATED_SLAVE_SERVER/* | sed '/<a href/c'"<br>"
echo '</span></a><br>'$FEDERATED_SLAVE_SERVER'</td>'
[ $SERVERCOUNTER2 = $ROWCOUNT ] && echo '</tr><tr>'
let SERVERCOUNTER2=$SERVERCOUNTER2+1
[ $SERVERCOUNTER2 -gt $ROWCOUNT ] && SERVERCOUNTER2=1
fi
done
echo '</tr></tbody></table><br>'
let SERVERLISTCOUNT=$SERVERLISTCOUNT+1
done
fi
fi

echo '</div></form></body></html>'
exit
