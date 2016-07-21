#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

#This file is part of Karoshi SERVERNAME.
#
#Karoshi SERVERNAME is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Karoshi SERVERNAME is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Karoshi SERVERNAME.  If not, see <http://www.gnu.org/licenses/>.

#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Network Backup Logs"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=22

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

#Assign DATE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = DATEcheck ]
	then
		let COUNTER=$COUNTER+1
		DATE=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9-'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign LOGTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = LOGTYPEcheck ]
	then
		let COUNTER=$COUNTER+1
		LOGTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/backup_view_logs_fm.cgi";'
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
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################
#Check to see that a SERVERNAME has been chosen
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"You must choose a server to enable or disable."
	show_status
fi

#Check to see that DATE is not blank
if [ -z "$DATE" ]
then
	MESSAGE=$"The date cannot be blank."
	show_status
fi

if [ -z "$LOGTYPE" ]
then
	LOGTYPE=summary
fi

#Check that date is valid
DAY=`echo $DATE | cut -d- -f1`
MONTH=`echo $DATE | cut -d- -f2`
YEAR=`echo $DATE | cut -d- -f3`

#Check to see that DAY, MONTH or YEAR is not blank
if [ -z "$DAY" ] || [ -z "$MONTH" ] || [ -z "$YEAR" ]
then
	MESSAGE=$"The date cannot be blank."
	show_status
fi

if [ $DAY -gt 31 ]
then
	MESSAGE=$"Incorrect date format."
	show_status
fi

if [ $MONTH -gt 12 ]
then
	MESSAGE=$"Incorrect date format."
	show_status
fi

if [ $YEAR -lt 2006 ] || [ $YEAR -gt 3006 ]
then
	MESSAGE=$"Incorrect date format."
	show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" ><tr><td style="vertical-align: top;"><div class="sectiontitle">'$SERVERNAME: $"Backup logs" $DAY-$MONTH-$YEAR'</div></td>

<td style="vertical-align: top;"><form action="/cgi-bin/admin/backup_view_logs.cgi" name="testform" method="post">'
if [ $LOGTYPE = summary ]
then
	echo '<input name="_SERVERNAME_'$SERVERNAME'_LOGTYPE_detailed_DATE_'$DATE'_" type="submit" class="button" value="'$"Detailed logs"'">'
else
	echo '<input name="_SERVERNAME_'$SERVERNAME'_LOGTYPE_summary_DATE_'$DATE'_" type="submit" class="button" value="'$"Summary logs"'">'
fi
echo '</form></td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/backup_view_logs_fm.cgi" method="post">
<button class="button" name="_SelectServer_" value="_">
'$"Select server"'
</button>
</form>
</td>
<td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_Backup_Logs"><img class="images" alt="" src="/images/help/info.png"><span>'$"These are the backup logs for your server."'</span></a>
</td>
</tr></tbody></table>


</div><br><div id="infobox">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/backup_view_logs.cgi | cut -d' ' -f1`
#View logs
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$DAY:$MONTH:$YEAR:$SERVERNAME:$LOGTYPE:" | sudo -H /opt/karoshi/web_controls/exec/backup_view_logs
echo "</div></div></div></body></html>"
exit

