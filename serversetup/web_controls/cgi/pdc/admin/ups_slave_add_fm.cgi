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
#jsharrad@karoshi.org.uk

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
MOBILE=no
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

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/ups_add_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE5'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script language="JavaScript" src="/all/calendar/ts_picker.js" type="text/javascript"></script>
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
echo '<form action="/cgi-bin/admin/ups_slave_add.cgi" name="tstest" method="post"><div id="actionbox"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>
<td style="vertical-align: top;"><div class="sectiontitle">'$TITLE5'</div></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELP1'</span></a></td></tr></tbody></table><br>'


#Check to see if there are any master ups available

if [ ! -d /opt/karoshi/server_network/ups/master ]
then
MESSAGE=$ERRORMSG7
show_status
fi

if [ `ls -1 /opt/karoshi/server_network/ups/master/ | wc -l` = 0 ]
then
MESSAGE=$ERRORMSG7
show_status
fi

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;">'$MASTERUPSMSG'</td>
        <td>'
#Generate list of UPC data
echo '<select name="_UPSSERVER_" style="width: 200px;"><option> </option>'

for UPSSERVERS in /opt/karoshi/server_network/ups/master/*
do
UPSSERVER=`basename $UPSSERVERS`
if [ -d /opt/karoshi/server_network/ups/master/$UPSSERVER/drivers/ ]
then
if [ `ls -1 /opt/karoshi/server_network/ups/master/$UPSSERVER/drivers/ | wc -l` != 0 ]
then
for UPSMODELS in /opt/karoshi/server_network/ups/master/$UPSSERVER/drivers/*
do
UPSMODEL=`basename $UPSMODELS`
echo '<option value="'$UPSSERVER','$UPSMODEL'">'$UPSSERVER': '$UPSMODEL'</option>'
done
fi
fi
done
echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELP4'</span></a></td></tr>
</tbody></table><br><br>'

#Show list of ssh enabled servers that do not have a main UPS
/opt/karoshi/web_controls/show_servers $MOBILE addslaveups "$ACTIONMSG2"
echo '</div></form></div></body></html>'
exit

