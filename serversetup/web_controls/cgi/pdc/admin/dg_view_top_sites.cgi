#!/bin/bash
#Copyright (C) 2008  Paul Sharrad

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
########################
#Required input variables
########################
# _DAY_
# _MONTH_
# _YEAR_
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Top Sites"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	2: { sorter: false}
    		}
		});
    } 
);
</script>
</head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=5

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

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/dg_view_top_sites_fm.cgi";'
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

#Check to see that DATE is not blank
if [ -z "$DATE" ]
then
	MESSAGE=$"The date cannot be blank."
	show_status
fi

DAY=`echo $DATE | cut -d- -f1`
MONTH=`echo $DATE | cut -d- -f2`
YEAR=`echo $DATE | cut -d- -f3`

#Check to see that DAY is not blank
if [ -z "$DAY" ]
then
	MESSAGE=$"The date cannot be blank."
	show_status
fi

#Check to see that MONTH is not blank
if [ -z "$MONTH" ]
then
	MESSAGE=$"The date cannot be blank."
	show_status
fi

#Check to see that YEAR is not blank
if [ -z "$YEAR" ]
then
	MESSAGE=$"The date cannot be blank."
	show_status
fi

#Check that day is not greater than 31
if [ $DAY -gt 31 ]
then
	MESSAGE=$"Date input error."
	show_status
fi

#Check that the month is not greater than 12
if [ $MONTH -gt 12 ]
then
	MESSAGE=$"Date input error."
	show_status
fi

if [ $YEAR -lt 2006 ] || [ $YEAR -gt 3006 ]
then
	MESSAGE=$"The year is not valid."
	show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/dg_view_top_sites.cgi | cut -d' ' -f1`
#View logs
echo '<b>'$"Top Sites" $DAY-$MONTH-$YEAR'</b><br><br></div><div id="infobox">'
echo \<form action=\"/cgi-bin/admin/dg_view_site_logs2.cgi\" method=\"post\"\>
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$DAY:$MONTH:$YEAR:" | sudo -H /opt/karoshi/web_controls/exec/dg_view_top_sites
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 102 ]
then
	MESSAGE=`echo $"No log exists for this date."`
	show_status
fi
if [ $EXEC_STATUS = 103 ]
then
	MESSAGE=`echo $"No sites for this search exist in this log."`
	show_status
fi

echo '</form></div></div></div></body></html>'
exit
