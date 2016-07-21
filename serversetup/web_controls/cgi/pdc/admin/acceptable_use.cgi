#!/bin/bash
#Copyright (C) 2014  Paul Sharrad

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

if [ $MOBILE = yes ]
then
	TOOLTIPCLASS="info"
	TABLECLASS=mobilestandard
	WIDTH1=100
	WIDTH2=50
	WIDTH3=50
	WIDTH4=100
else
	TOOLTIPCLASS="info infoleft"
	TABLECLASS=standard
	WIDTH1=200
	WIDTH2=175
	WIDTH3=75
	WIDTH4=150
fi

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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Acceptable Use"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>

<script>
<!--
function SetAllCheckBoxes(FormName, FieldName, CheckValue)
{
	if(!document.forms[FormName])
		return;
	var objCheckBoxes = document.forms[FormName].elements[FieldName];
	if(!objCheckBoxes)
		return;
	var countCheckBoxes = objCheckBoxes.length;
	if(!countCheckBoxes)
		objCheckBoxes.checked = CheckValue;
	else
		// set the check value for all check boxes
		for(var i = 0; i < countCheckBoxes; i++)
			objCheckBoxes[i].checked = CheckValue;
}
// -->
</script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
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

echo '<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body onLoad="start()"><div id="pagecontainer">'

function send_data {
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/acceptable_use.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$GRACETIME:$USERNAMES:" | sudo -H /opt/karoshi/web_controls/exec/acceptable_use
}

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#echo $DATA
#########################
#Assign data to variables
#########################
END_POINT=21
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

[ -z $ACTION ] && ACTION=notset

if [ $ACTION = setgracetime ]
then
	#Assign GRACETIME
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GRACETIMEcheck ]
		then
			let COUNTER=$COUNTER+1
			GRACETIME=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	send_data
fi

if [ $ACTION = approve ]
then
	#Get users to approve
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			USERNAMES=`echo $DATA | cut -s -d'_' -f$COUNTER- | sed 's/_ACTION_approve_USERNAME_/,/g'`
			break
			fi
		let COUNTER=$COUNTER+1
	done
fi

if [ $ACTION = enableac ] || [ $ACTION = disableac ]
then
	send_data
fi

#Check to see if acceptable use is enabled or disabled.
if [ -f /opt/karoshi/server_network/acceptable_use_authorisations/grace_time_disabled ]
then
	ACCEPTABLEUSESTATUS=$"Disabled"
	GRACETIMESTATUSMSG=$"Enable acceptable use"
	ICON=/images/submenus/user/grace_time_disabled.png
	ACTION2=enableac
	ACTIONMSG=$"Enable"
else
	ACCEPTABLEUSESTATUS=$"Enabled"
	GRACETIMESTATUSMSG=$"Disable acceptable use"
	ICON=/images/submenus/user/grace_time_enabled.png
	ACTION2=disableac
	ACTIONMSG=$"Disable"
fi

if [ "$ACTION" = resetstatus ]
then
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

	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/acceptable_use.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:::$GROUP:" | sudo -H /opt/karoshi/web_controls/exec/acceptable_use	
fi

[ -f /opt/karoshi/server_network/acceptable_use_authorisations/grace_time ] && GRACETIME=`sed -n 1,1p /opt/karoshi/server_network/acceptable_use_authorisations/grace_time | tr -cd 0-9` 
[ -z "$GRACETIME" ] && GRACETIME=14

#Generate navigation bar
if [ $MOBILE = no ]
then
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
	echo '<form action="/cgi-bin/admin/acceptable_use.cgi" name="acceptableuse" method="post"><div id="actionbox3"><div id="titlebox">
	<table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
	<tr><td style="vertical-align: top; width: 150px;"><div class="sectiontitle">'$"Acceptable Use"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Acceptable_Use"><img class="images" alt="" src="/images/help/info.png"><span>'$"The acceptable use policy gives new users a grace period to sign and return an acceptable use policy."' '$"User accounts are automatically disabled once the trial time is ended unless they are authorised."'</span></a></td></tr></tbody></table>
	<br>'

else
	#Show back button for mobiles
	echo '<form action="/cgi-bin/admin/acceptable_use.cgi" name="acceptableuse" method="post"><div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Acceptable Use"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
fi

if [ "$ACTION" = approve ]
then
	[ "$MOBILE" = no ] && echo '</div><div id="infobox">'
	send_data
	#Reload page
	echo '<script>
	window.location = "acceptable_use.cgi";
	</script>'		
fi
#Show acceptable use options for admin staff.

echo '<table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
<tr><td style="width: '$WIDTH1'px;">'$"Status"'</td><td style="width: '$WIDTH2'px;">
<button class="info" name="_Status_" value="_ACTION_'$ACTION2'_">
<img src="'$ICON'" alt="'$GRACETIMESTATUSMSG'">
<span>'$GRACETIMESTATUSMSG'</span>
</button>
</td><td style="width: '$WIDTH3'px;"><input name="_ACTION_'$ACTION2'_" type="submit" class="button" value="'$ACCEPTABLEUSESTATUS'"></td><td></td></tr>
<tr><td>'$"Grace Time"'</td><td><input maxlength="2" size="2" name="_GRACETIME_" value="'$GRACETIME'"></td>
<td><input name="_ACTION_setgracetime_" type="submit" class="button" value="'$"Set Grace Time"'"></td>
<td><a class="'$TOOLTIPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Acceptable_Use"><img class="images" alt="" src="/images/help/info.png"><span>'$"The grace time is the amount of time a new user is allowed to log into the system before signing and returning the acceptable use policy. This time is set in days."'</span></a></td>
</tr>
<tr><td>'$"Reset Status"'</td><td>'

#Show list of groups to reset the acceptable use grace time for
/opt/karoshi/web_controls/group_dropdown_list | sed 's/<option><\/option>/<option value="allusers">'$"All Users"'<\/option>/g' | sed 's/200/'$WIDTH4'/g'

echo '</td><td><input name="_ACTION_resetstatus_" type="submit" class="button" value="'$"Reset"'"></td><td><a class="'$TOOLTIPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Acceptable_Use"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the group that you want to reset the acceptable use status for."'</span></a></td>
</tbody></table><br>'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

#Get list of pending users
PROCESS_USERS=yes
if [ ! -d /opt/karoshi/server_network/acceptable_use_authorisations/pending ]
then
	PROCESS_USERS=no
fi

if [ $PROCESS_USERS = yes ]
then
	if [ `ls -1 /opt/karoshi/server_network/acceptable_use_authorisations/pending | wc -l` -lt 1 ]
	then
		PROCESS_USERS=no
	fi
fi

if [ $PROCESS_USERS = yes ]
then
	echo '<table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
	<tr><td style="vertical-align: top; width: 150px;"><div class="sectiontitle">'$"Pending Users"'</div></td>
	<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Acceptable_Use#View_pending_users"><img class="images" alt="" src="/images/help/info.png"><span>'$"The acceptable use policy gives new users a grace period to sign and return an acceptable use policy."' '$"User accounts are automatically disabled once the trial time is ended unless they are authorised."'</span></a></td>
	</tr></tbody></table><br>
	<table id="myTable" class="tablesorter" style="text-align: left;" ><thead>
	<tr><th style="vertical-align: top; width: 100px;"><b>'$"Username"'</b></th>'
	if [ $MOBILE = no ]
	then
		echo '<th style="vertical-align: top; width: 100px;"><b>'$"Created by"'</b></th><th style="vertical-align: top; width: 100px;"><b>'$"Creation Date"'</b></th>'
	fi
	echo '<th style="vertical-align: top; width: 150px;"><b>'$"Trial Days Remaining"'</b></th><th style="vertical-align: top; width: 80px;"><b>'$"Approve"'</b></th></tr></thead><tbody>
	'
	for PENDING_USER_FULL in /opt/karoshi/server_network/acceptable_use_authorisations/pending/*
	do
		PENDING_USER=`basename $PENDING_USER_FULL`
		PENDING_USER_DATA=`sed -n 1,1p $PENDING_USER_FULL`
		DAY_COUNT=`echo $PENDING_USER_DATA | cut -d, -f1`
		USER_CREATOR=`echo $PENDING_USER_DATA | cut -d, -f2`
		CREATION_DATE=`echo $PENDING_USER_DATA | cut -d, -f3`

		echo '<tr><td>'$PENDING_USER'</td>'
		if [ $MOBILE = no ]
		then
			echo '<td>'$USER_CREATOR'</td><td>'$CREATION_DATE'</td>'
		fi
		echo '<td>'$DAY_COUNT'</td><td><input name="_ACTION_approve_USERNAME_" value="'$PENDING_USER'" type="checkbox"></td></tr>'
	done

	echo '</tbody></table>'
fi


if [ $PROCESS_USERS = yes ]
then
	echo '<br><input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"><input class="button" type="button" onclick="SetAllCheckBoxes('\'acceptableuse\'', '\'_ACTION_approve_USERNAME_\'', true);" value="'$"Select all"'">'
fi

echo '</div>' 
[ $MOBILE = no ] && echo '</div>'
echo '</form></div></body></html>'
exit
