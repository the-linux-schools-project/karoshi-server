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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/dhcp ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/dhcp
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
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

DHCPSERVER=dhcp3-server

echo '<div id="actionbox3"><div id="titlebox">


<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tr><td style="vertical-align: top; width:180px"><div class="sectiontitle">'$TITLE2'</div></td><td style="vertical-align: top;"><a href="dhcp_fm.cgi"><input class="button" type="button" name="" value="'$TITLE'"></a></td><td style="vertical-align: top;"><a href="dhcp_reservations.cgi"><input class="button" type="button" name="" value="'$TITLE3'"></a></td>
</tr>
</tbody></table><br>
</div><div id="infobox"><br>'

LEASEPATH=/var/lib/dhcp/dhcpd.leases
[ -d /var/lib/dhcp3 ] && LEASEPATH=/var/lib/dhcp3/dhcpd.leases

if [ ! -f $LEASEPATH ]
then
echo $ERRORMSG1
echo '</div></div></body></html>'
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
echo '</tbody></table></div></div></body></html>'

exit
