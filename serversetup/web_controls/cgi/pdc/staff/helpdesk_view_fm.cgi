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
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
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
  <title>'$TITLE' - '$TITLE2'</title>
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body><div id="pagecontainer">'

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
/opt/karoshi/web_controls/generate_navbar_staff
echo '<form action="/cgi-bin/staff/helpdesk_add_fm.cgi" method="post"><div id="actionbox"><b>'$TITLE' - '$TITLE2'</b> <a class="info" href="javascript:void(0)"><input name="_ADD_" type="image" class="images" src="/images/submenus/user/helpdesk/add.png" value="_ADD_"><span>'$CREATEREQUESTSMSG'</span></a></form><br><br>'
[ $SEARCHCRITERIA'null' = null ] && SEARCHCRITERIA=ASSIGNED
#Check to see if there are any new jobs
if [ ! -d /opt/karoshi/helpdesk/todo/ ]
then
echo $ERRORMSG6'</div></form></div></body></html>'
exit
fi

if [ `ls -1 /opt/karoshi/helpdesk/todo/ | wc -l` = 0 ]
then
echo $ERRORMSG6'</div></form></div></body></html>'
exit
fi

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 140px;"><b>'$NAMEMSG'</b></td><td style="width: 140px;"><b>'$JOBTITLEMMSG'</b></td><td style="width: 120px;"><b>'$LOCATIONMSG'</b></td><td style="width: 100px;"><b>'$WAITTIMEMSG'</b></td><td style="width: 120px;"><b>'$ASSIGNEDMSG'</b></td><td style="width: 60px;"><b>'$ACTIONMSG'</b></td></tr>
'
for NEWJOB in `grep -w -l 'NAME="'$REMOTE_USER'"' /opt/karoshi/helpdesk/todo/*`
do
NEWJOB=`basename $NEWJOB`
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

echo '<tr><td style="vertical-align: top;">'$NAME'</td><td style="vertical-align: top;">'$JOBTITLE'</td><td style="vertical-align: top;">'$LOCATION'</td><td style="vertical-align: top;">'$WAITTIME'</td><td style="vertical-align: top;">'$ASSIGNED'</td><td><form action="/cgi-bin/staff/helpdesk_action_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="_JOBNAME_'$NEWJOB'_" type="image" class="images" src="/images/submenus/user/helpdesk/action.png" value="_JOBNAME_'$NEWJOB'_"><span>'$JOBTITLE'</span></a></form></td></tr>'
done
echo '</tbody></table></div></html>'

exit


