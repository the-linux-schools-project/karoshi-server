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
  <title>'$"Archive exam accounts"'</title><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '
<form action="/cgi-bin/admin/exam_accounts_archive.cgi" method="post"><div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" ><tbody>
	<tr><td><div class="sectiontitle">'$"Archive exam accounts"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Exam_Accounts#Archive_Exam_Accounts"><img class="images" alt="" src="/images/help/info.png"><span>'$"All data will be archived from the exam accounts to an examfiles folder in the network share that you choose."'<br><br>'$"Only a member of the selected group can access this folder."'</span></a></td></tr></tbody></table><br><br>
<table class="standard" style="text-align: left;" >
<tbody>
<tr><td style="width: 180px;">'$"Username"'</td><td><div id="suggestions"></div><input tabindex= "1" style="width: 200px;" name="_USERNAME_" value="'"$USERNAME"'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Archive_Exam_Accounts"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the username that will be set as the owner of the archived files."'</span></a></td></tr>
<tr><td>'$"Group"'</td><td>'

#Show a dropdown list of all groups
/opt/karoshi/web_controls/group_dropdown_list

echo '</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Archive_Exam_Accounts"><img class="images" alt="" src="/images/help/info.png"><span>'$"If you choose a group all users in the group will have full access to the archived files."'</span></a></td></tr>
<tr><td>'$"Network Share"'</td><td><select name="_SHARE_" style="width: 200px;"><option disabled selected value>'$"Select a network share"'</option>'

#Show a list of network shares to archive the accounts to
for SERVERS in /opt/karoshi/server_network/network_shares/*
do
	SERVER=$(basename "$SERVERS")
	SERVER_SHORT=$(echo "$SERVER" | cut -d. -f1)
	if [[ $(ls -1 /opt/karoshi/server_network/network_shares/"$SERVER" | wc -l) -gt 0 ]]
	then
		for NETSHARES in /opt/karoshi/server_network/network_shares/"$SERVER"/*
		do
			NETSHARE=$(basename "$NETSHARES")
			source /opt/karoshi/server_network/network_shares/"$SERVER"/"$NETSHARE"
			if [ "$NETSHARE" != sysvol ] && [ "$NETSHARE" != netlogon ] && [ "$NETSHARE" != applications ]
			then
				echo '<option value="'"$NETSHARE"'_SERVER_'"$SERVER"'_">'"$SERVER_SHORT"': '"$NETSHARE"'</option>'
			fi
		done
	fi
done


echo '</select></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Archive_Exam_Accounts"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the network share to archive the exam accounts to."'</span></a></td></tr>
<tr><td>
'$"Exceptions"'
</td><td>
<input tabindex= "3" name="_EXCEPTIONLIST_" style="width: 200px;" size="20" type="text">
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Archive_Exam_Accounts"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in any exam accounts that you do not want to be archived separated by spaces."'</span></a>
</td></tr></tbody></table><br>
<input value="'$"Submit"'" class="button" type="submit">
</div>
</div>
</form>
</div></body>
</html>
'
exit
