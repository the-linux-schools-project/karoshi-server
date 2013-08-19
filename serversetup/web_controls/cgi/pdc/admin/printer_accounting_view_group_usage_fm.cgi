#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printer_accounting ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printer_accounting
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE7'</title><META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE"><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/script.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

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
echo '<form name="myform" action="/cgi-bin/admin/printer_accounting_view_usage.cgi" method="post">'

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE7'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$PRINTMENUMSG'</a>
</div></div>
'
else
echo '<b>'$TITLE7'</b><br><br>'
fi

echo '
<input name="_TYPE_" value="group" type="hidden">
<div id="suggestions"></div>'

if [ $MOBILE = yes ]
then 
echo '<div id="mobileactionbox">'
echo ''$GROUPMSG'<br>'
#Show list of primary groups
/opt/karoshi/web_controls/group_dropdown_list | sed 's/_GROUP_/_NAME_/g'
echo '<br>'$MONTHMSG'<br>
<select style="width: 200px;" name="_MONTH_">
<option value="all"></option>
<option value="Jan">January</option>
<option value="Feb">February</option>
<option value="Mar">March</option>
<option value="Apr">April</option>
<option value="May">May</option>
<option value="Jun">June</option>
<option value="Jul">July</option>
<option value="Aug">August</option>
<option value="Sep">September</option>
<option value="Oct">October</option>
<option value="Noc">November</option>
<option value="Dec">December</option>
</select><br>
'$YEARMSG'<br><select style="width: 200px;" name="_YEAR_">'

#Show years
YEAR=`date +%Y`
let COUNTER=$YEAR-8
while [ $COUNTER -le $YEAR ]
do
SELECTED=""
[ $COUNTER = $YEAR ] && SELECTED='selected="selected"'
echo '<option '$SELECTED'>'$COUNTER'</option>'
let COUNTER=$COUNTER+1
done
echo '</select><br><br>'

else
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;">'$GROUPMSG'</td><td>'

#Show list of primary groups
/opt/karoshi/web_controls/group_dropdown_list | sed 's/_GROUP_/_NAME_/g'

echo '</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Printer_Accounting#Group_Printer_Usage"><img class="images" alt="" src="/images/help/info.png"><span>'"$HELPMSG9"'</span></a></td></tr>
<tr><td style="width: 180px;">'$MONTHMSG'</td><td>
<select style="width: 200px;" name="_MONTH_">
<option value="all"></option>
<option value="Jan">January</option>
<option value="Feb">February</option>
<option value="Mar">March</option>
<option value="Apr">April</option>
<option value="May">May</option>
<option value="Jun">June</option>
<option value="Jul">July</option>
<option value="Aug">August</option>
<option value="Sep">September</option>
<option value="Oct">October</option>
<option value="Noc">November</option>
<option value="Dec">December</option>
</select>

</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Printer_Accounting#Group_Printer_Usage"><img class="images" alt="" src="/images/help/info.png"><span>'"$HELPMSG6"'</span></a>
      </td></tr>
<tr><td style="width: 180px;">'$YEARMSG'</td><td>
<select style="width: 200px;" name="_YEAR_">'
#Show years
YEAR=`date +%Y`
let COUNTER=$YEAR-8
while [ $COUNTER -le $YEAR ]
do
SELECTED=""
[ $COUNTER = $YEAR ] && SELECTED='selected="selected"'
echo '<option '$SELECTED'>'$COUNTER'</option>'
let COUNTER=$COUNTER+1
done
echo '</select>
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Printer_Accounting#Group_Printer_Usage"><img class="images" alt="" src="/images/help/info.png"><span>'"$HELPMSG7"'</span></a></td></tr>
</tbody></table>
'
fi

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi
echo '<input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div></form></body></html>
'

exit

