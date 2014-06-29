#!/bin/bash
#Change password
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

############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/dhcp ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/dhcp
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
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
  <title>'$TITLE3'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
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
END_POINT=11
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
#Assign TCPIPADDRESS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = TCPIPADDRESScheck ]
	then
		let COUNTER=$COUNTER+1
		TCPIPADDRESS=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
echo '<script type="text/javascript">
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/dhcp_reservations.cgi";
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
	MESSAGE="$ERRORMSG12"
	show_warnings
	fi
fi

if [ $ACTION = reallyadd ]
then
	#Check that tcpip is not blank
	if [ -z "$TCPIPADDRESS" ]
	then
		ACTION=view
		MESSAGE="$ERRORMSG10"
		show_warnings
	else
		#Check that the tcpip number has been entered correctly
		#Check dots
		if [ `echo $TCPIPADDRESS | sed 's/\./\n /g'  | sed /^$/d | wc -l` != 4 ]
		then
			ACTION=view
			MESSAGE="$ERRORMSG11"
			show_warnings
		fi
		#Check that no number is greater than 255
		HIGHESTNUMBER=`echo $TCPIPADDRESS | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p`
		if [ $HIGHESTNUMBER -gt 255 ]
		then
			ACTION=view
			MESSAGE="$ERRORMSG11"
			show_warnings
		fi
		#Check to see that the tcpip number has not already been added
		if [ -f /opt/karoshi/server_network/dhcp/reservations ]
		then
			if [ `grep -R -w "$TCPIPADDRESS" /opt/karoshi/server_network/dhcp/reservations | wc -l` -gt 0 ]
			then
				ACTION=view
				MESSAGE="$ERRORMSG15"
				show_warnings		
			fi
		fi
	fi
	#Check that mac address is not blank
	if [ -z "$MACADDRESS" ]
	then
		ACTION=view
		MESSAGE="$ERRORMSG13"
		show_warnings
	else
		#Check that the mac address is formatted correctly
		#Check colons 00:13:77:b8:39:17
		if [ `echo "$MACADDRESS" | sed 's/:/\n/g' | wc -l` != 6 ]
		then
			ACTION=view
			MESSAGE="$ERRORMSG14"
			show_warnings	
		fi
		#Check max chars
		for LINEDATA in `echo "$MACADDRESS" | sed 's/:/\n/g'`
		do
			if [ `echo "$LINEDATA" | wc -L` != 2 ]
			then
				ACTION=view
				MESSAGE="$ERRORMSG14"
				show_warnings
			fi
		done
		#Check to see that the mac address has not already been added
		if [ -f /opt/karoshi/server_network/dhcp/reservations ]
		then
			if [ `grep -R -w "$MACADDRESS" /opt/karoshi/server_network/dhcp/reservations | wc -l` -gt 0 ]
			then
				ACTION=view
				MESSAGE="$ERRORMSG16"
				show_warnings		
			fi
		fi
	fi		
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	WIDTH1=180
	WIDTH2=110
	WIDTH3=110
	WIDTH4=200
	ICON1=/images/submenus/system/edit.png
	ICON2=/images/submenus/system/delete.png
	TABLECLASS=standard

	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	WIDTH1=80
	WIDTH2=100
	WIDTH3=80
	WIDTH4=150
	ICON1=/images/submenus/system/editm.png
	ICON2=/images/submenus/system/deletem.png
	TABLECLASS=mobilestandard
fi

echo '<form id="reservervations" name="reservervations" action="/cgi-bin/admin/dhcp_reservations.cgi" name="reservation" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$TITLE3'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$MENUMSG'</a>
	</div></div><div id="mobileactionbox">
'
	if [ $ACTION = view ]
	then
		echo '<input name="_ACTION_add_reservation_" type="submit" class="button" value="'$ADDRESERVATION'"><br><br>'
	else
		echo '<input name="_ACTION_view_" type="submit" class="button" value="'$VIEWRESERVATIONS'"><br><br>'
	fi
else
	echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>
	<td style="vertical-align: top; width:180px"><div class="sectiontitle">'$TITLE3'</div></td>
	<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Reservation"><img class="images" alt="" src="/images/help/info.png"><span>'$RESERVATIONHELP'</span></a></td>
	<td style="vertical-align: top;">'

	if [ $ACTION = view ]
	then
		echo '<input name="_ACTION_add_reservation_" type="submit" class="button" value="'$ADDRESERVATION'">'
	else
		echo '<input name="_ACTION_view_" type="submit" class="button" value="'$VIEWRESERVATIONS'">'
	fi
	echo '</td><td style="vertical-align: top;"><a href="dhcp_view_leases.cgi"><input class="button" type="button" name="" value="'$TITLE2'"></a></td><td style="vertical-align: top;"><a href="dhcp_fm.cgi"><input class="button" type="button" name="" value="'$TITLE'"></a></td></tr></tbody></table></div><div id="infobox">
	'
fi

function view_reservations {

SHOWENTRIES=no
if [ -d /opt/karoshi/server_network/dhcp/reservations ]
then 
	if [ `ls -1 /opt/karoshi/server_network/dhcp/reservations | wc -l` -gt 0 ]
		then
		SHOWENTRIES=yes
		echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
		<tr><td style="width: '$WIDTH1'px;"><b>'$HOSTNAMEMSG'</b></td><td style="width: '$WIDTH2'px;"><b>'$MACMSG'</b></td><td style="width:'$WIDTH3'px;"><b>'$TCPMSG'</b></td></tr>'

		for CLIENTHOSTNAMES in /opt/karoshi/server_network/dhcp/reservations/*
			do
			CLIENTHOSTNAME=`basename $CLIENTHOSTNAMES`
			#Get details
			source $CLIENTHOSTNAMES
			echo '<tr><td>'$CLIENTHOSTNAME'</td><td>'$MACADDRESS'</td><td>'$TCPIPADDRESS'</td><td>
			<a class="info" href="javascript:void(0)"><input name="_ACTION_edit_'$CLIENTHOSTNAME'_CLIENTHOSTNAME_'$CLIENTHOSTNAME'_MACADDRESS_'$MACADDRESS'_TCPIPADDRESS_'$TCPIPADDRESS'_" type="image" class="images" src="'$ICON1'" value=""><span>'$EDITMSG'</span></a>
			</td><td>
			<a class="info" href="javascript:void(0)"><input name="_ACTION_delete_CLIENTHOSTNAME_'$CLIENTHOSTNAME'_" type="image" class="images" src="'$ICON2'" value=""><span>'$DELETEMSG'</span></a>
			</td></tr>'
			done
		echo '</tbody></table><br>'
	fi
fi

if [ $SHOWENTRIES = no ]
then
echo $ERRORMSG9"<br>"
fi
}

function add_reservation {

echo '<input type="hidden" name="_ACTION_reallyadd_" value="English"><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: '$WIDTH1'px;">'$HOSTNAMEMSG'</td>
<td><input tabindex= "1" style="width: '$WIDTH4'px;" name="_CLIENTHOSTNAME_" value="'$CLIENTHOSTNAME'" 
 size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Reservation"><img class="images" alt="" src="/images/help/info.png"><span>'$HOSTNAMEHELP'</span></a></td></tr>
<tr><td>'$MACMSG'</td><td><input tabindex= "2" style="width: '$WIDTH4'px;" name="_MACADDRESS_" value="'$MACADDRESS'"
 size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Reservation"><img class="images" alt="" src="/images/help/info.png"><span>'$MACHELP'</span></a></td></tr>
<tr><td>'$TCPMSG'</td><td><input tabindex= "2" style="width: '$WIDTH4'px;" name="_TCPIPADDRESS_"  value="'$TCPIPADDRESS'"
 size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=DHCP_Reservation"><img class="images" alt="" src="/images/help/info.png"><span>'$TCPHELP'</span></a></td></tr> 
</tbody></table><br>'

echo '<br>'

echo '<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"></div>'
}

[ $ACTION = view ] && view_reservations
[ $ACTION = add ] && add_reservation
[ $ACTION = edit ] && add_reservation


if [ $ACTION = reallyedit ] || [ $ACTION = delete ] || [ $ACTION = reallyadd ]
	then
	MACADDRESS=`echo $MACADDRESS | sed 's/:/%3A/g'`
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/dhcp_reservations.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$CLIENTHOSTNAME:$MACADDRESS:$TCPIPADDRESS:" | sudo -H /opt/karoshi/web_controls/exec/dhcp_reservations
	#view_reservations
	#Reload page
	echo '<script>
	document.getElementById("reservervations").submit();
	</script>'

fi
echo '</div></div></form></div></body></html>'
exit
