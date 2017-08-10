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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html>
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Change a Student's Password"'</title>
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<META HTTP-EQUIV="refresh" CONTENT="300; URL=/cgi-bin/blank.cgi">
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

echo '</head><body><div id="pagecontainer">'


#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+-')
#########################
#Assign data to variables
#########################
END_POINT=10
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

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_staff
else
	DIV_ID=mobileactionbox
fi

#Check password settings
source /opt/karoshi/server_network/security/password_settings

echo '<form action="/cgi-bin/staff/change_student_password.cgi" method="post">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Change a Student's Password"'</span>
<a href="/cgi-bin/staff/mobile_menu.cgi">'$"User Menu"'</a>
</div></div>
'
else
	echo '<div id="'"$DIV_ID"'"><div id="titlebox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Change a Student's Password"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Password"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will change the password of the user for access to all servers on the Karoshi system."'</span></a></td></tr></tbody></table><br>'
fi

if [ "$MOBILE" = yes ]
then
	echo '<div id="mobileactionbox">
<div id="suggestions"></div>
'$"Username"'<br>
<input tabindex= "1" style="width: 160px;" name="____USERNAME____" 
 value="'"$USERNAME"'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"><br>
'$"New Password"'<br>
<input tabindex= "2" style="width: 160px;" name="____PASSWORD1____" value="'"$PASSWORD1"'" size="20" type="password"><br>
'$"Confirm New Password"'<br>
<input tabindex= "3" style="width: 160px;" name="____PASSWORD2____" value="'"$PASSWORD2"'" size="20" type="password"><br><br>
<div id="photobox"><img src="/images/blank_user_image.jpg" width="140" height="180"></div>
'
else
	echo '<table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"Username"'</td>
        <td><div id="suggestions"></div>
<input tabindex= "1" style="width: 200px;" name="____USERNAME____" 
 value="'$USERNAME'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Password"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the username that you want to change the password for."'</span></a>
</td>'

#Show user photo
echo '<td colspan="1" rowspan="4" style="vertical-align: top;">'
echo '<div id="photobox"><img alt="photo" src="/images/blank_user_image.jpg" width="140" height="180"></div>'

echo '</td></tr>
      <tr>
        <td>
'$"New Password"'</td>
        <td><input tabindex= "2" style="width: 200px;" name="____PASSWORD1____" value="'"$PASSWORD1"'" size="20" type="password"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Password"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new password that you want the user to have."'<br><br>'
[ "$PASSWORDCOMPLEXITY" = on ] && echo ''$"Upper and lower case characters and numbers are required."'<br><br>'
echo ''$"The Minimum password length is "''"$MINPASSLENGTH"'.<br><br>'$"The following special characters are allowed"'<br><br> space !	&quot;	# 	$	%	&amp; 	(	) 	*	+	, 	-	.	/ 	:
;	&lt;	=	&gt;	?	@ 	[	\	]	^	_	` 	{	|	}	~</span></a>
</td>
      </tr>
      <tr>
        <td style="vertical-align: top;">
'$"Confirm New Password"'</td>
        <td style="vertical-align: top;"><input tabindex= "3" style="width: 200px;" name="____PASSWORD2____" value="'"$PASSWORD2"'" size="20" type="password"></td>
      </tr>
<tr>
     <td style="vertical-align: top; height: 120px;">
</td>
      </tr>
    </tbody>
  </table><br><br>
'
fi

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">'

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></form></div></body></html>'
exit

