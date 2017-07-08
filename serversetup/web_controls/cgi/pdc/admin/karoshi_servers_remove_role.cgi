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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Remove Server Role"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g')
#########################
#Assign data to variables
#########################
END_POINT=21
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

#Assign MODULE
DATANAME=MODULE
get_data
MODULE="${DATAENTRY//UNDERSCORE/_}"

#Assign SERVERNAME
DATANAME=SERVERNAME
get_data
SERVERNAME="${DATAENTRY//UNDERSCORE/_}"

#Assign FORMCODE
DATANAME=FORMCODE
get_data
FORMCODE="${DATAENTRY//UNDERSCORE/_}"

#Assign MODULECODE
DATANAME=MODULECODE
get_data
MODULECODE="${DATAENTRY//UNDERSCORE/_}"

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="${DATAENTRY//UNDERSCORE/_}"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'");'
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi";'
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

if [[ $(grep -c ^"$REMOTE_USER": /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################

if [ -z "$ACTION" ]
then
	ACTION=viewmodules
fi

#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The servername cannot be blank."
	show_status
fi

if [ "$ACTION" = remove ] || [ "$ACTION" = reallyremove ]
then
	#Check to see that MODULE is not blank
	if [ -z "$MODULE" ]
	then
		MESSAGE=$"The module cannot be blank."
		show_status
	fi
fi

if [ "$ACTION" = reallyremove ]
then
	#Check to see that FORMCODE is not blank
	if [ -z "$FORMCODE" ]
	then
		MESSAGE=$"The code cannot be blank."
		show_status
	fi
	if [ -z "$MODULECODE" ]
	then
		MESSAGE=$"The code cannot be blank."
		show_status
	fi

	if [ "$MODULECODE" != "$FORMCODE" ]
	then
		MESSAGE=$"The code did not match."
		show_status
	fi
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

ICON1=/images/warnings/server.png

echo '<div id="actionbox"><div class="sectiontitle">'$"Remove Server Role"' - '"$SERVERNAME"'</div><br><br>'

if [ "$ACTION" = reallyremove ]
then
	MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/karoshi_servers_remove_role.cgi | cut -d' ' -f1)
	#Remove module
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$MODULE:" | sudo -H /opt/karoshi/web_controls/exec/karoshi_servers_remove_role

	echo "<form METHOD=POST ACTION=\"/cgi-bin/admin/karoshi_servers_view.cgi\" target=\"_top\" name = \"frm\">
		</form><script>document.frm.submit();</script><form>"
	exit
fi

function get_role_name {
ROLE_NAME="$ROLE_FILE"
ROLE_NAME_STATUS=notset
CONSEQUENCES=""


case "$ROLE_FILE" in
	apachereverseproxyserver)
	ROLE_NAME=$"Reverse Proxy Server"
	CONSEQUENCES=$"Unflags this server as an Apache reverse proxy server. Disables proxy module and restarts apache."
	ROLE_NAME_STATUS=set
	;;
	distributionserver)
	ROLE_NAME=$"Distribution Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a distribution server."
	;;
	homeaccess)
	ROLE_NAME=$"Home Access Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a Home Access server and removes the Home Access files."
	;;
	apacheserver)
	ROLE_NAME=$"Web Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as an Apache server."
	;;
	backupserver)
	ROLE_NAME=$"Backup Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a backup server. Stops all backups to this server."
	;;
	dhcpserver)
	ROLE_NAME=$"DHCP Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a DHCP server. Stops the dhcp service from running on this server."
	;;
	emailserver)
	ROLE_NAME=$"E-Mail Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as an E-Mail server. Stops Sogo, Postfix, Dovecot, and Mailscanner from running on the server."
	;;
	fileserver)
	if [[ "$SERVERNAME" != $(hostname-fqdn) ]]
	then
		ROLE_NAME=$"File Server"
		ROLE_NAME_STATUS=set
		CONSEQUENCES=$"Unflags this server as a file server. Re-maps any groups using this server back to the main server."
	fi
	;;
	joomlaserver)
	ROLE_NAME=$"Joomla"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server from using joomla. Deletes all joomla files and the joomla database."
	;;
	minidlnaserver)
	ROLE_NAME=$"MiniDLNA Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a MiniDLNA server. Stops MiniDLNA on this server."
	;;
	moodle)
	ROLE_NAME=$"Moodle Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a moodle server. Deletes all moodle files and the moodle database."
	;;
	gitlab)
	ROLE_NAME=$"Gitlab Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a gitlab server. Deletes all gitlab files, repositories and user data."
	;;
	richdocuments)
	ROLE_NAME=$"richdocuments"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Removes the richdocuments plugin for Owncloud and removes the LibreOffice Online Server."
	;;
	ocsserver)
	ROLE_NAME=$"OCS Inventory"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as an OCS server. Deletes all OCS files and the OCS database."
	;;
	printserver)
	ROLE_NAME=$"Print Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a print server. Stops cups on the server."
	;;
	squid)
	ROLE_NAME=$"Squid Internet Proxy"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as an Internet Proxy server. Stops squid and dansguardian from running on the server."
	;;
	monitoring)
	ROLE_NAME=$"Monitor Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a monitor server. Stops mon from running."
	;;
	remote_ssh)
	ROLE_NAME=$"Remote SSH Access"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server for allowing remote access. Firewall rules changed to stop ssh access to this server."
	;;
	radioserver)
	ROLE_NAME=$"Internet Radio Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a radio server. Stops icecast-server from running on the server."
	;;
	radiusserver)
	ROLE_NAME=$"Radius Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a radus server. Stops radius from running on the server."
	;;
	openvpn)
	ROLE_NAME=$"OpenVPN Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as an OpenVPN server. Stops openvpn from running on the server."
	;;
	owncloud)
	ROLE_NAME=$"Owncloud Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as an Owncloud server. Deletes all owncloud files and user data."
	;;
	federated_server)
	ROLE_NAME=$"Federated Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Unflags this server as a federated server. Disables federated password synchronisation. Disables federated file synchronisation. Enables user creation in the webmanagement for this server."
	;;
	REMOVESERVER)
	ROLE_NAME=$"Remove Server"
	ROLE_NAME_STATUS=set
	CONSEQUENCES=$"Removes this server from the system."
	;;
	esac
}

if [ "$ACTION" = remove ]
then
	ROLE_FILE="$MODULE"
	get_role_name
	REMOVE_CODE="${RANDOM:0:3}"
	echo '<br><img alt="Warning" src="/images/warnings/warning.png"> <b>'$"WARNING"'</b> - '$"Removing modules assumes that you have backed up or do not need the data on the module you are removing."'<br><br>
<form action="/cgi-bin/admin/karoshi_servers_remove_role.cgi" method="post">
<input name="___ACTION___" value="reallyremove" type="hidden">
<input name="___FORMCODE___" value="'"$REMOVE_CODE"'" type="hidden">
<input name="___MODULE___" value="'"$MODULE"'" type="hidden">
<input name="___SERVERNAME___" value="'"$SERVERNAME"'" type="hidden">
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top; width: 180px; height: 30px;">'$"Module"'</td><td style="vertical-align: top; text-align: left;  width: 150px;">'"$ROLE_NAME"'</td><td style="vertical-align: top; width: 250px;"></td></tr>
<tr><td style="vertical-align: top;">'$"Information"'</td><td style="vertical-align: top; text-align: left;" colspan="2">'"$CONSEQUENCES"'</td></tr>
<tr><td style="vertical-align: top; height: 30px;">'$"Code"'</td>
<td style="vertical-align: top; text-align: left;"><b>'"$REMOVE_CODE"'</b></td></tr>
<tr><td>'$"Confirm"'</td>
 <td style="vertical-align: top; text-align: left;"><input tabindex= "2" name="___MODULECODE___" maxlength="3" size="4" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the code above to confirm the action that you want to take."'</span></a></td></tr>
</tbody></table><br><br><input value="'$"Submit"'" class="button" type="submit"></form>'

fi

if [ "$ACTION" = viewmodules ]
then
	echo '<br><img alt="Warning" src="/images/warnings/warning.png"> <b>'$"WARNING"'</b> - '$"Removing modules assumes that you have backed up or do not need the data on the module you are removing."'<br><br><br>
<form action="/cgi-bin/admin/karoshi_servers_remove_role.cgi" method="post">
<input name="___ACTION___" value="remove" type="hidden">
<input name="___SERVERNAME___" value="'"$SERVERNAME"'" type="hidden">
<table class="standard" style="text-align: left;" ><tbody>
'

	if [ -d /opt/karoshi/server_network/federated_ldap_servers/"$SERVERNAME" ]
	then
		ROLE_FILE=federated_server
		get_role_name
		if [ "$ROLE_NAME_STATUS" != notset ]
		then
			echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;">'"$ROLE_NAME"'</td><td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><input name="___MODULE___'"$ROLE_FILE"'___" type="image" class="images" src="'$ICON1'" value=""><span>'$CONSEQUENCES'</span></a></td></tr>'
		fi
	else
		for ROLES in /opt/karoshi/server_network/servers/$SERVERNAME/*
		do
			ROLE_FILE=$(basename "$ROLES")
			get_role_name

			if [ "$ROLE_NAME_STATUS" != notset ] && [ "$ROLE_FILE" != 1dc ] && [ "$ROLE_FILE" != 1domainmember ] && [ "$ROLE_FILE" != 2users-groups ]
			then
				echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;"><b>'$ROLE_NAME'</b></td><td style="vertical-align: top; width: 600px;">'"$CONSEQUENCES"'</td><td style="vertical-align: top;">
				<button class="button" name="___RemoveRole___" value="___MODULE___'"$ROLE_FILE"'___">
				'$"Remove"'
				</button>
				</td></tr>'
			fi
		done
	fi

	if [[ "$SERVERNAME" != $(hostname-fqdn) ]] && [ ! -d /opt/karoshi/server_network/federated_ldap_servers/"$SERVERNAME" ]
	then
		echo '<tr><td style="vertical-align: top; width: 180px; height: 40px;"><b>'$"Remove Server"'</b></td><td style="vertical-align: top; width: 600px;"></td><td style="vertical-align: top;">
		<button class="button" name="___RemoveServer___" value="___MODULE___REMOVESERVER__">
		'$"Remove"'
		</button>
		</td></tr>'
	fi
	echo '</tbody></table><br></form>'
fi
echo '</div></div></body></html>'
