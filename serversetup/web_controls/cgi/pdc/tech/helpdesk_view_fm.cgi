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
  <title>'$"Technical Support"' - '$"Requests"'</title><META HTTP-EQUIV="refresh" CONTENT="300">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
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

#Detect mobile browser
MOBILE=no
[ `echo $HTTP_USER_AGENT | grep -c Mobile` -gt 0 ] && MOBILE=yes

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	/opt/karoshi/web_controls/generate_navbar_admin_mobile
fi

echo '<div id="'$DIV_ID'"><form action="/cgi-bin/admin/helpdesk_view_fm.cgi" method="post">'


#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<table class="standard" style="text-align: left;" >
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"'"></a></td>
<td style="vertical-align: middle;"><b>'$"Technical Support"' - '$"Requests"'</b></td>
<td style="vertical-align: middle;">
<button class="info" name="_ViewAssigned_" value="_SEARCHCRITERIA_ASSIGNED_">
<img src="/images/submenus/user/helpdesk/staff.png" alt="'$"All"'">
<span>'$"All"'</span>
</button>
</form></td>
</tr></tbody></table><br>'
else
	echo '<b>'$"Technical Support"' - '$"Requests"'</b> <a class="info" href="javascript:void(0)"><input name="_SEARCHCRITERIA_ASSIGNED_" type="image" class="images" src="/images/submenus/user/helpdesk/staff.png" value="_SEARCHCRITERIA_ASSIGNED_"><span>All</span></a></form>'
fi

[ -z "$SEARCHCRITERIA" ] && SEARCHCRITERIA=ASSIGNED

#Reload the page every 3 minutes
echo '
<form id="refresh_form" action="/cgi-bin/admin/helpdesk_view_fm.cgi" method="post">
 <input type="hidden" name="_SEARCHCRITERIA_'$SEARCHCRITERIA'_" value="_SEARCHCRITERIA_'$SEARCHCRITERIA'_"> 
</form>
<script>
setTimeout(function(){
document.getElementById("refresh_form").submit();
}, 180000);
</script>
'

#Check to see if there are any new jobs
if [ ! -d /opt/karoshi/server_network/helpdesk/todo/ ]
then
	echo $"There are no new requests to view."'</div></form></div></body></html>'
	exit
fi

if [ `ls -1 /opt/karoshi/server_network/helpdesk/todo/ | wc -l` = 0 ]
then
	echo $"There are no new requests to view."'</div></form></div></body></html>'
	exit
fi

echo '<table class="standard" style="text-align: left;" >
<tbody><tr><td style="width: 90px;"><b>Date</b></td><td style="width: 130px;"><b>'$"Name"'</b></td><td style="width: 140px;"><b>'$"Request Summary"'</b></td><td style="width: 120px;"><b>'$"Location"'</b></td><td style="width: 90px;"><b>'$"Wait Time"'</b></td><td style="width: 90px;"><b>'$"Priority"'</b></td><td style="width: 100px;"><b>'$"Assigned to"'</b></td><td style="width: 30px;"></td><td style="width: 60px;"><b>'$"Action"'</b></td></tr>
'
for NEWJOB in `grep -w -l ^$SEARCHCRITERIA /opt/karoshi/server_network/helpdesk/todo/*`
do
	NEWJOB=`basename $NEWJOB`
	NEWJOB=`basename $NEWJOB`
	DATE=`echo $NEWJOB | cut -d"." -f1`
	TIME=`date +%H:%M -d @$DATE`
	DATE=`date +%d-%m-%y -d @$DATE`
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

	ASSIGNED2=$ASSIGNED
	[ -z "$ASSIGNED2" ] && ASSIGNED2=$"Not Assigned"

	echo '<tr><td style="vertical-align: top;">'$DATE'<br>'$TIME'</td><td style="vertical-align: top;">'$NAME'</td><td style="vertical-align: top;">'$JOBTITLE'</td><td style="vertical-align: top;">'$LOCATION'</td><td style="vertical-align: top;">'$WAITTIME'</td><td style="vertical-align: top;">'$PRIORITY'</td><td style="vertical-align: top;">'$ASSIGNED'</td><td>
	<form action="/cgi-bin/admin/helpdesk_view_fm.cgi" method="post">
	<button class="info" name="_ViewAssigned_" value="_SEARCHCRITERIA_ASSIGNED='$ASSIGNED'_">
	<img src="/images/submenus/user/helpdesk/staff.png" alt="'$ASSIGNED2'">
	<span>'$ASSIGNED2'</span>
	</button>
	</form></td><td><form action="/cgi-bin/admin/helpdesk_action_fm.cgi" method="post">
	<button class="info" name="_ViewJob_" value="_JOBNAME_'$NEWJOB'_">
	<img src="/images/submenus/user/helpdesk/action.png" alt="'$ASSIGNED2'">
	<span>'$JOBTITLE'</span>
	</button>
	</form></td></tr>'
done
echo '</tbody></table></div></html>'

exit


