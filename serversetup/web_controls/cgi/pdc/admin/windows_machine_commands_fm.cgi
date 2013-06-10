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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/windows_machine_commands ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/windows_machine_commands
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
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
DIV_ID=menubox
fi
echo '<form action="/cgi-bin/admin/windows_machine_commands.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE'</b></a></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td></tr></tbody></table>'
else
echo '<b>'$TITLE'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a><br><br>'
fi

echo '
  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr>
         <td style="width: 180px;">'$COMMANDMSG'</td>
        <td>
        <select name="_COMMAND_" style="width: 200px;">
        <option></option>
	<option value="shutdown">'$SHUTDOWNMSG'</option>
        <option value="restart">'$RESTARTMSG'</option>
	<option value="abortshutdown">'$ABORTSHUTDOWNMSG'</option>
	<option value="startservice">'$STARTSERVICEMSG'</option>
	<option value="stopservice">'$STOPSERVICEMSG'</option>
	<option value="servicestatus">'$SERVICESTATUSMSG'</option>'
#	<option value="showprinters">'$SHOWPRINTERSMSG'</option>
echo	'<option value="showshares">'$SHOWSHARESMSG'</option>
	<option value="showfiles">'$SHOWFILESMSG'</option>
	</select></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG4'</span></a>
      </td></tr>
      <tr>
        <td>'$EXTRAOPTIONSMSG'</td>
        <td><input tabindex= "5" name="_OPTIONS_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG5'</span></a>
      </td>
      </tr>
    </tbody>
  </table><br>'

#Show list of enabled servers
SERVERLISTARRAY=( `ls -1 /opt/karoshi/server_network/windows_servers/` )
SERVERLISTCOUNT=${#SERVERLISTARRAY[@]}
SERVERCOUNTER=0
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_'$KAROSHISERVER'_" type="image" class="images" src="'$SERVERICON'" value="_SERVER_'$KAROSHISERVER'_"><span>'$KAROSHISERVER'</span></a><br>'$KAROSHISERVER'</td>'
[ $SERVERCOUNTER = 5 ] && echo '</tr><tr>'
let SERVERCOUNTER=$SERVERCOUNTER+1
done
echo '</tr><tr><td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_allservers_" type="image" class="images" src="'$SERVERICON2'" value="_SERVER_allservers_"><span>'$ALLSERVERMSG'</span></a><br>'$ALLSERVERMSG'</td>'
echo '</tr></tbody></table></div></form></body></html>'

exit
