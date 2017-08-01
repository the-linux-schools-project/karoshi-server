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
################################
#Get date for yesterday
################################
EPOCH_TODAY=$(date +%s)
let ONEDAY=60*60*24
let EPOCH_YESTERDAY="$EPOCH_TODAY-$ONEDAY"
LOG_DATE=$(date +%d-%m-%Y -d @"$EPOCH_YESTERDAY")

[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Global Internet Usage"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) -->

<link rel="stylesheet" href="/all/calendar2/calendar.css">
<script src="/all/stuHover.js"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/dg_view_global_usage.cgi" name="testform" method="post"><b></b>
  <div id="actionbox"><div id="titlebox"><div class="sectiontitle">'$"Global Internet Usage"' <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Internet Usage logs are updated at the end of every day."'</span></a>
</div><br>

<table class="standard" style="text-align: left;" >
    <tbody>
'
echo '<tr><td style="width: 180px;">'$"Log Date"'</td><td>'
echo "<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$LOG_DATE\" size=14 maxlength=10 name=\"_DATE_\"></td><td style=\"vertical-align: top;\">
	<script>
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script></td></tr>"



echo '</tbody></table><br>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></div>
</form>
</div></body></html>
'
exit
