#!/bin/bash
#Copyright (C) 2008  Paul Sharrad

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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/label_groups ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/label_groups
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
source /opt/karoshi/web_controls/group_dropdown_def
#Check if timout should be disabled
if [ `echo $REMOTE___ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi

YEAR=`date +%Y`
let STARTYEAR=$YEAR-9
let ENDYEAR=$YEAR+2

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/label_groups.cgi" method="post"><div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr>
<td style="vertical-align: top;"><b>'$TITLE'</b></td>
<td style="vertical-align: top;"><a href="/cgi-bin/admin/groups.cgi"><input class="button" type="button" name="" value="'$VIEWGROUPSMSG'"></a></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#Labelling_groups"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td></tr></tbody></table>
<br></div><div id="infobox">'

#groups
COUNTER=1
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr>'
for GROUPNAMES in /opt/karoshi/server_network/group_information/*
do
GROUPNAME=`basename $GROUPNAMES`
UPPERGROUPNAME=${GROUPNAME^^}
LABEL=${!UPPERGROUPNAME}
echo '<td style="width: 100px;">'$GROUPNAME'</td><td style="width: 100px;"><input maxlength="20" size="10" name="____'$UPPERGROUPNAME':" value="'$LABEL'"></td><td style="width: 40px;"></td>'

if [ $COUNTER = 3 ]
then
echo "</tr><tr>"
COUNTER=0
fi
let COUNTER=$COUNTER+1
done
echo '</tbody></table><br>
<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
</div>
</form>
</div></body>
</html>
'
exit

