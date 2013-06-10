#!/bin/bash
#Copyright (C) 2010  Paul Sharrad
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script language="JavaScript" src="/all/calendar/ts_picker.js" type="text/javascript"></script>
        <!-- Timestamp input popup (European Format) --><script src="/all/stuHover.js" type="text/javascript"></script>'
echo "</head>"
echo "<body onLoad="start()">"
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
echo '<form action="/cgi-bin/admin/ups_add.cgi" name="tstest" method="post"><div id="actionbox"><b>'$TITLE1'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELP1'</span></a><br><br>'


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

echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELP2'</span></a></td></tr>
<tr><td>'$PORTMSG'</td><td><select name="_UPSPORT_" style="width: 200px;"><option value="auto">auto</option><option value="/dev/ttyS0">/dev/ttyS0</option><option value="/dev/ttyS1">/dev/ttyS1</option></select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELP3'</span></a></td></tr>
</tbody></table><br><br>'

#Show list of ssh enabled servers
SERVERLISTARRAY=( `ls -1 /opt/karoshi/server_network/servers` )
SERVERLISTCOUNT=${#SERVERLISTARRAY[@]}
SERVERCOUNTER=0
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'

while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_SERVER_'$KAROSHISERVER'_" type="image" class="images" src="'$SERVERICON'" value="_SERVER_'$KAROSHISERVER'_"><span>'$KAROSHISERVER'<br><br>'
cat /opt/karoshi/server_network/servers/$KAROSHISERVER/* | sed '/<a href/c'"<br>"
echo '</span></a><br>'$KAROSHISERVER'</td>'
[ $SERVERCOUNTER = 5 ] && echo '</tr><tr>'
let SERVERCOUNTER=$SERVERCOUNTER+1
done
echo '</tr></tbody></table></div></form></body></html>'
exit




