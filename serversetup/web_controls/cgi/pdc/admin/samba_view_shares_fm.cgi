#!/bin/bash
#Copyright (C) 2012  Paul Sharrad

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
ICON1=/images/submenus/system/enabled.png
ICON2=/images/submenus/system/disabled.png
ICON3=/images/submenus/system/delete.png

[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/samba_shares ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/samba_shares
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE"><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
<body onLoad="start()"><div id="pagecontainer">'

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
echo '<form name="myform" action="/cgi-bin/admin/samba_view_shares.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE2'</b></a></td></tr></tbody></table><br>'
else
echo '<div class="sectiontitle">'$TITLE2'</div><br>'
fi

echo '
  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 180px;"><b>'$SERVERMSG'</b></td><td style="width: 90px;"><b>'$SHAREMSG'</b></td><td style="width: 90px;"><b>'$GROUPMSG'</b></td><td style="width: 90px;"><b>'$GROUPPERMSMSG'</b></td><td style="width: 90px;"><b>'$OTHERSPERMSMSG'</b></td><td style="width: 30px;"></td><td style="width: 30px;"></td></tr>'

for SERVERS in /opt/karoshi/server_network/extra_network_shares/*
do
SERVER=`basename $SERVERS`
for SHARES in /opt/karoshi/server_network/extra_network_shares/$SERVER/*.conf
do
SHARE=`basename "$SHARES" | sed 's/.conf$//g'`
#Get group and permissions
GROUP=`grep "force group" /opt/karoshi/server_network/extra_network_shares/$SERVER/"$SHARE.conf" | cut -d= -f2 | sed 's/ +//g'`
CREATEMASK=`grep "create mask" /opt/karoshi/server_network/extra_network_shares/$SERVER/"$SHARE.conf" | cut -d= -f2 | sed 's/ //g'`

GROUPPERMS=$READONLYMSG
[ $CREATEMASK = 0664 ] && GROUPPERMS=$FULLACCESSMSG 
[ $CREATEMASK = 0666 ] && GROUPPERMS=$FULLACCESSMSG

OTHERPERMS=$READONLYMSG
[ $CREATEMASK = 0666 ] && OTHERPERMS=$FULLACCESSMSG

#Get server data
source /opt/karoshi/server_network/extra_network_shares/$SERVER/"$SHARE.info"
echo '<tr><td>'$SERVER'</td><td>'$SHARE'</td><td>'$GROUP'</td><td>'$GROUPPERMS'</td><td>'$OTHERPERMS'</td><td>'

if [ ! -f /opt/karoshi/server_network/extra_network_shares/$SERVER/"$SHARE".disabled ]
then
echo '<a class="info" href="javascript:void(0)"><input name="_ACTION_disable_SHARE_'$SHARE'_SERVERTYPE_'$SERVERTYPE'_SERVERNAME_'$SERVER'_SERVERMASTER_'$SERVERMASTER'_" type="image" class="images" src="'$ICON1'" value=""><span>'$DISABLEMSG' '$SHARE'</span></a>'
else
echo '<a class="info" href="javascript:void(0)"><input name="_ACTION_enable_SHARE_'$SHARE'_SERVERTYPE_'$SERVERTYPE'_SERVERNAME_'$SERVER'_SERVERMASTER_'$SERVERMASTER'_" type="image" class="images" src="'$ICON2'" value=""><span>'$ENABLEMSG' '$SHARE'</span></a>'
fi
echo '</td><td><a class="info" href="javascript:void(0)"><input name="_ACTION_delete_SHARE_'$SHARE'_SERVERTYPE_'$SERVERTYPE'_SERVERNAME_'$SERVER'_SERVERMASTER_'$SERVERMASTER'_" type="image" class="images" src="'$ICON3'" value=""><span>'$DELETEMSG' '$SHARE'</span></a></td></tr>'

done
done

echo '</tbody></table></div></form></div></body></html>'
exit

