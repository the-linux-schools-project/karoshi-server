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
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Technical Support"' - '$"Requests"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
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

TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\.%+_:\-'`
#########################
#Assign data to variables
#########################
END_POINT=7

#Assign SEARCHCRITERIA
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SEARCHCRITERIAcheck ]
	then
		let COUNTER=$COUNTER+1
		SEARCHCRITERIA=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3D/=/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox"><b>'$"Technical Support"' - '$"Completed Requests"'</b></div><div id="infobox"><br>'
[ -z "$SEARCHCRITERIA" ] && SEARCHCRITERIA=ASSIGNED
#Check to see if there are any completed jobs
if [ ! -d /opt/karoshi/server_network/helpdesk/completed/ ]
then
	echo $"There are no completed requests to view."'</div></form></div></body></html>'
	exit
fi

if [ `ls -1 /opt/karoshi/server_network/helpdesk/completed/ | wc -l` = 0 ]
then
	echo $"There are no completed requests to view."'</div></form></div></body></html>'
	exit
fi

echo '<table id="myTable" class="tablesorter" style="text-align: left;" >
<thead><tr><th style="width: 100px;"><b>Date</b></th><th style="width: 130px;"><b>'$"Name"'</b></th><th style="width: 140px;"><b>'$"Request Summary"'</b></th><th style="width: 120px;"><b>'$"Location"'</b></th><th style="width: 90px;"><b>'$"Wait Time"'</b></th><th style="width: 90px;"><b>'$"Priority"'</b></th><th style="width: 100px;"><b>'$"Assigned to"'</b></th><th style="width: 30px;"></th><th style="width: 60px;"><b>'$"Action"'</b></th></tr></thead><tbody>
'
for COMPLETED_JOB in `grep -l $SEARCHCRITERIA /opt/karoshi/server_network/helpdesk/completed/*`
do
	COMPLETED_JOB=`basename $COMPLETED_JOB`
	DATE=`echo $COMPLETED_JOB | cut -d"." -f1`
	TIME=`date +%H:%M -d @$DATE`
	DATE=`date +%d-%m-%y -d @$DATE`

	source /opt/karoshi/server_network/helpdesk/completed/$COMPLETED_JOB

	let WAITTIME=($COMPLETEDDATE2-$DATE2)
	if [ $WAITTIME -lt 60 ]
	then
		#Show time in seconds
		if [ $WAITTIME = 1 ]
		then 
			WAITTIME=`echo $WAITTIME $"second"`
		else
			WAITTIME=`echo $WAITTIME $"seconds"`
		fi
	else
		#Convert to minutes
		let WAITTIME=$WAITTIME/60
		if [ $WAITTIME -lt 60 ]
		then
			#Show time in minutes
			if [ $WAITTIME = 1 ]
			then
				WAITTIME=`echo $WAITTIME $"minute"`
			else
				WAITTIME=`echo $WAITTIME $"minutes"`
			fi
		else
			#Convert time to hours
			let WAITTIME=$WAITTIME/60
			if [ $WAITTIME -lt 24 ]
			then
				#Show time in hours
				if [ $WAITTIME = 1 ]
				then
					WAITTIME=`echo $WAITTIME $"hour"`
				else
					WAITTIME=`echo $WAITTIME $"hours"`
				fi
			else
				#Covert time to days
				let WAITTIME=$WAITTIME/24
				if [ $WAITTIME = 1 ]
				then
					WAITTIME=`echo $WAITTIME $"day"`
				else
					WAITTIME=`echo $WAITTIME $"days"`
				fi
			fi
		fi
	fi

	echo '<tr><td style="vertical-align: top;">'$DATE' '$TIME'</td><td style="vertical-align: top;">'$NAME'</td><td style="vertical-align: top;">'$JOBTITLE'</td><td style="vertical-align: top;">'$LOCATION'</td><td style="vertical-align: top;">'$WAITTIME'</td><td style="vertical-align: top;">'$PRIORITY'</td><td style="vertical-align: top;">'$ASSIGNED'</td><td>
	<form action="/cgi-bin/admin/helpdesk_view_completed_fm.cgi" method="post">
	<button class="info" name="_AssignedJob_" value="_SEARCHCRITERIA_'$ASSIGNED'_">
	<img src="/images/submenus/user/helpdesk/staff.png" alt="'$ASSIGNED2'">
	<span>'$ASSIGNED'</span>
	</button>
	</form>
	</td><td>
	<form action="/cgi-bin/admin/helpdesk_action_completed_fm.cgi" method="post">
	<button class="info" name="_ViewUserAssignedJobs_" value="_JOBNAME_'$COMPLETED_JOB'_">
	<img src="/images/submenus/user/helpdesk/action.png" alt="'$JOBTITLE'">
	<span>'$JOBTITLE'</span>
	</button>
	</form>
	</td></tr>'
done
echo '</tbody></table></div></div></div></html>'

exit


