#!/bin/bash
#Change password
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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Warning Messages"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/js/jquery.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	1: { sorter: false}
    		}
		});
    }
);
</script>

<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

echo '</head><body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><div class="sectiontitle">'$"Warning Messages"'</div>'

#Show warning messages
#Check for any web management warnings
if [ -f /opt/karoshi/web_controls/warnings/summary.txt ]
then
	echo '<table id="myTable" class="tablesorter" style="text-align: left;" ><thead><tr><th style="width: 450px;"><b>'$"Description"'</b></th><th><b>Check</b></th></tr></thead><tbody>'
	for WARNING_FILE in `ls /opt/karoshi/web_controls/warnings/raw_messages/`
	do
		DATA=`cat /opt/karoshi/web_controls/warnings/raw_messages/"$WARNING_FILE"`
		LINK=`echo "$DATA" | cut -d"," -f1`
		DESCRIPTION=`echo "$DATA" | cut -d"," -f2`
		echo '<tr><td>'$DESCRIPTION'</td><td>
		<form name="checkservers" action="'$LINK'" method="get">
		<button class="button" name="Check" value="_">
		'$"Check"'
		</button>
		</form>
		</td></tr>'
	done
	echo '<tr><td>'$"Clear all warning messages"'</td><td>
	<form name="ClearMessages" action="clear_warnings_fm.cgi" method="post">
	<button class="button" name="ClearMessages" value="_">
	'$"Clear all"'
	</button>
	</form>
	</td></tr></tbody></table>'
else
	echo $"There are no warning messages."
fi

echo '</div></div></body></html>'


########################
#Unique key
########################
#+NfSlIeXzogrDRf0Q7W5LJPRH
