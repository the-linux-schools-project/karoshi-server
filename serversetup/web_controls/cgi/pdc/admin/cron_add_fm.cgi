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
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/cron ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/cron
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
  <title>'"$TITLE"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script type="text/javascript">
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

echo '</head><body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
TABLECLASS=standard
STYLEWIDTH=200
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
STYLEWIDTH=120
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then

echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$SYSMENUMSG'</a>
</div>
</div><div id="mobileactionbox">
<form action="/cgi-bin/admin/cron_view_fm.cgi" method="post">
<input name="" type="submit" class="button" value="'$TITLE2'">
</form><br>
'


else
echo '<div id="'$DIV_ID'"><div id="titlebox">
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr>
<td style="vertical-align: top;"><b>'$TITLE'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=View_Scheduled_Jobs"><img class="images" alt="" src="/images/help/info.png"><span>'"$SERVERHELP2"'</span></a></td>
<td style="vertical-align: top;"><a href="/cgi-bin/admin/cron_view_fm.cgi"><input class="button" type="button" name="" value="'$TITLE2'"></a></td>
</tr></table></div><div id ="infobox">'
fi

echo '<form action="/cgi-bin/admin/cron_add.cgi" name="selectservers" method="post">'
echo '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$MINUTEMSG'</td>
<td><select name="___MINUTES___" style="width: '$STYLEWIDTH'px;">
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
<option value="*">'$EVERYMINUTEMSG'</option>
<option value="*/5">'$EVERYMSG' 5 '$MINUTESMSG'</option>
<option value="*/10">'$EVERYMSG' 10 '$MINUTESMSG'</option>
<option value="*/15">'$EVERYMSG' 15 '$MINUTESMSG'</option>
<option value="*/20">'$EVERYMSG' 20 '$MINUTESMSG'</option>
<option value="*/30">'$EVERYMSG' 30 '$MINUTESMSG'</option>
</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'"$MINUTEHELP"'</span></a>
</td></tr>
<tr><td>'$HOURMSG'</td>
<td><select name="___HOUR___" style="width: '$STYLEWIDTH'px;">
<option value="*">'$EVERYHOURMSG'</option>
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
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'"$HOURHELP"'</span></a>
      </td></tr>
<tr><td>'$DAYMSG'</td>
<td><select name="___DAY___" style="width: '$STYLEWIDTH'px;">
<option value="*">'$EVERYDAYMSG'</option>
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
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'"$DAYHELP"'</span></a>
</td></tr>
<tr><td>'$MONTHMSG'</td>
<td><select name="___MONTH___" style="width: '$STYLEWIDTH'px;">
<option value="*">'$EVERYMONTHMSG'</option>
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
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'"$MONTHHELP"'</span></a>
</td></tr>
<tr><td>'$DAYOFWEEKMSG'</td>
<td><select name="___DOFW___" style="width: '$STYLEWIDTH'px;">
<option value="1-7">'$EVERYDAYMSG'</option>
<option value="1-5">'$WORKINGWEEKMSG'</option>
<option value="6-7">'$WEEKENDMSG'</option>
<option value="1-3-5">'$MONDAY'-'$WEDNESDAY'-'$FRIDAY'</option>
<option value="1">'$MONDAY'</option>
<option value="2">'$TUESDAY'</option>
<option value="3">'$WEDNESDAY'</option>
<option value="4">'$THURSDAY'</option>
<option value="5">'$FRIDAY'</option>
<option value="6">'$SATURDAY'</option>
<option value="7">'$SUNDAY'</option>
</select></td>
<td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Scheduled_Job"><img class="images" alt="" src="/images/help/info.png"><span>'"$DOFWHELP"'</span></a>
      </td></tr>
      <tr>
        <td>
'$COMMANDMSG'</td>
        <td><input tabindex= "2" name="___COMMAND___" size="25" style="width: '$STYLEWIDTH'px;" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'"$COMMANDHELP"'</span></a>
      </td></tr></tbody></table><br><br>'

#Show list of servers
/opt/karoshi/web_controls/show_servers $MOBILE servers "$ACTIONMSG2"

[ $MOBILE = no ] && echo '</div>'

echo '</div></form></div></body></html>'

exit
