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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Configure Backup"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/backup_configure_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g'`

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

#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = delete ] || [ "$ACTION" = edit ] || [ "$ACTION" = reallyedit ] || [ "$ACTION" = reallydelete ]
then
	#Assign BACKUPNAME
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPNAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	if [ "$ACTION" = reallyedit ]
	then
		#Assign BACKUPFOLDER
		COUNTER=2
		while [ $COUNTER -le $END_POINT ]
		do
			DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			if [ `echo $DATAHEADER'check'` = BACKUPFOLDERcheck ]
			then
				let COUNTER=$COUNTER+1
				BACKUPFOLDER=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
				break
			fi
			let COUNTER=$COUNTER+1
		done

		#Assign DURATION
		COUNTER=2
		while [ $COUNTER -le $END_POINT ]
		do
			DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			if [ `echo $DATAHEADER'check'` = DURATIONcheck ]
			then
				let COUNTER=$COUNTER+1
				DURATION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
				break
			fi
			let COUNTER=$COUNTER+1
		done
	fi
fi

if [ "$ACTION" = assignbackupserver ]
then
	#Assign BACKUPSERVER
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPSERVERcheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPSERVER=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

if [ "$ACTION" = setbackupstatus ]
then
	#Assign BACKUPSTATUS
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPSTATUScheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPSTATUS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
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
	MESSAGE=$"You must choose a server."
	show_status
fi

if [ "$ACTION" = delete ] || [ "$ACTION" = edit ] || [ "$ACTION" = reallyedit ] || [ "$ACTION" = reallydelete ]
then
	
	if [ -z "$BACKUPNAME" ]
	then
		MESSAGE=$"Blank backup name."
		show_status
	fi
	if [ "$ACTION" = reallyedit ]
	then
		if [ -z "$BACKUPFOLDER" ]
		then
			MESSAGE=$"Blank backup folder."
			show_status
		fi

		if [ -z "$DURATION" ]
		then
			MESSAGE=$"Blank duration."
			show_status
		fi
	fi
fi

if [ "$ACTION" = assignbackupserver ]
then
	if [ -z "$BACKUPSERVER" ]
	then
		MESSAGE=$"Blank backup servername."
		show_status
	fi
fi

if [ "$ACTION" = setbackupstatus ]
then
	if [ -z "$BACKUPSTATUS" ]
	then
		MESSAGE=$"Blank backup status."
		show_status
	fi
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tr><td style="vertical-align: top;"><div class="sectiontitle">'$"Configure Backup"' - '$SERVERNAME'</div></td><td style="vertical-align: top;">
<a href="/cgi-bin/admin/backup_configure_fm.cgi"><input class="button" type="button" name="" value="'$"Select server"'"></a>
</td>'

if [ "$ACTION" = view ] || [ "$ACTION" = reallyedit ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ] || [ "$ACTION" = assignbackupserver ] || [ "$ACTION" = setbackupstatus ]
then
	echo '<td><form action="/cgi-bin/admin/backup_configure.cgi" name="testform" method="post">
	<input name="____ACTION____add____SERVERNAME____'$SERVERNAME'____" type="submit" class="button" value="'$"Add Backup Folder"'"></form></td>
	<td><form action="/cgi-bin/admin/backup_assign_fm.cgi" name="testform" method="post">
	<input name="_SERVERNAME_'$SERVERNAME'_" type="submit" class="button" value="'$"Change Backup Server"'"></form></td>'
fi

if [ "$ACTION" = edit ] || [ "$ACTION" = add ]
then
	echo '<td><form action="/cgi-bin/admin/backup_configure.cgi" name="testform" method="post">
	<input name="____SERVERNAME____'$SERVERNAME'____" type="submit" class="button" value="'$"View Backups"'"></form></td>'
fi
echo '</tr></tbody></table>
</div><br><div id="infobox">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/backup_configure.cgi | cut -d' ' -f1`
#View logs
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$ACTION:$BACKUPNAME:$BACKUPFOLDER:$DURATION:$BACKUPSERVER:$BACKUPSTATUS:" | sudo -H /opt/karoshi/web_controls/exec/backup_configure
echo "</div></div></div></body></html>"
exit
