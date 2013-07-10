#!/bin/bash
#new_group
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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/new_group ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/new_group
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
  <title>'$TITLE2'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/new_primary_group.cgi" method="post"><div id="actionbox"><span style="font-weight: bold;">'$TITLE2'</span><br>
  <br>'


#Check that this server is not part of a federated setup
if [ -f /opt/karoshi/server_network/servers/$HOSTNAME/federated_server ]
then
echo $ERRORMSG11 '</div></body></html>'
exit
fi

echo ' <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 180px;">'$GROUPMSG2'</td><td><input name="_NEWPRIGROUP_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=New_Primary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2a'<br><br>'$HELPMSG2b'</span></a>

</td></tr>

<tr><td>'$PROFILEMSG'</td><td>'
#Generate list of profiles
echo '<select name="_PROFILE_" style="width: 200px;"><option value=""></option>'
for PROFILES in /home/applications/profiles/*
do
PROFILE=`basename $PROFILES`
if [ $PROFILE != default_roaming_profile ]
then
echo '<option value="'$PROFILE'">'$PROFILE'</option>'
fi
done
echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a></td></tr>
<tr><td>'$HOMESERVERMSG'</td><td><select name="_HOMESERVER_" style="width: 200px;"><option value=""></option>'

#Generate a list of servers for the home folders
FILESERVERCOUNT=0
for KAROSHI_SERVER in /opt/karoshi/server_network/servers/*
do
KAROSHI_SERVER=`basename $KAROSHI_SERVER`
if [ -f /opt/karoshi/server_network/servers/$KAROSHI_SERVER/fileserver ]
then
SERVERARRAY[$FILESERVERCOUNT]=$KAROSHI_SERVER
let FILESERVERCOUNT=$FILESERVERCOUNT+1
fi
done
COUNTER=0
while [ $COUNTER -le $FILESERVERCOUNT ]
do
echo '<option value="'${SERVERARRAY[$COUNTER]}'">'${SERVERARRAY[$COUNTER]}'</option>'
let COUNTER=$COUNTER+1
done
echo '</td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG4'</span></a></td></tr>'
#Show categories
echo '<tr><td>'$CATEGORYMSG'</td><td><select name="_CATEGORY_" style="width: 200px;">
<option value=""></option>
<option value="students">'$STUDENTMSG'</option>
<option value="personnel">'$PERSONNELMSG'</option>
<option value="other">'$OTHERMSG'</option>
<option value="trustees">'$TRUSTEESMSG'</option>
</td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG5'</span></a></td></tr>
<tr><td>'$SECONDARYGROUPMSG'</td><td>'
#Show a list of secondary groups to be a member of
echo '<input name="_SECGROUP_" value="staff" type="checkbox">staff</td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG6'</span></a></td></tr>'
echo '</tbody></table><br><br>
</div>
<div id="submitbox">
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div>
</form>
</body>
</html>
'
exit


