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

############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/banned_users_view ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/banned_users_view
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/css/pro_dropdown_2/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA_ARRAY=( `echo $DATA | sed 's/_USERNAME_/_USERNAME_ /g' | sed 's/_VIEWLOG_/_VIEWLOG_ /g'` )
END_POINT=`echo ${#DATA_ARRAY[@]}`
let END_POINT=$END_POINT*2
#Assign USERARRAY
COUNTER=2
ARRAY_COUNT=0
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
then
let COUNTER=$COUNTER+1
USERARRAY[$ARRAY_COUNT]=`echo $DATA | cut -s -d'_' -f$COUNTER`
let ARRAY_COUNT=$ARRAY_COUNT+1
fi
let COUNTER=$COUNTER+1
done

#Assign VIEWARRAY
COUNTER=2
ARRAY_COUNT=0
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = VIEWLOGcheck ]
then
let COUNTER=$COUNTER+1
VIEWARRAY[$ARRAY_COUNT]=`echo $DATA | cut -s -d'_' -f$COUNTER`
let ARRAY_COUNT=$ARRAY_COUNT+1
fi
let COUNTER=$COUNTER+1
done

#########################
#Assign data to variables
#########################
END_POINT=4

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/banned_users_view_fm.cgi";'
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

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/banned_users_view2.cgi | cut -d' ' -f1`
if [ $USERARRAY'null' != null ]
then
#Allow users
sudo -H /opt/karoshi/web_controls/exec/banned_users_view2 $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:`echo ${USERARRAY[@]:0} | sed 's/ /:/g'`
#View any chosen logs
MESSAGE=$COMPLETEDMSG
show_status
fi

if [ $VIEWARRAY'null' != null ]
then
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo "<div id="actionbox">"
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:`echo ${VIEWARRAY[@]:0} | sed 's/ /:/g'`" | sudo -H /opt/karoshi/web_controls/exec/incident_log_view2
echo "</div>"
fi
echo "</div></body></html>"
