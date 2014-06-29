#!/bin/bash
#Copyright (C) 2012  Paul Sharrad

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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_choose_background ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_choose_background
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
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
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

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
MAXSTYLES=5
WIDTH1=180
WIDTH2=400
WIDTH3=300
CHARS=25
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=mobileactionbox
TABLECLASS=mobilestandard
MAXSTYLES=4
WIDTH1=90
WIDTH2=160
WIDTH3=120
CHARS=11
fi


[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$MENUMSG'</a>
</div></div><div id="'$DIV_ID'">'
else

echo '<form action="/cgi-bin/admin/linux_client_background_upload_fm.cgi" method="post"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td><b>'$TITLE'</b></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Linux_Client_Background"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>
</td><td style="vertical-align: top;">
<a class="info" href="javascript:void(0)"><input name="_UPLOAD_" type="image" class="images"  src="/images/submenus/client/upload.png" value=""><span>'$UPLOADMSG'</span></a>
</td></tr></tbody></table></form><br>'
fi

function show_status {
echo '<script type="text/javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/linux_client_choose_background_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function upload_background {
echo '<script type="text/javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/linux_client_background_upload_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#Check to see if any backgrounds have been uploaded
if [ ! -d /var/lib/samba/netlogon/linuxclient/backgrounds ]
then
MESSAGE=$ERRORMSG1
upload_background
fi

if [ `ls -1 /var/lib/samba/netlogon/linuxclient/backgrounds | wc -l` = 0 ]
then
MESSAGE=$ERRORMSG1
upload_background
fi

echo '<form action="/cgi-bin/admin/linux_client_choose_background.cgi" method="post"><table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>'

#Get the default background
DEFAULTBACKGROUND=notset
[ -f /var/lib/samba/netlogon/linuxclient/backgrounds/defaultbackground ] && source /var/lib/samba/netlogon/linuxclient/backgrounds/defaultbackground

for BACKGROUNDS in /var/lib/samba/netlogon/linuxclient/backgrounds/*.png
do
BACKGROUND=`basename "$BACKGROUNDS" | sed 's/.png$//g'`
BACKGROUND_SHORT=${BACKGROUND:0:$CHARS}
if [ $BACKGROUND = $DEFAULTBACKGROUND ]
then
echo '<tr><td style="width: '$WIDTH1'px; vertical-align: top; background-color: rgb(204, 0, 0); text-align: left;"><b>Default Background</b><br><br>'$BACKGROUND_SHORT'</td><td>
<a class="info" href="javascript:void(0)"><input name="___ACTION___choose___BACKGROUND___'$BACKGROUND'___" type="image" class="images" style="width: '$WIDTH2'px; height: '$WIDTH3'px;" src="/images/linuxclient/backgrounds/'$BACKGROUND'.png" value=""><span>'$BACKGROUND'</span></a>
</td></tr>'
else
echo '<tr><td style="width: '$WIDTH1'px; vertical-align: top; text-align: left;">'$BACKGROUND_SHORT'</td><td>
<a class="info" href="javascript:void(0)"><input name="___ACTION___choose___BACKGROUND___'$BACKGROUND'___" type="image" class="images" style="width: '$WIDTH2'px; height: '$WIDTH3'px;" src="/images/linuxclient/backgrounds/'$BACKGROUND'.png" value=""><span>'$BACKGROUND'</span></a>
</td><td style="width: '$WIDTH1'px; vertical-align: top;">
<a class="info" href="javascript:void(0)"><input name="___ACTION___delete___BACKGROUND___'$BACKGROUND'___" type="image" class="images" src="/images/submenus/file/delete.png" value=""><span>'$DELETEMSG'<br>'$BACKGROUND'</span></a>
</td></tr>'
fi
done

echo '</tr></tbody></table></form><br></div></div></body></html>'
exit
