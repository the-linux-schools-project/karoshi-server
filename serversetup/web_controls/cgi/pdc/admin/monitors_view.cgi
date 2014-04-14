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
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_view ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitors_view
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">'
echo '<script type="text/javascript">'
echo '<!--'
echo 'function SetAllCheckBoxes(FormName, FieldName, CheckValue)'
echo '{'
echo '	if(!document.forms[FormName])'
echo '		return;'
echo '	var objCheckBoxes = document.forms[FormName].elements[FieldName];'
echo '	if(!objCheckBoxes)'
echo '		return;'
echo '	var countCheckBoxes = objCheckBoxes.length;'
echo '	if(!countCheckBoxes)'
echo '		objCheckBoxes.checked = CheckValue;'
echo '	else'
echo '		// set the check value for all check boxes'
echo '		for(var i = 0; i < countCheckBoxes; i++)'
echo '			objCheckBoxes[i].checked = CheckValue;'
echo '}'
echo '// -->'
echo '</script><script src="/all/stuHover.js" type="text/javascript"></script>'
echo "</head><body><div id='pagecontainer'>"
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/monitors_add_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$ERRORMSG1
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td style="vertical-align: top; width: 110px;"><b>'"$TITLE"'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_Monitors"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/monitors_add_fm.cgi" name="monitors" method="post">
<input name="ADDMONITOR" type="submit" class="button" value="'$ADDMONITORMSG'">
</form></td><td style="vertical-align: top;"><form action="/cgi-bin/admin/mon_status.cgi" name="monitors" method="post">
<input name="MONITORSTATUS" type="submit" class="button" value="'$NETWORKSTATUSMSG'">
</form></td></tr></tbody></table>
<br>'

#Show monitors

if [ ! -d /opt/karoshi/server_network/mon/monitors ]
then
MESSAGE=$ERRORMSG4
show_status
fi 

if [ `ls -1 /opt/karoshi/server_network/mon/monitors | wc -l` = 0 ] && [ `ls -1 /opt/karoshi/server_network/mon/monitors_disabled | wc -l` = 0 ]
then
MESSAGE=$ERRORMSG4
show_status
fi

#Show table of sites
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">'
echo "<tbody>"
echo '<tr><td style="width: 180px;"><b>'$MONITORMSG'</b></td><td><b>'$ENABLEDMSG'</b></td><td><b>'$EDITTITLE'</b></td><td><b>'$DELETETITLE'</b></td><td><b>'$INFOMSG'</b></td></tr>'

for MONITORNAME in /opt/karoshi/server_network/mon/monitors/*
do
MONITORNAME=`basename $MONITORNAME`
MONITORNAME2=`echo $MONITORNAME | sed 's/_/%%%%%/g'`
MONITOR_SERVICES=`grep service /opt/karoshi/server_network/mon/monitors/$MONITORNAME | sed 's/service//g' |sed 's/$/<br>/g'`
SERVICE_TCPIPS=`sed -n 4,4p /opt/karoshi/server_network/mon/monitors/$MONITORNAME | cut -d' ' -f3-`

echo '<tr>

<td style="vertical-align: top;">'$MONITORNAME'</td>

<td style="vertical-align: top;"><form action="/cgi-bin/admin/monitors_enable_disable.cgi" name="monitors" method="post"><a class="info" href="javascript:void(0)"><input name="_MONITOR_'$MONITORNAME2'_" type="image" class="images" src="/images/submenus/system/enable_monitor.png" value=""><span>'$DISABLEMSG' - '$MONITORNAME'</span></a></form></td>

<td style="vertical-align: top;"><form action="/cgi-bin/admin/monitors_add_fm.cgi" name="monitors" method="post"><a class="info" href="javascript:void(0)"><input name="_MONITOR_'$MONITORNAME2'_" type="image" class="images" src="/images/submenus/system/edit.png" value=""><span>'$EDITMSG' - '$MONITORNAME'</span></a></form></td>

<td style="vertical-align: top;"><form action="/cgi-bin/admin/monitors_delete.cgi" name="monitors" method="post"><a class="info" href="javascript:void(0)"><input name="_MONITOR_'$MONITORNAME2'_" type="image" class="images" src="/images/submenus/system/delete.png" value=""><span>'$DELETEMSG' - '$MONITORNAME'</span></a></form></td>

<td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$TCPIPS_MONITORED:'<br>'$SERVICE_TCPIPS'<br>'$MONITOREDMSG:'<br>'$MONITOR_SERVICES'</span></a></td></tr>'
done

if [ -d /opt/karoshi/server_network/mon/monitors_disabled ]
then
if [ `ls -1 /opt/karoshi/server_network/mon/monitors_disabled | wc -l` -gt 0 ]
then

for MONITORNAME in /opt/karoshi/server_network/mon/monitors_disabled/*
do
MONITORNAME=`basename $MONITORNAME`
MONITORNAME2=`echo $MONITORNAME | sed 's/_/%%%%%/g'`
MONITOR_SERVICES=`grep service /opt/karoshi/server_network/mon/monitors_disabled/$MONITORNAME | sed 's/service//g' |sed 's/$/<br>/g'`
SERVICE_TCPIPS=`sed -n 4,4p /opt/karoshi/server_network/mon/monitors_disabled/$MONITORNAME | cut -d' ' -f3-`

echo '<tr>

<td style="vertical-align: top;">'$MONITORNAME'</td>

<td style="vertical-align: top;"><form action="/cgi-bin/admin/monitors_enable_disable.cgi" name="monitors" method="post"><a class="info" href="javascript:void(0)"><input name="_MONITOR_'$MONITORNAME2'_" type="image" class="images" src="/images/submenus/system/disable_monitor.png" value=""><span>'$ENABLEMSG' - '$MONITORNAME'</span></a></form></td>

<td style="vertical-align: top;"><form action="/cgi-bin/admin/monitors_add_fm.cgi" name="monitors" method="post"><a class="info" href="javascript:void(0)"><input name="_MONITOR_'$MONITORNAME2'_" type="image" class="images" src="/images/submenus/system/edit.png" value=""><span>'$EDITMSG' - '$MONITORNAME'</span></a></form></td>

<td style="vertical-align: top;"><form action="/cgi-bin/admin/monitors_delete.cgi" name="monitors" method="post"><a class="info" href="javascript:void(0)"><input name="_MONITOR_'$MONITORNAME2'_" type="image" class="images" src="/images/submenus/system/delete.png" value=""><span>'$DELETEMSG' - '$MONITORNAME'</span></a></form></td>

<td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$TCPIPS_MONITORED:'<br>'$SERVICE_TCPIPS'<br>'$MONITOREDMSG:'<br>'$MONITOR_SERVICES'</span></a></td></tr>'
done
fi
fi

echo '</tbody></table></div></div></body></html>'
exit
