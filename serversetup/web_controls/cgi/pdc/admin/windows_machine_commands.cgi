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
########################
#Required input variables
########################
# _SERVER_
# _COMMAND_
# _OPTIONS_
##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/windows_machine_commands ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/windows_machine_commands
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\+%-'`
#########################
#Assign data to variables
#########################
END_POINT=15
#Assign SERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERcheck ]
then
let COUNTER=$COUNTER+1
SERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign COMMAND
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = COMMANDcheck ]
then
let COUNTER=$COUNTER+1
COMMAND=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign OPTIONS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = OPTIONScheck ]
then
let COUNTER=$COUNTER+1
OPTIONS=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/windows_machine_commands_fm.cgi";'
echo '</script>'
echo "</body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi
#########################
#Check data
#########################
#Check to see that server is not blank
if [ $SERVER'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that the command is not blank
if [ $COMMAND'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

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
echo '<div id="'$DIV_ID'">'


[ $COMMAND = startservice ] && COMMAND2=$STARTSERVICEMSG
[ $COMMAND = stopservice ] && COMMAND2=$STOPSERVICEMSG
[ $COMMAND = servicestatus ] && COMMAND2=$SERVICESTATUSMSG
[ $COMMAND = shutdown ] && COMMAND2=$SHUTDOWNMSG
[ $COMMAND = restart ] && COMMAND2=$RESTARTMSG
[ $COMMAND = abortshutdown ] && COMMAND2=$ABORTSHUTDOWNMSG
[ $COMMAND = showprinters ] && COMMAND2=$SHOWPRINTERSMSG
[ $COMMAND = showshares ] && COMMAND2=$SHOWSHARESMSG
[ $COMMAND = showfiles ] && COMMAND2=$SHOWFILESMSG

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE' - '$COMMAND2' '$TCPIP'</b></a></td></tr></tbody></table>'
else
echo '<b>'$TITLE' - '$COMMAND2' '$TCPIP'</b><br><br>'
fi
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/windows_machine_commands.cgi | cut -d' ' -f1`
#Run command
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVER:$COMMAND:$OPTIONS:" | sudo -H /opt/karoshi/web_controls/exec/windows_machine_commands
EXEC_STATUS=`echo $?`

if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
fi

exit
