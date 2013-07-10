#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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
#  _DNSACTION_ either adddnsentry deletednsentry viewdnsentries
#  _TCPIPENTRY_
#  _SHORTNAME_
#  _FULLNAME_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/dns ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/dns
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE4'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">'
echo "<link rel="stylesheet" href="/css/$STYLESHEET">"
echo "</head>"
echo "<body>"
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+'`
#########################
#Assign data to variables
#########################
END_POINT=11

#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
then
let COUNTER=$COUNTER+1
SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign SERVERTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERTYPEcheck ]
then
let COUNTER=$COUNTER+1
SERVERTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign _TCPIP_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPIPcheck ]
then
let COUNTER=$COUNTER+1
TCPIP=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ $TCPIPENTRY'null' != null ]
then
break
fi
fi
let COUNTER=$COUNTER+1
done
TCPIP=`echo $TCPIP | tr -cd '0-9\._:\n-'`

#Assign _DNSENTRY_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DNSENTRYcheck ]
then
let COUNTER=$COUNTER+1
DNSENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/dnsadd_fm.cgi";'
echo '</script>'
echo "</body></html>"
exit
}

function show_dns {
echo "
<form action=\"/cgi-bin/admin/dnsview.cgi\" method=\"post\" id=\"showdns\">
<input type="hidden" name="_SERVERNAME_$SERVERNAME"_"SERVERTYPE_$SERVERTYPE"_"ACTION_view_" value=''>
</form>
<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('showdns').submit();
//-->
</script>
</div></body></html>
"
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

#Check to see that SERVERNAME is not blank
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$ERRORMSG6
show_status
fi

#Check to see that SERVERTYPE is not blank
if [ $SERVERTYPE'null' = null ]
then
MESSAGE=$ERRORMSG7
show_status
fi

#Check to see that DNSENTRY is not blank
if [ $DNSENTRY'null' = null ]
then
MESSAGE=$ERRORMSG12
show_status
fi

#Check to see that TCPIP is not blank
if [ $TCPIP'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check that TCPIPENTRY is in correct format
if [ `echo $TCPIP | sed 's/\./\n /g'  | sed /^$/d | wc -l` != 4 ]
then
MESSAGE=$ERRORMSG5
show_status
fi

HIGHESTNUMBER=`echo $TCPIP | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p`
if [ $HIGHESTNUMBER -gt 255 ]
then
MESSAGE=$ERRORMSG6
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/dnsadd.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$TCPIP:$DNSENTRY:$SERVERNAME:$SERVERTYPE:" | sudo -H /opt/karoshi/web_controls/exec/dnsadd
if [ `echo $?` = 0 ]
then
show_dns
else
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
show_status
fi



echo '</body></html>'
exit
