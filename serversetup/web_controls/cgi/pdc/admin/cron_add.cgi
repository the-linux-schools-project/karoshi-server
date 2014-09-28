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
########################
#Required input variables
########################
#  _MINUTES_
#  _HOUR_
#  _DAY_
#  _MONTH_
#  _DOFW_
#  _COMMAND_
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Schedule Job"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body><div id="pagecontainer">'
#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
fi
echo '<div id="'$DIV_ID'">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\/*%+"-' | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g' | sed 's/%A0+//g' | sed 's/%A0//g'`
#########################
#Assign data to variables
#########################
END_POINT=45
#Assign MINUTES
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MINUTEScheck ]
then
let COUNTER=$COUNTER+1
MINUTES=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign HOUR
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = HOURcheck ]
then
let COUNTER=$COUNTER+1
HOUR=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign DAY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DAYcheck ]
then
let COUNTER=$COUNTER+1
DAY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign MONTH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MONTHcheck ]
then
let COUNTER=$COUNTER+1
MONTH=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign DOFW
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DOFWcheck ]
then
let COUNTER=$COUNTER+1
DOFW=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign COMMAND
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = COMMANDcheck ]
then
let COUNTER=$COUNTER+1
COMMAND=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
echo 'window.location = "/cgi-bin/admin/cron_add_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

function show_jobs {
echo "
<form action=\"/cgi-bin/admin/cron_view.cgi\" method=\"post\" id=\"showdns\">
<input type=\"hidden\" name=\"_SERVERNAME_$SERVERNAME"_"SERVERTYPE_$SERVERTYPE"_"\" value=\"\">
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
#Check to see that MINUTES is not blank
if [ "$MINUTES"'null' = null ]
then
MESSAGE=$"The minutes must not be blank."
show_status
fi
#Check to see that HOUR is not blank
if [ "$HOUR"'null' = null ]
then
MESSAGE=$"The hour must not be blank."
show_status
fi
#Check to see DAY is not blank
if [ "$DAY"'null' = null ]
then
MESSAGE=$"The day must not be blank."
show_status
fi
#Check to see MONTH is not blank
if [ "$MONTH"'null' = null ]
then
MESSAGE=$"The month must not be blank."
show_status
fi
#Check to see DOFW is not blank
if [ "$DOFW"'null' = null ]
then
MESSAGE=$"The day of week must not be blank."
show_status
fi
#Check to see COMMAND is not blank
if [ "$COMMAND"'null' = null ]
then
MESSAGE=$"The command must not be blank."
show_status
fi
#Check to see SERVERNAME is not blank
if [ "$SERVERNAME"'null' = null ]
then
MESSAGE=$"The server must not be blank."
show_status
fi

#Check to see that SERVERTYPE is not blank
if [ $SERVERTYPE'null' = null ]
then
MESSAGE=$"The server cannot be blank."
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/cron_add.cgi | cut -d' ' -f1`
#Add cron job
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MINUTES:$HOUR:$DAY:$MONTH:$DOFW:$COMMAND:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:" | sudo -H /opt/karoshi/web_controls/exec/cron_add
show_jobs
echo "</div></div></body></html>"
exit

