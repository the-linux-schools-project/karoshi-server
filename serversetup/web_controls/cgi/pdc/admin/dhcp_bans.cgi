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

#Website: http://www.karoshi.org.uk

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"DHCP Bans"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter({
	headers: {
	1: { sorter: "MAC" },
	2: { sorter: "ipAddress" },
	3: { sorter: false},
	4: { sorter: false}
    		}
		});
    } 
);
</script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`

#########################
#Assign data to variables
#########################
END_POINT=15
#Assign CLIENTHOSTNAME

COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = CLIENTHOSTNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		CLIENTHOSTNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign MACADDRESS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = MACADDRESScheck ]
		then
		let COUNTER=$COUNTER+1
		MACADDRESS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3A/:/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign COMMENT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = COMMENTcheck ]
		then
		let COUNTER=$COUNTER+1
		COMMENT=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3A/:/g'`
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

[ -z "$ACTION" ] && ACTION=view

function show_warnings {
echo '<script>
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/dhcp_bans.cgi";
</script>'

exit
}

#Check data

if [ $ACTION = reallyadd ] || [ $ACTION = delete ]
then
	#Check that clienthostname is not blank
	if [ -z "$CLIENTHOSTNAME" ]
	then
	ACTION=view
	MESSAGE=$"You have not entered in a client name."
	show_warnings
	fi
fi

if [ $ACTION = reallyadd ]
then
	#Check that mac address is not blank
	if [ -z "$MACADDRESS" ]
	then
		ACTION=view
		MESSAGE=$"You have not entered a mac address."
		show_warnings
	else
		#Check that the mac address is formatted correctly
		#Check colons 00:13:77:b8:39:17
		if [ `echo "$MACADDRESS" | sed 's/:/\n/g' | wc -l` != 6 ]
		then
			ACTION=view
			MESSAGE=$"You have not entered in a valid mac address."
			show_warnings	
		fi
		#Check max chars
		for LINEDATA in `echo "$MACADDRESS" | sed 's/:/\n/g'`
		do
			if [ `echo "$LINEDATA" | wc -L` != 2 ]
			then
				ACTION=view
				MESSAGE=$"You have not entered in a valid mac address."
				show_warnings
			fi
		done
		#Check to see that the mac address has not already been added
		if [ $(grep -r -h -w "$MACADDRESS" /opt/karoshi/server_network/dhcp/bans/ | grep -c -w "$MACADDRESS") -gt 0 ]
		then
				ACTION=view
				MESSAGE=$"This mac address is already in use."
				show_warnings
		fi
	fi
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	WIDTH1=180
	WIDTH2=110
	WIDTH3=300
	WIDTH4=70	
	WIDTH5=200
	ICON1=/images/submenus/system/edit.png
	ICON2=/images/submenus/system/delete.png
	TABLECLASS=standard

	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	WIDTH1=80
	WIDTH2=100
	WIDTH3=100
	WIDTH4=70
	WIDTH5=150
	ICON1=/images/submenus/system/editm.png
	ICON2=/images/submenus/system/deletem.png
	TABLECLASS=mobilestandard
fi

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

echo '<form name="reservervationbuttons" action="/cgi-bin/admin/dhcp_bans.cgi" method="post">'

if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"DHCP Bans"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="mobileactionbox">
'
	if [ $ACTION = view ]
	then
		echo '<input name="_ACTION_add_ban_" type="submit" class="button" value="'$"Add DHCP Ban"'"><br><br>'
	else
		echo '<input name="_ACTION_view_" type="submit" class="button" value="'$"View DHCP Bans"'"><br><br>'
	fi
else
	WIDTH=100
	ICON1=/images/submenus/system/add.png
	ICON2=/images/submenus/system/ban.png
	ICON3=/images/submenus/system/dhcp.png
	ICON4=/images/submenus/system/edit.png
	ICON5=/images/submenus/system/delete.png
	ICON6=/images/submenus/system/reload.png

	echo '
	<div class="sectiontitle">'$"DHCP Bans"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Bans"><img class="images" alt="" src="/images/help/info.png"><span>'$"This allows stop a MAC address from being assigned a tcpip number."'</span></a></div><table class="tablesorter"><tbody><tr>'

	if [ $ACTION = view ]
	then
		echo '
			<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
				<button class="info" name="_BanDHCP_" value="_ACTION_add_ban_">
					'$"Add"'<br>
					<img src="'$ICON1'" alt="'$"Add DHCP Ban"'">
					<span>'$"Add DHCP Ban"'</span>
				</button>
			</td>
		'
	else
		echo '
			<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
				<button class="info" name="_ViewDHCPBans_" value="_ACTION_view_">
					'$"View"'<br>
					<img src="'$ICON2'" alt="'$"View banned DHCP devices"'">
					<span>'$"View banned DHCP devices"'</span>
				</button>
			</td>

		'
	fi



	echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<button class="info" formaction="dhcp_view_leases.cgi" name="_ConfigureDHCP_" value="_">
			'$"DHCP Leases"'<br>
			<img src="'$ICON3'" alt="'$"View DHCP Leases"'">
			<span>'$"View DHCP Leases"'</span>
		</button>
	</td>



		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info" formaction="dhcp_fm.cgi" name="_ConfigureDHCP_" value="_">
				'$"Configure"'<br>
				<img src="'$ICON4'" alt="'$"Configure DHCP"'">
				<span>'$"Configure DHCP"'</span>
			</button>
		</td>
	</tbody></table><br>
	'

	if [ -d /opt/karoshi/server_network/dhcp/bans_delete ]
	then
		echo '
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info" name="_DeleteAll_" value="_ACTION_reallydelete_">
				'$"Delete"'<br>
				<img src="'$ICON5'" alt="'$"Delete DHCP bans"'">
				<span>'$"Delete DHCP bans"'</span>
			</button>
		</td>'
	fi
	if [ -f /opt/karoshi/server_network/dhcp/restart_required ]
	then
		echo '
		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
			<button class="info" name="_ActivateChanges_" value="_ACTION_restartdhcp_">
				'$"Activate Changes"'<br>
				<img src="'$ICON6'" alt="'$"Activate Changes"'">
				<span>'$"Activate Changes"'</span>
			</button>
		</td>
		'
	fi
	echo '</tr></tbody></table></form></div><div id="infobox">
	'
fi

function view_bans {

SHOWENTRIES=no
if [ -d /opt/karoshi/server_network/dhcp/bans ]
then 
	if [ `ls -1 /opt/karoshi/server_network/dhcp/bans | wc -l` -gt 0 ]
	then
		SHOWENTRIES=yes
		#Check if we have any entries to delete
		CHECKDELETED=no
		[ -d /opt/karoshi/server_network/dhcp/bans_delete ] && CHECKDELETED=yes
		echo '<form id="bans" name="bans" action="/cgi-bin/admin/dhcp_bans.cgi" method="post"><table id="myTable" class="tablesorter" style="text-align: left;" ><thead>
		<tr><th style="width: '$WIDTH1'px;"><b>'$"Host name"'</b></th><th style="width: '$WIDTH2'px;"><b>'$"Mac Address"'</b></th><th style="width: '$WIDTH3'px;"><b>'$"Comment"'</b></th><th style="width:'$WIDTH4'px;">'
		if [ ! -d /opt/karoshi/server_network/dhcp/bans_delete/ ]
		then
			echo '<button class="button" name="_DeleteAll_" value="_ACTION_deleteall_CLIENTHOSTNAME_deleteall_">
			'$"Select all"'
			</button>'
		else
			echo '<button class="button" name="_DeleteAll_" value="_ACTION_clearall_CLIENTHOSTNAME_clearall_">
			'$"Clear all"'
			</button>'
		fi
		echo '</th></tr></thead><tbody>'

		for CLIENTHOSTNAMES in /opt/karoshi/server_network/dhcp/bans/*
		do
			CLIENTHOSTNAME=`basename $CLIENTHOSTNAMES`
			ALTDELETEMSG=$"Delete ban"
			DELETEACTION=delete
			DELETESTYLE=""
			if [ -f /opt/karoshi/server_network/dhcp/bans_delete/"$CLIENTHOSTNAME" ]
			then
				ALTDELETEMSG=$"Cancel delete ban"
				DELETEACTION=canceldelete
				DELETESTYLE='style="color: #FFF; background-color:#CA0D26"'
			fi
			#Get details
			COMMENT=""
			source $CLIENTHOSTNAMES
			echo '<tr><td id="'$CLIENTHOSTNAME'" '$DELETESTYLE'>'$CLIENTHOSTNAME'</td><td '$DELETESTYLE'>'$MACADDRESS'</td><td '$DELETESTYLE'>'$COMMENT'</td><td '$DELETESTYLE'>
			<button class="info" name="_Delete_" value="_ACTION_'$DELETEACTION'_CLIENTHOSTNAME_'$CLIENTHOSTNAME'_">
			<img src="'$ICON2'" alt="'$ALTDELETEMSG'">
			<span>'$ALTDELETEMSG'</span>
			</button>
			</td></tr>'
		done
		echo '</tbody></table></form><br>'
	fi
fi

if [ $SHOWENTRIES = no ]
then
	echo $"There are no current dhcp bans.""<br>"
fi
}

function add_ban {
FORMACTION=reallyadd

echo '<form name="addban" action="/cgi-bin/admin/dhcp_bans.cgi" method="post"><input type="hidden" name="_ACTION_'$FORMACTION'_" value="English"><table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
<tr><td style="width: '$WIDTH1'px;">'$"Host name"'</td>
<td><input tabindex= "1" style="width: '$WIDTH5'px;" name="_CLIENTHOSTNAME_" value="'$CLIENTHOSTNAME'" 
 size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Ban"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the host name of the client computer or device that you want to ban."'</span></a></td></tr>
<tr><td>'$"Mac Address"'</td><td><input tabindex= "2" style="width: '$WIDTH5'px;" name="_MACADDRESS_" value="'$MACADDRESS'"
 size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Ban"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the mac address of the client computer or device that you want to ban."'</span></a></td></tr>
<tr><td>'$"Comment"'</td><td><input tabindex= "3" style="width: '$WIDTH5'px;" name="_COMMENT_" size="20" type="text"></td>
</tbody></table><br>'

echo '<br>'

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></form>'
}

[ $ACTION = view ] && view_bans
[ $ACTION = add ] && add_ban

if [ $ACTION = reallydelete ] || [ $ACTION = delete ] || [ $ACTION = canceldelete ] || [ $ACTION = deleteall ] || [ $ACTION = clearall ] || [ $ACTION = reallyadd ] || [ $ACTION = restartdhcp ]
then
	MACADDRESS=`echo $MACADDRESS | sed 's/:/%3A/g'`
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/dhcp_bans.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$CLIENTHOSTNAME:$MACADDRESS:$COMMENT:" | sudo -H /opt/karoshi/web_controls/exec/dhcp_bans
	#view_bans
	FORMID=bans
	if [ "$ACTION" = delete ] || [ $ACTION = canceldelete ]
	then
		FORMID="$CLIENTHOSTNAME"
	fi
	#Reload page
	echo '<form id="'$FORMID'" name="bans" action="/cgi-bin/admin/dhcp_bans.cgi#'$FORMID'" method="post"><script>
	document.getElementById("'$FORMID'").submit();
	</script></form>'

fi
echo '</div></div></div></body></html>'
exit
