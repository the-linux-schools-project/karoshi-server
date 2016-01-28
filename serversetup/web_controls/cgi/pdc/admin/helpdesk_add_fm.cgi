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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

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
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Technical Support"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: www.dynamicdrive.com
		* Visit Dynamic Drive at www.dynamicdrive.com for full source code
		***********************************************/
	</script>
	<script>
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi
echo '</head><body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
if [ $MOBILE = no ]
then
	TOOLTIPCLASS="info"
	DIV_ID=actionbox
	TABLECLASS=standard
	WIDTH1=192
	WIDTH2=200
	WIDTH3=400
	COLS=70
	ROWS=6
	/opt/karoshi/web_controls/generate_navbar_admin
else
	TOOLTIPCLASS="info infoleft"
	DIV_ID=actionbox
	TABLECLASS=mobilestandard
	WIDTH1=132
	WIDTH2=140
	WIDTH3=140
	COLS=18
	ROWS=4
fi

echo '<form action="/cgi-bin/admin/helpdesk_add.cgi" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Technical Support"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">'
else
	echo '<div class="sectiontitle">'$"Technical Support"' - '$"Add Request"'</div><br>'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left;" >
<tbody>
<tr><td style="width: '$WIDTH1'px;">'$"Name"'</td><td ><input value="'$REMOTE_USER'" tabindex="1" style="width: '$WIDTH1'px;" maxlength="22" size="20" name="_NAME_"></td><td></td></tr>
<tr><td style="width: '$WIDTH1'px;">'$"Request Summary"'</td><td style="vertical-align: top;"><input tabindex="2" maxlength="24" style="width: '$WIDTH1'px;" size="20" name="_JOBTITLE_"></td><td style="vertical-align: top;"><a class="'$TOOLTIPCLASS'" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a title or summary for the job that you want completed."'</span></a></td>
</tr>
<tr><td style="width: '$WIDTH1'px;">'$"Computer Number"'</td><td><input tabindex="3" maxlength="30" style="width: '$WIDTH1'px;" size="20" name="_ASSETNUMBER_"></td><td style="vertical-align: top;"><a class="'$TOOLTIPCLASS'" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"The computer number is used to help identify where it is situated in the room. This can be left blank."'</span></a></td>
</tr>
<tr><td>'$"Location"'</td><td>
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

echo '<select tabindex="4" style="width: '$WIDTH2'px;" name="_LOCATION_"><option label="blank" value=""></option>'
COUNTER=1
while [ $COUNTER -lt $LOCATION_COUNT ]
do
	LOCATION=`sed -n $COUNTER,$COUNTER'p' /var/lib/samba/netlogon/locations.txt`
	echo '<option>'$LOCATION'</option>'
	let COUNTER=$COUNTER+1
done
echo '</select></td><td></td></tr>'
echo '<tr><td>'$"Department"'</td>
<td>
<select tabindex="5" style="width: '$WIDTH2'px;" name="_DEPARTMENT_">
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
</select>
</td><td></td></tr>
<tr><td>'$"Category"'</td>
<td>
<select tabindex= "6" style="width: '$WIDTH2'px;" name="_CATEGORY_">
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
</select></td><td>
 <a class="'$TOOLTIPCLASS'" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the category for the problem."'</span></a></td>
</tr>
<tr><td>'$"Extended Details"'</td><td><textarea style="width: '$WIDTH3'px;" tabindex="7" cols="'$COLS'" rows="'$ROWS'" name="_REQUEST_"></textarea></td>
<td><a class="'$TOOLTIPCLASS'" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the details for the help request."'</span></a></td>
</tr>
</tbody></table><br><br>'
if [ $MOBILE = no ]
then
	echo '</div><div id="submitbox">'
fi
echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></form></div></body></html>
'
exit
