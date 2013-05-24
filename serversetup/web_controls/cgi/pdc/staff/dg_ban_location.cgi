#!/bin/bash
#Copyright (C) 2007  Paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
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
#  _LOCATION_
##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
SLEEPTIME=5
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_location_controls ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_location_controls
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo "<html><head><title>$TITLE1</title><meta http-equiv='"'REFRESH'"' content='"'0; URL='$HTTP_REFERER''"'>"
echo '<link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=4

#Assign LOCATION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LOCATIONcheck ]
then
let COUNTER=$COUNTER+1
LOCATION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '</script>'
echo "</body></html>"
exit
}

#########################
#Check data
#########################
#Check to see that location is not blank
if [ $LOCATION'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that location is listed 
if [ `grep -c $LOCATION /var/lib/samba/netlogon/locations.txt` = 0 ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that the member of staff is not restricted
if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
if [ `grep -c -w $REMOTE_USER /opt/karoshi/web_controls/staff_restrictions.txt` -gt 0 ]
then
sudo -H /opt/karoshi/web_controls/exec/record_staff_error $REMOTE_USER:$REMOTE_ADDR:$REMOTE_USER
sleep $SLEEPTIME
MESSAGE=$ERRORMSG12
show_status
fi
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/staff/dg_ban_location.cgi | cut -d' ' -f1`
#Ban location
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$LOCATION:" | sudo -H /opt/karoshi/web_controls/exec/dg_ban_location
BAN_STATUS=`echo $?`
MESSAGE=`echo $LOCATION - $COMPLETEDMSG1`
[ $BAN_STATUS = 105 ] && MESSAGE=`echo $LOCATION - $ERRORMSG3`
[ $BAN_STATUS = 106 ] && MESSAGE=`echo $LOCATION - $ERRORMSG3`
show_status
exit
