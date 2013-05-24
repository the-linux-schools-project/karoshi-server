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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/staff_restrictions ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/staff_restrictions
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/staff_restrictions.cgi";'
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

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/staff_restrictions2.cgi" method="post"><div id="actionbox"><b>'$TITLE'</b><br><br>'
echo '<table class="standard" style="text-align: left; height: 20px;" border="0" cellpadding="2" cellspacing="2">'
echo '<tbody>'
echo '<tr><td style="width: 180px;">'$ADDSTAFFMSG'</td><td><input name="_STAFFNAME_" size="25" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td></tr>'
echo '</tbody></table>'

if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
STAFF_COUNT=`cat /opt/karoshi/web_controls/staff_restrictions.txt | wc -l`
else
STAFF_COUNT=0
fi
#Show restricted staff list
if [ $STAFF_COUNT -gt 0 ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">'
echo '<tbody>'
echo '<tr><td style="width: 150px;"><b>'$RESTRICTEDMSG'</b></td><td><b>Remove</b></td></tr>'
echo '</tbody></table><br>'
echo '<table class="standard" style="text-align: left; width: 334px;" border="0" cellpadding="2" cellspacing="2">'
echo '<tbody>'
COUNTER=1
while [ $COUNTER -le $STAFF_COUNT ]
do
STAFFNAME=`sed -n $COUNTER,$COUNTER'p' /opt/karoshi/web_controls/staff_restrictions.txt`
echo '<tr><td style="width: 150px;">'$STAFFNAME'</td><td><input type="radio" name="_DELETE_" value="'$STAFFNAME'"><br></td></tr>'
let COUNTER=$COUNTER+1
done
echo '</tbody></table>'
fi
echo "</div>"
echo '<div id="submitbox"><input value="Submit" type="submit"> <input value="Reset" type="reset"></div>'
echo '</form></body></html>'
exit
