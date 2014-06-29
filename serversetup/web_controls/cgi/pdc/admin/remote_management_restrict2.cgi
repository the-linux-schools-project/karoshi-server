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
#  _TCPADDRESS_
#  _ACTION_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/remote_management_restrict ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/remote_management_restrict
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=6
#Assign _USERACTION_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = USERACTIONcheck ]
then
let COUNTER=$COUNTER+1
USERACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function view_tcpip {
echo '<SCRIPT language="Javascript">'
echo '                window.location = "/cgi-bin/admin/remote_management_restrict.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/remote_management_restrict.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function add_tcpip {
echo '<SCRIPT language="Javascript">'
echo '                window.location = "/cgi-bin/admin/remote_management_restrict_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
MESSAGE=$HTTPS_ERROR
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
#Check to see that USERACTION is not blank
if [ $USERACTION'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

ACTION=not_set
if [ `echo $USERACTION | grep -c editip` = 1 ]
then
ACTION=edit
TCPADDRESS=`echo $USERACTION | sed 's/editip//g'`
fi

if [ `echo $USERACTION | grep -c deleteip` = 1 ]
then
ACTION=remove
TCPADDRESS=`echo $USERACTION | sed 's/deleteip//g'`
fi

if [ `echo $USERACTION | grep -c addip` = 1 ]
then
ACTION=add
TCPADDRESS=`echo $USERACTION | sed 's/deleteip//g'`
fi

#Check to see that action is correct
if [ $ACTION != edit ] && [ $ACTION != remove ] && [ $ACTION != add ]
then
MESSAGE=$ERRORMSG2
show_status
fi
if [ $ACTION = add ]
then
add_tcpip
fi
if [ `echo $TCPADDRESS | grep -c level1` = 1 ]
then
ACCESSLEVEL="1+2"
TCPADDRESS=`echo $TCPADDRESS | sed 's/level1//g'`
fi
if [ `echo $TCPADDRESS | grep -c level3` = 1 ]
then
ACCESSLEVEL="3"
TCPADDRESS=`echo $TCPADDRESS | sed 's/level3//g'`
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo "<div id="actionbox">"
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/remote_management_restrict2.cgi | cut -d' ' -f1`
if [ $ACTION = remove ]
then
sudo -H /opt/karoshi/web_controls/exec/remote_management_restrict $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$TCPADDRESS::$ACCESSLEVEL
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 102 ]
then
MESSAGE=$ERRORMSG7
show_status
fi
view_tcpip
fi
if [ $ACTION = edit ]
then
sudo -H /opt/karoshi/web_controls/exec/remote_management_restrict $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$TCPADDRESS::$ACCESSLEVEL
fi
echo "</div>"
echo "</div></body></html>"
exit
