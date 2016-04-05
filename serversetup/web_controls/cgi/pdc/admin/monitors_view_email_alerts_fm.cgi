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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"View E-Mail - SMS Alerts"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
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
</head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
FILE=`echo $DATA | cut -s -d_ -f7`

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox"><table class="standard" style="text-align: left; " ><tbody>
<tr><td style="vertical-align: top;"><b>'$"View E-Mail - SMS Alerts"'</b></td>
<td style="vertical-align: top;">
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Viewing_E-Mail_-_SMS_Alerts"><img class="images" alt="" src="/images/help/info.png"><span>'$"The following accounts will be sent details of any network failures."'</span></a>
</td>
<td style="vertical-align: top;">
	<form action="/cgi-bin/admin/monitors_add_email_alert_fm.cgi" method="post">
		<button class="button" name="_AddEmailAlert_" value="_">
		'$"Add E-Mail Alert"'
		</button>
	</form>
</td>
<td style="vertical-align: top;">
	<form action="/cgi-bin/admin/mon_status.cgi" method="post">
		<button class="button" name="_NetworkStatus_" value="_">
		'$"Network Status"'
		</button>
	</form>
</td>
</tr></tbody></table>
<br>'

SHOWENABLEDLAERTS=no
if [ -d /opt/karoshi/server_network/mon/email_alerts/ ]
then
	if [ `ls -1 /opt/karoshi/server_network/mon/email_alerts/ | wc -l` -gt 0 ]
	then
		SHOWENABLEDLAERTS=yes
	fi
fi

SHOWDISABLEDLAERTS=no
if [ -d /opt/karoshi/server_network/mon/email_alerts_disabled/ ]
then
	if [ `ls -1 /opt/karoshi/server_network/mon/email_alerts_disabled/ | wc -l` -gt 0 ]
	then
		SHOWDISABLEDLAERTS=yes
	fi
fi


if [ $SHOWENABLEDLAERTS = yes ] && [ $SHOWDISABLEDLAERTS = yes ]
then
	echo '<table id="myTable" class="tablesorter" style="text-align: left; " >
    <thead>
<tr><th style="width: 120px;"><b>'$"Contact Name"'</b></th><th style="width: 180px;"><b>'$"E-Mail"'</b></th><th style="width: 180px;"><b>'$"Sender"'</b></th><th style="width: 140px;"><b>'$"E-Mail Server"'</b></th><th style="width: 70px;"><b>'$"Enabled"'</b></th><th style="width: 70px;"><b>'$"Edit"'</b></th><th style="width: 70px;"><b>'$"Delete"'</b></th><th style="width: 70px;"><b>'$"Test"'</b></th></tr></thead><tbody>'
fi


#Enabled alerts

if [ $SHOWENABLEDLAERTS = yes ]
then
	for EMAILALERT in /opt/karoshi/server_network/mon/email_alerts/*
	do
		EMAILALERT=`basename $EMAILALERT`
		source /opt/karoshi/server_network/mon/email_alerts/$EMAILALERT
		echo '<tr><td style="vertical-align: top;">'$EMAILALERT'</td><td style="vertical-align: top;">'$EMAILADDRESS'</td><td style="vertical-align: top;">'$SENDER'</td><td style="vertical-align: top;">'$EMAILSERVER'</td>
		<td>
			<form action="/cgi-bin/admin/monitors_disable_email_alert.cgi" method="post">
				<button class="info" name="_Disable_" value="_NAME_'$EMAILALERT'_">
				<img src="/images/submenus/system/enable_monitor.png" alt="'$"Disable"' '$EMAILALERT'">
				<span>'$"Disable"' '$EMAILALERT'</span>
				</button>
			</form>
		</td>
		<td>
			<form action="/cgi-bin/admin/monitors_add_email_alert_fm.cgi" method="post">
				<button class="info" name="_Edit_" value="_NAME_'$EMAILALERT'_EMAILTO_'$EMAILADDRESS'_EMAILFROM_'$SENDER'_MAILSERVER_'$EMAILSERVER'_">
				<img src="/images/submenus/system/edit.png" alt="'$"Edit"' '$EMAILALERT'">
				<span>'$"Edit"' '$EMAILALERT'</span>
				</button>
			</form>
		</td>
		<td>
			<form action="/cgi-bin/admin/monitors_delete_email_alert.cgi" method="post">
				<button class="info" name="_Delete_" value="_NAME_'$EMAILALERT'_">
				<img src="/images/submenus/system/delete.png" alt="'$"Delete"' '$EMAILALERT'">
				<span>'$"Delete"' '$EMAILALERT'</span>
				</button>
			</form>
		</td>
		<td>
			<form action="/cgi-bin/admin/monitors_test_email_alert.cgi" method="post">
				<button class="info" name="_Test_" value="_NAME_'$EMAILALERT'_">
				<img src="/images/submenus/system/test.png" alt="'$"Test"' '$EMAILALERT'">
				<span>'$"Test"' '$EMAILALERT'</span>
				</button>
			</form>
		</td>
		</tr>'
	done
fi

#Disabled alerts
if [ $SHOWDISABLEDLAERTS = yes ]
then
	for EMAILALERT in /opt/karoshi/server_network/mon/email_alerts_disabled/*
	do
		EMAILALERT=`basename $EMAILALERT`
		source /opt/karoshi/server_network/mon/email_alerts_disabled/$EMAILALERT
		echo '<tr><td style="vertical-align: top;">'$EMAILALERT'</td><td style="vertical-align: top;">'$EMAILADDRESS'</td><td style="vertical-align: top;">'$SENDER'</td><td style="vertical-align: top;">'$EMAILSERVER'</td>
		<td>
		<form action="/cgi-bin/admin/monitors_disable_email_alert.cgi" method="post">
			<button class="info" name="_Enable_" value="_NAME_'$EMAILALERT'_">
			<img src="/images/submenus/system/disable_monitor.png" alt="'$"Enable"' '$EMAILALERT'">
			<span>'$"Enable"' '$EMAILALERT'</span>
			</button>
		</form>
		</td>
		<td>
		<form action="/cgi-bin/admin/monitors_add_email_alert_fm.cgi" method="post">
			<button class="info" name="_Edit_" value="_NAME_'$EMAILALERT'_EMAILTO_'$EMAILADDRESS'_EMAILFROM_'$SENDER'_MAILSERVER_'$EMAILSERVER'_">
			<img src="/images/submenus/system/edit.png" alt="'$"Edit"' '$EMAILALERT'">
			<span>'$"Edit"' '$EMAILALERT'</span>
			</button>
		</form>
		</td>
		<td>
		<form action="/cgi-bin/admin/monitors_delete_email_alert.cgi" method="post">
			<button class="info" name="_Delete_" value="_NAME_'$EMAILALERT'_">
			<img src="/images/submenus/system/delete.png" alt="'$"Delete"' '$EMAILALERT'">
			<span>'$"Delete"' '$EMAILALERT'</span>
			</button>
		</form>
		</td>
		<td>
		<form action="/cgi-bin/admin/monitors_test_email_alert.cgi" method="post">
			<button class="info" name="_Test_" value="_NAME_'$EMAILALERT'_">
			<img src="/images/submenus/system/test.png" alt="'$"Test"' '$EMAILALERT'">
			<span>'$"Test"' '$EMAILALERT'</span>
			</button>
		</form>
		</td>
		</tr>'
	done

fi

if [ $SHOWENABLEDLAERTS = yes ] && [ $SHOWDISABLEDLAERTS = yes ]
then
	echo ' </tbody></table>'
fi
echo '<br><br></div></div></body></html>'
exit
