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
#  _PRINTERNAME_
#  _LOCATION_
#  _PRINTERADDRESS_
#  _PRINTERQUEUE_
#  _PRINTERDESC_
#  _PRINTERTYPE_
#  _PRINTERPORT_
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Add Network Printer"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%/+-'`
#########################
#Assign data to variables
#########################
END_POINT=14
#Assign PRINTERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRINTERNAMEcheck ]
then
let COUNTER=$COUNTER+1
PRINTERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER |  tr -cd 'A-Za-z0-9_'`
break
fi
let COUNTER=$COUNTER+1
done
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
#Assign PRINTERADDRESS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRINTERADDRESScheck ]
then
let COUNTER=$COUNTER+1
PRINTERADDRESS=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PRINTERQUEUE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRINTERQUEUEcheck ]
then
let COUNTER=$COUNTER+1
PRINTERQUEUE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PRINTERTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRINTERTYPEcheck ]
then
let COUNTER=$COUNTER+1
PRINTERTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PRINTERDESC
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRINTERDESCcheck ]
then
let COUNTER=$COUNTER+1
PRINTERDESC=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PRINTERPORT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRINTERPORTcheck ]
then
let COUNTER=$COUNTER+1
PRINTERPORT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_printers {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers_add_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function add_ppd {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
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
#Check to see that PRINTERNAME is not blank
if [ $PRINTERNAME'null' = null ]
then
MESSAGE=$"The printer name cannot be blank."
show_status
fi
#Check to see that PRINTERADDRESS is not blank
if [ $PRINTERADDRESS'null' = null ]
then
MESSAGE=$"The printer address cannot be blank."
show_status
fi
#Check to see that PRINTERTYPE is not blank
if [ $PRINTERTYPE'null' = null ]
then
MESSAGE=$"The printer type cannot be blank."
show_status
fi
#Check to see that PRINTERPORT is not blank
if [ $PRINTERPORT'null' = null ]
then
MESSAGE=$"The printer port cannot be blank."
show_status
fi

#Check that this printer has not already been added
if [ `lpstat -a | grep -c -w ^$PRINTERNAME` != 0 ]
then
MESSAGE=$"This printer queue already exists."
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers_add.cgi | cut -d' ' -f1`
#Add printer
sudo -H /opt/karoshi/web_controls/exec/printers_add $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$PRINTERNAME:$LOCATION:$PRINTERADDRESS:$PRINTERQUEUE:$PRINTERDESC:$PRINTERTYPE:$PRINTERPORT
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $"There was a problem with this action.": $"Please check the karoshi web administration logs for more details."`
else
MESSAGE=`echo $PRINTERNAME - $"Printer added."`
fi
show_printers
echo "</div></body></html>"
exit
