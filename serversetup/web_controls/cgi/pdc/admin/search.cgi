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
########################
#Required input variables
########################
#  _SEARCH_
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER "] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server
############################
#Show page
############################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=$(cat | tr -cd 'A-Za-z0-9\%._:\-+')
#########################
#Assign data to variables
#########################
END_POINT=3
#Assign SEARCH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SEARCHcheck ]
	then
		let COUNTER=$COUNTER+1
		SEARCH=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Search Karoshi Web Management"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi

#########################
#Check data
#########################

#Sort out spaces
SEARCH=$(echo "$SEARCH" | sed 's/+/ /g')

echo '<div id="actionbox3"><div id="titlebox">'

echo '<table class="standard" style="text-align: left;" >
<tr><td style="vertical-align: top;"><div class="sectiontitle">'$"Search"' '$"Web Management"' - '"$SEARCH"'</div></td></tr></tbody></table><br>
</div><div id="infobox">'

#Check to see that SEARCH is not blank
if [ -z "$SEARCH" ]
then
	echo $"No results found.""</div></div></div></body></html>"
	exit
fi

#make sure that the search criteria has at least three spaces
if [ "${#SEARCH}" -le 2 ]
then
	echo $"Enter in more that two characters to search.""</div></div></div></body></html>"
	exit
fi

COUNTER=1
WIDTH=100
ICON1="/images/search.png"


for SEARCHRESULT in $(/opt/karoshi/web_controls/generate_navbar_admin | grep "href=" | grep -i \"*"$SEARCH" | grep -v 'class="mid"' | grep -v singletext | grep -v 'class="top"' | sed 's% %SPACE%g')
do 
	URL=$(echo "$SEARCHRESULT" | cut -d= -f2 | cut -d'"' -f2)
	TITLE=$(echo "$SEARCHRESULT" | cut -d">" -f3 | cut -d"<" -f1 | sed 's%SPACE% %g')
	#Try and get some help info for the page
	HELPINFO=$(echo "$SEARCHRESULT" | cut -s -d"!" -f2 | sed 's%SPACE% %g' | sed 's%--%%g' | sed 's%>%%g')

	echo '<b><a href="'"$URL"'">'"$TITLE"'</a></b><p class="search-result">'"https://$HTTP_HOST/$URL"'</p>'
	[ ! -z "$HELPINFO" ] && echo ''"$HELPINFO"''

	echo '<br><br>'
done
echo '</div></div></div></body></html>'
exit


