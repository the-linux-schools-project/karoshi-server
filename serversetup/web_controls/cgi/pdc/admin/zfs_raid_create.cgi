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
########################
#Required input variables
########################
#  _SERVER_
#  _PASSWORD1_  Root Password
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server


function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/zfs_raid_create_fm.cgi";'
echo '</script>
'
echo "</div></body></html>"
exit
}

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Create ZFS Raid"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%/+-' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g'`

#########################
#Assign data to variables
#########################

#Assign SERVER

END_POINT=32
#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SERVERTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERTYPEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SERVERMASTER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERMASTERcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERMASTER=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign CREATETYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = CREATETYPEcheck ]
	then
		let COUNTER=$COUNTER+1
		CREATETYPE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
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
#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The server cannot be blank."
	show_status
fi

#Check to see that SERVERTYPE is not blank
if [ -z "$SERVERTYPE" ]
then
	MESSAGE=$"The servertype cannot be blank."
	show_status
fi

#Check to see that SERVERMASTER is not blank
if [ $SERVERTYPE = federatedslave ]
then
	if [ -z "$SERVERMASTER" ]
	then
		MESSAGE=$"The servermaster cannot be blank."
		show_status
	fi
fi

MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=menubox
fi

echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<table class="standard" style="text-align: left;">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Create ZFS Raid" - $SERVERNAME'</b></a></td>
</tr></tbody></table>'
else
	WIDTH=100
	ICON1="/images/submenus/system/computer.png"
	ICON2="/images/submenus/system/zfs.png"

	echo '<div id="titlebox">

	<div class="sectiontitle">'$"Create ZFS Raid"' - '$SERVERNAME' <a class="info" target="_blank" href="http://www.linuxgfx.co.uk/karoshi/documentation/wiki/index.php?title=ZFS_Raid"><img class="images" alt="" src="/images/help/info.png"><span>"'$"Choose the server you want to view the raid information for."'"</span></a></div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<form action="zfs_raid_create_fm.cgi" name="selectservers" method="post">
				<button class="info infonavbutton" name="CreateRaid" value="_">
					<img src="'$ICON1'" alt="'$"Select Server"'">
					<span>'$"Select a server."'</span><br>
					'$"Select Server"'
				</button>
			</form>
		</td>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<form action="zfs_raid_control_fm.cgi" name="selectservers" method="post">
				<button class="info infonavbutton" name="SelectServer" value="_">
					<img src="'$ICON1'" alt="'$"ZFS Status"'">
					<span>'$"ZFS Status"'</span><br>
					'$"ZFS Status"'
				</button>
			</form>
		</td>

	</tr></tbody></table>

<br></div><div id="infobox">
<br>'

fi

Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/zfs_raid_create.cgi | cut -d' ' -f1`
echo '<form action="/cgi-bin/admin/zfs_raid_create2.cgi" name="selectservers" method="post">'
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$CREATETYPE:" | sudo -H /opt/karoshi/web_controls/exec/zfs_raid_create

echo "</form></div></div></div></body></html>"
exit
