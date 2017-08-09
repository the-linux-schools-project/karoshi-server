#!/bin/bash
#Copyright (C) 2015  Paul Sharrad

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

[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
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
  <title>'$"Configure Backup"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script language="JavaScript" src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) -->'

echo '<link rel="stylesheet" href="/all/calendar2/calendar.css">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/backup_configure.cgi" name="testform" method="post">
  <div id="actionbox3"><div id="titlebox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Configure Backup"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Configure_Backup"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the server that you want to configure the backup for."'</span></a></td></tr></tbody></table></div><div id="infobox">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi"'
echo '</script>'
echo "</div></body></html>"
exit
}

#Check to see that a backup server has been configured
if [ ! -d /opt/karoshi/server_network/backup_servers/backup_settings ]
then
	MESSAGE=$"No karoshi backup servers have been enabled."
	show_status
fi

if [[ $(ls -1 /opt/karoshi/server_network/backup_servers/backup_settings | wc -l) = 0 ]]
then
	MESSAGE=$"No karoshi backup servers have been enabled."
	show_status
fi

#Show list of servers
MOBILE=no
/opt/karoshi/web_controls/show_servers "$MOBILE" backups $"Configure" view notset "____"

echo '</div></div></form></div></body></html>'
exit
