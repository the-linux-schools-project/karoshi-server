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
#  ___LINUXVERSION___
#  ___SOFTWARE___
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_set_repository ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_set_repository
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\%+-'`
#Convert underscores
DATA=`echo $DATA | sed 's/___/tripleunderscore/g' | sed 's/_/underscore/g' | sed 's/tripleunderscore/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=10
#Assign LINUXVERSION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LINUXVERSIONcheck ]
then
let COUNTER=$COUNTER+1
LINUXVERSION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _URI_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = URIcheck ]
then
let COUNTER=$COUNTER+1
URI=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/underscore/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _DISTRIBUTION_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DISTRIBUTIONcheck ]
then
let COUNTER=$COUNTER+1
DISTRIBUTION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/underscore/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _SECTIONS_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SECTIONScheck ]
then
let COUNTER=$COUNTER+1
SECTIONS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/underscore/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _LINUXVERSION_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LINUXVERSIONcheck ]
then
let COUNTER=$COUNTER+1
LINUXVERSION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/underscore/_/g'`
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
#Check to see that LINUXVERSION is not blank
if [ $LINUXVERSION'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
URI
#Check to see that URI is not blank
if [ $URI'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that DISTRIBUTION is not blank
if [ $DISTRIBUTION'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
#Check to see that SECTIONS is not blank
if [ $SECTIONS'null' = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/linux_client_set_repository2.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/linux_client_set_repository $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$LINUXVERSION:$URI:$DISTRIBUTION:$SECTIONS
SOFTWARESTATUS=`echo $?`
MESSAGE=`echo $LINUXVERSION: $COMPLETEDMSG`
if [ $SOFTWARESTATUS = 101 ]
then
MESSAGE=$ERRORMSG4
fi
if [ $SOFTWARESTATUS = 102 ]
then
MESSAGE=$ERRORMSG4
fi
show_status
exit

