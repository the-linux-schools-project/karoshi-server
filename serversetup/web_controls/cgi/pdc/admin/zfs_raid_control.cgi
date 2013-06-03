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
########################
#Required input variables
########################
#  _SERVER_
#  _PASSWORD1_  Root Password
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/software_raid ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/software_raid
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/zfs_raid_control_fm.cgi";'
echo '</script>
'
echo "</body></html>"
exit
}

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE4'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body>'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%/+-'`

#########################
#Assign data to variables
#########################

END_POINT=30
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
#Check to see that SERVERNAME is not blank
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Check to see that SERVERTYPE is not blank
if [ $SERVERTYPE'null' = null ]
then
MESSAGE=$ERRORMSG15
show_status
fi

#Check to see that SERVERMASTER is not blank
if [ $SERVERTYPE = federatedslave ]
then
if [ $SERVERMASTER'null' = null ]
then
MESSAGE=$ERRORMSG16
show_status
fi
fi

MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
fi

echo '<div id="'$DIV_ID'">'


#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE4 - $SERVERNAME'</b></a></td></tr></tbody></table>'
else
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td style="vertical-align: top;"><a href="zfs_raid_control_fm.cgi"><img alt="" src="/images/warnings/server.png"></a></td><td><b>'$TITLE4' - '$SERVERNAME'</b></td>
<td><a class="info" target="_blank" href="http://www.linuxgfx.co.uk/karoshi/documentation/wiki/index.php?title=ZFS_Raid"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG5'</span></a>
</td></tr></tbody></table><br>'

fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/zfs_raid_control.cgi | cut -d' ' -f1`
echo '<form action="/cgi-bin/admin/zfs_raid_control2.cgi" name="selectservers" method="post">'
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:" | sudo -H /opt/karoshi/web_controls/exec/zfs_raid_control

echo "</form></div></body></html>"
exit
