#!/bin/bash
#Copyright (C) 2009  Paul Sharrad
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

#Language
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/time ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/time
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

#Get current date and time
DAY=`date +%d`
MONTH=`date +%m`
YEAR=`date +%Y`

HOUR=`date +%H`
MINUTES=`date +%M`
SECONDS=`date +%S`

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script language="JavaScript" src="/all/calendar/ts_picker.js" type="text/javascript"></script>
        <!-- Timestamp input popup (European Format) --><script src="/all/stuHover.js" type="text/javascript"></script>'
echo "</head>"
echo "<body onLoad="start()">"
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
echo '<form action="/cgi-bin/admin/time.cgi" name="tstest" method="post"><div id="actionbox"><b>'$TITLE'</b><br><br>'



echo "$TIMEMSG:<br>
<input type=\"Text\" name=\"timestamp\" value=\"$DAY-$MONTH-$YEAR $HOUR:$MINUTES:$SECONDS\">
<a href=\"javascript:show_calendar('document.tstest.timestamp', document.tstest.timestamp.value);\"><img src=\"/all/calendar/cal.gif\" width=\"16\" height=\"16\" border=\"0\" alt=\"Click Here to Pick up the timestamp\"></a><br><br>

                <!--- End European Date and Time -->"

#Show list of ssh enabled servers
SERVERLISTARRAY=( `ls -1 /opt/karoshi/server_network/servers` )
SERVERLISTCOUNT=${#SERVERLISTARRAY[@]}
SERVERCOUNTER=0
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"
if [ -f /opt/karoshi/server_network/info ]
then
source /opt/karoshi/server_network/info
LOCATION_NAME="- $LOCATION_NAME"
fi

echo '<b>'$MYSERVERSMSG' '$LOCATION_NAME'</b><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'

while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_network_SERVERNAME_'$KAROSHISERVER'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$KAROSHISERVER'<br><br>'
cat /opt/karoshi/server_network/servers/$KAROSHISERVER/* | sed '/<a href/c'"&nbsp"
echo '</span></a><br>'$KAROSHISERVER'</td>'
[ $SERVERCOUNTER = 5 ] && echo '</tr><tr>'
let SERVERCOUNTER=$SERVERCOUNTER+1
done
echo '</tr></tbody></table><br>'


#Show list of federated servers
if [ -d /opt/karoshi/server_network/federated_ldap_servers/ ]
then
if [ `ls -1 /opt/karoshi/server_network/federated_ldap_servers/ | wc -l` -gt 0 ]
then
for FEDERATED_SERVERS in /opt/karoshi/server_network/federated_ldap_servers/*
do
FEDERATED_SERVER=`basename $FEDERATED_SERVERS`
if [ -f /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/info ]
then
source /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/info
LOCATION_NAME="- $LOCATION_NAME"
fi
echo '<b>'$FEDERATEDSERVERSMSG' '$LOCATION_NAME'</b><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_federated_SERVERNAME_'$FEDERATED_SERVER'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$FEDERATED_SERVER'<br><br>'
cat /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/servers/$FEDERATED_SERVER/* | sed '/<a href/c'"&nbsp"
echo '</span></a><br>'$FEDERATED_SERVER'</td>'

SERVERCOUNTER2=0
for FEDERATED_SLAVE_SERVERS in /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/servers/*
do
FEDERATED_SLAVE_SERVER=`basename $FEDERATED_SLAVE_SERVERS`
[ $SERVERCOUNTER2 = 6 ] && echo '</tr><tr>'
if [ $FEDERATED_SLAVE_SERVER != $FEDERATED_SERVER ]
then
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_federatedslave_SERVERMASTER_'$FEDERATED_SERVER'_SERVERNAME_'$FEDERATED_SLAVE_SERVER'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$FEDERATED_SLAVE_SERVER'<br><br>'
cat /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/servers/$FEDERATED_SLAVE_SERVER/* | sed '/<a href/c'"&nbsp"
echo '</span></a><br>'$FEDERATED_SLAVE_SERVER'</td>'
let SERVERCOUNTER2=$SERVERCOUNTER2+1
fi
done
echo '</tr></tbody></table><br>'
done
fi
fi

echo '</div></form></body></html>'
exit
