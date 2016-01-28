#!/bin/bash
#Update Server Proxy Settings 
#Copyright (C) 2011  Paul Sharrad

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

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Configure Server Proxy Settings"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body onLoad="start()"><div id="pagecontainer">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/update_server_proxy_settings_choose_server_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=15

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

#Assign SERVERMASTER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERMASTERcheck ]
then
let COUNTER=$COUNTER+1
SERVERMASTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Check to see that a server has been picked to shut down
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$"The servername cannot be blank."
show_status
fi
#Check to see that a server type is not blank
if [ $SERVERTYPE'null' = null ]
then
MESSAGE=$"The servertype cannot be blank."
show_status
fi



#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/admin/update_server_proxy_settings.cgi" method="post"><div id="'$DIV_ID'">'

[ -f /opt/karoshi/server_network/upstream_proxy_settings/$SERVERNAME ] && source /opt/karoshi/server_network/upstream_proxy_settings/$SERVERNAME

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" >
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Configure Server Proxy Settings"' - '$SERVERNAME'</b></a></td></tr></tbody></table><br>'
else
echo '<b>'$"Configure Server Proxy Settings"' - '$SERVERNAME'</b><br><br>'
fi

if [ $MOBILE = yes ]
then
echo '
'$"Proxy name/TCPIP"'<br>
<input tabindex= "1" style="width: 160px;" name="_TCPIP_" value="'$TCPIP'" size="20" type="text"><br>
'$"Proxy Port"'<br>
<input tabindex= "2" style="width: 160px;" name="_PORT_" value="'$PORT'" size="20" type="text"><br>
'$"Username"'<br>
<input tabindex= "3" style="width: 160px;" name="_USERNAME_" 
 value="'$USERNAME'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"><br>
'$"Enter in the password needed to connect to the proxy server."'<br>
<input tabindex= "4" style="width: 160px;" name="_PASSWORD_" value="'$PASSWORD'" size="20" type="password"><br>
'
else
echo '<table class="standard" style="text-align: left;" >
    <tbody>
<tr><td style="width: 180px;">'$"Proxy name/TCPIP"'</td><td><input tabindex= "1" value="'$TCPIP'" style="width: 200px;" name="_TCPIP_"  size="20" type="text"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name or tcpip number of the internet proxy server that you want this server to use for updates."'</span></a></td>
</tr>
<tr><td style="width: 180px;">'$"Proxy Port"'</td><td><input tabindex= "2" value="'$PORT'" style="width: 200px;" name="_PORT_"  size="20" type="text"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the port number of the internet proxy server."'</span></a></td>
</tr>
      <tr>
        <td style="width: 180px;">
'$"Username"'</td>
        <td>
<input tabindex= "3" style="width: 200px;" name="_USERNAME_" 
 value="'$USERNAME'" size="20" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a username to connect to the proxy server. Leave this blank if it is not needed."'</span></a></td>
</tr>
      <tr>
        <td>
'$"Password"'</td>
        <td><input tabindex= "4" style="width: 200px;" value="'$PASSWORD'" name="_PASSWORD_" size="20" type="password"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new password that you want the user to have."'<br><br>'$"The following special characters are allowed"':<br><br>space ! # $ & ( ) + - =  %</span></a></td>
      </tr>
    </tbody>
  </table>'
fi

echo '<input name="_SERVERNAME_" value="'$SERVERNAME'" type="hidden">
<input name="_SERVERTYPE_" value="'$SERVERTYPE'" type="hidden">
<input name="_SERVERMASTER_" value="'$SERVERMASTER'" type="hidden">'

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
else
echo '<br>'
fi
echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div></form></div></body></html>'
exit
