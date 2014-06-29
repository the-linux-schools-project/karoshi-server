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

##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><META HTTP-EQUIV="refresh" CONTENT="60"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
echo '</head><body><div id="pagecontainer">'
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

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
fi

#Check that a print server has been declared
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$PRINTSERVERERRORMSG'")';
echo 'window.location = "karoshi_servers_view.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

[ ! -f /opt/karoshi/server_network/printserver ] && show_status

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then

echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE1'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$MENUMSG'</a>
</div></div>
'

else
echo '<div id="titlebox"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top;"><b>'$TITLE1'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Manage_Print_Queues"><img class="images" alt="" src="/images/help/info.png"><span>'"$HELPMSG1"'</span></a></td>
<td style="vertical-align: top;">
<form action="/cgi-bin/admin/printers_add_fm.cgi" name="printers" method="post"><input name="ADDPRINTER" type="submit" class="button" value="'$ADDPRINTERMSG'"></form>
</td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers_delete.cgi" name="printers" method="post">
<input name="DELETEPRINTER" type="submit" class="button" value="'$DELETEPRINTERMSG'"></form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/locations.cgi" name="printers" method="post">
<input name="ADDLOCATION" type="submit" class="button" value="'$ADDLOCATIONMSG'"></form></td>
</tr></tbody></table></div>
'
fi

[ $MOBILE = no ] && echo '<div id="infobox">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/printers $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:
[ $MOBILE = no ] && echo '</div>'
echo "</div></div></body></html>"
exit
