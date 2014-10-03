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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Web Management Language"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
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

echo '</head><body><div id="pagecontainer">'


#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/admin/remote_management_change_language2.cgi" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Web Management Language"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
else
echo '<div class="sectiontitle">'$"Web Management Language"'</div><br>'
fi

if [ $MOBILE = yes ]
then
echo ''$"Language"'<br>
<select name="_LANGCHOICE_" style="width: 160px;">
'
#Generate dropdown list of langauges
for LANGDIR in /opt/karoshi/web_controls/language/*
do
LANG=`basename $LANGDIR`
if [ $LANG'check' = $LANGCHOICE'check' ]
then
echo '<option selected="selected">'$LANG'</option>'
else
echo '<option>'$LANG'</option>'
fi
done
echo '</select><br><br>'

else

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;">'$"Language"'</td><td><select name="_LANGCHOICE_" style="width: 185px;">'
#Generate dropdown list of langauges
echo '
<option value="ar.UTF-8">العربية</option>
<option value="cs.UTF-8">Čeština</option>
<option value="da.UTF-8">Dansk</option>
<option value="de.UTF-8">Deutsch</option>
<option value="el.UTF-8">Eλληνικά</option>
<option value="en.UTF-8">English</option>
<option value="es.UTF-8">Español</option>
<option value="fr.UTF-8">Français</option>
<option value="hi.UTF-8">हिन्द</option>
<option value="he.UTF-8">עברית</option>
<option value="it.UTF-8">Italiano</option>
<option value="ko.UTF-8">한국어</option>
<option value="nb.UTF-8">Bokmål</option>
<option value="nl.UTF-8">Nederlands</option>
<option value="pl.UTF-8">Polski</option>
<option value="pt.UTF-8">Português</option>
<option value="ru.UTF-8">Pусский</option>
<option value="sv.UTF-8">Svenska</option>
<option value="sw.UTF-8">Kiswahili</option>
<option value="zh.UTF-8">语</option> ' | sort -t ">" -k 2

echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the language that you want for the Web Management."'<br><br>'$"This will not affect other web management users."'</span></a></td>
      </tr>
    </tbody>
  </table>
  <br>'

fi

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div></form></div></body></html>'
exit
