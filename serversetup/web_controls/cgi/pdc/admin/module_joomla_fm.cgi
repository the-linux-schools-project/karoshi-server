#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

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

source /opt/karoshi/server_network/domain_information/domain_name

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Setup Joomla Website"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'

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
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The server cannot be blank."
	show_status
fi

#Check to see if this module has already been installed on the server
if [ -f /opt/karoshi/server_network/servers/$SERVERNAME/joomlaserver ]
then
	STATUSMSG=$"This module has already been set up on this server."
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form id="form1" name="combobox" action="/cgi-bin/admin/module_joomla.cgi" method="post"><div id="actionbox">
<table class="standard" style="text-align: left;" ><tr><td style="vertical-align: top;"><div class="sectiontitle">'$"Setup Joomla Website"' - '$SERVERNAME'</div></td><td style="vertical-align: top;">
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Joomla"><img class="images" alt="" src="/images/help/info.png"><span>'$"You will need to choose an alias for this server for web access. Either enter in a custom alias or choose one from the dropdown list."'</span></a>
</td></tr></tbody></table><br>

<br><input name="_SERVERNAME_" value="'$SERVERNAME'" type="hidden">
<b>'$"Description"'</b><br><br>
'$"This will setup the Joomla content management system as a website for your school."' '$"if you would like all staff to be able to log in and add information to the website enable the ldap authentication module in the Plug in Manager section."'<br><br>'

if [ ! -z "$STATUSMSG" ]
then
	echo ''$STATUSMSG'<br><br>'
fi

echo '<b>'$"Parameters"'</b><br><br>
  <table class="standard" style="text-align: left;">
    <tbody>
<tr><td style="width: 180px;">'$"Web Domain"'</td><td>'

echo '<input type="text" name="_ALIAS_" style="width: 200px;" value="" size="10"></td><td>.'$REALM'</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Joomla"><img class="images" alt="" src="/images/help/info.png"><span>'$"You will need to choose an alias for this server for web access. Either enter in a custom alias or choose one from the dropdown list."'</span></a></td></tr>
<tr><td></td><td><select name="_ALIASLIST_" style="width: 200px;" size="1" onchange="document.combobox._ALIAS_.value = document.combobox._ALIASLIST_.options[document.combobox._ALIASLIST_.selectedIndex].value;document.combobox._ALIASLIST_.value=&#39;&#39;">
<option label="selected" value="" selected="selected"></option>'
            
#Show alias choice

if [ -f /opt/karoshi/server_network/aliases/$SERVERNAME ]
then
#Show any custom aliases that have been assigned
echo '<option style="color:black ; font-weight:bold" value="">'$"Assigned Aliases"'</option>'
for CUSTOM_ALIAS in `cat /opt/karoshi/server_network/aliases/$SERVERNAME`
do
echo '<option style="color:green">'$CUSTOM_ALIAS'</option>'
done
echo '<option style="color:black ; font-weight:bold" value="">'$"Unassigned Aliases"'</option>'
fi

#Get a set of available aliases to check

#Check www.realm
[ `nslookup www.$REALM 127.0.0.1 | grep -c ^Name:` = 0 ] && echo '<option>www</option>'
COUNTER=1
while [ $COUNTER -le 10 ]
do
[ `nslookup www$COUNTER.$REALM 127.0.0.1 | grep -c ^Name:` = 0 ] && echo '<option>www'$COUNTER'</option>'
let COUNTER=$COUNTER+1
done
echo '</select></td><td></td><td></td></tr>
</tbody></table><br><br></div><div id="submitbox"><input value="'$"Submit"'" class="button" type="submit"></div></form></div></body></html>'
exit

