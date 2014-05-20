#!/bin/bash
#Copyright (C) 2014  Paul Sharrad

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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

############################
#Language
############################
SHUTDOWN_CODE=`echo ${RANDOM:0:3}`
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitorix ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitorix
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
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script type="text/javascript" src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
		***********************************************/
	</script>
	<script type="text/javascript">
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head><body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
TABLECLASS=standard
WIDTH=180
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
WIDTH=160
fi

echo '<form action="/cgi-bin/admin/monitorix.cgi" name="selectservers" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$SYSMENUMSG'</a>
</div></div><div id="mobileactionbox">'
else
echo '<div class="sectiontitle">'$TITLE'</div><br></div><div id="infobox">'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: '$WIDTH'px;">'$INTERVALMSG'</td>
        <td style="vertical-align: top; text-align: left;">

<select name="____INTERVAL____">
<option value="D">'$DAILYMSG'</option>
<option value="W">'$WEEKLYMSG'</option>
<option value="M">'$MONTHLYMSG'</option>
<option value="Y">'$YEARLYMSG'</option>
</select>
</td></tr>
<tr><td>'$GRAPHMSG'</td><td>
<select name="____GRAPHTYPE____" size="1">
            <option value="all">All graphs</option>
            <optgroup label="System load average and usage">
              <option value="_system1">System load</option>
              <option value="_system2">Active processes</option>
              <option value="_system3">Memory allocation</option>
            </optgroup>
            <optgroup label="Global kernel usage">
              <option value="_kern1">Kernel usage</option>
              <option value="_kern2">Context switches and forks</option>
              <option value="_kern3">VFS usage</option>
            </optgroup>
            <optgroup label="Kernel usage per processor">
              <option value="_proc0">Processor 0</option>
              <option value="_proc1">Processor 1</option>
              <option value="_proc2">Processor 2</option>
              <option value="_proc3">Processor 3</option>
            <optgroup label="Filesystem usage and I/O activity">
              <option value="_fs01">Filesystems usage</option>
              <option value="_fs02">Disk I/O activity</option>
              <option value="_fs03">Inode usage</option>
              <option value="_fs04">Time spent in I/O activity</option>
            <optgroup label="Network traffic and usage">
              <option value="_net01">eth0 Network traffic</option>
              <option value="_net02">eth0 Network packets</option>
              <option value="_net03">eth0 Network errors</option>
            <optgroup label="Netstat statistics">
              <option value="_netstat1">IPv4 states</option>
              <option value="_netstat2">IPv6 states</option>
              <option value="_netstat3">Active close</option>
              <option value="_netstat4">Passive close</option>
              <option value="_netstat5">UDP statistics</option>
            </optgroup>
            <optgroup label="System services demand">
              <option value="_serv1">System services demand</option>
              <option value="_serv2">IMAP and POP3 services</option>
              <option value="_serv3">SMTP service</option>
            </optgroup>
            <optgroup label="Network port traffic">
              <option value="_port0">Port 25 (IN-SMTP)</option>
              <option value="_port1">Port 21 (IN-FTP)</option>
              <option value="_port2">Port 80 (IN-HTTP)</option>
              <option value="_port3">Port 22 (IN-SSH)</option>
              <option value="_port4">Port 110 (IN-POP3)</option>
              <option value="_port5">Port 139 (IN-NETBIOS)</option>
              <option value="_port6">Port 3306 (IN-MYSQL)</option>
              <option value="_port7">Port 53 (IN-DNS)</option>
              <option value="_port8">Port 143 (IN-IMAP)</option>
            <optgroup label="Users using the system">
              <option value="_user1">Users logged in</option>
              <option value="_user2">Samba users</option>
              <option value="_user3">Netatalk users</option>
            </optgroup>
            <optgroup label="Devices interrupt activity">
              <option value="_int1">Interrupt activity</option>
              <option value="_int2">Core activity</option>
              <option value="_int3">Interrupt activity</option>
            </optgroup>
          </select>
</td></tr>
</tbody></table><br>
'

#Show list of servers
/opt/karoshi/web_controls/show_servers $MOBILE servers "$ACTIONMSG" no no ____

[ $MOBILE = no ] && echo '</div>'

echo '</div></form></div></body></html>'
exit
