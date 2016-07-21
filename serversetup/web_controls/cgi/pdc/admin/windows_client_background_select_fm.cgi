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
THISYEAR=`date +%Y`
let GROUPSTART=$THISYEAR-8
let GROUPEND=$THISYEAR+5
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Windows Background - Select"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
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
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">
<form action="/cgi-bin/admin/windows_client_background_select.cgi" name="selectgroups" method="post"><span style="font-weight: bold;">
'$"Windows Background - Select"'</span><br>
  <br>
'
#Check to see if any files have been uploaded
FILECOUNT=0
if [ -d /var/www/karoshi/win_background_upload/ ]
then
FILECOUNT=`ls -1 /var/www/karoshi/win_background_upload/ | wc -l`
FILEDATA=`ls -1 /var/www/karoshi/win_background_upload/ | sed -n 1,1p`
FILENAME=`echo $FILEDATA | grep '\<bmp\>'`
fi

if [ $FILECOUNT != 1 ]
then
echo ''$"An incorrect number of files have been uploaded."'</div></div></body></html>'
exit
fi

if [ `echo $FILENAME'null' | sed 's/ //g'` = null ]
then
echo ''$"You have not uploaded a bmp file."'</div></div></body></html>'
exit
else
FILENAME=`ls -1 /var/www/karoshi/win_background_upload/ | sed -n 1,1p`
#replace spaces
FILENAME2=`echo $FILENAME | sed 's/ /SPACECORRECT/g'`
[ -f /var/www/karoshi/win_background_upload/$FILENAME2 ] || mv /var/www/karoshi/win_background_upload/"$FILENAME" /var/www/karoshi/win_background_upload/$FILENAME2
fi

if [ $FILECOUNT -lt 1 ]
then
echo ''$"You have not uploaded a bmp file."'</div></div></body></html>'
exit
fi
echo ''$"Uploaded file"' : '$FILENAME'<br><br>'$"Please select the groups that you want to copy the background to."''
FILENAME=$FILENAME2
echo '
<br><br><input name="_FILENAME_" value="'$FILENAME'" type="hidden">
<table class="standard" style="text-align: left;" >
 <tbody><tr><td style="width: 100px;"><b>'$"Group"'</b></td><td style="width: 50px;"></td><td style="width: 100px;"><b>'$"Group"'</b></td><td style="width: 50px;"></td><td style="width: 100px;"><b>'$"Group"'</b></td><td style="width: 50px;"></td><td style="width: 100px;"><b>'$"Group"'</b></td><td style="width: 50px;"></td></tr>'
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
<td>itadmin</td><td><input name="_PRIGROUP_" value="itadmin" type="checkbox"><br></td></tr>'



#Show extra options
COUNTER=1
if [ -d /opt/karoshi/server_network/group_information/optional_groups/ ]
then
for OPTGROUPS in /opt/karoshi/server_network/group_information/optional_groups/*
do
OPTGROUP=`basename $OPTGROUPS`

echo '<td>'$OPTGROUP'</td><td><input name="_PRIGROUP_" value="'$OPTGROUP'" type="checkbox"><br></td>'
let COUNTER=$COUNTER+1
if [ $COUNTER = 5 ]
then
echo '</tr><tr>'
COUNTER=1
fi
done
echo '</tr>'
fi


echo '</tbody></table>
</div>
<div id="submitbox">
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"> <input type="button" onclick="SetAllCheckBoxes('\'selectgroups\'', '\'_PRIGROUP_\'', true);" value="'$"Select all"'">
</div>
</form>
</div></body>
</html>
'
exit

########################
#Unique key
########################
#5IOA6xZP/e2hVbdTDr5Lxn1zv
