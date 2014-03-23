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

HOUR=`date +%H`
MINUTES=`date +%M`
SECONDS=`date +%S`

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script language="JavaScript" src="/all/calendar/ts_picker.js" type="text/javascript"></script>
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

echo '</head><body onLoad="start()"><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%+'`

END_POINT=9
#Assign _DAY_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DAYcheck ]
then
let COUNTER=$COUNTER+1
DAY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

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
DIV_ID=actionbox3
TABLECLASS=standard
WIDTH1=180
WIDTH2=200
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
WIDTH1=90
WIDTH2=120
fi

echo '<form action="/cgi-bin/admin/update_servers.cgi" name="tstest" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

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
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>
<td style="vertical-align: top;"></td><td><div class="sectiontitle">'$TITLE'</div></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers"><img class="images" alt="" src="/images/help/info.png"><span>'$UPDATESERVERHELP'</span></a></td></tr></tbody></table><br>'
fi

#Preselect day
if [ ! -z $DAY ]
then
[ $DAY = 1 ] && OP1='selected="selected"'
[ $DAY = 2 ] && OP2='selected="selected"'
[ $DAY = 3 ] && OP3='selected="selected"'
[ $DAY = 4 ] && OP4='selected="selected"'
[ $DAY = 5 ] && OP5='selected="selected"'
[ $DAY = 6 ] && OP6='selected="selected"'
[ $DAY = 7 ] && OP7='selected="selected"'
[ $DAY = 8 ] && OP8='selected="selected"'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: '$WIDTH1'px;">'$DAYMSG'</td><td>
<select style="width: '$WIDTH2'px;" name="_DAY_">
<option value=""></option>
<option value="never">'$NEVERMSG'</option>
<option '$OP1' value="1">'$MONMSG'</option>
<option '$OP2' value="2">'$TUESMSG'</option>
<option '$OP3' value="3">'$WEDMSG'</option>
<option '$OP4' value="4">'$THURSMSG'</option>
<option '$OP5' value="5">'$FRIMSG'</option>
<option '$OP6' value="6">'$SATMSG'</option>
<option '$OP7' value="7">'$SUNMSG'</option>
<option '$OP8' value="8">'$EVERYDAYMSG'</option>
</select>
</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$DAYHELP'</span></a></td></tr>
<tr><td>'$HOURMSG'</td><td><input tabindex= "1" value="'$HOUR'" name="_HOURS_" style="width: '$WIDTH2'px;" size="3" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$TIMEHELP'</span></a></td></tr>
<tr><td>'$MINMSG'</td><td><input tabindex= "1" value="'$MINUTES'" name="_MINUTES_" style="width: '$WIDTH2'px;" size="3" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Update_Servers#Scheduling_Server_Updates"><img class="images" alt="" src="/images/help/info.png"><span>'$TIMEHELP'</span></a></td></tr>
</tbody></table><br>'

[ $MOBILE = no ] && echo '</div><div id="infobox">'

#Show list of servers
/opt/karoshi/web_controls/show_servers $MOBILE all "$SCHEDULEMSG" notset updateserver

[ $MOBILE = no ] && echo '</div>'
echo '</div></form></div></body></html>'
exit

