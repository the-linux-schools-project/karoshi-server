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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/helpdesk ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/helpdesk
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
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title>
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body>'

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_staff
else
DIV_ID=actionbox2
fi


echo '<form action="/cgi-bin/staff/helpdesk_add.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/staff/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/staff/mobile_user_menu.cgi"><b>'$TITLE'</b></a></td></tr></tbody></table><br>'
else
echo '<b>'$TITLE'</b><br><br>'
fi

echo '<table class="standard" style="text-align: left; height: 91px;" border="0" cellpadding="2" cellspacing="2">
<tbody>
<tr><td style="width: 180px;">'$JOBTITLEMMSG'</td><td><input tabindex= "1" maxlength="24" style="width: 200px;" size="20" name="_JOBTITLE_"> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td></tr>
<tr><td style="width: 180px;">'$ASSETNUMBERMSG'</td><td><input tabindex= "3" maxlength="10" style="width: 200px;" size="20" name="_ASSETNUMBER_">  <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a></td></tr>
<tr><td>'$LOCATIONMSG'</td><td>
'

###############################
#Location
###############################
if [ -f /var/lib/samba/netlogon/locations.txt ]
then
LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
else
LOCATION_COUNT=0
fi

echo '<select tabindex= "2" style="width: 200px;" name="_LOCATION_"><option value=""></option>'
COUNTER=1
while [ $COUNTER -le $LOCATION_COUNT ]
do
LOCATION=`sed -n $COUNTER,$COUNTER'p' /var/lib/samba/netlogon/locations.txt`
echo '<option>'$LOCATION'</option>'
let COUNTER=$COUNTER+1
done
echo '</select></td></tr>'
echo '<tr><td>'$DEPARTMENTMSG'</td>
<td>
<select tabindex= "3" style="width: 200px;" name="_DEPARTMENT_">
<option value=""></option>
<option value="'$DEPARTMENT1'">'$DEPARTMENT1'</option>
<option value="'$DEPARTMENT2'">'$DEPARTMENT2'</option>
<option value="'$DEPARTMENT3'">'$DEPARTMENT3'</option>
<option value="'$DEPARTMENT4'">'$DEPARTMENT4'</option>
<option value="'$DEPARTMENT5'">'$DEPARTMENT5'</option>
<option value="'$DEPARTMENT6'">'$DEPARTMENT6'</option>
<option value="'$DEPARTMENT7'">'$DEPARTMENT7'</option>
<option value="'$DEPARTMENT8'">'$DEPARTMENT8'</option>
<option value="'$DEPARTMENT9'">'$DEPARTMENT9'</option>
<option value="'$DEPARTMENT10'">'$DEPARTMENT10'</option>
<option value="'$DEPARTMENT11'">'$DEPARTMENT11'</option>
<option value="'$DEPARTMENT12'">'$DEPARTMENT12'</option>
<option value="'$DEPARTMENT13'">'$DEPARTMENT13'</option>
<option value="'$DEPARTMENT14'">'$DEPARTMENT14'</option>
<option value="'$DEPARTMENT15'">'$DEPARTMENT15'</option>
<option value="'$DEPARTMENT16'">'$DEPARTMENT16'</option>
<option value="'$DEPARTMENT17'">'$DEPARTMENT17'</option>
<option value="'$DEPARTMENT18'">'$DEPARTMENT18'</option>
<option value="'$DEPARTMENT19'">'$DEPARTMENT19'</option>
<option value="'$DEPARTMENT20'">'$DEPARTMENT20'</option>
</select>
</td></tr>
<tr><td>'$CATEGORYMSG'</td>
<td>
<select tabindex= "4" style="width: 200px;" name="_CATEGORY_">
<option value=""></option>
<option value="'$CATEGORY1'">'$CATEGORY1'</option>
<option value="'$CATEGORY2'">'$CATEGORY2'</option>
<option value="'$CATEGORY3'">'$CATEGORY3'</option>
<option value="'$CATEGORY4'">'$CATEGORY4'</option>
<option value="'$CATEGORY5'">'$CATEGORY5'</option>
<option value="'$CATEGORY6'">'$CATEGORY6'</option>
<option value="'$CATEGORY7'">'$CATEGORY7'</option>
<option value="'$CATEGORY8'">'$CATEGORY8'</option>
<option value="'$CATEGORY9'">'$CATEGORY9'</option>
<option value="'$CATEGORY10'">'$CATEGORY10'</option>
<option value="'$CATEGORY11'">'$CATEGORY11'</option>
</select> 
 <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a>
</td></tr>
<tr><td>'$USERPROBLEMMSG'</td><td><textarea tabindex= "5" cols="70" rows="8" name="_REQUEST_"></textarea></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG4'</span></a></td></tr>
</tbody></table><br>'

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi

echo '<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"></div></form></body></html>'
exit
