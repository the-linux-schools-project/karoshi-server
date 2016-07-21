#!/bin/bash
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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server


#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=15
#Assign NAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = NAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		NAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign LIMIT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = LIMITcheck ]
	then
		let COUNTER=$COUNTER+1
		LIMIT=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
let COUNTER=$COUNTER+1
done

#Assign GROUPLIMIT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = GROUPLIMITcheck ]
	then
		let COUNTER=$COUNTER+1
		GROUPLIMIT=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign TOTAL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = TOTALcheck ]
	then
		let COUNTER=$COUNTER+1
		TOTAL=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

TYPE=group
STARTCGI=printer_accounting_group_limits_fm.cgi
#Assign TYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = TYPEcheck ]
	then
		let COUNTER=$COUNTER+1
		TYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

if [ -z "$TYPE" ]
then
	if [ $TYPE = user ]
	then
		STARTCGI=printer_accounting_user_limits_fm.cgi
	fi
fi


function show_status {
echo '<script>'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/'$STARTCGI'";'
echo '</script>'
echo "</div></div></body></html>"
exit
}


##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Edit Printer Limits"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
</head><body onLoad="start()"><div id="pagecontainer">'

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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################
#Check to see that NAME is not blank
if [ -z "$NAME" ]
then
	MESSAGE=$"The user or group name cannot be blank."
	show_status
fi
#Check to see that LIMIT is not blank
if [ -z "$LIMIT" ]
then
	LIMIT=0
fi

MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=menubox
fi
echo '<form name="myform" id="myform" action="/cgi-bin/admin/printer_accounting_edit_limits.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<table class="standard" style="text-align: left;" >
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Edit Printer Limits"'</b></a></td></tr></tbody></table>'
else
	echo '<b>'$"Edit Printer Limits"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Each Primary Group has a limit set for the amount of printing that each user can do in that group."'<br><br>'$"User limits override group limits."'</span></a><br><br>'
fi

echo '
<input name="_NAME_" value="'$NAME'" type="hidden">
<input name="_TYPE_" value="'$TYPE'" type="hidden">'

if [ $TYPE != userdelete ] && [ $TYPE = user ]
then
	echo '
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">'$"Username"'</td><td>'$NAME'</td></tr>
<tr><td>'$"User Limit"'</td><td>'$LIMIT'</td></tr>
<tr><td>'$"Group Limit"'</td><td>'$GROUPLIMIT'</td></tr>
<tr><td>'$"Print Total"'</td><td>'$TOTAL'</td></tr>
<tr><td>'$"Additional Credits"'</td><td><input maxlength="10" size="10" name="_LIMIT_" value=""> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the amount of additional printer credits that you want this user to have."'<br><br>'$"User limits override group limits."'</span></a></td></tr></tbody></table>
'
fi

if [ $TYPE != userdelete ] && [ $TYPE = group ]
then
	echo '<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;"><b>'$"User or Primary Group"'</b></td><td><b>'$"Limit"'</b></td></tr>
<tr><td>'$NAME'</td><td><input maxlength="10" size="10" name="_LIMIT_" value="'$LIMIT'"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Set the page limits that you want for each user or group."'</span></a></td></tr></tbody></table>
'
fi


if [ $TYPE = userdelete ]
then
echo
echo '<input name="_LIMIT_" value="'$LIMIT'" type="hidden"></form>'
echo "<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('myform').submit();
//-->
</script>"

fi

if [ $MOBILE = no ]
then
	echo '</div><div id="submitbox">'
fi
echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></form></div></body></html>
'
exit
