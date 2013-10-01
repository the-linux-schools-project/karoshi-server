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
########################
#Required input variables
########################
#  _CERTTYPE_
#  _SERVER_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/ssl_certs ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/ssl_certs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################

END_POINT=10

#Assign SERVER
#SERVER=`echo $DATA | cut -d_ -f6`

#Assign SERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERcheck ]
then
let COUNTER=$COUNTER+1
SERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/ssl_certs_commercial_fm.cgi";'
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
#Check to see that SERVER is not blank
if [ $SERVER'null' = null ]
then
MESSAGE=$ERRORMSG10
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
#Fill in form for certificate

echo '<form action="/cgi-bin/admin/ssl_certs_commercial_create2.cgi" method="post"><div id="actionbox"><b>'$SERVER' - '$TITLE1'</b><br><br>'

#Get current certificate data if it has been set
COUNTRYCODE=GB
STATE=County
LOCALITY=City
ORGANISATIONNAME=School
UNITNAME=ICT_Dept
COMMONNAME=$HOSTNAME
CONTACTEMAIL=email
if [ -f /opt/karoshi/server_network/ssl/cert_data/$SERVER ]
then
COUNTRYCODE=`sed -n 1,1p /opt/karoshi/server_network/ssl/cert_data/$SERVER`
STATE=`sed -n 2,2p /opt/karoshi/server_network/ssl/cert_data/$SERVER`
LOCALITY=`sed -n 3,3p /opt/karoshi/server_network/ssl/cert_data/$SERVER`
ORGANISATIONNAME=`sed -n 4,4p /opt/karoshi/server_network/ssl/cert_data/$SERVER`
UNITNAME=`sed -n 5,5p /opt/karoshi/server_network/ssl/cert_data/$SERVER`
COMMONNAME=`sed -n 6,6p /opt/karoshi/server_network/ssl/cert_data/$SERVER`
CONTACTEMAIL=`sed -n 7,7p /opt/karoshi/server_network/ssl/cert_data/$SERVER`
fi

echo '<table class="standard"><tbody>'
echo '<tr><td style="width: 180px;">'$COUNTRYCODEMSG'</td><td><input tabindex= "1" value="'$COUNTRYCODE'" name="___COUNTRYCODE___" maxlength="2" size="25" type="text"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$COUNTRYCODEHELP'<br><br>'$COMMONNAMEHELP2'</span></a></td>
</tr>'
echo '<tr><td>'$STATEMSG'</td><td><input tabindex= "2" value="'$STATE'" name="___STATE___" size="25" type="text"></td></tr>'
echo '<tr><td>'$CITYMSG'</td><td><input tabindex= "3" value="'$LOCALITY'" name="___LOCALITY___" size="25" type="text"></td></tr>'
echo '<tr><td>'$SCHOOLMSG'</td><td><input tabindex= "4" value="'$ORGANISATIONNAME'" name="___INSTITUTENAME___" size="25" type="text"></td></tr>'
echo '<tr><td>'$DEPTNAMEMSG'</td><td><input tabindex= "5" value="'$UNITNAME'" name="___DEPARTMENT___" size="25" type="text"></td></tr>'
echo '<tr><td>'$COMMONNAMEMSG'</td><td><input tabindex= "6" value="'$COMMONNAME'" name="___COMMONNAME___" size="25" type="text"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$COMMONNAMEHELP'<br><br>'$COMMONNAMEHELP2'</span></a></td>
</tr>'
echo '<tr><td>'$EMAILMSG'</td><td><input tabindex= "7" value="'$CONTACTEMAIL'" name="___EMAIL___" size="25" type="text"></td></tr>'
echo '</tbody></table>'

echo '<input name="___SERVER___" value="'$SERVER'" type="hidden">'
echo '</div><div id="submitbox"><input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"></div>'
echo '</form></body</html>'

exit
