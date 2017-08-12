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
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Web Management Name"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script></head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
FILE=`echo $DATA | cut -s -d_ -f7`

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
SERVERICON="/images/submenus/system/computer.png"

source /opt/karoshi/server_network/domain_information/domain_name
source /opt/karoshi/web_controls/version

echo '<form action="/cgi-bin/admin/remote_management_name.cgi" method="post"><div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top;"><div class="sectiontitle">'$"Web Management Name"'</div></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will add the name of your institution to the top of the web management and to the show servers page."'</span></a></td></tr></tbody></table><br>

  <table class="standard" style="text-align: left;" >
    <tbody>
<tr><td style="width: 180px;">'$"Site Name"'</td><td><input required="required" tabindex= "1" value="'$LONGNAME'" name="_LONGNAME_" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the site name."'</span></a></td></tr>
<tr><td style="width: 180px;">'$"Short Site Name"'</td><td><input required="required" tabindex= "2" value="'$SHORTNAME'" name="_SHORTNAME_" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the short site name. This will be displayed in the web management."'</span></a></td></tr>
</tbody></table><br><br>'

if [ -f /opt/karoshi/server_network/info ]
then
	source /opt/karoshi/server_network/info
	source /opt/karoshi/web_controls/version
	LOCATION_NAME="- $LOCATION_NAME"
fi

/opt/karoshi/web_controls/show_servers no pdc $"Submit"

#Show list of federated servers
if [ -d /opt/karoshi/server_network/federated_ldap_servers/ ]
then
	if [ `ls -1 /opt/karoshi/server_network/federated_ldap_servers/ | wc -l` -gt 0 ]
	then
		for FEDERATED_SERVERS in /opt/karoshi/server_network/federated_ldap_servers/*
		do
			FEDERATED_SERVER=`basename $FEDERATED_SERVERS`
			LOCATION_NAME=""
			if [ -f /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/info ]
			then
			source /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/info
			LOCATION_NAME="- $LOCATION_NAME"
			fi
			echo '<b>'$"Federated Servers"' '$LOCATION_NAME'</b><table class="standard" style="text-align: left;" ><tbody><tr>'
			echo '<tr><td style="vertical-align: top; text-align: left;">
			<button class="button" name="_SetFedName_" value="_SERVERTYPE_federated_SERVERNAME_'$FEDERATED_SERVER'_">
			'$FEDERATED_SERVER'
			</button>
			</td></tr></tbody></table><br>'
		done
	fi
fi
echo '</div></div></form></div></body></html>
'
exit
