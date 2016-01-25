#!/bin/bash
#Copyright (C) 2013  Paul Sharrad

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"User Web Folders"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
echo '
</head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

#########################
#Assign data to variables
#########################
END_POINT=11
#Assign group
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
#Assign action
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
#Assign SERVICECHECK
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVICECHECKcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVICECHECK=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

[ -z "$ACTION" ] && ACTION=check
[ -z "$SERVICECHECK" ] && SERVICECHECK=yes
[ -z "$USERNAME" ] && USERNAME=notset

#Generate navigation bar
if [ $MOBILE = no ]
then
	TOOLTIPCLASS="info"
	DIV_ID=actionbox3
	[ -z "$GROUP" ] && DIV_ID=actionbox
	TABLECLASS=standard
	WIDTH1=180
	WIDTH2=200
	HEIGHT1=25
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	TOOLTIPCLASS="info infoleft"
	DIV_ID=actionbox
	TABLECLASS=mobilestandard
	WIDTH1=120
	WIDTH2=140
	HEIGHT1=30
fi
echo '<form name="myform" action="/cgi-bin/admin/user_web_folders.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"User Web Folders"' '$GROUP'</span>' 

	if [ -z "$GROUP" ]
	then
		echo '<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>'
	else
		echo '<a href="/cgi-bin/admin/user_web_folders.cgi">'$"Select Group"'</a>'
	fi

	echo '</div></div><div id="mobileactionbox">
'
else
echo '<div id="'$DIV_ID'">'

[ ! -z "$GROUP" ] && echo '<div id="titlebox">'

echo '<table class="standard" style="text-align: left;" ><tbody>
<tr>
<td style="vertical-align: top;">
<div class="sectiontitle">'$"User Web Folders"'</div>
</td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=User_web_folders"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows users to have web folders hosted from their home areas. Any files and folders in a public_html folder in the user's home area will be available via apache on their server."'</span></a></td>
<td style="vertical-align: top;">'
[ ! -z "$GROUP" ] && echo '<a href="user_web_folders.cgi"><input class="button" type="button" name="" value="Choose group"></a>'
echo '</td>
</tr></table><br>'
fi

#Show list of groups to check
if [ -z "$GROUP" ]
then
	echo '<table class="'$TABLECLASS'" style="text-align: left;" >
	    <tbody><tr><td style="width: '$WIDTH1'px;">'$"Primary Group"'</td>
	<td>'
	/opt/karoshi/web_controls/group_dropdown_list | sed 's/style="width: 200px;">/style="width: '$WIDTH2'px; height: '$HEIGHT1'px;">/g'
	echo '</td>
	<td><a class="'$TOOLTIPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=User_web_folders"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the group that you want to set the web folder status for."'</span></a></td>
	</tr></tbody></table><br><br>
	'
	[ $MOBILE = no ] && echo '</div><div id="submitbox">'
	echo '<input value="'$"Submit"'" class="button" type="submit">
	</div></form></div></body></html>
	'
	exit
fi

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$GROUP:$ACTION:$USERNAME:$SERVICECHECK:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/user_web_folders

[ $MOBILE = no ] && echo '</div>'
echo '</div></form></div></body></html>'
exit

