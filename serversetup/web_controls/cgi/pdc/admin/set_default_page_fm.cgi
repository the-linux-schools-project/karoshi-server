#!/bin/bash
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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/set_default_page ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/set_default_page
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
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
DIV_ID=menubox
fi
echo '<form action="/cgi-bin/admin/set_default_page.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE'</b></a> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td></tr></tbody></table>'
else
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>
<td style="vertical-align: top;"><div class="sectiontitle">'$TITLE'</div></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td></tr></tbody></table><br>'
fi

echo '

  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$CHOICEMSG'</td>
        <td>

<select name="_DEFAULTPAGE_" style="width: 200px;">
	<option></option>
        <option value="add_user_fm.cgi">'$ADDUSERMSG'</option>
        <option value="change_password_fm.cgi">'$CHANGEPASSWORDMSG'</option>
        <option value="show_user_info_fm.cgi">'$SHOWUSERINFOMSG'</option>
        <option value="lockout_reset_fm.cgi">'$RESETLOCKOUTMSG'</option>
        <option value="incident_log_view_fm.cgi">'$VIEWINCIDENTLOGSMSG'</option>


        <option value="helpdesk_view_fm.cgi">'$HELPDESKMSG'</option>
        <option value="view_karoshi_web_management_logs.cgi">'$WEBMANAGEMENTLOGSMSG'</option>
	<option value="file_manager.cgi">'$FILEMANAGERMSG'</option>'




[ -f /opt/karoshi/server_network/printserver ] && echo '<option value="printers.cgi">'$PRINTERQUEUEMSG'</option>'
[ -f /opt/karoshi/server_network/monitoringserver ] &&	echo '<option value="mon_status.cgi">'$SYSTEMMONITORMSG'</option>'
[ -f /opt/karoshi/server_network/proxyserver ] && echo '<option value="dg_view_top_sites_fm.cgi">'$TOPINTERNETSITESMSG'</option>'

echo '</select></td></tr></tbody></table>
'
if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi
echo '<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
</div></form></div></body></html>
'
exit
