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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_ppd_assign ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_ppd_assign
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
echo "</body></html>"
exit
}

function view_printers {
echo '<SCRIPT language="Javascript">'
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
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
#Check to see that PRINTERNAME is not blank
if [ $PRINTERNAME'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
#Check to see that PAGESIZE is not blank
if [ $PAGESIZE'null' = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi
#Check to see that Colour is not blank
if [ $COLOUR'null' = null ]
then
MESSAGE=$ERRORMSG5
show_status
fi
#Check to see that PRINTERPPD is not blank
if [ $PRINTERPPD'null' = null ]
then
MESSAGE=$ERRORMSG7
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

echo "<div id="actionbox">"
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers_ppd_assign2.cgi | cut -d' ' -f1`
#Add ppd file to printer
sudo -H /opt/karoshi/web_controls/exec/printers_ppd_assign $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$PRINTERNAME:$PAGESIZE:$COLOUR:$PRINTERPPD
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $ERRORMSG6`
show_status
fi
MESSAGE=`echo $COMPLETEDMSG $PRINTERNAME`
show_status
echo "</div>"
echo "</body></html>"
exit
