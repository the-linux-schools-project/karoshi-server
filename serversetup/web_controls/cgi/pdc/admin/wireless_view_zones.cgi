#!/bin/bash
#Wireless_view_zones
#Copyright (C) 2009 Paul Sharrad

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

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Wireless Zones"2'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>
<body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox"><div class="sectiontitle">'$"View Wireless Zones"'</div><br>
'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`

#########################
#Assign data to variables
#########################
END_POINT=3

#Assign ZONECHOICE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ZONECHOICEcheck ]
then
let COUNTER=$COUNTER+1
ZONECHOICE=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd 'A-Za-z0-9_\-+'`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/wireless_view_zones_fm.cgi"'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$"You must access this page via https."
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$"You must be a Karoshi Management User to complete this action."
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$"You must be a Karoshi Management User to complete this action."
show_status
fi
#########################
#Check data
#########################

if [ $ZONECHOICE'null' = null ]
then
MESSAGE=$"No wireless zones have been added."
show_status
fi

if [ `echo $ZONECHOICE | grep -c ^delete` = 1 ]
then
ACTION=delete
else
ACTION=edit
fi
ZONE=`echo $ZONECHOICE | sed 's/^edit//g' | sed 's/^delete//g'`


Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/wireless_view_zones.cgi | cut -d' ' -f1`

if [ $ACTION = delete ]
then
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ZONE:" | sudo -H /opt/karoshi/web_controls/exec/wireless_delete_zone
fi

if $ACTION = edit ]
then
echo '<input name="_ZONECHOICE_" value="'$ZONECHOICE'" type="hidden"
<table class="standard" style="text-align: left; height: 10px;" >
    <tbody>
<tr><td style="width: 180px;">'$TCPIPMSG'</td><td><input name="_TCPIP_" maxlength="20" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$TCPIPHELPMSG1'<br><br>'$TCPIPHELPMSG2'</span></a></td></tr>
<tr><td style="width: 180px;">'$WPAMSG'</td><td><input name="_WPAKEY_" maxlength="63" size="63" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'<br><br>'$HELPMSG4'</span></a>
</td></tr></tbody></table>'
fi

if [ `echo $?` = 101 ]
then
MESSAGE=`echo $"There was a problem with this action." $"Please check the karoshi web administration logs for more details."`
else
MESSAGE=`echo $WPAKEY '\n\n' $COMPLETEDMSG`
fi
show_status
exit
