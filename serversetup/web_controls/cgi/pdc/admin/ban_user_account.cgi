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

#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
	TIMEOUT=86400
fi
############################
#Show page
############################
BANLENGTH=7
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Ban User Account"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
if [ ! -z "$DATA" ]
then
	END_POINT=18
	#Assign HOUR
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAENTRY'check'` = HOURcheck ]
		then
			let COUNTER=$COUNTER+1
			HOUR=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign MINUTES
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAENTRY'check'` = MINUTEScheck ]
		then
			let COUNTER=$COUNTER+1
			MINUTES=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign DAY
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAENTRY'check'` = DAYcheck ]
		then
			let COUNTER=$COUNTER+1
			DAY=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign MONTH
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAENTRY'check'` = MONTHcheck ]
		then
			let COUNTER=$COUNTER+1
			MONTH=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign YEAR
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAENTRY'check'` = YEARcheck ]
		then
			let COUNTER=$COUNTER+1
			YEAR=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign INCIDENT
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAENTRY'check'` = INCIDENTcheck ]
		then
			let COUNTER=$COUNTER+1
			INCIDENT=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/2B/ /g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign ACTIONTAKEN
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAENTRY'check'` = ACTIONTAKENcheck ]
		then
			let COUNTER=$COUNTER+1
			ACTIONTAKEN=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/2B/ /g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign STUDENTS
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAENTRY'check'` = STUDENTScheck ]
		then
			let COUNTER=$COUNTER+1
			STUDENTS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/2B/ /g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign BANLENGTH
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAENTRY'check'` = BANLENGTHcheck ]
		then
			let COUNTER=$COUNTER+1
			BANLENGTH=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi
DATE_INFO=`date +%F`
[ -z "$DAY" ] && DAY=`echo $DATE_INFO | cut -d- -f3`
[ -z "$MONTH" ] && MONTH=`echo $DATE_INFO | cut -d- -f2`
[ -z "$YEAR" ] && YEAR=`echo $DATE_INFO | cut -d- -f1`

TIME_INFO=`date +%T`
[ -z "$HOUR" ] && HOUR=`echo $TIME_INFO | cut -d: -f1`
[ -z "$MINUTES" ] && MINUTES=`echo $TIME_INFO | cut -d: -f2`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/ban_user_account.cgi";'
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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
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

echo '<form action="/cgi-bin/admin/ban_user_account2.cgi" method="post">
<div id="actionbox">'

echo '<table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Ban User Account"'</div></td>
<td style="vertical-align: top;">
<button class="button" formaction="/cgi-bin/admin/banned_users_view_fm.cgi" name="ViewBannedUsers" value="_">
'$"View Banned Users"'
</button>
</td>
</tbody></table>

<table class="standard" style="text-align: left; top: 207px; left: 232px; width: 674px; height: 61px;">
<tbody><tr><td>'$"Incident Time and Date"'</td><td>'
#HOUR
echo '<input name="_HOUR_" value="'$HOUR'" size="2" maxlength="2" type="text">:'
echo '<input name="_MINUTES_" value="'$MINUTES'" size="2" maxlength="2" type="text">'
echo '</td><td>'
echo '<input name="_DAY_" value="'$DAY'" size="2" maxlength="2" type="text">'
echo '<input name="_MONTH_" value="'$MONTH'" size="2" maxlength="2" type="text">'
echo '<input name="_YEAR_" value="'$YEAR'" size="4" maxlength="4" type="text">'
echo '</td></tr><tr><td>'$"Ban duration in days - leave blank for a permanent ban."'</td><td>'
echo '<input name="_BANLENGTH_" value="'$BANLENGTH'" size="2" maxlength="3" type="text"> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Acceptable_Use"><img class="images" alt="" src="/images/help/info.png"><span>'$"Users are automatically allowed after their ban duration is up. The ban duration will include weekends and holidays."'</span></a>
'
echo '</td><td></td></tr></tbody></table>'
#Students involved
echo '<br>'$"Please enter the usernames you want to ban from the system separated by spaces:"'<br><br>'
echo '<input value="'$STUDENTS'" name="_STUDENTS_" size="53" type="text">'
#Incident and action taken
echo '<br><br>Incident Report<br>'
echo '<textarea cols="77" rows="4" name="_INCIDENT_">'$INCIDENT'</textarea><br><br>Action Taken<br>'
echo '<textarea cols="77" rows="4" name="_ACTIONTAKEN_">'$"User account banned."'</textarea>'

echo '</div><div id="submitbox"> <input value="Submit" class="button" type="submit"> <input value="Reset" class="button" type="reset"> </div></form></div></body></html>'
exit
