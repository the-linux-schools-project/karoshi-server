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

ICON1=/images/submenus/system/cert.png
ICON2=/images/submenus/system/cert_enabled.png
ICON3=/images/submenus/system/cert_disabled.png
ICON4=/images/submenus/system/cert_create.png

[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/remote_management_access ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/remote_management_access
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo '</script>'
echo "</div></body></html>"
exit
}

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/remote_management_access.cgi" method="post">
<div id="actionbox"><span style="font-weight: bold;">'$TITLE'</span><br><br>'

#Check to see the level of user
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/remote_management_access_fm.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:" | sudo -H /opt/karoshi/web_controls/exec/remote_management_level

USERLEVEL=`echo $?`
#Check the level is correct

if [ $USERLEVEL != 201 ] && [ $USERLEVEL != 202 ] && [ $USERLEVEL != 203 ]
then
MESSAGE="$ERRORMSG1"
show_status
fi

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody>'

#Primary admin - show key options for all web management users
if [ $USERLEVEL = 201 ]
then
COUNTER=1
LINECOUNT=`cat /opt/karoshi/web_controls/web_access_admin | wc -l`
while [ $COUNTER -le $LINECOUNT ]
do
ADMIN_USER=`sed -n $COUNTER,$COUNTER'p' /opt/karoshi/web_controls/web_access_admin | cut -d: -f1`
if [ $ADMIN_USER'null' != null ]
then
echo '<td style="width: 180px;">'$ADMIN_USER'</td>'
#Check if a client certificate exists for this user
if [ -d /opt/karoshi/server_network/ssl/web_management/client_certs/$ADMIN_USER ]
then
#Show client cert details icon
echo '<td style="vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_ACTION_SHOWDETAILS_USER_'$ADMIN_USER'_" type="image" class="images" src="'$ICON1'" value=""><span>'$ADMIN_USER' - '$SHOWCERTMSG'</span></a></td>'

if [ -d /opt/karoshi/server_network/ssl/web_management/client_certs_revoked/$ADMIN_USER ]
then
#Show enable cert icon
echo '<td style="vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_ACTION_ENABLECERT_USER_'$ADMIN_USER'_" type="image" class="images" src="'$ICON2'" value=""><span>'$ADMIN_USER' - '$ENABLECERTMSG'</span></a></td>'
else
#Show disable cert icon
echo '<td style="vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_ACTION_DISABLECERT_USER_'$ADMIN_USER'_" type="image" class="images" src="'$ICON3'" value=""><span>'$ADMIN_USER' - '$DISABLECERTMSG'</span></a></td>'
fi

else
#Show create certificate icon
echo '<td style="vertical-align: top; text-align: left;"><a class="info" href="javascript:void(0)"><input name="_ACTION_CREATECERT_USER_'$ADMIN_USER'_" type="image" class="images" src="'$ICON4'" value=""><span>'$ADMIN_USER' - '$CREATECERTMSG'</span></a></td>'
fi

echo "</tr>"
fi

let COUNTER=$COUNTER+1
done


echo '</tbody></table></div></body></html>'

fi



exit
echo '<form action="/cgi-bin/admin/remote_management_change_password.cgi" method="post">
<div id="actionbox">
<span style="font-weight: bold;">'$TITLE'</span><br>
  <br>
  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$USERNAMEMSG'</td>
        <td><input name="_USERNAME_" value="'$REMOTE_USER'" size="20" type="text"></td>
      </tr>
      <tr>
        <td>
'$PASSWORDMSG'</td>
        <td><input name="_PASSWORD1_" size="20" type="password"></td>
      </tr>
      <tr>
        <td>
'$CONFIRMMSG'</td>
        <td><input name="_PASSWORD2_" size="20" type="password"></td>
      </tr>
    </tbody>
  </table>
</div>
<div id="submitbox">
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div>
</form>
</body>
</html>
'
exit
