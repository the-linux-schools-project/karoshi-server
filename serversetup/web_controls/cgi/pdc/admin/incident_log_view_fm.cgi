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
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"View Incident Logs"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/system/add.png

echo '<form action="/cgi-bin/admin/incident_log_view.cgi" name="selectedsites" method="post">
<div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"View Incident Logs"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Record_Incident"><img class="images" alt="" src="/images/help/info.png"><span>'$"View the incident logs for a user."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" formaction="incident_log_add.cgi" name="_ViewIncidentLogs_" value="_">
			<img src="'"$ICON1"'" alt="'$"Add Incident Log"'">
			<span>'$"Add Incident Log"'</span><br>
			'$"Add"'
		</button>
	</td>
</tr></tbody></table>
<br>
<table class="standard" style="text-align: left;" >
<tbody>
<tr><td style="width: 180px;">'$"Filter"'</td><td>
<select name="_ALPHABET_" style="width: 200px;">
<option>A</option>
<option>B</option>
<option>C</option>
<option>D</option>
<option>E</option>
<option>F</option>
<option>G</option>
<option>H</option>
<option>I</option>
<option>K</option>
<option>K</option>
<option>L</option>
<option>M</option>
<option>N</option>
<option>O</option>
<option>P</option>
<option>Q</option>
<option>R</option>
<option>S</option>
<option>T</option>
<option>U</option>
<option>V</option>
<option>W</option>
<option>X</option>
<option>Y</option>
<option>Z</option>
<option selected="selected" value="ALL">'$"All"'</option>
</select>
</td></tr></tbody></table>
<br>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div>
</form>
</div>
</div></body>
</html>
'
exit
