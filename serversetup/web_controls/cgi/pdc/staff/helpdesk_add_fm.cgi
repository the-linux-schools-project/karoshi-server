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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs

export TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
then
	TIMEOUT=86400
fi

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Technical Support"'</title>
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body><div id="pagecontainer">'

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_staff
else
	DIV_ID=actionbox2
fi


echo '<form action="/cgi-bin/staff/helpdesk_add.cgi" method="post">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
	<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/staff/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"'"></a></td>
	<td style="vertical-align: middle;"><a href="/cgi-bin/staff/mobile_user_menu.cgi"><b>'$"Technical Support"'</b></a></td></tr></tbody></table><br>'
else
	echo '<div id="'"$DIV_ID"'"><div id="titlebox"><div class="sectiontitle">'$"Technical Support"' - '$"Add Request"'</div><br><br>'
fi

echo '<table class="standard" style="text-align: left; height: 91px;" >
<tbody>
<tr><td style="width: 180px;">'$"Request Summary"'</td><td><input tabindex= "1" maxlength="24" style="width: 200px;" size="20" name="_JOBTITLE_"> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a title or summary for the job that you want completed."'</span></a></td></tr>
<tr><td style="width: 180px;">'$"Computer Number"'</td><td><input tabindex= "3" maxlength="10" style="width: 200px;" size="20" name="_ASSETNUMBER_">  <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"The computer number is used to help identify where it is situated in the room. This can be left blank."'</span></a></td></tr>
<tr><td>'$"Location"'</td><td>
'

###############################
#Location
###############################
if [ -f /var/lib/samba/netlogon/locations.txt ]
then
	LOCATION_COUNT=$(cat /var/lib/samba/netlogon/locations.txt | wc -l)
else
	LOCATION_COUNT=0
fi

echo '<select tabindex= "2" style="width: 200px;" name="_LOCATION_"><option label="blank" value=""></option>'
COUNTER=1
while [ "$COUNTER" -lt "$LOCATION_COUNT" ]
do
	LOCATION=$(sed -n "$COUNTER,$COUNTER"'p' /var/lib/samba/netlogon/locations.txt)
	echo '<option>'"$LOCATION"'</option>'
	let COUNTER="$COUNTER"+1
done
echo '</select></td></tr>'
echo '<tr><td>'$"Department"'</td>
<td>
<select tabindex= "3" style="width: 200px;" name="_DEPARTMENT_">
<option label="blank" value=""></option>
<option value="'$"Art"'">'$"Art"'</option>
<option value="'$"Business Studies"'">'$"Business Studies"'</option>
<option value="'$"Citizenship"'">'$"Citizenship"'</option>
<option value="'$"Economics"'">'$"Economics"'</option>
<option value="'$"English"'">'$"English"'</option>
<option value="'$"Languages"'">'$"Languages"'</option>
<option value="'$"Geography"'">'$"Geography"'</option>
<option value="'$"History"'">'$"History"'</option>
<option value="'$"ICT"'">'$"ICT"'</option>
<option value="'$"Mathematics"'">'$"Mathematics"'</option>
<option value="'$"Media Studies"'">'$"Media Studies"'</option>
<option value="'$"Music"'">'$"Music"'</option>
<option value="'$"Physical Education"'">'$"Physical Education"'</option>
<option value="'$"Personal and Social Education"'">'$"Personal and Social Education"'</option>
<option value="'$"Religious Studies"'">'$"Religious Studies"'</option>
<option value="'$"Science"'">'$"Science"'</option>
<option value="'$"Technology"'">'$"Technology"'</option>
<option value="'$"Office Staff"'">'$"Office Staff"'</option>
<option value="'$"Other"'">'$"Other"'</option>
<option label="blank" value="'$""'">'$""'</option>
</select>
</td></tr>
<tr><td>'$"Category"'</td>
<td>
<select tabindex= "4" style="width: 200px;" name="_CATEGORY_">
<option label="blank" value=""></option>
<option value="'$"Hardware"'">'$"Hardware"'</option>
<option value="'$"Software"'">'$"Software"'</option>
<option value="'$"Internet"'">'$"Internet"'</option>
<option value="'$"Printing"'">'$"Printing"'</option>
<option value="'$"Whiteboard"'">'$"Whiteboard"'</option>
<option value="'$"Projector"'">'$"Projector"'</option>
<option value="'$"Wireless"'">'$"Wireless"'</option>
<option value="'$"Laptop"'">'$"Laptop"'</option>
<option value="'$"Online Classroom"'">'$"Online Classroom"'</option>
<option value="'$"Website"'">'$"Website"'</option>
<option value="'$"Other"'">'$"Other"'</option>
</select> 
 <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the category for the problem."'</span></a>
</td></tr>
<tr><td>'$"Extended Details"'</td><td><textarea tabindex= "5" cols="70" rows="8" name="_REQUEST_"></textarea></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the details for the help request."'</span></a></td></tr>
</tbody></table><br><br>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">'

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></form></div></body></html>'
exit
