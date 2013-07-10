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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/ssl_certs ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/ssl_certs
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

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE4'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body onLoad="start()">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=8
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

[ $SERVER'null' = null ] && SERVER=notset

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

############################
#Stage 1 - Create server key and server.crt
############################

echo '<div id="actionbox"><b>1 - '$TITLE1'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Commercial_SSL_Certificate"><img class="images" alt="" src="/images/help/info.png"><span>'"$HELPMSG2"'</span></a>
<br><br>'
#Show list of karoshi servers
SERVERLISTARRAY=( `ls -1 /opt/karoshi/server_network/servers/` )
SERVERLISTCOUNT=${#SERVERLISTARRAY[@]}
SERVERCOUNTER=0
CONTACTCOUNT=0
SERVERICON="/images/submenus/system/computer.png"
SERVERICON2="/images/submenus/system/all_computers.png"
SERVERICON3="/images/submenus/system/grey_computer.png"
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
if [ -f /opt/karoshi/server_network/ssl/commercial_ssl_certs/web-management ] && [ $SERVER != web-management ]
then
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><form action="/cgi-bin/admin/ssl_certs_commercial_fm.cgi" name="selectservers" method="post"><a class="info" href="javascript:void(0)"><input name="_SERVER_web-management_" type="image" class="images" src="'$SERVERICON3'" value=""><span>Web Management</span></a><br>Web Management</form></td>'
let CONTACTCOUNT=$CONTACTCOUNT+1
else
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><form action="/cgi-bin/admin/ssl_certs_commercial_create.cgi" name="selectservers" method="post"><a class="info" href="javascript:void(0)"><input name="_SERVER__web-management_" type="image" class="images" src="'$SERVERICON2'" value=""><span>Web Management</span></a><br>Web Management</form></td>'
fi
while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}
if [ -f /opt/karoshi/server_network/ssl/commercial_ssl_certs/$KAROSHISERVER ] && [ $KAROSHISERVER != $SERVER ]
then
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><form action="/cgi-bin/admin/ssl_certs_commercial_fm.cgi" name="selectservers" method="post"><a class="info" href="javascript:void(0)"><input name="_SERVER_'$KAROSHISERVER'_" type="image" class="images" src="'$SERVERICON3'" value=""><span>'$KAROSHISERVER'<br><br>'
cat /opt/karoshi/server_network/servers/$KAROSHISERVER/* | sed '/<a href/c'"&nbsp"
echo '</span></a><br>'$KAROSHISERVER'</form></td>'
let CONTACTCOUNT=$CONTACTCOUNT+1
else
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><form action="/cgi-bin/admin/ssl_certs_commercial_create.cgi" name="selectservers" method="post"><a class="info" href="javascript:void(0)"><input name="_SERVER_'$KAROSHISERVER'_" type="image" class="images" src="'$SERVERICON'" value="'$KAROSHISERVER'"><span>'$KAROSHISERVER'<br><br>'
cat /opt/karoshi/server_network/servers/$KAROSHISERVER/* | sed '/<a href/c'"&nbsp"
echo '</span></a><br>'$KAROSHISERVER'</form></td>'

fi
[ $SERVERCOUNTER = 5 ] && echo '</tr><tr>'
let SERVERCOUNTER=$SERVERCOUNTER+1
done

echo  '</tr></tbody></table><br>'


############################
#Stage 2 - Create contact info
############################

if [ $CONTACTCOUNT -gt 0 ]
then
echo '<b>2 - '$TITLE5'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG4'</span></a><br><br>'

SERVERCOUNTER=0
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
if [ -f /opt/karoshi/server_network/ssl/commercial_ssl_certs/web-management ] && [ $SERVER != web-management ]
then
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><form action="/cgi-bin/admin/ssl_certs_commercial_show_crt.cgi" name="selectservers" method="post"><a class="info" href="javascript:void(0)"><input name="___SERVER___web-management___" type="image" class="images" src="'$SERVERICON2'" value="webmanagement"><span>Web Management</span></a><br>Web Management</form></td>'
else
echo '<td style="width: 90px; vertical-align: top; text-align: left;"></td>'
fi
while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}
if [ -f /opt/karoshi/server_network/ssl/commercial_ssl_certs/$KAROSHISERVER ] && [ $KAROSHISERVER != $SERVER ]
then
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><form action="/cgi-bin/admin/ssl_certs_commercial_show_crt.cgi" name="selectservers" method="post"><a class="info" href="javascript:void(0)"><input name="___SERVER___'$KAROSHISERVER'___" type="image" class="images" src="'$SERVERICON'" value="'$KAROSHISERVER'"><span>'$KAROSHISERVER'</span></a><br>'$KAROSHISERVER'</form></td>'
else
echo '<td style="width: 90px; vertical-align: top; text-align: left;"></td>'

fi
[ $SERVERCOUNTER = 5 ] && echo '</tr><tr>'
let SERVERCOUNTER=$SERVERCOUNTER+1
done
echo '</tr></tbody></table><br>'
fi

############################
#Stage 3 - Install Certificate
############################

if [ $CONTACTCOUNT -gt 0 ]
then
echo '<b>3 - '$TITLE7'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG6'</span></a><br><br>'

SERVERCOUNTER=0
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
if [ -f /opt/karoshi/server_network/ssl/commercial_ssl_certs/web-management ] && [ $SERVER != web-management ]
then
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><form action="/cgi-bin/admin/ssl_certs_commercial_install.cgi" name="selectservers" method="post"><a class="info" href="javascript:void(0)"><input name="___SERVER___web-management___" type="image" class="images" src="'$SERVERICON2'" value="webmanagement"><span>Web Management</span></a><br>Web Management</form></td>'
else
echo '<td style="width: 90px; vertical-align: top; text-align: left;"></td>'
fi
while [ $SERVERCOUNTER -lt $SERVERLISTCOUNT ]
do
KAROSHISERVER=${SERVERLISTARRAY[$SERVERCOUNTER]}
if [ -f /opt/karoshi/server_network/ssl/commercial_ssl_certs/$KAROSHISERVER ] && [ $KAROSHISERVER != $SERVER ]
then
echo '<td style="width: 90px; vertical-align: top; text-align: left;"><form action="/cgi-bin/admin/ssl_certs_commercial_install.cgi" name="selectservers" method="post"><a class="info" href="javascript:void(0)"><input name="___SERVER___'$KAROSHISERVER'___" type="image" class="images" src="'$SERVERICON'" value="'$KAROSHISERVER'"><span>'$KAROSHISERVER'</span></a><br>'$KAROSHISERVER'</form></td>'
else
echo '<td style="width: 90px; vertical-align: top; text-align: left;"></td>'

fi
[ $SERVERCOUNTER = 5 ] && echo '</tr><tr>'
let SERVERCOUNTER=$SERVERCOUNTER+1
done
echo '</tr></tbody></table><br>'
fi

echo '</div></body></html>'
exit
