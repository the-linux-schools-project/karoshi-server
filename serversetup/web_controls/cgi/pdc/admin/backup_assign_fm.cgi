#!/bin/bash
#backup_assign
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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/backup_assign ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/backup_assign
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign SERVERNAME

COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/karoshi_servers_view.cgi"'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Check data
#########################
#Check to see that servername is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$ERRORMSG1
	show_status
fi

#Check to see that a backup server has been configured
if [ ! -d /opt/karoshi/server_network/backup_servers/servers ]
then
	MESSAGE=$ERRORMSG2
	show_status
fi

if [ `ls -1 /opt/karoshi/server_network/backup_servers/servers | wc -l` = 0 ]
then
	MESSAGE=$ERRORMSG2
	show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/backup_assign.cgi" method="post">
<div id="actionbox">

<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tr><td style="vertical-align: top;"><div class="sectiontitle">'$TITLE - $SERVERNAME'</div></td><td style="vertical-align: top;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td></tr></tbody></table><br>

<input name="_SERVER_" value="'$SERVERNAME'" type="hidden">
'

if [ -d /opt/karoshi/server_network/backup_servers/backup_settings/$SERVERNAME ]
then
CURRENTBSERVER=`sed -n 1,1p /opt/karoshi/server_network/backup_servers/backup_settings/$SERVERNAME/backupserver`

echo '<br><br><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody>
<tr><td style="width: 10px; vertical-align: top; text-align: left;"></td><td style="width: 250px; vertical-align: top; text-align: left;">'$CURRENTBSERVERMSG'</td><td style="width: 250px; vertical-align: top; text-align: left;">'$CURRENTBSERVER'</td><td style="vertical-align: top; text-align: left;">
<input name="_SERVERNAME_removebackupoption_" type="submit" class="button" value="'$NOBACKUPMSG'">
</td></tr></tbody></table><br><br>'
fi

MOBILE=no
/opt/karoshi/web_controls/show_servers $MOBILE backupservers "$CHOOSESERVERMSG" backupserver $SERVERNAME

echo '</tbody></table></div></form></div></body></html>'
exit
