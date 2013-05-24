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

##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/ups ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/ups
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'


function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/ups_add_fm.cgi";'
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
echo '<div id="actionbox">
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="vertical-align: top;"><b>'$TITLE2'</b></td><td style="vertical-align: middle;">
<form action="/cgi-bin/admin/ups_add_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="" type="image" class="images" src="/images/submenus/system/ups_add.png" value=""><span>'$TITLE1'</span></form></a></td><td style="vertical-align: middle;">
<form action="/cgi-bin/admin/ups_slave_add_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="" type="image" class="images" src="/images/submenus/system/ups_slave_add.png" value=""><span>'$TITLE5'</span></form></a></td>
<td style="vertical-align: middle;">
<form action="/cgi-bin/admin/ups_device_add_fm.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="" type="image" class="images" src="/images/submenus/system/ups_add_device.png" value=""><span>'$TITLE6'</span></form></a></td>
</tr>
</tbody></table>
<br>'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/ups_status.cgi | cut -d' ' -f1`
#Show UPS status
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:" | sudo -H /opt/karoshi/web_controls/exec/ups_status
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 106 ]
then
MESSAGE=$ERRORMSG5
show_status
fi
echo "</div></body></html>"
exit
