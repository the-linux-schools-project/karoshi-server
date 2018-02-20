#!/bin/bash
#Copyright (C) 2010  Paul Sharrad

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
########################
#Required input variables
########################
# _SERVER_
# _COMMAND_
# _OPTIONS_
##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Windows Commands"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\+%-')
#########################
#Assign data to variables
#########################
END_POINT=15
function get_data {
COUNTER=2
DATAENTRY=""
while [[ $COUNTER -le $END_POINT ]]
do
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [[ "$DATAHEADER" = "$DATANAME" ]]
	then
		let COUNTER="$COUNTER"+1
		DATAENTRY=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
		break
	fi
	let COUNTER=$COUNTER+1
done
}

#Assign SERVER
DATANAME=SERVER
get_data
SERVER="$DATAENTRY"

#Assign COMMAND
DATANAME=COMMAND
get_data
COMMAND="$DATAENTRY"


#Assign OPTIONS
DATANAME=OPTIONS
get_data
OPTIONS="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'");'
echo 'window.location = "/cgi-bin/admin/windows_machine_commands_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [[ $(grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################
#Check to see that server is not blank
if [ -z "$SERVER" ]
then
	MESSAGE=$"The server cannot be blank."
	show_status
fi
#Check to see that the command is not blank
if [ -z "$COMMAND" ]
then
	MESSAGE=$"The command cannot be blank."
	show_status
fi

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=menubox
fi
echo '<div id="'"$DIV_ID"'">'


[ "$COMMAND" = startservice ] && COMMAND2=$"Start service"
[ "$COMMAND" = stopservice ] && COMMAND2=$"Stop service"
[ "$COMMAND" = servicestatus ] && COMMAND2=$"Service status"
[ "$COMMAND" = shutdown ] && COMMAND2=$"Shutdown"
[ "$COMMAND" = restart ] && COMMAND2=$"Restart"
[ "$COMMAND" = abortshutdown ] && COMMAND2=$"Abort shutdown"
[ "$COMMAND" = showprinters ] && COMMAND2=$"Show printers"
[ "$COMMAND" = showshares ] && COMMAND2=$"Show shares"
[ "$COMMAND" = showfiles ] && COMMAND2=$"Show open files"

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<table class="standard" style="text-align: left;">
	<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
	<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Windows Commands"' - '"$COMMAND2"' '"$TCPIP"'</b></a></td></tr></tbody></table>'
else
	echo '<b>'$"Windows Commands"' - '"$COMMAND2"' '"$TCPIP"'</b><br><br>'
fi
Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/windows_machine_commands.cgi | cut -d' ' -f1)
#Run command
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$SERVER:$COMMAND:$OPTIONS:" | sudo -H /opt/karoshi/web_controls/exec/windows_machine_commands
EXEC_STATUS="$?"

if [ "$EXEC_STATUS" = 101 ]
then
	MESSAGE=''$"There was a problem with this action."' '$"Please check the karoshi web administration logs for more details."''
fi

exit
