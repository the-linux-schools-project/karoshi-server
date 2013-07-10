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


##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/helpdesk ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/helpdesk
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" href="/css/'$STYLESHEET'"><title>'$TITLE'</title><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
echo '</head><body onLoad="start()"><form action="/cgi-bin/admin/helpdesk_action.cgi" method="post">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\.%+_:\-'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign JOBNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = JOBNAMEcheck ]
then
let COUNTER=$COUNTER+1
JOBNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/helpdesk_view_fm.cgi";'
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
#Check data
#########################
#Check to see that JOBNAME is not blank
if [ $JOBNAME'null' = null ]
then
MESSAGE=$ERRORMSG8
show_status
fi

if [ ! -f /opt/karoshi/helpdesk/todo/$JOBNAME ]
then
MESSAGE=$ERRORMSG9
show_status
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
WIDTH1=180
WIDTH2=200
WIDTH3=600
COLS=70
ROWS=6
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox
TABLECLASS=mobilestandard
WIDTH1=120
WIDTH2=140
WIDTH3=140
COLS=18
ROWS=4
fi
[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: left" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE' - '$TITLE3'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$HELPDESKMENUMSG'</a>
</div></div><div id="mobileactionbox">'
else
echo '<b>'$TITLE' - '$TITLE3'</b><br><br>'
fi



#Get data
source /opt/karoshi/helpdesk/todo/$JOBNAME

#Show job data

echo '<input name="_JOBNAME_" value="'$JOBNAME'" type="hidden">
<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody>
<tr><td style="width: '$WIDTH1'px;">'$JOBTITLEMMSG'</td><td>'$JOBTITLE'</td></tr>
<tr><td>'$NAMEMSG'</td><td>'$NAME'</td></tr>
<tr><td>'$LOCATIONMSG'</td><td>'$LOCATION'</td></tr>
<tr><td>'$DEPARTMENTMSG'</td><td>'$DEPARTMENT'</td></tr>
<tr><td>'$CATEGORYMSG'</td><td>'$CATEGORY'</td></tr>
<tr><td>'$USERPROBLEMMSG'</td><td>'$REQUEST'</td></tr>
<tr><td>'$UPDATEMSG'</td><td><input tabindex= "1" name="_ACTION_"  checked="checked" value="update" type="radio"></td></tr>
<tr><td>'$DELETEMSG'</td><td><input tabindex= "2" name="_ACTION_" value="delete" type="radio"></td></tr>
<tr><td>'$COMPLETEDMSG'</td><td><input tabindex= "3" name="_ACTION_" value="completed" type="radio"></td></tr>
<tr><td>'$ASSIGNEDMSG'</td><td>'
#Show list of technical staff
echo '<select tabindex= "4" style="width: '$WIDTH2'px;" name="_ASSIGNED_"><option>'$ASSIGNED'</option>'
cat /opt/karoshi/web_controls/web_access_admin | cut -d: -f1 | sed 's/^/<option>/g' | sed 's/$/<\/option>/g'
cat /opt/karoshi/web_controls/web_access_tech | cut -d: -f1 | sed 's/^/<option>/g' | sed 's/$/<\/option>/g'
echo '<option value=""></option></select>'

echo '</td></tr>
<tr><td>'$ASSIGNEDMSG3'</td><td><input tabindex= "5" name="_ASSIGNED2_" style="width: '$WIDTH2'px;" size="20" type="text"></td></tr>
<tr><td>'$PRIORITYMSG'</td><td>'

#Show priorities
echo '
<select tabindex= "6" style="width: '$WIDTH2'px;" name="_PRIORITY_">
<option value="'$PRIORITY'">'$PRIORITY'</option>
<option value="$PRIORITY1">'$PRIORITY1'</option>
<option value="$PRIORITY2">'$PRIORITY2'</option>
<option value="$PRIORITY3">'$PRIORITY3'</option>
<option value="$PRIORITY4">'$PRIORITY4'</option>
<option value=""></option></select>
'

echo '</td></tr>
<tr><td>'$FEEDBACKMSG'</td><td><textarea style="width: '$WIDTH3'px;" tabindex= "7" cols="'$COLS'" rows="'$ROWS'" name="_FEEDBACK_">'$FEEDBACK'</textarea></td></tr>
</tbody></table>'

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi

echo '<input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div></form></body></html>'
exit

