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

MOBILE=no

#Language
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

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/update_servers_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`


echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Configure NTP"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script>
<!--
function SetAllCheckBoxes(FormName, FieldName, CheckValue)
{
	if(!document.forms[FormName])
		return;
	var objCheckBoxes = document.forms[FormName].elements[FieldName];
	if(!objCheckBoxes)
		return;
	var countCheckBoxes = objCheckBoxes.length;
	if(!countCheckBoxes)
		objCheckBoxes.checked = CheckValue;
	else
		// set the check value for all check boxes
		for(var i = 0; i < countCheckBoxes; i++)
			objCheckBoxes[i].checked = CheckValue;
}
// -->
</script><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
'
echo "</head>"
echo '<body onLoad="start()"><div id="pagecontainer">'
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
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

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

#Get current ntp servers from the main server.
NTPSERVERS=$(grep ^server /etc/ntp.conf | grep -v 127.127.1.0 | sed "s/^server//g" | sed "s/^ //g" | cut -d" " -f1 | sort)
NTPSERVER1=$(echo $NTPSERVERS | cut -d" " -f1)
NTPSERVER2=$(echo $NTPSERVERS | cut -d" " -f2)
NTPSERVER3=$(echo $NTPSERVERS | cut -d" " -f3)
NTPSERVER4=$(echo $NTPSERVERS | cut -d" " -f4)

echo '<form action="/cgi-bin/admin/ntp2.cgi" name="selectservers" method="post"><div id="actionbox3"><div id="titlebox"><div class="sectiontitle">'$"Configure NTP"'</div><br>
<table class="standard" style="text-align: left; height: 50px;" >
<tbody><tr><td style="width: 180px;">'$"NTP Server"' 1</td>
<td><input tabindex= "1" name="_NTPSERVER1_" size="25" type="text" value="'$NTPSERVER1'"></td><td><a class="info" target="_blank" href="http://www.linuxgfx.co.uk/karoshi/documentation/wiki/index.php?title=Configure_NTP"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the NTP server addresses that you want the servers to get the time from."'</span></a>
</td></tr>
<tr><td>'$"NTP Server"' 2</td><td><input required="required" tabindex= "2" name="_NTPSERVER2_" size="25" type="text" value="'$NTPSERVER2'"></td><td></td></tr>
<tr><td>'$"NTP Server"' 3</td><td><input tabindex= "3" name="_NTPSERVER3_" size="25" type="text" value="'$NTPSERVER3'"></td><td></td></tr>
<tr><td>'$"NTP Server"' 4</td><td><input tabindex= "4" name="_NTPSERVER4_" size="25" type="text" value="'$NTPSERVER4'"></td><td></td></tr>
</tbody></table></div><div id="infobox">'

#Show list of servers 
/opt/karoshi/web_controls/show_servers $MOBILE servers $"Set NTP Server" "notset" showtime

[ $MOBILE = no ] && echo '</div>'

echo '</div></form></div></body></html>'

exit
