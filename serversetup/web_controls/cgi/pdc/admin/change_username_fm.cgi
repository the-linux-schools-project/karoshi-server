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

############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/change_username ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/change_username
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
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/script.js"></script>
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

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
WIDTH=200
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=mobileactionbox
TABLECLASS=mobilestandard
WIDTH=100
fi

echo '<form action="/cgi-bin/admin/change_username.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$MENUMSG'</a>
</div></div><div id="'$DIV_ID'">
'
else
echo '<div id="'$DIV_ID'"><div class="sectiontitle">'$TITLE'</div><br>'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left; height: 30px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$USERNAMEMSG'</td>
        <td><div id="suggestions"></div><input tabindex= "1" name="_USERNAME_" size="20" style="width: '$WIDTH'px;" type="text" id="inputString" onkeyup="lookup(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>
</td></tr>
<tr><td>'$NEWUSERNAMEMSG'</td><td><input tabindex= "2" name="_NEWUSERNAME_" size="20" style="width: '$WIDTH'px;" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a></td>
      </tr>
<tr><td>'$NEWFIRSTNAMEMSG'</td><td><input tabindex= "3" name="_FIRSTNAME_" size="20"  style="width: '$WIDTH'px;" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a></td>
      </tr>
<tr><td>'$NEWSURNAMEMSG'</td><td><input tabindex= "4" name="_SURNAME_" size="20"  style="width: '$WIDTH'px;" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Change_Username"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a></td>
      </tr>
    </tbody>
  </table>
  <br>'

[ $MOBILE = no ] && echo '</div><div id="submitbox">'
echo '<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
</div></form></div></body></html>
'
exit
