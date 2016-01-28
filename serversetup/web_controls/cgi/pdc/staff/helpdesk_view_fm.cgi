#!/bin/bash
#Copyright (C) 2010  Paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
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
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
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
  <title>'$"Technical Support"' - '$"Requests"'</title>
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
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
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body><div id="pagecontainer">'

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
/opt/karoshi/web_controls/generate_navbar_staff
echo '<div id="actionbox"><b>'$"Technical Support"' - '$"Requests"'</b><br><br>'
[ -z "$SEARCHCRITERIA" ] && SEARCHCRITERIA=ASSIGNED
#Check to see if there are any new jobs
if [ ! -d /opt/karoshi/server_network/helpdesk/todo/ ]
then
	echo $"There are no new requests to view."'</div></form></div></body></html>'
	exit
fi

if [ `grep -w -l 'NAME="'$REMOTE_USER'"' /opt/karoshi/server_network/helpdesk/todo/* | wc -l` = 0 ]
then
	echo $"There are no new requests to view."'</div></form></div></body></html>'
	exit
fi


echo '<table id="myTable" class="tablesorter" style="text-align: left;" >
<thead><tr><th style="width: 140px;"><b>'$"Name"'</b></th><th style="width: 140px;"><b>'$"Request Summary"'</b></th><th style="width: 120px;"><b>'$"Location"'</b></th><th style="width: 100px;"><b>'$"Wait Time"'</b></th><th style="width: 120px;"><b>'$"Assigned to"'</b></th><th style="width: 60px;"><b>'$"Action"'</b></th></tr></thead><tbody>
'
for NEWJOB in `grep -w -l 'NAME="'$REMOTE_USER'"' /opt/karoshi/server_network/helpdesk/todo/*`
do
	NEWJOB=`basename $NEWJOB`
	source /opt/karoshi/server_network/helpdesk/todo/$NEWJOB
	NOW=`date +%s`
	let WAITTIME=($NOW-$DATE2)
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

	echo '<tr><td style="vertical-align: top;">'$NAME'</td><td style="vertical-align: top;">'$JOBTITLE'</td><td style="vertical-align: top;">'$LOCATION'</td><td style="vertical-align: top;">'$WAITTIME'</td><td style="vertical-align: top;">'$ASSIGNED'</td><td><form action="/cgi-bin/staff/helpdesk_action_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="_JOBNAME_'$NEWJOB'_" type="image" class="images" src="/images/submenus/user/helpdesk/action.png" value="_JOBNAME_'$NEWJOB'_"><span>'$JOBTITLE'</span></a></form></td></tr>'
done
echo '</tbody></table></div></html>'

exit


