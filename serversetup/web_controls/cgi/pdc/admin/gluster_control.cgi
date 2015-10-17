#!/bin/bash
#Copyright (C) 2015  Paul Sharrad

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
  <title>'$"Gluster Volume Control"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script type="text/javascript" id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
TCPIP_ADDR=$REMOTE_ADDR

DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+*'`

#########################
#Assign data to variables
#########################
END_POINT=24
#Assign VOLUME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = VOLUMEcheck ]
	then
		let COUNTER=$COUNTER+1
		VOLUME=`echo $DATA | cut -s -d'_' -f$COUNTER`
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

#Assign SERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SERVERS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVERScheck ]
	then
		let COUNTER=$COUNTER+1
		SERVERS=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign FOLDER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = FOLDERcheck ]
	then
		let COUNTER=$COUNTER+1
		FOLDER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done



function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/gluster_control.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

[ -z "$ACTION" ] && ACTION=view

ACTION2=create
ACTIONMSG=$"Create Gluster Volume"
if [ "$ACTION" = create ] || [ "$ACTION" = addfolder ] || [ "$ACTION" = assignshare ] || [ "$ACTION" = removefolder ] || [ "$ACTION" = confirmremovefolder ] || [ "$ACTION" = reallyremovefolder ]  
then
ACTION2=view
ACTIONMSG=$"View Gluster Volumes"
fi
#########################
#Check data
#########################
TITLE="View Volumes"
[ $ACTION = create ] && TITLE=$"Create Volume"
[ $ACTION = reallycreate ] && TITLE=$"Creating Volume"
[ $ACTION = addfolder ] && TITLE=$"Add Folder"
[ $ACTION = reallyaddfolder ] && TITLE=$"Ading Folder"
[ $ACTION = assignshare ] && TITLE=$"Assign Network Share"
[ $ACTION = removefolder ] && TITLE=$"Remove Folder"

if [ "$ACTION" != create ] && [ "$ACTION" != reallycreate ] && [ "$ACTION" != restore ] && [ "$ACTION" != view ] && [ "$ACTION" != addfolder ] && [ "$ACTION" != reallyaddfolder ] && [ "$ACTION" != assignhomefolders ] && [ "$ACTION" != removefolder ] && [ "$ACTION" != reallyremovefolder ] && [ "$ACTION" != confirmremovefolder ]
then
	MESSAGE=$"You have not entered a correct action."
	show_status
fi

if [ "$ACTION" = reallycreate ]
then
	if [ -z "$VOLUME" ]
	then
		MESSAGE=$"You have not entered a volume name."
		show_status
	fi
	if [ -z "$SERVERS" ]
	then
		MESSAGE=$"You have not chosen any servers."
		show_status
	fi
	if [ `echo $SERVERS | sed 's/%2C/,/g' | grep -c ","` = 0 ]
	then
		MESSAGE=$"You have to choose at least two servers to create a distributed volume."
		show_status
	fi

	if [ -d /opt/karoshi/server_network/gluster-volumes/"$VOLUME" ]
	then
		MESSAGE=''$VOLUME' - '$"This volume has already been created."''
		show_status
	fi
fi

if [ "$ACTION" = reallyaddfolder ]
then
	if [ -z "$VOLUME" ]
	then
		MESSAGE=$"You have not entered a volume name."
		show_status
	fi
	if [ -z "$FOLDER" ]
	then
		MESSAGE=$"You have not chosen a folder path."
		show_status
	fi	
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=mobileactionbox
fi



#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu"><div class="expanded"><span>'$"Gluster Controls"' '$SERVER2'</span></div></div><div id="'$DIV_ID'">
'
else
	echo '<div id="'$DIV_ID'"><div id="titlebox">
<form action="/cgi-bin/admin/gluster_control.cgi" method="post"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top;"><div class="sectiontitle">Gluster - '$TITLE'</div></td>
<td><input name="_ACTION_'$ACTION2'_" type="submit" class="button" value="'$ACTIONMSG'"></td>
<td><a href="home_folders_fm.cgi"><input class="button" type="button" name="" value="'$"Home Folders"'"></a></td>
<td><a href="samba_shares.cgi"><input class="button" type="button" name="" value="'$"Network Shares"'"></a></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Gluster_Volumes"><img class="images" alt="" src="/images/help/info.png"><span>'$"Gluster Volumes"'</span></a></td></tr></tbody></table></form></div><div id="infobox">'
fi

echo '<form action="/cgi-bin/admin/gluster_control.cgi" method="post" id="form1" name="combobox">'
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/gluster_control.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$VOLUME:$SERVER:$SERVERS:$FOLDER:" | sudo -H /opt/karoshi/web_controls/exec/gluster_control
echo '</form>'

[ $MOBILE = no ] && echo '</div>'

echo '</div></div></body></html>'
exit
