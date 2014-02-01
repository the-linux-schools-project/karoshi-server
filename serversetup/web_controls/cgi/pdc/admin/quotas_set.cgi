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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
########################
#Required input variables
########################
#  _SERVER_
##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/file/quotas_set ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/file/quotas_set
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox"><b>'$TITLE'</b>
  <br>
  <br>
'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=10
#Assign GROUP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = GROUPcheck ]
then
let COUNTER=$COUNTER+1
GROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign SIZE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SIZEcheck ]
then
let COUNTER=$COUNTER+1
SIZE=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9/n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign MAXFILES
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MAXFILEScheck ]
then
let COUNTER=$COUNTER+1
MAXFILES=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign UNIT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = UNITcheck ]
then
let COUNTER=$COUNTER+1
UNIT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign USERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
then
let COUNTER=$COUNTER+1
USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/quotas_set_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
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
#Check to see that USER and GROUP are not blank
if [ $GROUP'null' = null ] && [ $USERNAME'null' = null ] 
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that SIZE is not blank
if [ $SIZE'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that UNIT is not blank
if [ $UNIT'null' = null ]
then
MESSAGE=$ERRORMSG5
show_status
fi
#Check that UNIT is the correct value
if [ $UNIT != MB ] && [ $UNIT != GB ] && [ $UNIT != TB ] 
then
MESSAGE=$ERRORMSG6
show_status
fi
#Check to see that MAXFILES is not blank
MAXFILES=`echo $MAXFILES | tr -cd '0-9/n'`
if [ $MAXFILES'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
#Check to see that MAXFILES is not blank
MAXFILES=`echo $MAXFILES | tr -cd '0-9/n'`
if [ $MAXFILES'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
#Check to see that USERNAME exists if USERNAME is not blank
if [ $USERNAME'null' != null ]
then
getent passwd $USERNAME 1>/dev/null 2>/dev/null
if [ `echo $?` != 0 ]
then
MESSAGE=`echo $USERNAME - $ERRORMSG7`
show_status
fi
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/quotas_set.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$GROUP:$SIZE:$MAXFILES:$UNIT:$USERNAME:" | sudo -H /opt/karoshi/web_controls/exec/quotas_set
echo "</div></div></body></html>"
exit

