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

##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
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
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><title>'$TITLE'</title></head><body><div id="pagecontainer">'
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
echo 'window.location = "/cgi-bin/staff/helpdesk_add_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

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
/opt/karoshi/web_controls/generate_navbar_staff

#Get data
source /opt/karoshi/helpdesk/todo/$JOBNAME

#Show job data
echo '<form action="/cgi-bin/staff/helpdesk_view_fm.cgi" method="post"><div id="actionbox"><b>'$TITLE' - '$TITLE3'</b><br><br>

<table class="standard" style="text-align: left; height: 91px;" border="0" cellpadding="2" cellspacing="2">
<tbody>
<tr><td style="width: 180px;">'$JOBTITLEMMSG'</td><td>'$JOBTITLE'</td></tr>
<tr><td>'$NAMEMSG'</td><td>'$NAME'</td></tr>
<tr><td>'$LOCATIONMSG'</td><td>'$LOCATION'</td></tr>
<tr><td>'$DEPARTMENTMSG'</td><td>'$DEPARTMENT'</td></tr>
<tr><td>'$CATEGORYMSG'</td><td>'$CATEGORY'</td></tr>
<tr><td>'$USERPROBLEMMSG'</td><td>'$REQUEST'</td></tr>
<tr><td>'$FEEDBACKMSG'</td><td>'$FEEDBACK'</td></tr>
</tbody></table></div>
<div id="submitbox">
<input value="'$BACKMSG'" type="submit">
</div></form></div></body></html>'
exit

