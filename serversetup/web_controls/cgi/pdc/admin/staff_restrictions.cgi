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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Staff Restrictions"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
</head><body><div id="pagecontainer">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/staff_restrictions.cgi";'
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

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/staff_restrictions2.cgi" method="post"><div id="actionbox3"><div id="titlebox"><div class="sectiontitle">'$"Staff Restrictions"'</div><br></div><div id="infobox">'
echo '<table class="standard" style="text-align: left; height: 20px;" >'
echo '<tbody>'
echo '<tr><td style="width: 180px;">'$"Add staff name"'</td><td><input name="_STAFFNAME_" size="25" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the usernames of any members of staff that you do not want to be able to access the staff section of the web management."'</span></a></td></tr>'
echo '</tbody></table><br><input value="Submit" type="submit"></form><br><br><form action="/cgi-bin/admin/staff_restrictions2.cgi" method="post">'

if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
	STAFF_COUNT=$(wc -l < /opt/karoshi/web_controls/staff_restrictions.txt)
else
	STAFF_COUNT=0
fi

ICON1=/images/submenus/file/delete.png

#Show restricted staff list
if [ "$STAFF_COUNT" -gt 0 ]
then
	echo '<table id="myTable" class="tablesorter" style="text-align: left;" ><thead>
	<tr><th style="width: 300px;"><b>'$"Restricted Staff"'</b></th><th style="width: 100px;"><b>Remove</b></th></tr></thead><tbody>'
	COUNTER=1
	while [ "$COUNTER" -le "$STAFF_COUNT" ]
	do
		STAFFNAME=$(sed -n $COUNTER,$COUNTER'p' /opt/karoshi/web_controls/staff_restrictions.txt)
		echo '<tr><td>'"$STAFFNAME"'</td><td>

		<button class="info" name="_DeleteUser_" value="_STAFFNAME_'$STAFFNAME'_DELETE_'$STAFFNAME'_">
			<img src="'"$ICON1"'" alt="'$"Remove"'">
			<span>'$"Remove"' '"$STAFFNAME"'</span><br>
		</button>

		</td></tr>'
		let COUNTER="$COUNTER"+1
	done
	echo '</tbody></table>'
fi

echo '</div></div></form></div></body></html>'
exit
