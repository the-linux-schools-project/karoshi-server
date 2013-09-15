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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/client_shutdown_time ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/client_shutdown_time
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/client_shutdown_time.cgi";'
echo '</script>'
echo "</body></html>"
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
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
WIDTH1=180
WIDTH2=400
WIDTH3=300
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=mobileactionbox
TABLECLASS=mobilestandard
WIDTH1=90
WIDTH2=160
WIDTH3=120
fi


[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

echo '<form action="/cgi-bin/admin/client_shutdown_time2.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$CLIENTMENUMSG'</a>
</div></div><div id="'$DIV_ID'">'
else
echo '<b>'$TITLE'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Client_Shutdown_Time"><img class="images" alt="" src="/images/help/info.png"><span>'$USERHELP1'</span></a>
      </td></tr><br><br>'
fi
#Get shutdown time
if [ -f /var/lib/samba/netlogon/domain_information/clientshutdowntime ]
then
SHUTDOWNTIME=`sed -n 1,1p /var/lib/samba/netlogon/domain_information/clientshutdowntime | tr -cd '0-9:'`
HOUR=`echo $SHUTDOWNTIME | cut -d: -f1`
MINUTES=`echo $SHUTDOWNTIME | cut -d: -f2`
fi
[ $HOUR'null' = null ] && HOUR=`date +%H`
[ $MINUTES'null' = null ] && MINUTES=`date +%M`

IDLETIME=10
[ -f /var/lib/samba/netlogon/domain_information/idletime ] && IDLETIME=`sed -n 1,1p /var/lib/samba/netlogon/domain_information/idletime`

echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td style="width: 180px;">'$TIMEMSG'</td><td><input maxlength="2" size="2" value="'$HOUR'" name="_HOUR_"></td><td><input maxlength="2" size="2" value="'$MINUTES'" name="_MINUTES_"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Client_Shutdown_Time"><img class="images" alt="" src="/images/help/info.png"><span>'$TIMEHELP'</span></a>
</td></tr>
<tr><td style="width: 180px;">'$IDLETIMEMSG'</td><td></td><td><input maxlength="2" size="2" value="'$IDLETIME'" name="_IDLETIME_"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Client_Shutdown_Time"><img class="images" alt="" src="/images/help/info.png"><span>'$IDLETIMEHELP'</span></a>
</td></tr>
</tbody></table>'


[ $MOBILE != yes ] && echo '</div><div id="submitbox">'

echo '<input value="Submit" type="submit"> <input value="Reset" type="reset"></div>'
echo '</form></body></html>'
exit
