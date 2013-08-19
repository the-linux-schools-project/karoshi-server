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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
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
DATE_INFO=`date +%F`
DAY=`echo $DATE_INFO | cut -d- -f3`
MONTH=`echo $DATE_INFO | cut -d- -f2`
YEAR=`echo $DATE_INFO | cut -d- -f1`

[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_view_logs ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_view_logs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'">
<script language="JavaScript" src="/all/calendar2/calendar_eu.js" type="text/javascript"></script>
        <!-- Timestamp input popup (European Format) -->
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/script.js"></script>
<link rel="stylesheet" href="/all/calendar2/calendar.css">
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

echo '</head><body onLoad="start()">'

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/admin/dg_view_user_logs.cgi" name="testform" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then

echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$INTERNETMENUMSG'</a>
</div></div><div id="mobileactionbox">
'

else
echo '<b>'$TITLE'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>
<br><br>'
fi

if [ $MOBILE = yes ]
then
echo '<div id="suggestions"></div>
'$USERNAMEMSG'<br>
<input tabindex= "1" name="_USERNAME_" size="14" style="width: 160px;" type="text" id="inputString" onkeyup="lookup(this.value);"><br>
'$WEBLOGDATE'<br>'
echo "<!-- calendar attaches to existing form element -->
	<input type=\"text\" style=\"width: 160px;\" value=\"$DAY-$MONTH-$YEAR\" size=14 maxlength=10 name=\"_DATE_\">
	<script language=\"JavaScript\" type=\"text/javascript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script><br>"
echo ''$LOGCOUNTMSG'<br>
<input tabindex= "1" name="_DAYCOUNT_" maxlength="2" size="2" value="1" type="text"><br><br>
'
else
echo '<div id="suggestions"></div><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 180px;">'$USERNAMEMSG'</td><td><input tabindex= "1" name="_USERNAME_" size="14" style="width: 200px;" type="text" id="inputString" onkeyup="lookup(this.value);"></td><td style="vertical-align: top; text-align: center;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a></td></tr>'
echo "<tr><td>$WEBLOGDATE</td><td>
<!-- calendar attaches to existing form element -->
	<input type=\"text\" style=\"width: 200px;\" value=\"$DAY-$MONTH-$YEAR\" size=14 maxlength=10 name=\"_DATE_\"></td><td style=\"vertical-align: top;\">
	<script language=\"JavaScript\" type=\"text/javascript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script></td></tr>"



echo '<tr><td>'$LOGCOUNTMSG'</td><td><input tabindex= "1" name="_DAYCOUNT_" maxlength="2" size="2" value="1" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a></td></tr>

</tbody></table><br>'
fi

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi

echo '<input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset"></div></form></body></html>'
exit
