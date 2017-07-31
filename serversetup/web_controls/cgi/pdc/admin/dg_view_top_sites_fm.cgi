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
DATE_INFO=$(date +%F)
DAY=$(echo "$DATE_INFO" | cut -d- -f3)
MONTH=$(echo "$DATE_INFO" | cut -d- -f2)
YEAR=$(echo "$DATE_INFO" | cut -d- -f1)

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
  <title>'$"Top Sites"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) -->
<link rel="stylesheet" href="/all/calendar2/calendar.css">
<script src="/all/stuHover.js"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/dg_view_top_sites.cgi" name="testform" method="post">
  <div id="actionbox"><div id="titlebox"><div class="sectiontitle">'$"Top Sites"'</div>
  <br>
<table class="standard" style="text-align: left;" >
    <tbody><tr><td style="width: 180px;">'$"Log Date"'</td><td>'
echo "<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$DAY-$MONTH-$YEAR\" size=14 maxlength=10 name=\"_DATE_\"></td><td style=\"vertical-align: top; text-align: center;\">
	<script>
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script></td></tr>"


echo '</tbody></table>
<br><br>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></div></form></div></body></html>
'
exit
