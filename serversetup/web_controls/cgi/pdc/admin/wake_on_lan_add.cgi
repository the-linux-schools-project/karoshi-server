#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/wake_on_lan_add ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/wake_on_lan_add
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">'
echo "<link rel="stylesheet" href="/css/$STYLESHEET"><script src=\"/all/stuHover.js\" type=\"text/javascript\"></script>"
echo "</head><body><div id='pagecontainer'>"
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/locations.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
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

echo '<form action="/cgi-bin/admin/wake_on_lan_add2.cgi" method="post"><div id="actionbox"><b>'$TITLE'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$WOLHELP'<br><br>'$WOLHELP2'</span></a><br><br>'
#Time to wake location up
echo '<table class="standard" style="text-align: left; height: 60px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 200px;"><b>'$TIMEMSG'</b></td><td>'
echo '<input maxlength="2" size="2" name="_HOUR_" value="08"> : <input maxlength="2" size="2" name="_MINUTES_" value="15"> </td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$TIMEHELP'</span></a></td></tr><tr><td><b>'$LOCATIONMSG'</b></td><td>'
#Show current rooms
LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
if [ $LOCATION_COUNT -gt 0 ]
then
echo '<select name="_LOCATION_">'
COUNTER=1
while [ $COUNTER -le $LOCATION_COUNT ]
do
LOCATION=`sed -n $COUNTER,$COUNTER'p' /var/lib/samba/netlogon/locations.txt`
echo '<option value="'$LOCATION'">'$LOCATION'</option>'
let COUNTER=$COUNTER+1
done
echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$LOCATIONHELP'</span></a></td></tr></tbody></table>'
else
MESSAGE=$ERROR_MESSAGE1
show_status
fi
echo "</div>"
echo '<div id="submitbox"><input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"></div>'
echo '</form></div></body></html>'
exit
