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
source /opt/karoshi/web_controls/version


############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
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
  <title>'$"Schedule Job"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script>
<!--
function SetAllCheckBoxes(FormName, FieldName, CheckValue)
{
	if(!document.forms[FormName])
		return;
	var objCheckBoxes = document.forms[FormName].elements[FieldName];
	if(!objCheckBoxes)
		return;
	var countCheckBoxes = objCheckBoxes.length;
	if(!countCheckBoxes)
		objCheckBoxes.checked = CheckValue;
	else
		// set the check value for all check boxes
		for(var i = 0; i < countCheckBoxes; i++)
			objCheckBoxes[i].checked = CheckValue;
}
// -->
</script>
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ "$MOBILE" = yes ]
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
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH1=200
	WIDTH2=200
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
	WIDTH1=140
	WIDTH2=160
fi

echo '<form action="/cgi-bin/admin/cron_add.cgi" method="post">'

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then

	echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"Schedule Job"'</span>
<a href="/cgi-bin/admin/cron_view_fm.cgi">'$"Scheduled Jobs"'</a>
</div>
</div><div id="mobileactionbox">
'


else
	WIDTH=100
	ICON1=/images/submenus/system/computer.png

	echo '<div id="'"$DIV_ID"'"><div id="titlebox">


	<div class="sectiontitle">'$"Schedule Job"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_Scheduled_Jobs"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the servers you want to view the scheduled commands on."'</span></a></div>
	<table class="tablesorter"><tbody><tr>

		<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
			<button class="info infonavbutton" formaction="/cgi-bin/admin/cron_view_fm.cgi" name="SelectServer" value="_">
				<img src="'"$ICON1"'" alt="'$"Scheduled Jobs"'">
				<span>'$"View the scheduled jobs for this server."'</span><br>
				'$"Scheduled Jobs"'
			</button>
		</td>

	</tr></tbody></table>
	
	</div><div id ="infobox">'
fi

echo '<table class="'"$TABLECLASS"'" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: '"$WIDTH1"'px;">
'$"Minutes"'</td>
<td><select name="___MINUTES___" style="width: '"$WIDTH2"'px;">
<option value="0">0</option>
<option value="5">5</option>
<option value="10">10</option>
<option value="15">15</option>
<option value="20">20</option>
<option value="25">25</option>
<option value="30">30</option>
<option value="35">35</option>
<option value="40">40</option>
<option value="45">45</option>
<option value="50">50</option>
<option value="55">55</option>
<option value="*">'$"Every minute"'</option>
<option value="*/5">'$"Every"' 5 '$"Minutes"'</option>
<option value="*/10">'$"Every"' 10 '$"Minutes"'</option>
<option value="*/15">'$"Every"' 15 '$"Minutes"'</option>
<option value="*/20">'$"Every"' 20 '$"Minutes"'</option>
<option value="*/30">'$"Every"' 30 '$"Minutes"'</option>
</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the minute you want the job to start on."'</span></a>
</td></tr>
<tr><td>'$"Hour"'</td>
<td><select name="___HOUR___" style="width: '"$WIDTH2"'px;">
<option value="*">'$"Every hour"'</option>
<option>0</option>
<option>1</option>
<option>2</option>
<option>3</option>
<option>4</option>
<option>5</option>
<option>6</option>
<option>7</option>
<option>8</option>
<option>9</option>
<option>10</option>
<option>11</option>
<option>12</option>
<option>13</option>
<option>14</option>
<option>15</option>
<option>16</option>
<option>17</option>
<option>18</option>
<option>19</option>
<option>20</option>
<option>21</option>
<option>22</option>
<option>23</option>
</select></td>
<td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the hour you want the job to start on."'</span></a>
      </td></tr>
<tr><td>'$"Day"'</td>
<td><select name="___DAY___" style="width: '"$WIDTH2"'px;">
<option value="*">'$"Every day"'</option>
<option>0</option>
<option>1</option>
<option>2</option>
<option>3</option>
<option>4</option>
<option>5</option>
<option>6</option>
<option>7</option>
<option>8</option>
<option>9</option>
<option>10</option>
<option>11</option>
<option>12</option>
<option>13</option>
<option>14</option>
<option>15</option>
<option>16</option>
<option>17</option>
<option>18</option>
<option>19</option>
<option>20</option>
<option>21</option>
<option>22</option>
<option>24</option>
<option>25</option>
<option>26</option>
<option>27</option>
<option>28</option>
<option>29</option>
<option>30</option>
<option>31</option>
</select></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the day of the month you want the job to start on."'</span></a>
</td></tr>
<tr><td>'$"Month"'</td>
<td><select name="___MONTH___" style="width: '"$WIDTH2"'px; height: '"$HEIGHT"'px;">
<option value="*">'$"Every Month"'</option>
<option>0</option>
<option>1</option>
<option>2</option>
<option>3</option>
<option>4</option>
<option>5</option>
<option>6</option>
<option>7</option>
<option>8</option>
<option>9</option>
<option>10</option>
<option>11</option>
<option>12</option>
</select></td>
<td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the month you want the job to start on."'</span></a>
</td></tr>
<tr><td>'$"Day of week"'</td>
<td><select name="___DOFW___" style="width: '"$WIDTH2"'px;">
<option value="1-7">'$"Every day"'</option>
<option value="1-5">'$"Every week day"'</option>
<option value="6-7">'$"Weekend"'</option>
<option value="1-3-5">'$"Monday"'-'$"Wednesday"'-'$"Friday"'</option>
<option value="1">'$"Monday"'</option>
<option value="2">'$"Tuesday"'</option>
<option value="3">'$"Wednesday"'</option>
<option value="4">'$"Thursday"'</option>
<option value="5">'$"Friday"'</option>
<option value="6">'$"Saturday"'</option>
<option value="7">'$"Sunday"'</option>
</select></td>
<td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the days of the week you want the job to run on."'</span></a>
      </td></tr>
      <tr>
        <td>
'$"Command"'</td>
        <td><input tabindex= "2" name="___COMMAND___" size="25" style="width: '"$WIDTH2"'px;" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the command or path to the command that you want to run."'</span></a>
      </td></tr></tbody></table><br><br>'

#Show list of servers
/opt/karoshi/web_controls/show_servers "$MOBILE" servers $"Schedule Job" notset notset ___

[ "$MOBILE" = no ] && echo '</div>'

echo '</div></form></div></body></html>'

exit
