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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/helpdesk ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/helpdesk
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE' - '$TITLE2'</title><META HTTP-EQUIV="refresh" CONTENT="300">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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

TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\.%+_:\-'`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign SEARCHCRITERIA
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SEARCHCRITERIAcheck ]
then
let COUNTER=$COUNTER+1
SEARCHCRITERIA=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3D/=/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
TABLECLASS=standard
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox
TABLECLASS=mobilestandard
fi
[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE' - '$TITLE2'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$HELPDESKMENUMSG'</a>
</div></div><div id="mobileactionbox">
<form action="/cgi-bin/admin/helpdesk_view_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="_SEARCHCRITERIA_ASSIGNED_" type="image" class="images" src="/images/submenus/user/helpdesk/staff.png" value="_SEARCHCRITERIA_ASSIGNED_"><span>All</span></a></form>'
else
echo '<b>'$TITLE' - '$TITLE2'</b> </div><div id="infobox"><form action="/cgi-bin/admin/helpdesk_view_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="_SEARCHCRITERIA_ASSIGNED_" type="image" class="images" src="/images/submenus/user/helpdesk/staff.png" value="_SEARCHCRITERIA_ASSIGNED_"><span>All</span></a></form>'
fi

[ $SEARCHCRITERIA'null' = null ] && SEARCHCRITERIA=ASSIGNED
#Check to see if there are any new jobs
if [ ! -d /opt/karoshi/helpdesk/todo/ ]
then
echo $ERRORMSG6'</div></div></body></html>'
exit
fi

if [ `ls -1 /opt/karoshi/helpdesk/todo/ | wc -l` = 0 ]
then
echo $ERRORMSG6'</div></div></body></html>'
exit
fi
if [ $MOBILE = yes ]
then
echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 90px;"><b>Date</b></td><td style="width: 120px;"><b>'$LOCATIONMSG'</b></td><td style="width: 30px;"></td><td style="width: 60px;"><b>'$ACTIONMSG'</b></td></tr>
'
else
echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 90px;"><b>Date</b></td><td style="width: 130px;"><b>'$NAMEMSG'</b></td><td style="width: 120px;"><b>'$JOBTITLEMMSG'</b></td><td style="width: 120px;"><b>'$LOCATIONMSG'</b></td><td style="width: 90px;"><b>'$WAITTIMEMSG'</b></td><td style="width: 90px;"><b>'$PRIORITYMSG'</b></td><td style="width: 100px;"><b>'$ASSIGNEDMSG'</b></td><td style="width: 30px;"></td><td style="width: 60px;"><b>'$ACTIONMSG'</b></td></tr>
'
fi

for NEWJOB in `grep -w -l ^$SEARCHCRITERIA /opt/karoshi/helpdesk/todo/*`
do
NEWJOB=`basename $NEWJOB`
DATE=`echo $NEWJOB | cut -d"." -f1`
TIME=`date +%H:%M -d @$DATE`
DATE=`date +%d-%m-%y -d @$DATE`
source /opt/karoshi/helpdesk/todo/$NEWJOB
NOW=`date +%s`
let WAITTIME=($NOW-$DATE2)
if [ $WAITTIME -lt 60 ]
then
#Show time in seconds
if [ $WAITTIME = 1 ]
then 
WAITTIME=`echo $WAITTIME $SECSMSG1`
else
WAITTIME=`echo $WAITTIME $SECSMSG2`
fi
else
#Convert to minutes
let WAITTIME=$WAITTIME/60
if [ $WAITTIME -lt 60 ]
then
#Show time in minutes
if [ $WAITTIME = 1 ]
then
WAITTIME=`echo $WAITTIME $MINSMSG1`
else
WAITTIME=`echo $WAITTIME $MINSMSG2`
fi
else
#Convert time to hours
let WAITTIME=$WAITTIME/60
if [ $WAITTIME -lt 24 ]
then
#Show time in hours
if [ $WAITTIME = 1 ]
then
WAITTIME=`echo $WAITTIME $HOURSMSG1`
else
WAITTIME=`echo $WAITTIME $HOURSMSG2`
fi
else
#Covert time to days
let WAITTIME=$WAITTIME/24
if [ $WAITTIME = 1 ]
then
WAITTIME=`echo $WAITTIME $DAYMSG1`
else
WAITTIME=`echo $WAITTIME $DAYMSG2`
fi
fi
fi
fi

ASSIGNED2=$ASSIGNED
[ $ASSIGNED2'null' = null ] && ASSIGNED2=$ASSIGNEDMSG2

if [ $MOBILE = yes ]
then
echo '<tr><td style="vertical-align: top;">'$DATE'<br>'$TIME'</td><td style="vertical-align: top;">'$LOCATION'</td><td>
<form action="/cgi-bin/admin/helpdesk_view_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="_SEARCHCRITERIA_ASSIGNED='$ASSIGNED'_" type="image" class="images" src="/images/submenus/user/helpdesk/staff.png" value="_SEARCHCRITERIA_ASSIGNED='$ASSIGNED'_"><span>'$ASSIGNED2'</span></a></form></td><td><form action="/cgi-bin/admin/helpdesk_action_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="_JOBNAME_'$NEWJOB'_" type="image" class="images" src="/images/submenus/user/helpdesk/action.png" value="_JOBNAME_'$NEWJOB'_">
<span><b>'$NAMEMSG'</b><br>'$NAME'<br><br><b>'$PRIORITYMSG'</b><br>'$PRIORITY'<br><br><b>'$LOCATIONMSG'</b><br>'$LOCATION'<br><br><b>'$JOBTITLEMMSG'</b><br>'$JOBTITLE'</span></a></form></td></tr>'
else
echo '<tr><td style="vertical-align: top;">'$DATE'<br>'$TIME'</td><td style="vertical-align: top;">'$NAME'</td><td style="vertical-align: top;">'$JOBTITLE'</td><td style="vertical-align: top;">'$LOCATION'</td><td style="vertical-align: top;">'$WAITTIME'</td><td style="vertical-align: top;">'$PRIORITY'</td><td style="vertical-align: top;">'$ASSIGNED'</td><td>
<form action="/cgi-bin/admin/helpdesk_view_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="_SEARCHCRITERIA_ASSIGNED='$ASSIGNED'_" type="image" class="images" src="/images/submenus/user/helpdesk/staff.png" value="_SEARCHCRITERIA_ASSIGNED='$ASSIGNED'_"><span>'$ASSIGNED2'</span></a></form></td><td><form action="/cgi-bin/admin/helpdesk_action_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="_JOBNAME_'$NEWJOB'_" type="image" class="images" src="/images/submenus/user/helpdesk/action.png" value="_JOBNAME_'$NEWJOB'_"><span>'$JOBTITLE'</span></a></form></td></tr>'
fi

done
[ $MOBILE = no ] && echo '</div>'
echo '</tbody></table></div></html>'
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:no:" | sudo -H /opt/karoshi/web_controls/exec/helpdesk_warning_message
exit


