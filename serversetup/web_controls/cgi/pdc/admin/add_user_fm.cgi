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
source /opt/karoshi/server_network/security/password_settings
#Force users to change password on first logon if it has been set.
[ -z "$CHANGEPASSFIRSTLOGIN" ] && CHANGEPASSFIRSTLOGIN=no
if [ "$CHANGEPASSFIRSTLOGIN" = yes ]
then
	NEXTLOGON1=selected
	NEXTLOGON2=""
else
	NEXTLOGON2=selected
	NEXTLOGON1=""
fi

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#Delete the existing add user image if it has been uploaded but not used
[ -d "/var/www/karoshi/add_user_image/$REMOTE_USER" ] && rm -f -R "/var/www/karoshi/add_user_image/$REMOTE_USER"

#Get install type
INSTALL_TYPE=education
if [ -f /opt/karoshi/server_network/install_type ]
then
	INSTALL_TYPE=$(sed -n 1,1p /opt/karoshi/server_network/install_type)
fi

if [ -f /opt/karoshi/server_network/default_username_style ]
then
	source /opt/karoshi/server_network/default_username_style
	[ "$DEFAULTSTYLE" = 1 ] && SELECT1='selected="selected"'
	[ "$DEFAULTSTYLE" = 2 ] && SELECT2='selected="selected"'
	[ "$DEFAULTSTYLE" = 3 ] && SELECT3='selected="selected"'
	[ "$DEFAULTSTYLE" = 4 ] && SELECT4='selected="selected"'
	[ "$DEFAULTSTYLE" = 5 ] && SELECT5='selected="selected"'
	[ "$DEFAULTSTYLE" = 6 ] && SELECT6='selected="selected"'
	[ "$DEFAULTSTYLE" = 7 ] && SELECT7='selected="selected"'
	[ "$DEFAULTSTYLE" = 8 ] && SELECT8='selected="selected"'
	[ "$DEFAULTSTYLE" = 9 ] && SELECT9='selected="selected"'
	[ "$DEFAULTSTYLE" = 10 ] && SELECT10='selected="selected"'
else
	DEFAULTSTYLE=1
	SELECT1='selected="selected"'
fi


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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Add a New User"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
echo '
<script>
function rewriteselect() {
document.myform.____USERNAMESTYLE____.options.selectedIndex.length=0;
var firstnameValue = (document.myform.____FIRSTNAME____.value).toLowerCase();
var surnameValue = (document.myform.____SURNAME____.value).toLowerCase();
var enrollmentValue = document.myform.____ENROLLMENTNUMBER____.value;
var yearValue = document.myform.____GROUP____.value;
var selectedstyle = document.myform.____USERNAMESTYLE____.value
var status1 = false;
var status2 = false;
var status3 = false;
var status4 = false;
var status5 = false;
var status6 = false;
var status7 = false;
var status8 = false;
var status9 = false;
var status10 = false;

var el = document.getElementById("extraoptions1");
el.innerHTML = "";

var el = document.getElementById("extraoptions2");
el.innerHTML = "";

if (selectedstyle == "userstyleS2") {
	status2 = "true";
}

if (selectedstyle == "userstyleS3") {
	status3 = "true";
}

if (selectedstyle == "userstyleS4") {
	status4 = "true";
}

if (selectedstyle == "userstyleS5") {
	status5 = "true";
}

if (selectedstyle == "userstyleS6") {
	status6 = "true";
}

if (selectedstyle == "userstyleS7") {
	status7 = "true";
}

if (selectedstyle == "userstyleS8") {
	status8 = "true";
}

if (selectedstyle == "userstyleS9") {
	status9 = "true";
}

if (selectedstyle == "userstyleS10") {
	var el = document.getElementById("extraoptions1");
el.innerHTML = "Username";

var el = document.getElementById("extraoptions2");'

if [ "$MOBILE" = no ]
then
	echo 'el.innerHTML = "<input tabindex= \"6\" value=\"'"$USERNAME"'\" name=\"____USERNAME____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";'
else
	echo 'el.innerHTML = "<input tabindex= \"6\" value=\"'"$USERNAME"'\" name=\"____USERNAME____\" style=\"width: 200px\; text-align: center;\" size=\"20\" type=\"text\"><br>";'
fi

echo 'usernameValue = "'$"Enter a username"'";
	status10 = "true";
}

if (yearValue.indexOf("yr") != -1) {
	yearValue = yearValue[4]+yearValue[5];
} else {
	yearValue = "";
}

if (firstnameValue == "") {
	firstnameValue = "arnold";
}

if (surnameValue == "") {
	surnameValue = "user";
}

if (enrollmentValue == "") {
	enrollmentValue = "Enrollment number";
}

'

if [ "$INSTALL_TYPE" = education ]
then
	echo 'document.myform.____USERNAMESTYLE____.options[0]=new Option("" + firstnameValue[0] + surnameValue + yearValue, "userstyleS1", false, status1);
document.myform.____USERNAMESTYLE____.options[1]=new Option("" + yearValue + firstnameValue[0] + surnameValue, "userstyleS2", false, status2);
document.myform.____USERNAMESTYLE____.options[2]=new Option("" + surnameValue + firstnameValue[0] + yearValue, "userstyleS3", false, status3);
document.myform.____USERNAMESTYLE____.options[3]=new Option("" + firstnameValue + "." + surnameValue + yearValue, "userstyleS4", false, status4);
document.myform.____USERNAMESTYLE____.options[4]=new Option("" + surnameValue + "." + firstnameValue + yearValue, "userstyleS5", false, status5);
document.myform.____USERNAMESTYLE____.options[5]=new Option("" + yearValue + surnameValue + firstnameValue[0], "userstyleS6", false, status6);
document.myform.____USERNAMESTYLE____.options[6]=new Option("" + yearValue + firstnameValue + surnameValue[0], "userstyleS7", false, status7);
document.myform.____USERNAMESTYLE____.options[7]=new Option("" + firstnameValue + surnameValue[0], "userstyleS8", false, status8);
document.myform.____USERNAMESTYLE____.options[8]=new Option("" + enrollmentValue, "userstyleS9", false, status9);
document.myform.____USERNAMESTYLE____.options[9]=new Option("" + usernameValue, "userstyleS10", false, status10);'
else
	echo 'document.myform.____USERNAMESTYLE____.options[0]=new Option("" + firstnameValue[0] + surnameValue + yearValue, "userstyleS1", false, status1);
document.myform.____USERNAMESTYLE____.options[1]=new Option("" + surnameValue + firstnameValue[0] + yearValue, "userstyleS3", false, status3);
document.myform.____USERNAMESTYLE____.options[2]=new Option("" + firstnameValue + "." + surnameValue + yearValue, "userstyleS4", false, status4);
document.myform.____USERNAMESTYLE____.options[3]=new Option("" + surnameValue + "." + firstnameValue + yearValue, "userstyleS5", false, status5);
document.myform.____USERNAMESTYLE____.options[4]=new Option("" + firstnameValue + surnameValue[0], "userstyleS8", false, status8);
document.myform.____USERNAMESTYLE____.options[5]=new Option("" + usernameValue, "userstyleS10", false, status10);'

fi
echo '}
</script>
</head><body onLoad="rewriteselect(); start();">
<div id="pagecontainer">

'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-')
#########################
#Assign data to variables
#########################
FILE=$(echo "$DATA" | cut -s -d_ -f5)

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox
fi
echo '<form name="myform" action="/cgi-bin/admin/add_user.cgi" method="post">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Add a New User"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
	IMAGE1=/images/submenus/file/movedownm.png
	IMAGE2=/images/submenus/file/moveupm.png
	TABLECLASS=mobilestandard
	ROWCOUNT=14
else
	IMAGE1=/images/submenus/file/movedown.png
	IMAGE2=/images/submenus/file/moveup.png
	TABLECLASS=standard
	ROWCOUNT=7
	echo '<div id="'$DIV_ID'"><div id="titlebox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Add a New User"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User"><img class="images" alt="" src="/images/help/info.png"><span>'$"Add new users to your system."'</span></a></td></tr></tbody></table><br></div><div id="infobox">'
fi

#Check that this server is not part of a federated setup
if [ -f /opt/karoshi/server_network/servers/"$HOSTNAME"/federated_server ]
then
	echo $"This server is part of a federated system. Users must be created on the main federation server." '</div></div></body></html>'
	exit
fi

#Get request data if asked
if [ ! -z "$FILE" ]
then
	if [ -f "/opt/karoshi/user_requests/new_users/$FILE" ]
	then
		NEW_USER_DATA=$(sed -n 1,1p "/opt/karoshi/user_requests/new_users/$FILE")
		FORENAME=$(echo "$NEW_USER_DATA" | cut -d: -f1)
		SURNAME=$(echo "$NEW_USER_DATA" | cut -d: -f2)
		GROUP=$(echo "$NEW_USER_DATA" | cut -d: -f3)
		ENROLLMENTNUMBER=$(echo "$NEW_USER_DATA" | cut -d: -f4)
		echo '<input name="____REQUESTFILE____" value="'"$FILE"'" type="hidden">'
	fi
fi

echo '
<script>
function showRow(rowId) {
for (var i = 1; i <= '"$ROWCOUNT"'; i++) {
	document.getElementById(rowId+i).style.display = "";
    }
}

function hideRow(rowId) {
for (var i = 1; i <= '"$ROWCOUNT"'; i++) {
	document.getElementById(rowId+i).style.display = "none";
    }
}

function hideLink(linkId) {
    document.getElementById(linkId).style.display = "none";
}

function showLink(linkId) {
    document.getElementById(linkId).style.display = "";
}
</script>


<button style="display: yes;" type="button" id="ToggleAdvanced" class="info" onclick="showRow('\''advanced'\''); showLink('\'ToggleBasic\''); hideLink('\'ToggleAdvanced\'');">
<img src="'"$IMAGE1"'" alt="'$"Advanced"'">
<span>'$"Show advanced fields."'</span><br>
</button>

<button style="display: none;" type="button" id="ToggleBasic" class="info" onclick="hideRow('\''advanced'\''); showLink('\'ToggleAdvanced\''); hideLink('\'ToggleBasic\'');">
<img src="'"$IMAGE2"'" alt="'$"Basic"'">
<span>'$"Hide advanced fields."'</span><br>
</button>
'

echo '<table class="'"$TABLECLASS"'" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">'$"Forename"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr>'

echo '<td><input required="required" tabindex= "1" value="'"$FORENAME"'" name="____FIRSTNAME____" style="width: 200px;" size="20" type="text"></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter the firstname for this user."'</span></a></td></tr>

<tr><td>'$"Surname"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr>'

echo '<td><input required="required" tabindex= "2" value="'"$SURNAME"'" name="____SURNAME____" style="width: 200px;" size="20" type="text"></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter the surname for this user."'</span></a></td></tr>

<tr><td>'$"Password"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr>'

echo '<td><input required="required" pattern=".{'"$MINPASSLENGTH"',128}" title="'$"Password length required:"' '"$MINPASSLENGTH"'" tabindex= "3" name="____PASSWORD1____" style="width: 200px;" size="20" type="password"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter a password and confirm it in the box below."'<br><br>'$"The following special characters are allowed"'<br><br> space !	&quot;	# 	$	%	&amp; 	(	) 	*	+	, 	-	.	/ 	:
;	&lt;	=	&gt;	?	@ 	[	\	]	^	_	` 	{	|	}	~	~<br><br>'

[ "$PASSWORDCOMPLEXITY" = on ] && echo ''$"Upper and lower case characters and numbers are required."'<br><br>'

echo ''$"The Minimum password length is "''"$MINPASSLENGTH"'.<br></span></a></td></tr>

<tr><td>'$"Confirm Password"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr>'

echo '<td><input required="required" pattern=".{'"$MINPASSLENGTH"',128}" title="'$"Password length required:"' '"$MINPASSLENGTH"'" tabindex= "4" name="____PASSWORD2____" style="width: 200px;" size="20" type="password"></td><td></td></tr>

<tr id="advanced1" style="display:none;"><td>'$"User code"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr id="advanced8" style="display:none;">'

echo '<td><input tabindex= "5" value="'"$ENROLLMENTNUMBER"'" name="____ENROLLMENTNUMBER____" style="width: 200px;" size="20" type="text"></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$"Student enrolment number or staff code. This field can be left blank."'</span></a></td></tr>

<tr id="advanced2" style="display:none;"><td>'$"Room Number"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr id="advanced9" style="display:none;">'

echo '<td><input tabindex= "6" value="'"$ROOMNUMBER"'" name="____ROOMNUMBER____" style="width: 200px;" size="20" type="text"></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$"The room number for the user. This field can be left blank."'</span></a></td></tr>

<tr id="advanced3" style="display:none;"><td>'$"Telephone Number"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr id="advanced10" style="display:none;">'

echo '<td><input tabindex= "7" value="'"$TELEPHONENUMBER"'" name="____TELEPHONENUMBER____" style="width: 200px;" size="20" type="text"></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$"The telephone number for the user. This field can be left blank."'</span></a></td></tr>

<tr id="advanced4" style="display:none;"><td>'$"Fax Number"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr id="advanced11" style="display:none;">'

echo '<td><input tabindex= "8" value="'"$FAXNUMBER"'" name="____FAXNUMBER____" style="width: 200px;" size="20" type="text"></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$"The fax number for the user. This field can be left blank."'</span></a></td></tr>

<tr id="advanced5" style="display:none;"><td>'$"Mobile Number"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr id="advanced12" style="display:none;">'

echo '<td><input tabindex= "9" value="'"$MOBILENUMBER"'" name="____MOBILENUMBER____" style="width: 200px;" size="20" type="text"></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$"The mobile number for the user. This field can be left blank."'</span></a></td></tr>

<tr id="advanced6" style="display:none;"><td>'$"Change at next logon"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr id="advanced13" style="display:none;">'

echo '<td>
<select  tabindex= "10" name="____NEXTLOGON____" style="width: 200px;">
<option value="y" '"$NEXTLOGON1"'>'$"Yes"'</option>
<option value="n" '"$NEXTLOGON2"'>'$"No"'</option>
</select>
</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will force the user to change their password at next logon."'</span></a></td></tr>
<tr><td>'$"Primary group"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr>'

echo '<td>'
if [ -z "$FILE" ]
then
	/opt/karoshi/web_controls/group_dropdown_list | sed 's/<select name="_GROUP_"/<select tabindex="11" name="____GROUP____"/g'| sed 's/style="width: 200px;">/style="width: 200px;" onClick="rewriteselect();">/g'
else
	/opt/karoshi/web_controls/group_dropdown_list | sed 's/<select name="_GROUP_"/<select tabindex="12" name="____GROUP____"/g' | sed 's/<option><\/option>/<option selected="selected">'"$GROUP"'<\/option>/g'
fi
echo '</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$"The groups give different levels of access."' '$"The itadmin group is for the network administrator."' '$"Only members of itadmin and the tech groups gain administrator access to windows computers joined to the domain."'</span></a></td></tr>

<tr><td>'$"Username style"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr>'

echo '<td><select  tabindex= "13" name="____USERNAMESTYLE____" style="width: 200px;" onClick="rewriteselect();">
<option value="userstyleS1" '"$SELECT1"'>'$"auser09"'</option>'
[ "$INSTALL_TYPE" = education ] && echo '<option value="userstyleS2" '"$SELECT2"'>'$"Style"' 2: '$"09auser"'</option>'
echo '<option value="userstyleS3" '"$SELECT3"'>'$"usera09"'</option>
<option value="userstyleS4" '"$SELECT4"'>'$"arnold.user09"'</option>
<option value="userstyleS5" '"$SELECT5"'>'$"user.arnold09"'</option>'
[ "$INSTALL_TYPE" = education ] && echo '<option value="userstyleS6" '"$SELECT6"'>'$"09usera"'</option>'
[ "$INSTALL_TYPE" = education ] && echo '<option value="userstyleS7" '"$SELECT7"'>'$"09arnoldu"'</option>'
echo '<option value="userstyleS8" '"$SELECT8"'>'$"arnoldu"'</option>'
[ "$INSTALL_TYPE" = education ] && echo '<option value="userstyleS9" '"$SELECT9"'>'$"Enrollment number as username"'</option>'
echo '<option value="userstyleS10" '"$SELECT10"'>'$"Enter a username"'</option>
</select></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Username_Styles"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the username style you require."'</span></a></td></tr>

<tr><td><span id="extraoptions1"></span></td>'

[ "$MOBILE" = yes ] && echo '</tr><tr>'

echo '<td><span id="extraoptions2"></span></td><td></td></tr>
<tr id="advanced7" style="display:none; vertical-align:top;"><td>'$"User Photo"'</td>'

[ "$MOBILE" = yes ] && echo '</tr><tr id="advanced14" style="display:none;">'

echo '<td>
<iframe src="/cgi-bin/admin/add_user_upload_image_fm.cgi" width="135" height="165" scrolling="no" style="overflow:hidden; border: none;"></iframe>
</td><td style="vertical-align:top"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$"Click on the image to upload a JPG image for this user."'<br><br>'$"User images default to width 120px height 150px."'</span></a></td></tr>
</tbody></table><br>
'

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div>'

[ "$MOBILE" = no ] && echo '</div>'

echo '</form></div></body></html>'
exit

