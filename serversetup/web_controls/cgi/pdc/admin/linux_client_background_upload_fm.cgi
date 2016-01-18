#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<TITLE>'$"Linux Background - Upload"'</TITLE><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
MAXSTYLES=5
WIDTH1=180
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=mobileactionbox
TABLECLASS=mobilestandard
MAXSTYLES=4
WIDTH1=90
fi


[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Linux Background - Upload"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="'$DIV_ID'">'
else
echo '<form action="/cgi-bin/admin/linux_client_choose_background_fm.cgi" method="post"><table class="standard" style="text-align: left;" ><tbody><tr><td><b>'$"Linux Background - Upload"'</b></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Linux_Client_Background"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will replace the standard background with one of your choice. The backgrounds are applied when the client computer is rebooted."'</span></a>
</td><td style="vertical-align: top;">
<input name="_VIEW_" type="submit" class="button" value="'$"View Backgrounds"'">
</td></tr></tbody></table></form>'
fi

echo '<P>
'$"Please select the background that you want to upload."':
<P>
        <FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/linux_client_background_upload.cgi" METHOD="POST">
        <TABLE class="'$TABLECLASS'" BORDER="0" cellpadding="2" cellspacing="2">
        <TR><TD style="width: '$WIDTH1'px;" ALIGN=left>
                '$"Background"'
            </TD>
<td style="vertical-align: top;">
<INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="30"></td>'

if [ $MOBILE != yes ]
then
echo '<td style="vertical-align: middle;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"You must use a png format."'</span></a>
            </TD>'
fi
echo '</TR>
</TABLE>
<br><br>
<input value="'$"Submit"'" class="button" type="submit">
</form></div>
</BODY>
</HTML>
'
exit
