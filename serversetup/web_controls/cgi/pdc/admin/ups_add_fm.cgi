#!/bin/bash
#Copyright (C) 2010  Paul Sharrad

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

#Language
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/ups ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/ups
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

#Get current date and time
DAY=`date +%d`
MONTH=`date +%m`
YEAR=`date +%Y`

HOUR=`date +%H`
MINUTES=`date +%M`
SECONDS=`date +%S`

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script language="JavaScript" src="/all/calendar/ts_picker.js" type="text/javascript"></script>
        <!-- Timestamp input popup (European Format) --><script src="/all/stuHover.js" type="text/javascript"></script>'
echo "</head>"
echo '<body onLoad="start()"><div id="pagecontainer">'
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
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/ups_add.cgi" name="tstest" method="post"><div id="actionbox3"><div id="titlebox"><b>'$TITLE1'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_a_UPS"><img class="images" alt="" src="/images/help/info.png"><span>'$HELP1'</span></a>
<br><br></div><div id="infobox">'


echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;">'$UPSNAMEMSG'</td>
        <td>'
#Generate list of UPC data
echo '<select name="_UPSDRIVER_" style="width: 200px;">'
UPSDATA_LENGTH=`cat /opt/karoshi/server_network/ups/ups-model-information.csv | wc -l`

COUNTER=1
while [ $COUNTER -le $UPSDATA_LENGTH ]
do
UPSDATA=`sed -n $COUNTER,$COUNTER'p' /opt/karoshi/server_network/ups/ups-model-information.csv`
UPSMAKE=`echo $UPSDATA | cut -d, -f1,2 | sed 's/,/: /g'`
UPSMODEL=`echo $UPSDATA | cut -d, -f2`
UPSDRIVER=`echo $UPSDATA | cut -d, -f3`
echo '<option value="'$UPSMODEL,$UPSDRIVER'">'$UPSMAKE'</option>'
let COUNTER=$COUNTER+1
done

echo '</select></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_a_UPS"><img class="images" alt="" src="/images/help/info.png"><span>'$HELP2'</span></a></td></tr>
<tr><td>'$PORTMSG'</td><td><select name="_UPSPORT_" style="width: 200px;"><option value="auto">auto</option><option value="/dev/ttyS0">/dev/ttyS0</option><option value="/dev/ttyS1">/dev/ttyS1</option></select></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_a_UPS"><img class="images" alt="" src="/images/help/info.png"><span>'$HELP3'</span></a></td></tr>
</tbody></table><br><br>'

#Show list of servers
/opt/karoshi/web_controls/show_servers no servers "$ACTIONMSG"

echo '</div></div></form></div></body></html>'
exit




