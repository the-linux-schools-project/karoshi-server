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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/view_acceptable_use_authorisations ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/view_acceptable_use_authorisations
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
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
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
</script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body onLoad="start()">'

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
fi

echo '<form action="/cgi-bin/admin/view_acceptable_use_authorisations.cgi" name="selectservers" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE'</b></a></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td></tr></tbody></table>'
else
echo '<b>'$TITLE'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Acceptable_Use#View_pending_users"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>

<br><br>'
fi

echo '<form action="/cgi-bin/admin/view_acceptable_use_authorisations.cgi" name="selectservers" method="post">'

#Get list of pending users
PROCESS_USERS=yes
if [ ! -d /opt/karoshi/acceptable_use_authorisations/pending ]
then
echo $ERRORMSG1
PROCESS_USERS=no
fi

if [ $PROCESS_USERS = yes ]
then
if [ `ls -1 /opt/karoshi/acceptable_use_authorisations/pending | wc -l` -lt 1 ]
then
echo $ERRORMSG1
PROCESS_USERS=no
fi
fi

if [ $PROCESS_USERS = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top; width: 100px;"><b>'$USERNAMEMSG'</b></td><td style="vertical-align: top; width: 100px;"><b>'$CREATORMSG'</b></td><td style="vertical-align: top; width: 100px;"><b>'$CREATION_DATEMSG'</b></td><td style="vertical-align: top; width: 100px;"><b>'$GRACEMSG'</b></td><td style="vertical-align: top; width: 60px;"><b>'$APPROVEMSG2'</b></td></tr>
'
for PENDING_USER_FULL in /opt/karoshi/acceptable_use_authorisations/pending/*
do
PENDING_USER=`basename $PENDING_USER_FULL`
PENDING_USER_DATA=`sed -n 1,1p $PENDING_USER_FULL`
DAY_COUNT=`echo $PENDING_USER_DATA | cut -d, -f1`
USER_CREATOR=`echo $PENDING_USER_DATA | cut -d, -f2`
CREATION_DATE=`echo $PENDING_USER_DATA | cut -d, -f3`

echo '<tr><td>'$PENDING_USER'</td><td>'$USER_CREATOR'</td><td>'$CREATION_DATE'</td><td>'$DAY_COUNT'</td><td><input name="_USERNAME_" value="'$PENDING_USER'" type="checkbox"></td></tr>'
done

echo '</tbody></table><br><input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"> <input type="button" onclick="SetAllCheckBoxes('\'selectservers\'', '\'_USERNAME_\'', true);" value="'$SELECTMSG'">'
fi
echo '</div></form></body></html>'
exit
