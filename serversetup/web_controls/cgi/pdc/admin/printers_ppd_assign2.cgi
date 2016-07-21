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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Assign PPD File"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%/+-'`
#########################
#Assign data to variables
#########################
END_POINT=12
#Assign PRINTERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRINTERNAMEcheck ]
then
let COUNTER=$COUNTER+1
PRINTERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/123456789/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign COLOUR
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = COLOURcheck ]
then
let COUNTER=$COUNTER+1
COLOUR=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/123456789/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PAGESIZE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PAGESIZEcheck ]
then
let COUNTER=$COUNTER+1
PAGESIZE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/123456789/_/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PRINTERPPD
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PRINTERPPDcheck ]
then
let COUNTER=$COUNTER+1
PRINTERPPD=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/123456789/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function view_printers {
echo '<SCRIPT language="Javascript">'
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
#Check to see that PAGESIZE is not blank
if [ $PAGESIZE'null' = null ]
then
MESSAGE=$"The page size cannot be blank."
show_status
fi
#Check to see that Colour is not blank
if [ $COLOUR'null' = null ]
then
MESSAGE=$"The colour option cannot be blank."
show_status
fi
#Check to see that PRINTERPPD is not blank
if [ $PRINTERPPD'null' = null ]
then
MESSAGE=$"The printer ppd cannot be blank."
show_status
fi
#Check to see if we are uploading a ppd

if [ $PRINTERPPD = uploadppd ]
then
#Write data to temp file
echo PRINTERNAME=$PRINTERNAME > /var/www/karoshi/uploadppd
echo PAGESIZE=$PAGESIZE >> /var/www/karoshi/uploadppd
echo COLOUR=$COLOUR >> /var/www/karoshi/uploadppd
echo '<form name="setppd" action="/cgi-bin/admin/printers_ppd_upload_fm.cgi" method="post">
<input type="hidden" name="_PRINTERNAME_" value="'$PRINTERNAME'">
</form>
<script>
document.setppd.submit();
</script>'
exit
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers_ppd_assign2.cgi | cut -d' ' -f1`
#Add ppd file to printer
sudo -H /opt/karoshi/web_controls/exec/printers_ppd_assign $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$PRINTERNAME:$PAGESIZE:$COLOUR:$PRINTERPPD
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $"There was a problem adding this ppd. Please consult the Karoshi web administration logs."`
show_status
fi
MESSAGE=`echo $"The ppd file was added to" $PRINTERNAME`
show_status

echo "</div></body></html>"
exit
