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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Change a User Password"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
echo '</head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign USERNAME

COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign PASSWORD1
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PASSWORD1check ]
	then
		let COUNTER=$COUNTER+1
		PASSWORD1=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign PASSWORD2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PASSWORD2check ]
	then
		let COUNTER=$COUNTER+1
		PASSWORD2=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/admin/change_password.cgi" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Change a User Password"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div>
'
else
echo '<div class="sectiontitle">'$"Change a User Password"'</div><br>'
fi

if [ $MOBILE = yes ]
then
echo '<div id="mobileactionbox">
<div id="suggestions"></div>
'$"Username"'<br>
<input tabindex= "1" style="width: 160px;" name="____USERNAME____" 
 value="'$USERNAME'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"><br>
'$"New Password"'<br>
<input tabindex= "2" style="width: 160px;" name="____PASSWORD1____" value="'$PASSWORD1'" size="20" type="password"><br>
'$"Confirm New Password"'<br>
<input tabindex= "3" style="width: 160px;" name="____PASSWORD2____" value="'$PASSWORD2'" size="20" type="password"><br><br>
<div id="photobox"><img src="/images/blank_user_image.jpg" width="140" height="180"></div>
'
else
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"Username"'</td>
        <td><div id="suggestions"></div>
<input tabindex= "1" style="width: 200px;" name="____USERNAME____" 
 value="'$USERNAME'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Password"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will change the password of the user for access to all servers on the Karoshi system including moodle and email."'</span></a>
</td>'

#Show user photo
echo '<td colspan="1" rowspan="4" style="vertical-align: top;">'
echo '<div id="photobox"><img src="/images/blank_user_image.jpg" width="140" height="180"></div>'

echo '</td></tr>
      <tr>
        <td>
'$"New Password"'</td>
        <td><input tabindex= "2" style="width: 200px;" name="____PASSWORD1____" value="'$PASSWORD1'" size="20" type="password"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Password"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new password that you want the user to have."'<br><br>'$"The following special characters are allowed"'<br><br> space !	"	# 	$	%	& 	(	) 	*	+	, 	-	.	/ 	:
;	<	=	>	?	@ 	[	\	]	^	_	` 	{	|	}	~</span></a>
</td>
      </tr>
      <tr>
        <td style="vertical-align: top;">
'$"Confirm New Password"'</td>
        <td style="vertical-align: top;"><input tabindex= "3" style="width: 200px;" name="____PASSWORD2____" value="'$PASSWORD2'" size="20" type="password"></td>
      </tr>
<tr>
     <td style="vertical-align: top; height: 120px;">
</td>
      </tr>
    </tbody>
  </table>'
fi

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
else
echo '<br>'
fi
echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div>'
echo '</form></div></body></html>'
exit

