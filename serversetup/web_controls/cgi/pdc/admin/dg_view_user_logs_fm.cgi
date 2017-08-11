#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

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
source /opt/karoshi/web_controls/version

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
DATE_INFO=$(date +%F)
DAY=$(echo "$DATE_INFO" | cut -d- -f3)
MONTH=$(echo "$DATE_INFO" | cut -d- -f2)
YEAR=$(echo "$DATE_INFO" | cut -d- -f1)

[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"User Internet Logs"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) -->
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<link rel="stylesheet" href="/all/calendar2/calendar.css">
<script src="/all/stuHover.js"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'


if [ "$MOBILE" = yes ]
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
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/admin/dg_view_user_logs.cgi" name="testform" method="post">'

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"User Internet Logs"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'

else
	echo '<div class="sectiontitle">'$"User Internet Logs"' <a class="info" href="javascript:void(0)"><img class="images" alt="help" src="/images/help/info.png"><span>'$"Internet logs are updated every three minutes."'</span></a></div><br>'
fi

if [ "$MOBILE" = yes ]
then
	echo '<div id="suggestions"></div>
'$"Username"'<br>
<input required="required" tabindex= "1" name="_USERNAME_" size="14" style="width: 180px;" type="text" id="inputString" onkeyup="lookup(this.value);"><br>
'$"Log Date"'<br>'
	echo "<!-- calendar attaches to existing form element -->
	<input required=\"required\" tabindex= \"2\" type=\"text\" style=\"width: 160px;\" value=\"$DAY-$MONTH-$YEAR\" size=14 maxlength=10 name=\"_DATE_\">
	<script>
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script><br>"
	echo ''$"Number of days to view"'<br>
<input required="required" tabindex= "3" name="_DAYCOUNT_" maxlength="2" size="2" value="1" type="text"><br><br>
'
else
	echo '<table class="standard" style="text-align: left;" >
	<tbody>
	  <tr>
	    <td style="width: 180px;">
		'$"Username"'
	    </td>
	    <td>
		<div id="suggestions"></div><input required="required" tabindex= "1" name="_USERNAME_" size="14" style="width: 200px;" type="text" id="inputString" onkeyup="lookup(this.value);">
	    </td>
	    <td>
		<a class="info" href="javascript:void(0)"><img class="images" alt="help" src="/images/help/info.png"><span>'$"Enter in the username that you want to check the internet logs for."'</span></a>
	    </td>
        	<td colspan="1" rowspan="4" style="vertical-align: top;">
	 		<div id="photobox"><img alt="photo" src="/images/blank_user_image.jpg" width="140" height="180"></div>
		</td>
	  </tr>
	<tr><td>'$"Log Date"'</td><td>'

	echo "<!-- calendar attaches to existing form element -->
	<input required=\"required\" tabindex= \"2\" type=\"text\" style=\"width: 200px;\" value=\"$DAY-$MONTH-$YEAR\" size=14 maxlength=10 name=\"_DATE_\"></td><td>
	<script>
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script></td></tr>"

	#Check if we need to show a drop down for the domains if we have a trusted domain added
	if [ -d /opt/karoshi/server_network/domain_information/trusted_domains ]
	then
		source /opt/karoshi/server_network/domain_information/domain_name
		echo '<tr><td>'$"Domain"'</td><td><select name="_DOMAIN_" style="width: 200px; padding-left:0px;padding-right:0px"><option value="'"$REALM"'">'"$REALM"'</option>'
		for TRUSTED_DOMAIN in $(ls -1 /opt/karoshi/server_network/domain_information/trusted_domains)
		do
			echo '<option value="'"$TRUSTED_DOMAIN"'">'"$TRUSTED_DOMAIN"'</option>'	
		done
		echo '<option label="blank" value=""></option></select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the domain that this user is on."'</span></a></td></tr>'
	fi

	echo '<tr><td>'$"Number of days to view"'</td><td><input required="required" tabindex= "3" name="_DAYCOUNT_" maxlength="2" size="2" value="1" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This shows the number of sites a user has visited."'</span></a></td></tr>
<tr><td style="vertical-align: top; height: 120px;"></td><td></td><td></td></tr>
</tbody></table><br>'
fi

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div>'

[ "$MOBILE" = no ] && echo '</div>'

echo '</form></div></body></html>'
exit

