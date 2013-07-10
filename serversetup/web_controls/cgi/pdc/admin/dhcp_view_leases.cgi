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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/dhcp_view_leases ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/dhcp_view_leases
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
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

#Check what we are using for dhcp
if [ `grep -c ^conf-dir=/etc/dnsmasq.d /etc/dnsmasq.conf` -gt 0 ]
then
#Using dnsmasq
DHCPSERVER=dnsmasq
else
#Using dhcp3-server
DHCPSERVER=dhcp3-server
fi

echo '<div id="actionbox"><b>'$TITLE'</b><br><br>'

if [ $DHCPSERVER = dhcp3-server ]
then
LEASEPATH=/var/lib/dhcp/dhcpd.leases
[ -d /var/lib/dhcp3 ] && LEASEPATH=/var/lib/dhcp3/dhcpd.leases

if [ ! -f $LEASEPATH ]
then
echo $ERRORMSG1
echo '</div></body></html>'
exit
fi

#Get ipnumbers of leases
IPNUMBERS=( `grep -w ^lease $LEASEPATH | cut -d' ' -f2` )
#Get start times
STARTTIMES=( `grep -w starts $LEASEPATH | cut -d' ' -f5,6 | sed 's/;//g' | sed 's/ /_/g'` )
#Get end times
ENDTIMES=( `grep -w ends $LEASEPATH | cut -d' ' -f5,6 | sed 's/;//g' | sed 's/ /_/g'` )
#Get mac addresses
MACADDRESSES=( `grep -w hardware $LEASEPATH | cut -d' ' -f5 | sed 's/;//g'` )
#Get binding state
BINDINGSTATES=( `grep -w " binding state" $LEASEPATH | cut -d' ' -f 5 | sed 's/;//g'` )


LEASECOUNT=${#IPNUMBERS[@]}

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tr><td style="width: 120px;"><b>'$TCPIPMSG'</b></td><td style="width: 170px;"><b>'$STARTMSG'</b></td><td style="width: 170px;"><b>'$ENDMSG'</b></td><td style="width: 130px;"><b>'$MACMSG'</b></td><td style="width: 80px;"><b>'$STATUSMSG'</b></td></tr>'
#Show active leases
COUNTER=0
while [ $COUNTER -lt $LEASECOUNT ]
do
if [ `echo ${BINDINGSTATES[$COUNTER]} | sed 's/ //g'` = active ]
then
#Create table
echo "<tr><td>${IPNUMBERS[$COUNTER]}</td><td>${STARTTIMES[$COUNTER]}</td><td>${ENDTIMES[$COUNTER]}</td><td>${MACADDRESSES[$COUNTER]}</td><td>${BINDINGSTATES[$COUNTER]}</td></tr>"
fi
let COUNTER=$COUNTER+1
done

#Show lapsed leases
COUNTER=0
while [ $COUNTER -lt $LEASECOUNT ]
do
if [ `echo ${BINDINGSTATES[$COUNTER]} | sed 's/ //g'` = free ]
then
#Create table
echo "<tr><td>${IPNUMBERS[$COUNTER]}</td><td>${STARTTIMES[$COUNTER]}</td><td>${ENDTIMES[$COUNTER]}</td><td>${MACADDRESSES[$COUNTER]}</td><td>${BINDINGSTATES[$COUNTER]}</td></tr>"
fi
let COUNTER=$COUNTER+1
done
echo '</tbody></table></div></body></html>'

else
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tr><td style="width: 120px;"><b>'$TCPIPMSG'</b></td><td style="width: 130px;"><b>'$MACMSG'</b></td><td style="width: 170px;"><b>'$NAMEMSG'</b></td><td style="width: 170px;"><b>'$ENDMSG'</b></td></tr>'
LEASECOUNT=`cat /var/lib/misc/dnsmasq.leases | wc -l`
COUNTER=1
while [ $COUNTER -le $LEASECOUNT ]
do
LEASEDATA=`sed -n $COUNTER,$COUNTER'p' /var/lib/misc/dnsmasq.leases`
EXPIRES=`echo $LEASEDATA | cut -d' ' -f1`
EXPIRES=`perl -e 'print scalar(localtime('$EXPIRES')), "\n"'`
MAC=`echo $LEASEDATA | cut -d' ' -f2`
TCPIP=`echo $LEASEDATA | cut -d' ' -f3`
NAME=`echo $LEASEDATA | cut -d' ' -f4`
echo '<tr><td>'$TCPIP'</td><td>'$MAC'</td><td>'$NAME'</td><td>'"$EXPIRES"'</td></tr>'

let COUNTER=$COUNTER+1
done
echo '</tbody></table>'
fi
exit
