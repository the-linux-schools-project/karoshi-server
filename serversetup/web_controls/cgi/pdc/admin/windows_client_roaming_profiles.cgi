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

if [ $MOBILE = no ]
then
	TABLECLASS=standard
	WIDTH1=180
	WIDTH2=200
	HEIGHT1=17
	HEIGHT2=26
else
	TABLECLASS=mobilestandard
	WIDTH1=120
	WIDTH2=160
	HEIGHT1=30
	HEIGHT2=35
fi

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Windows Roaming Profiles"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
'

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


#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+'`
#########################
#Assign data to variables
#########################
END_POINT=17
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

#Assign GROUP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = GROUPcheck ]
	then
		let COUNTER=$COUNTER+1
		GROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign EXCEPTIONLIST
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = EXCEPTIONLISTcheck ]
	then
		let COUNTER=$COUNTER+1
		EXCEPTIONLIST=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign MODCODE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = MODCODEcheck ]
	then
		let COUNTER=$COUNTER+1
		MODCODE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign FORMCODE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = FORMCODEcheck ]
	then
		let COUNTER=$COUNTER+1
		FORMCODE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

if [ -z "$ACTION" ]
then
	ACTION=showmenu
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
fi

echo '<form name="profileform" action="/cgi-bin/admin/windows_client_roaming_profiles.cgi" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Windows Roaming Profiles"'</span>'
	if [ "$ACTION" = status ]
	then
		echo '<a href="/cgi-bin/admin/windows_client_roaming_profiles.cgi">'$"Menu"'</a>'
	else
		echo '<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>'
	fi
echo '</div></div><div id="mobileactionbox">
'
else
	echo '<table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Windows Roaming Profiles"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Roaming_Profiles"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will change the password of the user for access to all servers on the Karoshi system."'</span></a></td>'

if [ "$ACTION" = status ]
then
	echo '<td><button class="button" name="_Menu_" value="_">
	'$"Show Menu"'
	</button></td>'
fi

echo '</tr></tbody></table><br></div><div id="infobox">'
fi

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/windows_client_roaming_profiles.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################

if [ "$ACTION" = status ] || [ "$ACTION" = roaming ] || [ "$ACTION" = mandatory ]
then
	#Check to see that we have either a username or a group
	if [ -z "$USERNAME" ] && [ -z "$GROUP" ]
	then
		MESSAGE=$"You have not entered in a username or a group."
		show_status	
	fi

	if [ ! -z "$USERNAME" ]
	then
		#Check to see if the user exists
		getent passwd "$USERNAME" 1>/dev/null 
		if [ $? != 0 ]
		then
			MESSAGE=$"This user does not exist."
			show_status
		fi

		#Check that the username is not for a system account
		if [ $(id -u "$USERNAME") -lt 500 ]
		then
			MESSAGE=$"You cannot use a roaming profile with a system account."
			show_status
		fi

		#Check that the username is not the karoshi user
		if [ "$USERNAME" = karoshi ]
		then
			MESSAGE=$"You cannot use a roaming profile for the karoshi user."
			show_status
		fi
	fi
fi

#Check to see that username is not blank
if [ "$ACTION" = roaming ] || [ "$ACTION" = mandatory ]
then

	#Check to see that MODCODE is not blank
	if [ -z "$MODCODE" ]
	then
		MESSAGE=$"The modify code must not be blank."
		show_status
	fi
	#Check to see that FORMCODE is not blank
	if [ -z "$FORMCODE" ]
	then
		MESSAGE=$"The form code must not be blank."
		show_status
	fi

	#Check that modcode matches formcode
	if [ "$MODCODE" != "$FORMCODE" ]
	then
		MESSAGE=$"Incorrect modify code."
		show_status	
	fi
fi

if [ "$ACTION" = roaming ] || [ "$ACTION" = mandatory ] || [ "$ACTION" = status ]
then
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/windows_client_roaming_profiles.cgi | cut -d' ' -f1`
	#Enable roaming profile
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$GROUP:$EXCEPTIONLIST:$ACTION:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/windows_client_roaming_profiles
fi

#Show menu options for the page
if [ "$ACTION" = showmenu ]
then
	MOD_CODE=`echo ${RANDOM:0:3}`
	echo '<input name="_FORMCODE_" value="'$MOD_CODE'" type="hidden"><table class="'$TABLECLASS'" style="text-align: left; left: 232px;" >
    <tbody>
<tr><td style="width: '$WIDTH1'px;">'$"Option"'</td><td>
<select name="_ACTION_" style="width: '$WIDTH2'px;">
<option label="blank"></option>
<option value="mandatory">'$"Mandatory Profile"'</option>
<option value="roaming">'$"Roaming Profile"'</option>
<option value="status">'$"View Status"'</option>
</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Roaming_Profiles"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the profile action you want to carry out."'</span></a>
</td></tr>
<tr><td>
'$"Primary Group"'</td><td>'
	/opt/karoshi/web_controls/group_dropdown_list | sed 's/style="width: 200px;">/style="width: '$WIDTH2'px;">/g'
	echo '</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Roaming_Profiles"><img class="images" alt="" src="/images/help/info.png"><span>'$"All users in the group you select will be affected by the action you choose from this menu." $"Leave this blank if you want to enter in a username."'</span></a>
</td></tr>
<tr><td>
'$"Username"'
</td><td>
<input tabindex= "1" name="_USERNAME_" style="width: '$WIDTH2'px;" size="20" type="text">
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Roaming_Profiles"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a username or leave this blank if you want to choose an entire group."'</span></a>
</td></tr>
<tr><td>
'$"Exceptions"'
</td><td>
<input tabindex= "1" name="_EXCEPTIONLIST_" style="width: '$WIDTH2'px;" size="20" type="text">
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Roaming_Profiles"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in any user accounts that you do not want to modify separated by spaces."'</span></a>
</td></tr>
<tr><td style="height:50px; vertical-align: bottom">'$"Modify Code"'</td><td style="vertical-align: bottom; text-align: left;"><b>'$MOD_CODE'</b></td><td></td></tr>
<tr><td>'$"Confirm"'</td><td style="vertical-align: top; text-align: left;"><input name="_MODCODE_" maxlength="3" size="3" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Roaming_Profiles"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the code displayed on the page to confirm this action."'</span></a>
</td></tr>
</tbody></table>
<br><br>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">'


fi
[ "$MOBILE" = no ] && echo '</div>'
echo '</div></form></div></body></html>'

exit

