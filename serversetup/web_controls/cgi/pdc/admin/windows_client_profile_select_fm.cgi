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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/windows_profile_upload ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/windows_profile_upload
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi
THISYEAR=`date +%Y`
let GROUPSTART=$THISYEAR-8
let GROUPEND=$THISYEAR+5
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE2'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
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
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">
<form action="/cgi-bin/admin/windows_client_profile_select.cgi" name="selectgroups" method="post"><span style="font-weight: bold;">
'$TITLE2'</span> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Upload_a_new_profile"><img class="images" alt="" src="/images/help/info.png"><span>'$CHOOSEPROFILEMSG'</span></a><br>
  <br>
'
WIDTH1=15
WIDTH2=100
#Check to see if any files have been uploaded
FILECOUNT=0
if [ -d /var/www/karoshi/win_profile_upload/ ]
then
FILECOUNT=`ls -1 /var/www/karoshi/win_profile_upload/ | wc -l`
FILEDATA=`ls -1 /var/www/karoshi/win_profile_upload/ | sed -n 1,1p`
FILENAME=`echo "$FILEDATA" | grep '\<zip\>'`
[ `echo $FILENAME'null' | sed 's/ //g'` = null ] && FILENAME=`echo "$FILEDATA" | grep '\<tar\.gz\>'`
fi

if [ $FILECOUNT != 1 ]
then
echo ''$ERRORMSG1'</div></div></body></html>'
exit
fi

if [ `echo $FILENAME'null' | sed 's/ //g'` = null ]
then
echo ''$ERRORMSG2'</div></div></body></html>'
exit
else
FILENAME=`ls -1 /var/www/karoshi/win_profile_upload/ | sed -n 1,1p`
#Correct spaces
FILENAME2=`echo $FILENAME | sed 's/ /SPACECORRECT/g'`
[ -f /var/www/karoshi/win_profile_upload/$FILENAME2 ] || mv /var/www/karoshi/win_profile_upload/"$FILENAME" /var/www/karoshi/win_profile_upload/$FILENAME2
fi
#Show list of profiles to choose from

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;">'$UPLOADEDFILEMSG'</td><td>'$FILENAME'</td></tr>
<tr><td>'$WINVERMSG'</td><td>
<select name="___WINDOWSVER___" style="width: 200px;">
<option value="windowsxp">Windows XP</option>
<option value="windows7">Windows 7</option>
<option value="windows8.0">Windows 8.0</option>
<option value="windows8.1">Windows 8.1</option>
</select>
</td></tr>
</tbody></table>
'
echo '<br>'$GROUPMSG''
FILENAME=$FILENAME2
echo '
  <br><input name="___FILENAME___" value="'$FILENAME'" type="hidden">
  <br>
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
 <tbody><tr><td style="width: '$WIDTH1'px;"></td><td style="width: '$WIDTH2'px;"><b>'$GROUPMSG2'</b></td><td style="width: '$WIDTH1'px;"></td><td style="width: '$WIDTH2'px;"><b>'$GROUPMSG2'</b></td><td style="width: '$WIDTH1'px;"></td><td style="width: '$WIDTH2'px;"><b>'$GROUPMSG2'</b></td><td style="width: '$WIDTH1'px;"></td><td style="width: '$WIDTH2'px;"><b>'$GROUPMSG2'</b></td></tr>'

COUNTER=1
for GROUPNAMES in /opt/karoshi/server_network/group_information/*
do
GROUPNAME=`basename $GROUPNAMES`
if [ $COUNTER = 1 ]
then
echo '<tr>'
fi
echo '<td><input name="___PRIGROUP___" value="'$GROUPNAME'" type="checkbox"></td><td>'$GROUPNAME'</td>'
if [ $COUNTER = 4 ]
then
echo '</tr>'
COUNTER=1
else
let COUNTER=$COUNTER+1
fi
done

echo '</tbody></table><br>
  <input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"> <input type="button" class="button" onclick="SetAllCheckBoxes('\'selectgroups\'', '\'_PRIGROUP_\'', true);" value="'$SELECTMSG'">
</div>
</form>
</div></body>
</html>
'
exit
