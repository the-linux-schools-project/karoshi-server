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
#  _USERNAME_
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Search E-Mail logs"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><script language="JavaScript" src="/all/calendar2/calendar_eu.js" type="text/javascript"></script>
        <!-- Timestamp input popup (European Format) -->

<link rel="stylesheet" href="/all/calendar2/calendar.css">
</head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%+'`
#########################
#Assign data to variables
#########################
END_POINT=23

#Assign ACT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=$(echo $DATA | cut -s -d'_' -f$COUNTER)
	if [ $DATAHEADER'check' = ACTcheck ]
	then
		let COUNTER=$COUNTER+1
		ACT=$(echo $DATA | cut -s -d'_' -f$COUNTER)
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign DATE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=$(echo $DATA | cut -s -d'_' -f$COUNTER)
	if [ "$DATAHEADER"'check' = DATEcheck ]
	then
		let COUNTER=$COUNTER+1
		DATE=$(echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3A/-/g')
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SEARCH1
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=$(echo $DATA | cut -s -d'_' -f$COUNTER)
	if [ "$DATAHEADER"'check' = SEARCH1check ]
	then
		let COUNTER=$COUNTER+1
		SEARCH1=$(echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%40/@/g')
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SEARCH2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=$(echo $DATA | cut -s -d'_' -f$COUNTER)
	if [ "$DATAHEADER"'check' = SEARCH2check ]
	then
		let COUNTER=$COUNTER+1
		SEARCH2=$(echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%40/@/g')
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SEARCH3
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=$(echo $DATA | cut -s -d'_' -f$COUNTER)
	if [ "$DATAHEADER"'check' = SEARCH3check ]
	then
		let COUNTER=$COUNTER+1
		SEARCH3=$(echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%40/@/g')
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SEARCH4
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=$(echo $DATA | cut -s -d'_' -f$COUNTER)
	if [ "$DATAHEADER"'check' = SEARCH4check ]
	then
		let COUNTER=$COUNTER+1
		SEARCH4=$(echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%40/@/g')
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign HOURS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=$(echo $DATA | cut -s -d'_' -f$COUNTER)
	if [ "$DATAHEADER"'check' = HOURScheck ]
	then
		let COUNTER=$COUNTER+1
		HOURS=$(echo $DATA | cut -s -d'_' -f$COUNTER)
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign MINUTES
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=$(echo $DATA | cut -s -d'_' -f$COUNTER)
	if [ "$DATAHEADER"'check' = MINUTEScheck ]
	then
		let COUNTER=$COUNTER+1
		MINUTES=$(echo $DATA | cut -s -d'_' -f$COUNTER)
		break
	fi
	let COUNTER=$COUNTER+1
done

if [ -z "$DATE" ]
then
	DATE=$(date +%d-%m-%Y)
fi

DAY=$(echo "$DATE" | cut -d"-" -f1)
MONTH=$(echo "$DATE" | cut -d"-" -f2)
YEAR=$(echo "$DATE" | cut -d"-" -f3)

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/email_search_logs_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
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

#Show search criteria

echo '<form name="testform" action="/cgi-bin/admin/email_search_logs.cgi" method="post">
 <input type="hidden" name="_ACT_" value="yes"> 
  <div id="actionbox3"><div id="titlebox">
<div class="sectiontitle">'$"Search E-Mail logs"'</div><br>
<table class="standard" style="text-align: left; " >
<tbody>
<tr><td style="width: 180px;">'$"Date"'</td>
<td>'

echo "
<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$DAY-$MONTH-$YEAR\" style=\"width: 175px\" size=14 maxlength=10 name=\"_DATE_\">
	<script language=\"JavaScript\" type=\"text/javascript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script>"

echo '</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Search_E-Mail_Logs"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the date that you want to search the logs for."'</span></a></td></tr>
<tr><td>'$"Time"'</td><td><select name="_HOURS_" style="width: 60px;">'
if [ ! -z "$HOURS" ]
then
	echo '<option>'$HOURS'</option>
<option class="select-dash" disabled="disabled">---</option>'
fi

echo '<option></option>'

for HOURCHOICE in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
do
	echo "<option>"$HOURCHOICE"</option>"
done

echo '</select> : <select name="_MINUTES_" style="width: 60px;">'

if [ ! -z "$MINUTES" ]
then
	echo '<option>'$MINUTES'</option>
<option class="select-dash" disabled="disabled">---</option>'
fi

echo '<option></option>'

for MINUTECHOICE in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60
do
	echo "<option>"$MINUTECHOICE"</option>"
done

echo '</select></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Search_E-Mail_Logs"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the time that you want to search the logs for."' '$"These can be left blank."'</span></a></td>
</tr>
<tr><td>'$"Search"' 1</td><td><input tabindex= "3" name="_SEARCH1_" value="'$SEARCH1'" size="14" style="width: 200px;" type="text"></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Search_E-Mail_Logs"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the search criteria here."' '$"This could be an email address or message code."'</span></a></td></tr>
<tr><td>'$"Search"' 2</td><td><input tabindex= "4" name="_SEARCH2_" value="'$SEARCH2'" size="14" style="width: 200px;" type="text"></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Search_E-Mail_Logs"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in extra search criteria here."'</span></a></td>
</tr>
<tr><td>'$"Search"' 3</td><td><input tabindex= "4" name="_SEARCH3_" value="'$SEARCH3'" size="14" style="width: 200px;" type="text"></td></tr>
<tr><td>'$"Search"' 4</td><td><input tabindex= "4" name="_SEARCH4_" value="'$SEARCH4'" size="14" style="width: 200px;" type="text"></td></tr>
<tr><td></td><td>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</td>
</tbody></table>
</div><div id="infobox">'

#Show search results
if [ ! -z "$DATE" ] && [ ! -z "$ACT" ]
then
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/email_search_logs.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$DATE:$HOURS:$MINUTES:$SEARCH1:$SEARCH2:$SEARCH3:$SEARCH4:" | sudo -H /opt/karoshi/web_controls/exec/email_search_logs
fi

echo '</form></div></div></body></html>'
exit

