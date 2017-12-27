#!/bin/bash
#Change password
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
source /opt/karoshi/server_network/security/password_settings
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER" ] && source "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER"
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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Change User Password"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
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
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+')
#########################
#Assign data to variables
#########################
END_POINT=9
function get_data {
COUNTER=2
DATAENTRY=""
while [[ $COUNTER -le $END_POINT ]]
do
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [[ "$DATAHEADER" = "$DATANAME" ]]
	then
		let COUNTER="$COUNTER"+1
		DATAENTRY=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
		break
	fi
	let COUNTER=$COUNTER+1
done
}

#Assign USERNAME
DATANAME=USERNAME
get_data
USERNAME="$DATAENTRY"

#Assign PASSWORD1
DATANAME=PASSWORD1
get_data
PASSWORD1="$DATAENTRY"

#Assign PASSWORD2
DATANAME=PASSWORD2
get_data
PASSWORD2="$DATAENTRY"

#Assign NEXTLOGON
DATANAME=NEXTLOGON
get_data
NEXTLOGON="$DATAENTRY"

if [ -z "$NEXTLOGON" ]
then
	NEXTLOGON=no
fi

CHECKED=""
[ "$NEXTLOGON" = yes ] && CHECKED="checked"

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

#Check password settings
source /opt/karoshi/server_network/security/password_settings

echo '<form action="/cgi-bin/admin/change_password.cgi" method="post">'

[ "$MOBILE" = no ] && echo '<div id="'"$DIV_ID"'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Change a User Password"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div>'
else
	echo '<table class="standard" style="text-align: left;" ><tbody>
	<tr><td><div class="sectiontitle">'$"Change a User Password"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Password"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will change the password of the user for access to all servers on the Karoshi system."'</span></a></td></tr></tbody></table><br>'
fi

if [ "$MOBILE" = yes ]
then
echo '<div id="mobileactionbox">
<div id="suggestions"></div>
'$"Username"'<br>
<input required="required" tabindex= "1" style="width: 200px; height: 30px; text-align: center;" name="____USERNAME____" 
 value="'"$USERNAME"'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"><br>
'$"New Password"'<br>
<input pattern=".{'"$MINPASSLENGTH"',128}" title="'$"Password length required:"' '"$MINPASSLENGTH"'" tabindex= "2" style="width: 200px; height: 30px; text-align: center;" name="____PASSWORD1____" value="'"$PASSWORD1"'" size="20" type="password"><br>
'$"Confirm New Password"'<br>
<input pattern=".{'"$MINPASSLENGTH"',128}" title="'$"Password length required:"' '"$MINPASSLENGTH"'" tabindex= "3" style="width: 200px; height: 30px; text-align: center;" name="____PASSWORD2____" value="'"$PASSWORD2"'" size="20" type="password"><br>
'$"Change at next logon"'<br>
<input type="checkbox" name="____NEXTLOGON____" value="yes" '$CHECKED'><br><br>
<div style="width: 120px;" id="photobox"><img src="/images/blank_user_image.jpg" width="120" height="150" alt="photo"></div>
'
else
	echo '<table class="standard" style="text-align: left;" >
<tbody>
<tr><td style="width: 180px;">'$"Username"'</td><td><div id="suggestions"></div>
<input required="required" tabindex= "1" style="width: 200px;" name="____USERNAME____" 
 value="'"$USERNAME"'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Password"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the username that you want to change the password for."'</span></a>
</td></tr>
<tr>
<td>'$"New Password"'</td><td><input pattern=".{'"$MINPASSLENGTH"',128}" title="'$"Password length required:"' '"$MINPASSLENGTH"'" tabindex= "2" style="width: 200px;" name="____PASSWORD1____" value="'"$PASSWORD1"'" size="20" type="password"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Password"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new password that you want the user to have."'<br><br>'$"Leave the password fields blank if you want a random password."'<br><br>'$"The following special characters are allowed"'<br><br> space !	&quot;	# 	$	%	&amp; 	(	) 	*	+	, 	-	.	/ 	:
;	&lt;	=	&gt;	?	@ 	[	\	]	^	_	` 	{	|	}	~<br><br>'

[ "$PASSWORDCOMPLEXITY" = on ] && echo ''$"Upper and lower case characters and numbers are required."'<br><br>'
echo ''$"The Minimum password length is "''"$MINPASSLENGTH"'.<br></span></a>
</td>
</tr>
<tr><td style="vertical-align: top;">'$"Confirm New Password"'</td><td style="vertical-align: top;"><input pattern=".{'"$MINPASSLENGTH"',128}" title="'$"Password length required:"' '"$MINPASSLENGTH"'" tabindex= "3" style="width: 200px;" name="____PASSWORD2____" value="'"$PASSWORD2"'" size="20" type="password"></td><td></td>
      </tr>
	<tr><td style="vertical-align: top;">'$"Change at next logon"'</td><td><input type="checkbox" name="____NEXTLOGON____" value="yes" '"$CHECKED"'></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Password"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will force the user to change their password at next logon."'</span></a></td></tr>
<tr><td style="vertical-align: top;">'$"User Photo"'</td><td><div style="width: 120px;" id="photobox"><img src="/images/blank_user_image.jpg" width="120" height="150" alt="photo"></div></td><td></td></tr>
</tbody>
</table>'
fi

echo '<br><input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div>'

[ "$MOBILE" = no ] && echo '</div>'

echo '</form></div></body></html>'
exit

