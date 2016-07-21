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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Printer Usage"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
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
	<span>'$"Printer Usage"'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div>
'
else
echo '<b>'$"Printer Usage"'</b><br><br>'
fi

echo '<input name="_TYPE_" value="user" type="hidden"><div id="suggestions"></div>'

if [ $MOBILE = yes ]
then
echo '<div id="mobileactionbox">'
echo ''$"Username"'<br>
<input tabindex= "1" value="'$USERNAME'" name="_NAME_" style="width: 160px;" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"><br>
'$"Month"'<br>
<select style="width: 160px;" name="_MONTH_">
<option label="AllMonths" value="all"></option>
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
'$"Year"'<br><select style="width: 160px;" name="_YEAR_">'
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
echo '<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">'$"Username"'</td><td><input tabindex= "1" value="'$USERNAME'" name="_NAME_" style="width: 200px;" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Printer_Accounting#User_Printer_Usage"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the username that you want to view printer data for."'</span></a>
</td></tr>
<tr><td style="width: 180px;">'$"Month"'</td><td>
<select style="width: 200px;" name="_MONTH_">
<option label="AllMonths" value="all"></option>
<option value="Jan">'$"January"'</option>
<option value="Feb">'$"February"'</option>
<option value="Mar">'$"March"'</option>
<option value="Apr">'$"April"'</option>
<option value="May">'$"May"'</option>
<option value="Jun">'$"June"'</option>
<option value="Jul">'$"July"'</option>
<option value="Aug">'$"August"'</option>
<option value="Sep">'$"September"'</option>
<option value="Oct">'$"October"'</option>
<option value="Noc">'$"November"'</option>
<option value="Dec">'$"December"'r</option>
</select>
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Printer_Accounting#User_Printer_Usage"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the month that you want to view. Leave this blank to view the whole year."'</span></a>
      </td></tr>
<tr><td style="width: 180px;">'$"Year"'</td><td>
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
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Printer_Accounting#User_Printer_Usage"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the year that you want to view the printing data for."'</span></a></td></tr>
</tbody></table>
'
fi

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi
echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></form></div></body></html>
'

exit

