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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_install_software_packages ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_install_software_packages
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
echo '                window.location = "/cgi-bin/admin/linux_client_install_software_packages_fm.cgi";'
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
WIDTH2=50
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
WIDTH=160
WIDTH2=50
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
echo '<b>'$TITLE' - '$VERSION'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Linux_Client_Software_Packages"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a><br><br>'
fi

#Show a table of current software to install and remove
# install - /var/lib/samba/netlogon/linuxclient/version/install_list
# remove - /var/lib/samba/netlogon/linuxclient/version/remove_list

ICON1=/images/submenus/client/install_software.png
ICON2=/images/submenus/client/remove_software.png
ICON3=/images/submenus/client/delete_software.png

#Show input box
echo '<form action="/cgi-bin/admin/linux_client_install_software_packages2.cgi" name="selectservers" method="post"><input name="___VERSION___" value="'$VERSION'" type="hidden">
<b>'$ADDSOFTWAREPKG'</b><br><br><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: '$WIDTH'px;">'$SOFTWAREMSG'</td><td><input tabindex= "1" name="___ACTION___add___SOFTWARE___" style="width: '$WIDTH'px;" size="20" type="text"></td>
<td><a class="info" href="javascript:void(0)"><input name="___LIST___install___" type="image" class="images" src="'$ICON1'" value=""><span>'$INSTALLMSG'</span></a></td>
<td><a class="info" href="javascript:void(0)"><input name="___LIST___remove___" type="image" class="images" src="'$ICON2'" value=""><span>'$REMOVEMSG'</span></a></td></tr>
</tbody></table><br></form>'

#Show install list
if [ -f /var/lib/samba/netlogon/linuxclient/$VERSION/install_list ]
then
if [ `cat /var/lib/samba/netlogon/linuxclient/$VERSION/install_list | wc -l` -gt 0 ]
then
echo '<form action="/cgi-bin/admin/linux_client_install_software_packages2.cgi" name="selectservers" method="post">
<input name="___VERSION___" value="'$VERSION'" type="hidden">
<b>'$INSTALLLISTMSG'</b><br><br><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: '$WIDTH'px;"><b>'$SOFTWAREMSG'</b></td><td style="width: '$WIDTH2'px;"><b>'$INSTALLMSG'</b></td><td><b>'$DELETEMSG'</b></td></tr>'
for SOFTWARE in `cat /var/lib/samba/netlogon/linuxclient/$VERSION/install_list`
do
echo '<tr><td>'$SOFTWARE'</td><td><a class="info" href="javascript:void(0)"><input name="___LIST___install___ACTION___remove___SOFTWARE___'$SOFTWARE'___" type="image" class="images" src="'$ICON1'" value=""><span>'$INSTALLMSG $SOFTWARE'</span></a></td><td><a class="info" href="javascript:void(0)"><input name="___LIST___install___ACTION___delete___SOFTWARE___'$SOFTWARE'___" type="image" class="images" src="'$ICON3'" value=""><span>'$DELETEMSG $SOFTWARE'</span></a></td></tr>'
done
echo '</tbody></table><br></form>'
fi
fi

#Show remove list
if [ -f /var/lib/samba/netlogon/linuxclient/$VERSION/remove_list ]
then
if [ `cat /var/lib/samba/netlogon/linuxclient/$VERSION/remove_list | wc -l` -gt 0 ]
then
echo '<form action="/cgi-bin/admin/linux_client_install_software_packages2.cgi" name="selectservers" method="post">
<input name="___VERSION___" value="'$VERSION'" type="hidden">
<b>'$REMOVELISTMSG'</b><br><br><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: '$WIDTH'px;"><b>'$SOFTWAREMSG'</b></td><td style="width: '$WIDTH2'px;"><b>'$REMOVEMSG'</b></td><td><b>'$DELETEMSG'</b></td></tr>'
for SOFTWARE in `cat /var/lib/samba/netlogon/linuxclient/$VERSION/remove_list`
do
echo '<tr><td>'$SOFTWARE'</td><td><a class="info" href="javascript:void(0)"><input name="___LIST___remove___ACTION___install___SOFTWARE___'$SOFTWARE'___" type="image" class="images" src="'$ICON1'" value=""><span>'$INSTALLMSG $SOFTWARE'</span></a></td><td><a class="info" href="javascript:void(0)"><input name="___LIST___remove___ACTION___delete___SOFTWARE___'$SOFTWARE'___" type="image" class="images" src="'$ICON3'" value=""><span>'$DELETEMSG $SOFTWARE'</span></a></td></tr>'
done
echo '</tbody></table></form>'
fi
fi
echo '</div></div></body></html>'
exit


