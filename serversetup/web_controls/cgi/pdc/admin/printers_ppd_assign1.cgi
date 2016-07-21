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
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Assign PPD File"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

#########################
#Assign data to variables
#########################
END_POINT=3
#Assign PRINTERNAME

COUNTER=1
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PRINTERNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		PRINTERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
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
#Check data
#########################
#Check to see that PRINTERNAME is not blank
if [ -z "$PRINTERNAME" ]
then
	MESSAGE=$"The printer name cannot be blank."
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

#Detect mobile browser
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

echo '<form action="/cgi-bin/admin/printers_ppd_assign2.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<table class="standard" style="text-align: left;" >
	<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
	<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Assign PPD File"'</b></a></td>'
else
	echo '<table class="standard" style="text-align: left;" >
	<tbody><tr><td><b>'$"Assign PPD File"'</b></td>'
fi

echo '<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"A PPD is a linux printer driver. You will need to assign a printer driver to every printer queue that you set up."'</span></a></tr></tbody></table>
<br><input type="hidden" name="_PRINTERNAME_" value="'$PRINTERNAME'"><table class="standard" style="text-align: left; height: 120px;" ><tbody>'
#Show Printername
echo '<tr><td style="width: 180px;">'$"Printer"'</td><td>'$PRINTERNAME'</td></tr>'

#######################
#Guess default paper size
#######################
A4SELECTED='selected="selected"'
LETTERSELECTED=""

#Show list of page sizes
echo '
<tr><td>'$"Default Page Size"'</td><td>
<select style="width: 200px;" name="_PAGESIZE_">
<option value="A2">A2</option>
<option value="A3">A3</option>
<option value="Letter" '$LETTERSELECTED'>Letter</option>
<option value="A4" '$A4SELECTED'>A4</option>
<option value="A5" >A5</option>
<option value="A6">A6</option>
<option value="">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </option>
</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the default page size for this printer."'</span></a></td></tr>
<tr><td>'$"Print in Colour?"'</td><td>
<select style="width: 200px;" name="_COLOUR_">
<option value="yes">'$"yes"'</option>
<option value="no">'$"No"'</option>
</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This setting will only affect printers that can print in colour."'</span></a></td></tr>'

#Show printer manufacturer list to choose from
echo '<tr><td>'$"Printer Make"'</td><td><select style="width: 200px;" name="_PRINTERPPD_">'
echo '<option value=""></option>'
echo '<option value="uploadppd">'$"Upload PPD File"'</option>'
#Get list of printer drivers
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/printers_ppd_assign1.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/printers_show_drivers $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$PRINTERMAKE

echo '</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the make of your printer from this list. If the printer make is not listed you will need to get a PPD from the internet and use the Upload PPD option."'</span></a></td></tr>'
echo '</tbody></table><br>'

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div>'
echo '</form></div></body></html>'
exit

