#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Language
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/update_servers ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/update_servers
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
        <!-- Timestamp input popup (European Format) --><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script type="text/javascript" src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
		***********************************************/
	</script>
	<script type="text/javascript">
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head><body onLoad="start()">'
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
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
WIDTH=180
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
WIDTH=160
fi
[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$SYSMENUMSG'</a>
</div></div><div id="mobileactionbox">'
else
echo '
<b>'$TITLE'</b> 
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers"><img class="images" alt="" src="/images/help/info.png"><span>'$UPDATESERVERHELP'</span></a><br><br>'
fi

echo '<form action="/cgi-bin/admin/update_servers.cgi" name="tstest" method="post"><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>

<tr><td style="width: 180px;">'$DAYMSG'</td><td>
<select style="width: 200px;" name="_DAY_">
<option value=""></option>
<option value="never">'$NEVERMSG'</option>
<option value="1">'$MONMSG'</option>
<option value="2">'$TUESMSG'</option>
<option value="3">'$WEDMSG'</option>
<option value="4">'$THURSMSG'</option>
<option value="5">'$FRIMSG'</option>
<option value="6">'$SATMSG'</option>
<option value="7">'$SUNMSG'</option>
<option value="8">'$EVERYDAYMSG'</option>
</select>
</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$DAYHELP'</span></a></td></tr>
<tr><td>'$HOURMSG'</td><td><input tabindex= "1" value="'$HOUR'" name="_HOURS_" style="width: 200px;" size="3" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$TIMEHELP'</span></a></td></tr>
<tr><td>'$MINMSG'</td><td><input tabindex= "1" value="'$MINUTES'" name="_MINUTES_" style="width: 200px;" size="3" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$TIMEHELP'</span></a></td></tr>
</tbody></table><br><br>'

#Show list of ssh enabled servers
SERVERLISTARRAY=( `ls -1 /opt/karoshi/server_network/servers` )
SERVERLISTCOUNT=${#SERVERLISTARRAY[@]}
SERVERCOUNTER=0

if [ $MOBILE = no ]
then
ROWCOUNT=6
WIDTH=90
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"
SCHEDULEICON="/images/submenus/system/computer_schedule.png"
else
ROWCOUNT=3
WIDTH=70
SERVERICON="/images/submenus/system/computerm.png"
SERVERICON2="/images/submenus/system/all_computersm.png"
SCHEDULEICON="/images/submenus/system/computer_schedulem.png"
fi


if [ -f /opt/karoshi/server_network/info ]
then
source /opt/karoshi/server_network/info
LOCATION_NAME2="- $LOCATION_NAME"
fi

echo '<b>'$MYSERVERSMSG' '$LOCATION_NAME2'</b><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'

AUTOSCHEDULE=no
while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}
[ -f /opt/karoshi/server_network/upgrade_schedules/servers/$KAROSHISERVER ] && SERVERICON=$SCHEDULEICON

echo '<td style="width: '$WIDTH'px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_network_SERVERNAME_'$KAROSHISERVER'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$KAROSHISERVER'<br><br>'
[ -f /opt/karoshi/server_network/upgrade_schedules/servers/$KAROSHISERVER ] && cat /opt/karoshi/server_network/upgrade_schedules/servers/$KAROSHISERVER
cat /opt/karoshi/server_network/servers/$KAROSHISERVER/* | sed '/<a href/c'"<br>"
echo '</span></a><br>'$KAROSHISERVER'</td>'
[ $SERVERCOUNTER = $ROWCOUNT ] && echo '</tr><tr>'
[ $SERVERCOUNTER -gt 0 ] && AUTOSCHEDULE=yes
let SERVERCOUNTER=$SERVERCOUNTER+1
done
echo '</tr>'
if [ $AUTOSCHEDULE = yes ]
then
echo '<tr><td style="width: '$WIDTH'px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_network_SERVERNAME_all_" type="image" class="images" src="'$SERVERICON2'" value=""><span>'$LOCATION_NAME' - '$AUTOSCHEDULMSG2'<br><br></span></a><br>'$AUTOSCHEDULEMSG'</td></tr>'
fi
echo '</tbody></table><br>'


#Show list of federated servers
if [ -d /opt/karoshi/server_network/federated_ldap_servers/ ]
then
if [ `ls -1 /opt/karoshi/server_network/federated_ldap_servers/ | wc -l` -gt 0 ]
then
for FEDERATED_SERVERS in /opt/karoshi/server_network/federated_ldap_servers/*
do
AUTOSCHEDULE=no
FEDERATED_SERVER=`basename $FEDERATED_SERVERS`
[ -f /opt/karoshi/server_network/upgrade_schedules/federated_servers/$FEDERATED_SERVER/$FEDERATED_SERVER ] && SERVERICON=$SCHEDULEICON
if [ -f /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/info ]
then
source /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/info
LOCATION_NAME2="- $LOCATION_NAME"
fi
echo '<b>'$FEDERATEDSERVERSMSG' '$LOCATION_NAME2'</b><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
echo '<td style="width: '$WIDTH'px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_federated_SERVERNAME_'$FEDERATED_SERVER'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$FEDERATED_SERVER'<br><br>'
[  -f /opt/karoshi/server_network/upgrade_schedules/federated_servers/$FEDERATED_SERVER/$FEDERATED_SERVER ] && cat /opt/karoshi/server_network/upgrade_schedules/federated_servers/$FEDERATED_SERVER/$FEDERATED_SERVER
cat /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/servers/$FEDERATED_SERVER/* | sed '/<a href/c'"<br>"
echo '</span></a><br>'$FEDERATED_SERVER'</td>'

SERVERCOUNTER2=0
for FEDERATED_SLAVE_SERVERS in /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/servers/*
do
FEDERATED_SLAVE_SERVER=`basename $FEDERATED_SLAVE_SERVERS`
[ -f /opt/karoshi/server_network/upgrade_schedules/federated_servers/$FEDERATED_SERVER/$FEDERATED_SLAVE_SERVER ] && SERVERICON=$SCHEDULEICON
[ $SERVERCOUNTER2 = $ROWCOUNT ] && echo '</tr><tr>'
if [ $FEDERATED_SLAVE_SERVER != $FEDERATED_SERVER ]
then
let SERVERCOUNTER2=$SERVERCOUNTER2+1
echo '<td style="width: '$WIDTH'px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERTYPE_federatedslave_SERVERMASTER_'$FEDERATED_SERVER'_SERVERNAME_'$FEDERATED_SLAVE_SERVER'_" type="image" class="images" src="'$SERVERICON'" value=""><span>'$FEDERATED_SLAVE_SERVER'<br><br>'
[ -f /opt/karoshi/server_network/upgrade_schedules/federated_servers/$FEDERATED_SERVER/$FEDERATED_SLAVE_SERVER ] && cat /opt/karoshi/server_network/upgrade_schedules/federated_servers/$FEDERATED_SERVER/$FEDERATED_SLAVE_SERVER
cat /opt/karoshi/server_network/federated_ldap_servers/$FEDERATED_SERVER/servers/$FEDERATED_SLAVE_SERVER/* | sed '/<a href/c'"<br>"
echo '</span></a><br>'$FEDERATED_SLAVE_SERVER'</td>'
[ $SERVERCOUNTER2 -gt 0 ] && AUTOSCHEDULE=yes
fi
done
echo '</tr>'
if [ $AUTOSCHEDULE = yes ]
then
echo '<tr><td style="width: '$WIDTH'px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVERMASTER_'$FEDERATED_SERVER'_SERVERTYPE_federated_SERVERNAME_all_" type="image" class="images" src="'$SERVERICON2'" value=""><span>'$LOCATION_NAME' - '$AUTOSCHEDULMSG2'<br><br></span></a><br>'$AUTOSCHEDULEMSG'</td></tr>'
fi
echo '</tbody></table><br>'
done
fi
fi

echo '</form></div></body></html>'
exit
