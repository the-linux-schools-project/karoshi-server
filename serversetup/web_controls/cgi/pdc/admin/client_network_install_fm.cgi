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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/client_boot_controls ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/client_boot_controls
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

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
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
<form action="/cgi-bin/admin/client_network_install_fm.cgi" name="selectgroups" method="post"><span style="font-weight: bold;">
'$TITLE'</span><br>
  <br>
'

#Display a list of clients to control

#Normal boot
if [ -d /opt/karoshi/asset_register/network_install/normal_boot/ ]
then
if [ `ls -1 /opt/karoshi/asset_register/network_install/normal_boot/ | wc -l` -gt 0 ]
then
echo '<b>$STANDARDBOOTMSG</b><br><br><input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">'
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 120px;">'$LOCATIONMSG'</td><td style="width: 180px;">'$MACMSG'</td><td style="width: 120px;">'$TCPMSG'</td><td>'$NETWORKINSTALLMSG'</td><td>'$NORMALMSG'</td><td>'$MEMTESTMSG'</td><td>'$REMOVEMSG'</td>'
for LOCATIONS in /opt/karoshi/asset_register/network_install/normal_boot/*
do
LOCATION=`basename "$LOCATIONS"`
cat /opt/karoshi/asset_register/network_install/normal_boot/"$LOCATION"/*
done
echo '</tbody></table><input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"><br><br>'
else
echo $NOCLIENTSMSG"<br><br>"
fi
else
echo $NOCLIENTSMSG"<br><br>"
fi


echo '</div>
<div id="submitbox">
  <input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
</div>
</form>
</div></body>
</html>
'
exit
