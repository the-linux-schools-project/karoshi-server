#!/bin/bash
#Copyright (C) 2016 Paul Sharrad

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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Categories"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>
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
</head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`

#########################
#Assign data to variables
#########################
END_POINT=9
#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign CATEGORY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = CATEGORYcheck ]
	then
		let COUNTER=$COUNTER+1
		CATEGORY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/view_karoshi_web_admin_log.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ -z "$ACTION" ]
then
	ACTION=view
fi

if [ $ACTION = add ] || [ $ACTION = delete ] && [ ! -z "$CATEGORY" ]
then
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$CATEGORY:" | sudo -H /opt/karoshi/web_controls/exec/categories
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox3"><div id="titlebox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Categories"'</div></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/groups.cgi" name="groups" method="post">
<button class="button" name="Groups">
'$"Group Management"'
</button>
</form></td>
<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Categories"><img class="images" alt="" src="/images/help/info.png"><span>'$"Categories are sub containers in OU=People in the ldap structure."'</span></a></td>
</tr></tbody></table><br>
'

echo '<form action="/cgi-bin/admin/categories.cgi" method="post"><table class="tablesorter" style="text-align: left;" >'
echo '<tbody>'
echo '<tr><td style="width: 200px;">'$"New category"'</td><td style="width: 160px;"><input name="____ACTION____add____CATEGORY____" size="15" type="text"> </td><td style="width: 115px;"><input value="Submit" type="submit" class="button"></td></tr>
</tbody></table></form></div><div id="infobox">'

echo '<form action="/cgi-bin/admin/categories.cgi" method="post"><table id="myTable" class="tablesorter" style="text-align: left;" >
<thead><tr><th style="width: 410px;"><b>'$"Categories"'</b></th><th style="width: 70px;"><b>'$"Delete"'</b></th></tr></thead><tbody>'

for CATEGORY in $(ls -1 /opt/karoshi/server_network/categories/)
do
	source /opt/karoshi/server_network/categories/$CATEGORY
	echo '<tr><td>'$CATEGORYNAME'</td><td>'

	if [ "$CATEGORY" != other ] && [ "$CATEGORY" != personnel ] && [ "$CATEGORY" != students ]
	then
		echo '<button class="info" name="____DoDelete____" value="____ACTION____delete____CATEGORY____'$CATEGORY'____">
		<img src="/images/submenus/client/delete_location.png" alt="'$"Delete"' '$CATEGORY'">
		<span>'$"Delete"' '$CATEGORY'</span>
		</button>'
	fi
	echo '</td></tr>'
done

echo '</tbody></table></form><br></div></div></div></body></html>'
exit
