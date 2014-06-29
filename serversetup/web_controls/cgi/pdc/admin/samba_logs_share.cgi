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
########################
#Required input variables
########################
#  _USERNAME_
#  _SURNAME_
# _DAY_
# _MONTH_
# _YEAR_
##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/samba_view_logs ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/samba_view_logs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE3'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=11
#Assign SHARE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SHAREcheck ]
then
let COUNTER=$COUNTER+1
SHARE=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Assign DAYCOUNT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DAYCOUNTcheck ]
then
let COUNTER=$COUNTER+1
DAYCOUNT=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9-'`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/samba_logs_share_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
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
#Check to see that SHARE is not blank
if [ $SHARE'null' = null ]
then
MESSAGE=$ERRORMSG22
show_status
fi
#Check to see that DATE is not blank
if [ $DATE'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

DAY=`echo $DATE | cut -d- -f1`
MONTH=`echo $DATE | cut -d- -f2`
YEAR=`echo $DATE | cut -d- -f3`

#Check to see that DAYCOUNT is not blank
if [ $DAYCOUNT'null' = null ]
then
DAYCOUNT=1
fi

#Check that DAYCOUNT is not greater than 99
if [ $DAYCOUNT -gt 99 ]
then
MESSAGE=$ERRORMSG15
show_status
fi

#Loop round for the number of days to check the log for
COUNTER=1
while [ $COUNTER -le $DAYCOUNT ]
do
#Check to see that DAY is not blank
if [ $DAY'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that MONTH is not blank
if [ $MONTH'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that YEAR is not blank
if [ $YEAR'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check that day is not greater than 31
if [ $DAY -gt 31 ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Check that the month is not greater than 12
if [ $MONTH -gt 12 ]
then
MESSAGE=$ERRORMSG3
show_status
fi

if [ $YEAR -lt 2006 ] || [ $YEAR -gt 3006 ]
then
MESSAGE=$ERRORMSG4
show_status
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/samba_logs_share.cgi | cut -d' ' -f1`
#View logs
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SHARE:$DAY:$MONTH:$YEAR:" | sudo -H /opt/karoshi/web_controls/exec/samba_logs_share
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
show_status
fi
if [ $EXEC_STATUS = 102 ]
then
echo '<b>'$TITLE3 $SHARE $DAY-$MONTH-$YEAR : $ERRORMSG5'</b><br><br>'
fi

# Add one to the day
DATE=`date +%F -d "$YEAR-$MONTH-$DAY 1 days"`

DAY=`echo $DATE | cut -d- -f3`
MONTH=`echo $DATE | cut -d- -f2`
YEAR=`echo $DATE | cut -d- -f1`

let COUNTER=$COUNTER+1
done

echo '</div></div></body></html>'
exit
