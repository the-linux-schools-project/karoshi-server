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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_add ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_add
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
 <script type="text/javascript">
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
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td style="vertical-align: top; width: 110px;"><b>'"$TITLE"'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td>
<td style="vertical-align: top;">
<a href="/cgi-bin/admin/mon_status.cgi"><input class="button" type="button" name="" value="'$NETWORKSTATUSMSG'"></a>
</td>
<td style="vertical-align: top;">
<a href="/cgi-bin/admin/monitors_view.cgi"><input class="button" type="button" name="" value="'$VIEWMONITORSMSG'"></a>
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
#Dansguardian
DANSGUARDIAN=""
[ `grep -c "service dansguardian" /opt/karoshi/server_network/mon/$MONFOLDER/$MONITOR` -gt 0 ] && DANSGUARDIAN='checked="checked"'
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
fi

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$GRPMSG'</td>
        <td>'

if [ $EDITMODE = no ]
then
echo '<input tabindex="1" name="_GROUPNAME_" value="'$MONITOR'" size="20" type="text" style="width: 300px;">'
else
echo '<b>'$MONITOR'</b>'
echo '<input name="_GROUPNAME_" value="'$MONITOR'" type="hidden">'
fi
echo '</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a>
      </td>
      </tr>

<tr>
        <td>
'$ALTERAFTERMSG'</td>
        <td><input tabindex="2" name="_ALERTAFTER_" value="'$ALERTAFTER'" maxlength="1" size="1" type="text" style="width: 80px;"></td>
        <td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG9'</span></a>
      </td>
      </tr>
      <tr>
        <td>
'$MONINTMSG'</td>
        <td><input tabindex="2" name="_INTERVAL_" value="'$INTERVAL'" maxlength="2" size="2" type="text" style="width: 80px;"></td>
        <td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG4'</span></a>
      </td>
      </tr>

<tr><td>'$DAYMSG'</td><td>
<select name="_DAYSTART_" style="width: 80px;">
<option value=""></option>
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
<option value=""></option>
<option>Mon</option>
<option>Tue</option>
<option>Wed</option>
<option>Thu</option>
<option>Fri</option>
<option>Sat</option>
<option>Sun</option>
</select>
</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG7'</span></a></td></tr>

<tr><td>'$TIMEMSG'</td><td>
<select name="_HOURSTART_" style="width: 80px;">
<option value=""></option>
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
<option value=""></option>
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
</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG8'</span></a></td></tr>
<tr><td>'$TCPIPMSG'</td><td><input tabindex="2" name="_TCPIP_" value="'$TCPIPS'" type="text" style="width: 300px;"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a></td></tr></tbody></table>
<br><br><b>'$SERVICESMSG'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG5'</span></a><br><br>
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;"><input type="checkbox" name="_MONITORTYPES_" '$PING' value="ping"> ping <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG6'</span></a>
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
<input type="checkbox" name="_MONITORTYPES_" '$DANSGUARDIAN' value="dansguardian"> dansguardian
</td>
<td>
<input type="checkbox" name="_MONITORTYPES_" '$DNS' value="dns"> dns
</td>
</tr>
</tbody></table><br>
  <input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"> <input type="button" class="button" onclick="SetAllCheckBoxes('\'selectmonitors\'', '\'_MONITORTYPES_\'', true);" value="'$SELECTMSG'">
'
else
echo $ERRORMSG6
fi
echo '</form></div></div></body></html>'
exit

