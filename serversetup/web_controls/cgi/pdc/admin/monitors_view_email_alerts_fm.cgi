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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_email_alert ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_email_alert
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
  <title>'$TITLE2'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()">'
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

echo '<div id="actionbox"><table class="standard" style="text-align: left; " border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top;"><b>'$TITLE2'</b></td>
<td style="vertical-align: top;">
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_eMail_Alerts"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG7'</span></a>
</td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/monitors_add_email_alert_fm.cgi" method="post">
 <a class="info" href="javascript:void(0)"><input name="_ADDEMAILALERT_" type="image" class="images" src="/images/submenus/system/email_alert_add.png" value=""><span>'$ADDEMAILALERTMSG'</span></a></form></td>
</tr></tbody></table>
<br>'

echo '<table class="standard" style="text-align: left; " border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 120px;"><b>'$CONTACTNAMEMSG'</b></td><td style="width: 180px;"><b>'$EMAILMSG'</b></td><td style="width: 180px;"><b>'$SENDERMSG'</b></td><td style="width: 140px;"><b>'$MAILSERVERMSG'</b></td><td><b>'$ENABLEDMSG'</b></td><td><b>'$EDITTITLE'</b></td><td><b>'$DELETETITLE'</b></td><td><b>'$TESTMSG'</b></td></tr>'

#Enabled alerts
if [ -d /opt/karoshi/server_network/mon/email_alerts/ ]
then
if [ `ls -1 /opt/karoshi/server_network/mon/email_alerts/ | wc -l` -gt 0 ]
then

for EMAILALERT in /opt/karoshi/server_network/mon/email_alerts/*
do
EMAILALERT=`basename $EMAILALERT`
source /opt/karoshi/server_network/mon/email_alerts/$EMAILALERT
echo '<tr><td style="vertical-align: top;">'$EMAILALERT'</td><td style="vertical-align: top;">'$EMAILADDRESS'</td><td style="vertical-align: top;">'$SENDER'</td><td style="vertical-align: top;">'$EMAILSERVER'</td>

<td><form action="/cgi-bin/admin/monitors_disable_email_alert.cgi" method="post">
<a class="info" href="javascript:void(0)"><input name="_NAME_'$EMAILALERT'_" type="image" class="images" src="/images/submenus/system/enable_monitor.png" value=""><span>'$DISABLEMSG' '$EMAILALERT'</span></a></form></td>

<td><form action="/cgi-bin/admin/monitors_add_email_alert_fm.cgi" method="post">
<a class="info" href="javascript:void(0)"><input name="_NAME_'$EMAILALERT'_EMAILTO_'$EMAILADDRESS'_EMAILFROM_'$SENDER'_MAILSERVER_'$EMAILSERVER'_" type="image" class="images" src="/images/submenus/system/edit.png" value=""><span>'$EDITTITLE' '$EMAILALERT'</span></a></form></td>

<td><form action="/cgi-bin/admin/monitors_delete_email_alert.cgi" method="post">
<a class="info" href="javascript:void(0)"><input name="_NAME_'$EMAILALERT'_" type="image" class="images" src="/images/submenus/system/delete.png" value=""><span>'$DELETETITLE' '$EMAILALERT'</span></a></form></td>

<td><form action="/cgi-bin/admin/monitors_test_email_alert.cgi" method="post">
<a class="info" href="javascript:void(0)"><input name="_NAME_'$EMAILALERT'_" type="image" class="images" src="/images/submenus/system/test.png" value=""><span>'$TESTMSG' '$EMAILALERT'</span></a></form></td>

</tr>'
done
fi
fi

#Disabled alerts
if [ -d /opt/karoshi/server_network/mon/email_alerts_disabled/ ]
then
if [ `ls -1 /opt/karoshi/server_network/mon/email_alerts_disabled/ | wc -l` -gt 0 ]
then

for EMAILALERT in /opt/karoshi/server_network/mon/email_alerts_disabled/*
do
EMAILALERT=`basename $EMAILALERT`
source /opt/karoshi/server_network/mon/email_alerts_disabled/$EMAILALERT
echo '<tr><td style="vertical-align: top;">'$EMAILALERT'</td><td style="vertical-align: top;">'$EMAILADDRESS'</td><td style="vertical-align: top;">'$SENDER'</td><td style="vertical-align: top;">'$EMAILSERVER'</td>

<td><form action="/cgi-bin/admin/monitors_disable_email_alert.cgi" method="post">
<a class="info" href="javascript:void(0)"><input name="_NAME_'$EMAILALERT'_" type="image" class="images" src="/images/submenus/system/disable_monitor.png" value=""><span>'$ENABLEMSG' '$EMAILALERT'</span></a></form></td>

<td><form action="/cgi-bin/admin/monitors_add_email_alert_fm.cgi" method="post">
<a class="info" href="javascript:void(0)"><input name="_NAME_'$EMAILALERT'_EMAILTO_'$EMAILADDRESS'_EMAILFROM_'$SENDER'_MAILSERVER_'$EMAILSERVER'_" type="image" class="images" src="/images/submenus/system/edit.png" value=""><span>'$EDITTITLE' '$EMAILALERT'</span></a></form></td>

<td><form action="/cgi-bin/admin/monitors_delete_email_alert.cgi" method="post">
<a class="info" href="javascript:void(0)"><input name="_NAME_'$EMAILALERT'_" type="image" class="images" src="/images/submenus/system/delete.png" value=""><span>'$DELETETITLE' '$EMAILALERT'</span></a></form></td>

<td><form action="/cgi-bin/admin/monitors_test_email_alert.cgi" method="post">
<a class="info" href="javascript:void(0)"><input name="_NAME_'$EMAILALERT'_" type="image" class="images" src="/images/submenus/system/test.png" value=""><span>'$TESTMSG' '$EMAILALERT'</span></a></form></td>

</tr>'
done

fi
fi

echo ' </tbody></table><br><br></div></body></html>'
exit
