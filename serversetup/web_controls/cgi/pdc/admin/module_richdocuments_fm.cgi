#!/bin/bash
#Copyright (C) 2016 Matthew Jowett
#
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

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

source /opt/karoshi/server_network/domain_information/domain_name
source /opt/karoshi/web_controls/version

#Check if timeout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
	TIMEOUT=86400
fi

############################
#Show page
############################
echo 'Content-type: text/html

<!DOCTYPE html>
<html>

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>'$"Setup richdocuments"'</title>
	<meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
	<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
	<script src="/all/stuHover.js" type="text/javascript"></script>
</head>

<body onLoad="start()">
	<div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`

#########################
#Assign data to variables
#########################
END_POINT=5
#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi"'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Check data
#########################
#Check to see that servername is not blank
if [ $SERVERNAME'null' = null ]
then
	MESSAGE=$"The server cannot be blank."
	show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '
<form id="form1" name="combobox" action="/cgi-bin/admin/module_richdocuments.cgi" method="post">
	<div id="actionbox">
		<table class="standard" style="text-align: left;">
			<tr>
				<td style="vertical-align: top;">
					<div class="sectiontitle">'$"Setup richdocuments"' - '$SERVERNAME'</div>
				</td>
				<td style="vertical-align: top;">
					<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=richdocuments_server"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will setup richdocuments for Owncloud. An ownCloud application which integrates LibreOffice Online."'</span></a>
				</td>
			</tr>
		</table>
		<br>
		<input name="_SERVERNAME_" value="'$SERVERNAME'" type="hidden">
		<b>'$"Description"'</b>
		<br>
		<br>This will setup richdocuments for Owncloud. An Owncloud application which integrates LibreOffice Online.
		<br>LibreOffice Online WebSocket Daemon (loolwsd) and Leaflet platform for LibreOffice On-Line will both be installed and setup.
		<br>
		<br><b>Please note that richdocuments and LibreOffice Online are still early in development.</b>
		<br>richdocuments release: 1.1.4+ (dev)
		<br>LibreOffice Online release: 1.7.2+ (dev)
		<br>Poco C++ release: 1.7.4
		<br>LibreOffice Core: 5.2.1.2+ (dev)
		<br>
		<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=richdocuments_server">
			<br>
		</a>
		<br><b>'$"Parameters"'</b>
		<br>
		<br>
		<table class="standard" style="text-align: left; height: 15px;">
		<td style="width: 200px;">'$"LibreOffice Online Admin Panel"'</td>
			<tbody>
				<tr>
					<td>'$"Admin Panel Password"'</td>
					<td>
						<input type="password" name="_ADMINPASS1_" style="width: 200px;" size="20">
					</td>
					<td>'$"Confirm Password"'</td>
					<td>
						<input type="password" name="_ADMINPASS2_" style="width: 200px;" size="20">
					</td>
					<td>
						<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=richdocuments_server"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will be the password to access the LibreOffice Online admin panel."'</span></a>
					</td>
				</tr>
			</tbody>
		</table>
		<br>
		<br>
	</div>
	<div id="submitbox">
		<input value="'$" Submit "'" class="button" type="submit">
	</div>
</form>
</div>
</body>

</html>'

exit
