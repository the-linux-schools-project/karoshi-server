#!/bin/bash
#Copyright (C) 2013 Paul Sharrad

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
#  _VERSION_
#  _INSTALL_
#  _UPDATES_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_install_software_packages ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_install_software_packages
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`echo $DATA | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=17
#Assign VERSION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = VERSIONcheck ]
then
let COUNTER=$COUNTER+1
VERSION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign LIST
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LISTcheck ]
then
let COUNTER=$COUNTER+1
LIST=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
#Assign SOFTWARE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SOFTWAREcheck ]
then
let COUNTER=$COUNTER+1
SOFTWARE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "linux_client_install_software_packages_fm.cgi"'
echo '</script>'
echo "</body></html>"
exit
}

function completed {
echo '<form name="myForm" id="myForm" action="/cgi-bin/admin/linux_client_install_software_packages.cgi" method="post"><input name="_VERSION_" value="'$VERSION'" type="hidden"></form>'
echo "<script type='text/javascript'>document.myForm.submit();</script></body></html>"
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
#Check to see that VERSION is not blank
if [ -z "$VERSION" ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Check to see that LIST is not blank
if [ -z "$LIST" ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that ACTION is not blank
if [ -z "$ACTION" ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Check to see that SOFTWARE is not blank
if [ -z "$SOFTWARE" ]
then
MESSAGE=$ERRORMSG4
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/linux_client_install_software_packages2.cgi | cut -d' ' -f1`
#Set software control options
sudo -H /opt/karoshi/web_controls/exec/linux_client_install_software_packages $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$VERSION:$LIST:$ACTION:$SOFTWARE:
completed
exit