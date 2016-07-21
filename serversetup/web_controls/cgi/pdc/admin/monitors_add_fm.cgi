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
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Add Monitors"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
 <script>
<!--
function SetAllCheckBoxes(FormName, FieldName, CheckValue)
{
	if(!document.forms[FormName])
		return;
	var objCheckBoxes = document.forms[FormName].elements[FieldName];
	if(!objCheckBoxes)
		return;
	var countCheckBoxes = objCheckBoxes.length;
	if(!countCheckBoxes)
		objCheckBoxes.checked = CheckValue;
	else
		// set the check value for all check boxes
		for(var i = 0; i < countCheckBoxes; i++)
			objCheckBoxes[i].checked = CheckValue;
}
// -->
  </script>
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+'`

#########################
#Assign data to variables
#########################
END_POINT=9

#Assign MONITOR
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = MONITORcheck ]
	then
		let COUNTER=$COUNTER+1
		MONITOR=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign NAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = NAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		NAME=`echo $DATA | cut -s -d'_' -f$COUNTER | cut -d+ -f1`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign TCPIP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = TCPIPcheck ]
	then
		let COUNTER=$COUNTER+1
		TCPIPS=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9.'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">
<table class="standard" style="text-align: left;" ><tbody><tr><td style="vertical-align: top; width: 110px;"><b>'$"Add Monitors"'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Adding_in_Custom_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"You will need to have a monitoring server set up to use this feature. This will allow you to add in extra monitors for your network."'</span></a></td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/mon_status.cgi" method="post">
	<button class="button" name="_NetworkStatus_" value="_">
	'$"Network Status"'
	</button>
</form>
</td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/monitors_view.cgi" method="post">
	<button class="button" name="_ViewMonitors_" value="_">
	'$"View Monitors"'
	</button>
</form>
</td>
</tr></tbody></table><br>
<form action="/cgi-bin/admin/monitors_add.cgi" method="post" name="selectmonitors">'
ALERTAFTER=1
EDITMODE=no
#Check to see if a monitoring server has been setup
if [ -f /opt/karoshi/server_network/monitoringserver ]
then
	if [ `echo $MONITOR'null' | sed 's/ //g'` != null ]
	then
		EDITMODE=yes
		#Get existing monitoring information

		if [ -f /opt/karoshi/server_network/mon/monitors/$MONITOR ]
		then
			MONFOLDER=monitors
		else
			MONFOLDER=monitors_disabled
		fi

		#Show monitor information
		#Ping
		PING=""
		[ `grep -c "service ping" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && PING='checked="checked"'
		#pop3
		POP3=""
		[ `grep -c "service pop3" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && POP3='checked="checked"'
		#pop3s
		POP3S=""
		[ `grep -c "service pop3s" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && POP3S='checked="checked"'
		#imap
		IMAP=""
		[ `grep -c "service imap" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && IMAP='checked="checked"'
		#imaps
		IMAPS=""
		[ `grep -c "service imaps" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && IMAPS='checked="checked"'
		#samba
		SAMBA=""
		[ `grep -c "service samba" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && SAMBA='checked="checked"'
		#http
		HTTP=""
		[ `grep -c "service http" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && HTTP='checked="checked"'
		#https
		HTTPSECURE=""
		[ `grep -c "service https" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && HTTPSECURE='checked="checked"'
		#smtp
		SMTP=""
		[ `grep -c "service smtp" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && SMTP='checked="checked"'
		#cups
		CUPS=""
		[ `grep -c "service cups" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && CUPS='checked="checked"'
		#PROXY
		PROXY=""
		[ `grep -c "service proxy" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && PROXY='checked="checked"'
		#dns
		DNS=""
		[ `grep -c "service dns" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && DNS='checked="checked"'

		#alertafter
		ALERTAFTER=`grep alertafter /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR | sed -n 1,1p | tr -cd 0-9`
		[ -z $ALERTAFTER ] && ALERTAFTER=1

		#Interval
		INTERVAL=`grep interval /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR | sed -n 1,1p | tr -cd 0-9`

		GROUPDATA=`sed -n 4,4p  /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR`
		TCPIPS=`echo $GROUPDATA | cut -d' ' -f3-`
	else
		MONITOR=$NAME
		INTERVAL=5
	fi

	echo '<table class="standard" style="text-align: left;" >
	    <tbody>
	      <tr>
		<td style="width: 180px;">
	'$"Group name"'</td>
		<td>'

	if [ $EDITMODE = no ]
	then
		echo '<input tabindex="1" name="_GROUPNAME_" value="'$MONITOR'" size="20" type="text" style="width: 300px;">'
	else
		echo '<b>'$MONITOR'</b>'
		echo '<input name="_GROUPNAME_" value="'$MONITOR'" type="hidden">'
	fi
	echo '</td><td>
	<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Adding_in_Custom_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"This can be the name of the group of equipment that you want to monitor. Examples: switches, wireless access points."'</span></a>
	      </td>
	      </tr>

	<tr>
		<td>
	'$"Alert after"'</td>
		<td><input tabindex="2" name="_ALERTAFTER_" value="'$ALERTAFTER'" maxlength="1" size="1" type="text" style="width: 80px;"></td>
		<td>
	<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Adding_in_Custom_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"The number of times a failure is detected before sending an alert."'</span></a>
	      </td>
	      </tr>
	      <tr>
		<td>
	'$"Monitor check interval"'</td>
		<td><input tabindex="2" name="_INTERVAL_" value="'$INTERVAL'" maxlength="2" size="2" type="text" style="width: 80px;"></td>
		<td>
	<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Adding_in_Custom_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"The monitoring service will wait this amount of time in minutes between each check for this group."'</span></a>
	      </td>
	      </tr>

	<tr><td>'$"Monitor day interval"'</td><td>
	<select name="_DAYSTART_" style="width: 80px;">
	<option label="blank" value=""></option>
	<option>Mon</option>
	<option>Tue</option>
	<option>Wed</option>
	<option>Thu</option>
	<option>Fri</option>
	<option>Sat</option>
	<option>Sun</option>
	</select>
	 - 
	<select name="_DAYEND_" style="width: 80px;">
	<option label="blank" value=""></option>
	<option>Mon</option>
	<option>Tue</option>
	<option>Wed</option>
	<option>Thu</option>
	<option>Fri</option>
	<option>Sat</option>
	<option>Sun</option>
	</select>
	</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Adding_in_Custom_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"Leave blank for continuous monitoring or add in the start and end days."'</span></a></td></tr>

	<tr><td>'$"Monitor time interval"'</td><td>
	<select name="_HOURSTART_" style="width: 80px;">
	<option label="blank" value=""></option>
	<option>1am</option>
	<option>2am</option>
	<option>3am</option>
	<option>4am</option>
	<option>5am</option>
	<option>6am</option>
	<option>7am</option>
	<option>8am</option>
	<option>9am</option>
	<option>10am</option>
	<option>11am</option>
	<option>12am</option>
	</select>
	 - 
	<select name="_HOUREND_" style="width: 80px;">
	<option label="blank" value=""></option>
	<option>1pm</option>
	<option>2pm</option>
	<option>3pm</option>
	<option>4pm</option>
	<option>5pm</option>
	<option>6pm</option>
	<option>7pm</option>
	<option>8pm</option>
	<option>9pm</option>
	<option>10pm</option>
	<option>11pm</option>
	<option>12pm</option>
	</select>
	</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Adding_in_Custom_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"Leave blank for continuous monitoring or add in the hour start and end times."'</span></a></td></tr>
	<tr><td>'$"TCPIP numbers"'</td><td><input tabindex="2" name="_TCPIP_" value="'$TCPIPS'" type="text" style="width: 300px;"></td><td>
	<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Adding_in_Custom_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"You need to enter in the TCPIP numbers separated by spaces of the devices that you want to monitor."'</span></a></td></tr></tbody></table>
	<br><br><b>'$"Services to monitor"'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Monitor_Server#Adding_in_Custom_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"Pick the services that you want monitored for this group."'</span></a><br><br>
	<table class="standard" style="text-align: left;" ><tbody>
	<tr><td style="width: 180px;"><input type="checkbox" name="_MONITORTYPES_" '$PING' value="ping"> ping <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$"This is the most basic monitor type. Most devices will respond to a ping request."'</span></a>
	</td><td style="width: 200px;"><input type="checkbox" name="_MONITORTYPES_" '$POP3' value="pop3"> pop3
	</td></tr>
	<tr><td>
	<input type="checkbox" name="_MONITORTYPES_" '$POP3S' value="pop3s"> pop3s
	</td><td>
	<input type="checkbox" name="_MONITORTYPES_" '$IMAP' value="imap"> imap
	</td></tr>
	<tr><td>
	<input type="checkbox" name="_MONITORTYPES_" '$IMAPS' value="imaps"> imaps
	</td><td>
	<input type="checkbox" name="_MONITORTYPES_" '$SAMBA' value="samba"> samba
	</td></tr>
	<tr><td>
	<input type="checkbox" name="_MONITORTYPES_" '$HTTP' value="http"> http
	</td><td>
	<input type="checkbox" name="_MONITORTYPES_" '$HTTPSECURE' value="https"> https
	</td></tr>
	<tr><td>
	<input type="checkbox" name="_MONITORTYPES_" '$SMTP' value="smtp"> smtp
	</td>
	<td>
	<input type="checkbox" name="_MONITORTYPES_" '$CUPS' value="cups"> cups
	</td></tr>
	<tr><td>
	<input type="checkbox" name="_MONITORTYPES_" '$PROXY' value="PROXY"> proxy
	</td>
	<td>
	<input type="checkbox" name="_MONITORTYPES_" '$DNS' value="dns"> dns
	</td>
	</tr>
	</tbody></table><br>
	  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"> <input type="button" class="button" onclick="SetAllCheckBoxes('\'selectmonitors\'', '\'_MONITORTYPES_\'', true);" value="'$"Select all"'">
	'
else
	echo $"A monitoring server has not been added to the network."
fi
echo '</form></div></div></body></html>'
exit

