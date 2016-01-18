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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><title>'$"Help Desk"'</title></head><body onLoad="start()"><div id="pagecontainer">'
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
echo 'window.location = "/cgi-bin/admin/helpdesk_view_completed_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$"You must access this page via https."
show_status
fi

#########################
#Check data
#########################
#Check to see that JOBNAME is not blank
if [ $JOBNAME'null' = null ]
then
MESSAGE=$"The job name cannot be blank."
show_status
fi

if [ ! -f /opt/karoshi/server_network/helpdesk/completed/$JOBNAME ]
then
MESSAGE=$"This job does not exist."
show_status
fi


#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

#Get data
source /opt/karoshi/server_network/helpdesk/completed/$JOBNAME

#Show job data
echo '<form action="/cgi-bin/admin/helpdesk_action.cgi" method="post"><div id="actionbox"><b>'$"Help Desk"' - '$"Action Request"'</b><br><br>
<input name="_JOBNAME_" value="'$JOBNAME'" type="hidden">
<table class="standard" style="text-align: left; height: 91px;" >
<tbody>
<tr><td style="width: 180px;">'$"Request Summary"'</td><td>'$JOBTITLE'</td></tr>
<tr><td>'$"Name"'</td><td>'$NAME'</td></tr>
<tr><td>'$"Location"'</td><td>'$LOCATION'</td></tr>
<tr><td>'$"Department"'</td><td>'$DEPARTMENT'</td></tr>
<tr><td>'$"Category"'</td><td>'$CATEGORY'</td></tr>
<tr><td>'$"Extended Details"'</td><td>'$REQUEST'</td></tr>
<tr><td>'$"Not completed"'</td><td><input name="_ACTION_" value="notcompleted" type="checkbox"></td></tr>
<tr><td>'$"Assigned to"'</td><td>'$ASSIGNED'</td></tr>
<tr><td>'$"Priority"'</td><td>'$PRIORITY'</td></tr>
<tr><td>'$"Feedback"'</td><td>'$FEEDBACK'</td></tr>
</tbody></table></div>
<div id="submitbox">
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></form></div></body></html>'
exit

