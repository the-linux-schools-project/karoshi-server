#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

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
#  _UPLOADFOLDER_  primary group of the users to copy the files to
#  _UPLOADID_ process id
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Web Management - Upload Files"2'</title><meta http-equiv="REFRESH" content="0; URL=/cgi-bin/admin/web_management_upload_files_fm.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\_:\-.%'`
DATA=`echo $DATA | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign UPLOADFOLDER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = UPLOADFOLDERcheck ]
then
let COUNTER=$COUNTER+1
UPLOADFOLDER=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%2F/\//g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign UPLOADID
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = UPLOADIDcheck ]
then
let COUNTER=$COUNTER+1
UPLOADID=`echo $DATA | cut -s -d'_' -f$COUNTER`
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

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '</script>'
echo "</div></div></body></html>"
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
#Check to see that UPLOADFOLDER is not blank
if [ -z "$UPLOADFOLDER" ]
then
MESSAGE=$"The upload folder cannot be blank."
show_status
fi
#Check to see that UPLOADID is not blank
if [ -z "$UPLOADID" ]
then
MESSAGE=$"The upload id cannot be blank."
show_status
fi
#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
MESSAGE=$"The server cannot be blank."
show_status
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/web_management_upload_files_select.cgi | cut -d' ' -f1`
#Copy data to group
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="infobox">'
sudo -H /opt/karoshi/web_controls/exec/web_management_upload_files $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$UPLOADFOLDER:$UPLOADID:$SERVERNAME:

UPLOADFOLDER=`echo $UPLOADFOLDER | sed 's/UNDERSCORE/_/g'`
MESSAGE=`echo $"The files have been uploaded to the following path" : $UPLOADFOLDER`
show_status
exit
