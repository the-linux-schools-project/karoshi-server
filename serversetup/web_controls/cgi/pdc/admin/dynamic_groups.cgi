#!/bin/bash
#Copyright (C) 2015  Paul Sharrad

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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Dynamic Groups"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox"><div class="sectiontitle">'$"Dynamic Groups"'</div><br></div><div id="infobox">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+ '`
#########################
#Assign data to variables
#########################
END_POINT=7
#Assign APPENDUSERS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = APPENDUSERScheck ]
	then
		let COUNTER=$COUNTER+1
		APPENDUSERS=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/dynamic_groups.cgi | cut -d' ' -f1`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/dynamic_groups_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_status2 {
echo '<SCRIPT language="Javascript">'
echo 'window.location = "/cgi-bin/admin/dynamic_groups_fm.cgi";'
echo '</script>'
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

if [ `grep -c ^"$REMOTE_USER": /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#Get append option if it has not been set.
if [ -z "$APPENDUSERS" ]
then
	echo '<form name="myform" action="/cgi-bin/admin/dynamic_groups.cgi" method="post"><table class="standard" style="text-align: left;" ><tbody>
	<tr><td style="width: 180px;">'$"Append Users"'</td><td><select name="_APPENDUSERS_" style="width: 200px; height: 30px;" onClick="rewriteselect();">
        <option value="yes">'$"Yes"'</option>
        <option value="no">'$"No"'</option>
	</select></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choosing not to append will empty any users from the groups used in the csv file."'</span></a></td></tr></tbody></table><br><input value="'$"Submit"'" class="button" type="submit"></form></div></div></div></body></html>'
	exit
fi

#Act on the data if there is a file in /var/www/karoshi/dynamic_groups
if [ -d /var/www/karoshi/dynamic_groups ]
then
	if [ `ls -1 /var/www/karoshi/dynamic_groups | wc -l` = 1 ]
	then
		#Check that the csv file is an ASCII file
		CSVFILE=`ls -1 /var/www/karoshi/dynamic_groups | sed -n 1,1p`
		CSVFILEDATA=`file /var/www/karoshi/dynamic_groups/"$CSVFILE"`

		#Send the data to be processed.
 		if [ `echo "$CSVFILEDATA" | grep -c ASCII` -gt 0 ]
		then
			echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$APPENDUSERS:$CSVFILE:" | sudo -H /opt/karoshi/web_controls/exec/dynamic_groups
			#Remove /var/www/karoshi/dynamic_groups
			rm -f -R /var/www/karoshi/dynamic_groups
			show_status2
		else
			export MESSAGE=$"This is not a valid file format."
			#Remove /var/www/karoshi/dynamic_groups
			rm -f -R /var/www/karoshi/dynamic_groups
			show_status
		fi
	else
		#No data uploaded
		export MESSAGE=$"A CSV file has not been uploaded."
		show_status
	fi
else
	#No data uploaded
	export MESSAGE=$"A CSV file has not been uploaded."
	show_status
fi
exit


