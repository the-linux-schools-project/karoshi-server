#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Edit Scheduled Jobs"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: www.dynamicdrive.com
		* Visit Dynamic Drive at www.dynamicdrive.com for full source code
		***********************************************/
	</script>
	<script>
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head><body><div id="pagecontainer">'


#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\/*%+"-' | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g' | sed 's/%A0+//g' | sed 's/%A0//g'`
#########################
#Assign data to variables
#########################
END_POINT=21

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

#Assign SERVERTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERTYPEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SERVERMASTER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERMASTERcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERMASTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/cron_view_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

function show_jobs {
echo "
<form action=\"/cgi-bin/admin/cron_view.cgi\" method=\"post\" id=\"showdns\">
<input type="hidden" name="_SERVERNAME_$SERVERNAME"_"SERVERTYPE_$SERVERTYPE"_"" value=''>
</form>
<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('showdns').submit();
//-->
</script>
</div></div></body></html>
"
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
#Check to see that JOBNAME is not blank
if [ -z "$JOBNAME" ]
then
	MESSAGE=$"You have not chosen a job to edit or delete."
	show_status
fi
#Check that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The server cannot be blank."
	show_status
fi
#Check that SERVERTYPE is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$"The servertype cannot be blank."
	show_status
fi
#Check that ACTION is not blank
if [ -z "$ACTION" ]
then
	MESSAGE=$"The action cannot be blank."
	show_status
fi

#Generate navigation bar
if [ $ACTION != delete ]
then
	if [ $MOBILE = no ]
	then
		DIV_ID=actionbox
		#Generate navigation bar
		/opt/karoshi/web_controls/generate_navbar_admin
	else
		DIV_ID=menubox
	fi

	[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/cron_edit.cgi | cut -d' ' -f1`

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$ACTION:$JOBNAME:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/cron_edit
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 102 ]
then
	show_jobs
fi
exit
