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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/add_user ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/add_user
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all

if [ -f /opt/karoshi/server_network/default_username_style ]
then
source /opt/karoshi/server_network/default_username_style
[ $DEFAULTSTYLE = 1 ] && SELECT1='selected="selected"'
[ $DEFAULTSTYLE = 2 ] && SELECT2='selected="selected"'
[ $DEFAULTSTYLE = 3 ] && SELECT3='selected="selected"'
[ $DEFAULTSTYLE = 4 ] && SELECT4='selected="selected"'
[ $DEFAULTSTYLE = 5 ] && SELECT5='selected="selected"'
[ $DEFAULTSTYLE = 6 ] && SELECT6='selected="selected"'
[ $DEFAULTSTYLE = 7 ] && SELECT7='selected="selected"'
[ $DEFAULTSTYLE = 8 ] && SELECT8='selected="selected"'
[ $DEFAULTSTYLE = 9 ] && SELECT9='selected="selected"'
else
SELECT1='selected="selected"'
fi


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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE"><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script type="text/javascript" src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
		***********************************************/
	</script>
	<script type="text/javascript">
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
<script type="text/javascript">
function rewriteselect() {
document.myform._USERNAMESTYLE_.options.selectedIndex.length=0;
var firstnameValue = (document.myform._FIRSTNAME_.value).toLowerCase();
var surnameValue = (document.myform._SURNAME_.value).toLowerCase();
var enrollmentValue = document.myform._ENROLLMENTNUMBER_.value;
var yearValue = document.myform._GROUP_.value;
var selectedstyle = document.myform._USERNAMESTYLE_.value
var status1 = false;
var status2 = false;
var status3 = false;
var status4 = false;
var status5 = false;
var status6 = false;
var status7 = false;
var status8 = false;
var status9 = false;

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

if (yearValue.indexOf("yr") != -1) {
	yearValue = yearValue[4]+yearValue[5];
} else {
	yearValue = "";
}

if (firstnameValue == "") {
	firstnameValue = "arnold";
}

if (surnameValue == "") {
	surnameValue = "student";
}

if (enrollmentValue == "") {
	enrollmentValue = "Enrollment number as username";
}

document.myform._USERNAMESTYLE_.options[0]=new Option("Style 1: " + firstnameValue[0] + surnameValue + yearValue, "userstyleS1", false, status1);
document.myform._USERNAMESTYLE_.options[1]=new Option("Style 2: " + yearValue + firstnameValue[0] + surnameValue, "userstyleS2", false, status2);
document.myform._USERNAMESTYLE_.options[2]=new Option("Style 3: " + surnameValue + firstnameValue[0] + yearValue, "userstyleS3", false, status3);
document.myform._USERNAMESTYLE_.options[3]=new Option("Style 4: " + firstnameValue + "." + surnameValue + yearValue, "userstyleS4", false, status4);
document.myform._USERNAMESTYLE_.options[4]=new Option("Style 5: " + surnameValue + "." + firstnameValue + yearValue, "userstyleS5", false, status5);
document.myform._USERNAMESTYLE_.options[5]=new Option("Style 6: " + yearValue + surnameValue + firstnameValue[0], "userstyleS6", false, status6);
document.myform._USERNAMESTYLE_.options[6]=new Option("Style 7: " + yearValue + firstnameValue + surnameValue[0], "userstyleS7", false, status7);
document.myform._USERNAMESTYLE_.options[7]=new Option("Style 8: " + firstnameValue + surnameValue[0], "userstyleS8", false, status8);
document.myform._USERNAMESTYLE_.options[8]=new Option("Style 9: " + enrollmentValue, "userstyleS9", false, status9);
}
</script>
</head>
<body onLoad="start()">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
FILE=`echo $DATA | cut -s -d_ -f3`

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox
fi
echo '<form name="myform" action="/cgi-bin/admin/add_user.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$USERMENUMSG'</a>
</div></div>
'
else
echo '<div id="'$DIV_ID'"><b>'$TITLE'</b><br><br>'
fi

#Check that this server is not part of a federated setup
if [ -f /opt/karoshi/server_network/servers/$HOSTNAME/federated_server ]
then
echo $ERRORMSG11 '</div></body></html>'
exit
fi

#Get request data if asked
if [ $FILE'null' != null ]
then
if [ -f /opt/karoshi/user_requests/new_users/$FILE ]
then
NEW_USER_DATA=`sed -n 1,1p /opt/karoshi/user_requests/new_users/$FILE`
FORENAME=`echo $NEW_USER_DATA | cut -d: -f1`
SURNAME=`echo $NEW_USER_DATA | cut -d: -f2`
GROUP=`echo $NEW_USER_DATA | cut -d: -f3`
ENROLLMENTNUMBER=`echo $NEW_USER_DATA | cut -d: -f4`
echo '<input name="_REQUESTFILE_" value="'$FILE'" type="hidden">'
fi
fi

if [ $MOBILE = yes ]
then
echo '<div id="mobileactionbox">'
echo ''$FIRSTNAMEMSG'<br>
<input tabindex= "1" value="'$FORENAME'" name="_FIRSTNAME_" style="width: 160px;" size="20" type="text"><br>
'$SURNAMEMSG'<br>
<input tabindex= "2" value="'$SURNAME'" name="_SURNAME_" style="width: 160px;" size="20" type="text"><br>
'$PASSWORDMSG'<br>
<input tabindex= "3" name="_PASSWORD1_" style="width: 160px;" size="20" type="password"><br>
'$CONFIRMMSG'<br>
<input tabindex= "4" name="_PASSWORD2_" style="width: 160px;" size="20" type="password"><br>
'$ENROLLMENTNUMBERMSG'<br>
<input tabindex= "5" value="'$ENROLLMENTNUMBER'" name="_ENROLLMENTNUMBER_" style="width: 160px;" size="20" type="text"><br>
'$PRIGROUPMSG'<br>
'


if [ $FILE'null' = null ]
then
/opt/karoshi/web_controls/group_dropdown_list | sed 's/style="width: 200px;">/style="width: 160px;" onClick="rewriteselect();">/g'
else
/opt/karoshi/web_controls/group_dropdown_list | sed 's/<option><\/option>/<option selected="selected">'$GROUP'<\/option>/g'
fi
echo '<br>
'$USERSTYLEMSG'<br>
  <select name="_USERNAMESTYLE_" style="width: 160px;" onClick="rewriteselect();">
        <option value="userstyleS1" '$SELECT1'>'$STYLE1MSG': '$STYLE1MSGEX'</option>
        <option value="userstyleS2" '$SELECT2'>'$STYLE2MSG': '$STYLE2MSGEX'</option>
        <option value="userstyleS3" '$SELECT3'>'$STYLE3MSG': '$STYLE3MSGEX'</option>
        <option value="userstyleS4" '$SELECT4'>'$STYLE4MSG': '$STYLE4MSGEX'</option>
        <option value="userstyleS5" '$SELECT5'>'$STYLE5MSG': '$STYLE5MSGEX'</option>
        <option value="userstyleS6" '$SELECT6'>'$STYLE6MSG': '$STYLE6MSGEX'</option>
        <option value="userstyleS7" '$SELECT7'>'$STYLE7MSG': '$STYLE7MSGEX'</option>
        <option value="userstyleS8" '$SELECT8'>'$STYLE8MSG': '$STYLE8MSGEX'</option>
        <option value="userstyleS9" '$SELECT9'>'$STYLE9MSG': '$STYLE9MSGEX'</option>
	</select><br><br>
'
else

echo '
  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$FIRSTNAMEMSG'</td>
        <td><input tabindex= "1" value="'$FORENAME'" name="_FIRSTNAME_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User"><img class="images" alt="" src="/images/help/info.png"><span>'$USERHELP1'</span></a>
      </td></tr>
      <tr>
        <td>
'$SURNAMEMSG'</td>
        <td><input tabindex= "2" value="'$SURNAME'" name="_SURNAME_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$USERHELP2'</span></a>
      </td></tr>
      <tr>
        <td>
'$PASSWORDMSG'</td>
        <td><input tabindex= "3" name="_PASSWORD1_" style="width: 200px;" size="20" type="password"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$PASSWORDHELP'</span></a>
      </td></tr>
      <tr>
        <td>
'$CONFIRMMSG'</td>
        <td><input tabindex= "4" name="_PASSWORD2_" style="width: 200px;" size="20" type="password"></td>
      </tr>
<tr>
        <td>
'$ENROLLMENTNUMBERMSG'</td>
        <td><input tabindex= "5" value="'$ENROLLMENTNUMBER'" name="_ENROLLMENTNUMBER_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$ENROLLHELP'</span></a>
      </td></tr>
      <tr>
        <td>'$PRIGROUPMSG'</td>
        <td>'
if [ $FILE'null' = null ]
then
/opt/karoshi/web_controls/group_dropdown_list | sed 's/style="width: 200px;">/style="width: 200px;" onClick="rewriteselect();">/g'
else
/opt/karoshi/web_controls/group_dropdown_list | sed 's/<option><\/option>/<option selected="selected">'$GROUP'<\/option>/g'
fi

echo '
        </td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Detailed_Explanation"><img class="images" alt="" src="/images/help/info.png"><span>'$GROUPHELPMSG'</span></a>
      </td></tr>
<tr>
        <td>'$USERSTYLEMSG'</td>
        <td>
        <select name="_USERNAMESTYLE_" style="width: 200px;" onClick="rewriteselect();">
        <option value="userstyleS1" '$SELECT1'>'$STYLE1MSG': '$STYLE1MSGEX'</option>
        <option value="userstyleS2" '$SELECT2'>'$STYLE2MSG': '$STYLE2MSGEX'</option>
        <option value="userstyleS3" '$SELECT3'>'$STYLE3MSG': '$STYLE3MSGEX'</option>
        <option value="userstyleS4" '$SELECT4'>'$STYLE4MSG': '$STYLE4MSGEX'</option>
        <option value="userstyleS5" '$SELECT5'>'$STYLE5MSG': '$STYLE5MSGEX'</option>
        <option value="userstyleS6" '$SELECT6'>'$STYLE6MSG': '$STYLE6MSGEX'</option>
        <option value="userstyleS7" '$SELECT7'>'$STYLE7MSG': '$STYLE7MSGEX'</option>
        <option value="userstyleS8" '$SELECT8'>'$STYLE8MSG': '$STYLE8MSGEX'</option>
        <option value="userstyleS9" '$SELECT9'>'$STYLE9MSG': '$STYLE9MSGEX'</option>
	</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Username_Styles"><img class="images" alt="" src="/images/help/info.png"><span>'$USERNAMESTYLEHELP1'</span></a>
      </td></tr></tbody></table><br>

</div><div id="submitbox">'
fi
echo '<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
</div></form></body></html>
'
exit

