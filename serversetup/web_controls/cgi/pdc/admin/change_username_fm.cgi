#!/bin/bash
#change_username
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
  <title>'$"Change a Username"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\--'`
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
#Generate navigation bar

#Generate navigation bar
if [ $MOBILE = no ]
then
	TOOLTIPCLASS="info"
	DIV_ID=actionbox
	TABLECLASS=standard
	WIDTH1=180
	WIDTH2=200
	HEIGHT=20
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	TOOLTIPCLASS="info infoleft"
	DIV_ID=mobileactionbox
	TABLECLASS=mobilestandard
	WIDTH1=130
	WIDTH2=150
	HEIGHT=25
fi

echo '<form action="/cgi-bin/admin/change_username.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Change a Username"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="'$DIV_ID'">
'
else
echo '<div id="'$DIV_ID'">
<table class="standard" style="text-align: left;" ><tbody>
<tr>
<td><div class="sectiontitle">'$"Change a Username"'</div></td>'

if [ ! -z "$USERNAME" ]
then
	echo '<td style="vertical-align: top;">
	<button class="button" formaction="/cgi-bin/admin/show_user_info.cgi" name="_SERVERNAME_'`hostname-fqdn`'_SERVERTYPE_network_SERVERMASTER_notset_ACTION_notset_USERNAME_" value="'$USERNAME'">
	'$"Edit User"'
	</button>
	</td>'
fi

echo '<td style="vertical-align: top;">
	<button class="button" formaction="/cgi-bin/admin/groups.cgi" name="____GroupManagement____">
	'$"Group Management"'
	</button>
</td>
</tr></table>
<br>'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left; height: 30px;" >
    <tbody>
      <tr>
        <td style="width: '$WIDTH1'px;">
'$"Username"'</td>
        <td><div id="suggestions"></div><input tabindex= "1" name="_USERNAME_" value="'$USERNAME'" size="20" style="width: '$WIDTH2'px; height: '$HEIGHT'px;" type="text" id="inputString" onkeyup="lookup(this.value);"></td><td>
<a class="'$TOOLTIPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the username that you want to change."'</span></a>
</td></tr>
<tr><td>'$"New Username"'</td><td><input tabindex= "2" name="_NEWUSERNAME_" size="20" style="width: '$WIDTH2'px;  height: '$HEIGHT'px;" type="text"></td><td>
<a class="'$TOOLTIPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new username for this user."'</span></a></td>
      </tr>
<tr><td>'$"New forename"'</td><td><input tabindex= "3" name="_FIRSTNAME_" size="20"  style="width: '$WIDTH2'px;  height: '$HEIGHT'px;" type="text"></td><td>
<a class="'$TOOLTIPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new username for this user."'</span></a></td>
      </tr>
<tr><td>'$"New surname"'</td><td><input tabindex= "4" name="_SURNAME_" size="20"  style="width: '$WIDTH2'px;  height: '$HEIGHT'px;" type="text"></td><td>
<a class="'$TOOLTIPCLASS'" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new username for this user."'</span></a></td>
      </tr>
    </tbody>
  </table>
  <br>'

[ $MOBILE = no ] && echo '</div><div id="submitbox">'
echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></form></div></body></html>
'
exit
