#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_software_controls ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_software_controls
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/linux_client_software_controls_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

#########################
#Assign data to variables
#########################
END_POINT=6
#Assign VERSION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = VERSIONcheck ]
then
let COUNTER=$COUNTER+1
VERSION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
WIDTH=180
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
WIDTH=160
fi

#########################
#Check data
#########################
#Check to see that VERSION is not blank
if [ -z $VERSION ]
then
MESSAGE=$ERRORMSG1
show_status
fi

echo '<form action="/cgi-bin/admin/linux_client_software_controls2.cgi" name="selectservers" method="post">'
[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$MENUMSG'</a>
</div></div><div id="mobileactionbox">'
else
echo '<b>'$TITLE' - '$VERSION'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Linux_Client_Software_Controls"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a><br><br>'
fi

#Check current settings
if [ -f /var/lib/samba/netlogon/linuxclient/nonfree/auto ]
then
AICON="/images/submenus/client/allowed.png"
ASTATUS=no
else
AICON="/images/submenus/client/denied.png"
ASTATUS=yes
fi
if [ -f /var/lib/samba/netlogon/linuxclient/nonfree/graphics-drivers ]
then
GICON="/images/submenus/client/allowed.png"
GSTATUS=no
else
GICON="/images/submenus/client/denied.png"
GSTATUS=yes
fi
if [ -f /var/lib/samba/netlogon/linuxclient/nonfree/restricted-extras ]
then
RICON="/images/submenus/client/allowed.png"
RSTATUS=no
else
RICON="/images/submenus/client/denied.png"
RSTATUS=yes
fi
if [ -f /var/lib/samba/netlogon/linuxclient/nonfree/firmware-nonfree ]
then
FICON="/images/submenus/client/allowed.png"
FSTATUS=no
else
FICON="/images/submenus/client/denied.png"
FSTATUS=yes
fi
if [ -f /var/lib/samba/netlogon/linuxclient/$VERSION/enable_software_install ]
then
SICON="/images/submenus/client/allowed.png"
SSTATUS=no
else
SICON="/images/submenus/client/denied.png"
SSTATUS=yes
fi
if [ -f /var/lib/samba/netlogon/linuxclient/$VERSION/enable_updates ]
then
UICON="/images/submenus/client/allowed.png"
USTATUS=no
else
UICON="/images/submenus/client/denied.png"
USTATUS=yes
fi

#Show controls for auto, graphics drivers and restricted extras
echo '<input name="_VERSION_" value="'$VERSION'" type="hidden"><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;">'$AUTOSMSG'</td><td><a class="info" href="javascript:void(0)"><input name="_AUTO_'$ASTATUS'_" type="image" class="images" src="'$AICON'" value=""><span>'$AUTOHELPMSG'</span></a></td></tr>
<tr><td style="width: 180px;">'$GRAPHICSDRVERSMSG'</td><td><a class="info" href="javascript:void(0)"><input name="_GRAPHICS_'$GSTATUS'_" type="image" class="images" src="'$GICON'" value=""><span>'$GRAPHICSDRVERSHELPMSG'</span></a></td></tr>
<tr><td style="width: 180px;">'$RESTRICTEDSMSG'</td><td><a class="info" href="javascript:void(0)"><input name="_RESTRICTED_'$RSTATUS'_" type="image" class="images" src="'$RICON'" value=""><span>'$RESTRICTEDHELPSMSG'</span></a></td></tr>
<tr><td style="width: 180px;">'$FIRRMWAREMSG'</td><td><a class="info" href="javascript:void(0)"><input name="_FIRMWARE_'$FSTATUS'_" type="image" class="images" src="'$FICON'" value=""><span>'$FIRMWAREHELPMSG'</span></a></td></tr>
<tr><td style="width: 180px;">'$ENABLEINSTALLMSG'</td><td><a class="info" href="javascript:void(0)"><input name="_SOFTWARE_'$SSTATUS'_" type="image" class="images" src="'$SICON'" value=""><span>'$INSTALLHELP'</span></a></td></tr>
<tr><td style="width: 180px;">'$ENABLEUPDATESMSG'</td><td><a class="info" href="javascript:void(0)"><input name="_UPDATES_'$USTATUS'_" type="image" class="images" src="'$UICON'" value=""><span>'$UPDATEHELP'</span></a></td></tr>
</tbody></table></div></form></div></body></html>'
exit

