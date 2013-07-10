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
########################
#Required input variables
########################
#  _SERVER_
#  _PRIGROUP_
##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/home_folders ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/home_folders
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

#########################
#Generate navigation bar
#########################
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><b>'$TITLE2'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a><br><br>'

#########################
#Assign data to variables
#########################
END_POINT=6
#Assign SERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERcheck ]
then
let COUNTER=$COUNTER+1
SERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PRIGROUP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRIGROUPcheck ]
then
let COUNTER=$COUNTER+1
PRIGROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done



function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/home_folders_fm.cgi";'
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
#########################
#Check data
#########################
#Check to see that SERVER is not blank
if [ $SERVER'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that PRIGROUP is not blank
if [ $PRIGROUP'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that there are other karoshi servers available
if [ ! -d /opt/karoshi/server_network/servers/ ]
then
MESSAGE=$ERRORMSG3
show_status
fi

if [ `ls -1 /opt/karoshi/server_network/servers/ | wc -l` = 0 ]
then
MESSAGE=$ERRORMSG3
show_status
fi

FILESERVERCOUNT=0
for KAROSHI_SERVER in /opt/karoshi/server_network/servers/*
do
KAROSHI_SERVER=`basename $KAROSHI_SERVER`
if [ -f /opt/karoshi/server_network/servers/$KAROSHI_SERVER/fileserver ]
then
SERVERARRAY[$FILESERVERCOUNT]=$KAROSHI_SERVER
let FILESERVERCOUNT=$FILESERVERCOUNT+1
fi
done

if [ $FILESERVERCOUNT -le 1 ]
then
MESSAGE=$ERRORMSG4
show_status
fi

echo '<img alt="Warning" src="/images/warnings/warning.png"> '$LOGGEDINWARNMSG'<br><br>
<form action="/cgi-bin/admin/home_folders2.cgi" method="post">
<input name="_CURRENTSERVER_" value="'$SERVER'" type="hidden">
<input name="_PRIGROUP_" value="'$PRIGROUP'" type="hidden">
  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>

<tr><td style="width: 180px;">'$CURRENTSERVERMSG'</td><td>'$SERVER'</td></tr>
<tr><td>'$PRIGROUPMSG'</td><td>'$PRIGROUP'</td></tr>
<tr><td>'$COPYHOMEAREASMSG'</td><td><input name="_COPYHOMEAREAS_" value="yes" type="checkbox"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a></td></tr></tbody></table><br><br><b>'$NEWSERVERMSG'</b><br>'

#Display list of file servers
COUNTER=0
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tr>'
while [ $COUNTER -lt $FILESERVERCOUNT ]
do
if [ $SERVER != ${SERVERARRAY[$COUNTER]} ]
then
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_NEWSERVER_'${SERVERARRAY[$COUNTER]}'_" type="image" class="images" src="'$SERVERICON'" value="_NEWSERVER_'${SERVERARRAY[$COUNTER]}'_"><span>'${SERVERARRAY[$COUNTER]}'</span></a><br>'${SERVERARRAY[$COUNTER]}'</td>'
[ $COUNTER = 5 ] && echo '</tr><tr>'
fi
let COUNTER=$COUNTER+1
done 

echo '</tr></tbody></table></form></div></body></html>'
exit

