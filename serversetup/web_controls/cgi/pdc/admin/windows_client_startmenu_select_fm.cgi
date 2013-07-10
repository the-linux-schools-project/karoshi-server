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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/windows_startmenu_upload ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/windows_startmenu_upload
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
<link rel="stylesheet" href="/css/'$STYLESHEET'">
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
<body onLoad="start()">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">
<form action="/cgi-bin/admin/windows_client_startmenu_select.cgi" name="selectgroups" method="post"><span style="font-weight: bold;">
'$TITLE2'</span><br>
  <br>
'
#Check to see if any files have been uploaded
FILECOUNT=0
if [ -d /var/www/karoshi/win_startmenu_upload/ ]
then
FILECOUNT=`ls -1 /var/www/karoshi/win_startmenu_upload/ | wc -l`
FILEDATA=`ls -1 /var/www/karoshi/win_startmenu_upload/ | sed -n 1,1p`
FILENAME=`echo $FILEDATA | grep '\<zip\>'`
[ `echo $FILENAME'null' | sed 's/ //g'` = null ] && FILENAME=`echo "$FILEDATA" | grep '\<tar\.gz\>'`
fi

if [ $FILECOUNT != 1 ]
then
echo ''$ERRORMSG1'</div></body></html>'
exit
fi

if [ `echo $FILENAME'null' | sed 's/ //g'` = null ]
then
echo ''$ERRORMSG2'</div></body></html>'
exit
else
FILENAME=`ls -1 /var/www/karoshi/win_startmenu_upload/ | sed -n 1,1p`
#replace spaces
FILENAME2=`echo $FILENAME | sed 's/ /SPACECORRECT/g'`
[ -f /var/www/karoshi/win_startmenu_upload/$FILENAME2 ] || mv /var/www/karoshi/win_startmenu_upload/"$FILENAME" /var/www/karoshi/win_startmenu_upload/$FILENAME2
fi
#Show list of profiles to choose from
echo ''$UPLOADEDFILEMSG' : '$FILENAME'<br><br>'$GROUPMSG''
FILENAME=$FILENAME2
echo '
  <br><input name="_FILENAME_" value="'$FILENAME'" type="hidden">
  <br>
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
 <tbody><tr><td style="width: 100px;"><b>'$GROUPMSG2'</b></td><td style="width: 50px;"></td><td style="width: 100px;"><b>'$GROUPMSG2'</b></td><td style="width: 50px;"></td><td style="width: 100px;"><b>'$GROUPMSG2'</b></td><td style="width: 50px;"></td><td style="width: 100px;"><b>'$GROUPMSG2'</b></td><td style="width: 50px;"></td></tr>'
while [ $GROUPSTART -le $GROUPEND ]
do
echo '<tr><td>yr'$GROUPSTART'</td><td><input name="_PRIGROUP_" value="yr'$GROUPSTART'" type="checkbox"><br></td>'
let GROUPSTART=$GROUPSTART+1
echo '<td>yr'$GROUPSTART'</td><td><input name="_PRIGROUP_" value="yr'$GROUPSTART'" type="checkbox"><br></td>'
let GROUPSTART=$GROUPSTART+1
echo '<td>yr'$GROUPSTART'</td><td><input name="_PRIGROUP_" value="yr'$GROUPSTART'" type="checkbox"><br></td>'
let GROUPSTART=$GROUPSTART+1
echo '<td>yr'$GROUPSTART'</td><td><input name="_PRIGROUP_" value="yr'$GROUPSTART'" type="checkbox"><br></td></tr>'
let GROUPSTART=$GROUPSTART+1
done
echo '
<tr><td>staff</td><td><input name="_PRIGROUP_" value="staff" type="checkbox"><br></td>
<td>nonteachingstaff</td><td><input name="_PRIGROUP_" value="nonteachingstaff" type="checkbox"><br></td>
<td>officestaff</td><td><input name="_PRIGROUP_" value="officestaff" type="checkbox"><br></td>
<td>studentstaff</td><td><input name="_PRIGROUP_" value="studentstaff" type="checkbox"><br></td></tr>
<tr><td>guests</td><td><input name="_PRIGROUP_" value="guests" type="checkbox"><br></td>
<td>exams</td><td><input name="_PRIGROUP_" value="guests" type="checkbox"><br></td>
<td>tech</td><td><input name="_PRIGROUP_" value="tech" type="checkbox"><br></td>
<td>itadmin</td><td><input name="_PRIGROUP_" value="itadmin" type="checkbox"><br></td></tr>
</tbody></table>
</div>
<div id="submitbox">
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset"> <input type="button" onclick="SetAllCheckBoxes('\'selectgroups\'', '\'_PRIGROUP_\'', true);" value="'$SELECTMSG'">
</div>
</form>
</body>
</html>
'
exit
