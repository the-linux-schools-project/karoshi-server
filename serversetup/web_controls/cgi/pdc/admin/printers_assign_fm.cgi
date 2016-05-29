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
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Assign Printers to Locations"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
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
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body onLoad="start()"><div id="pagecontainer">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

function no_locations {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/locations.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
#########################
#Assign data to variables
#########################
END_POINT=3
#Assign _PRINTERNAME_
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

#Check to see that PRINTER is not blank
if [ -z "$PRINTERNAME"	 ]
then
	MESSAGE=$"You have not chosen any printers."
	show_status
fi

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
fi

echo '<form action="/cgi-bin/admin/printers_assign.cgi" method="post"><div id="actionbox3"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<table class="standard" style="text-align: left;">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$"Assign Printers to Locations"'</b></a></td></tr></tbody></table>'
else
	echo '<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top;"><b>'$"Assign Printers to Locations"'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Add a network printer for your client computers."'</span></a></td>
<td style="vertical-align: top;">
<button class="button" formaction="/cgi-bin/admin/printers.cgi" name="SHOWPRINTERS" value="_">
'$"Show Printers"'
</button>
</td>
<td style="vertical-align: top;">
<button class="button" formaction="/cgi-bin/admin/printers_delete.cgi" name="DELETEPRINTER" value="_">
'$"Delete Printers"'
</button>
</td>
<td style="vertical-align: top;">
<button class="button" formaction="/cgi-bin/admin/printers_view_assigned_fm.cgi" name="VIEWASSIGNED" value="_">
'$"View Assigned Printers"'
</button>
</td>
<td style="vertical-align: top;">
<button class="button" formaction="/cgi-bin/admin/locations.cgi" name="ADDLOCATION" value="_">
'$"Add Location"'
</button>
</td>
</tr></tbody></table><br></div><div id="infobox">'
fi


#Check to see that locations.txt exists
if [ ! -f /var/lib/samba/netlogon/locations.txt ]
then
	MESSAGE=$"No locations have been created."
	no_locations
	exit
fi

###############################
#Location
###############################
if [ -f /var/lib/samba/netlogon/locations.txt ]
then
	LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
else
	LOCATION_COUNT=0
fi

MAXCOLS=2
MAXHEADERS=1
if [ "$LOCATION_COUNT" -gt 10 ]
then
	MAXCOLS=4
	MAXHEADERS=2
fi

if [ "$LOCATION_COUNT" -gt 20 ]
then
	MAXCOLS=6
	MAXHEADERS=3
fi

if [ "$LOCATION_COUNT" -gt 30 ]
then
	MAXCOLS=8
	MAXHEADERS=4
fi

echo '<input type="hidden" name="_PRINTERNAME_" value="'$PRINTERNAME'"><table class="tablesorter" style="text-align: left;" ><tbody><tr><td style="width: 180px;">Printer</td><td style="width: 100px;">'$PRINTERNAME'</td></tr>
</tbody></table><br><table class="tablesorter" style="text-align: left;" ><thead><tr><th style="width: 180px; vertical-align: top;"><b>'$"Location"'</b></th><th style="width: 100px; vertical-align: top;"><b>'$"Assign"'</b></th>'


for (( i=1; i<$MAXHEADERS; i++ ))
do
	echo '<th style="width: 140px; vertical-align: top;"><b>'$"Location"'</b></th><th style="width: 90px; vertical-align: top;"><b>'$"Assign"'</b></th>'
done

	


echo '</tr></thead><tbody>'

COUNTER=1
COLCOUNT=0

while [ $COUNTER -lt $LOCATION_COUNT ]
do
	LOCATION=`sed -n $COUNTER,$COUNTER'p' /var/lib/samba/netlogon/locations.txt`

	if [ "$COLCOUNT" = 0 ]
	then
 		 echo "<tr>"
	fi

	if [ `grep ^$LOCATION"," /var/lib/samba/netlogon/printers.txt | grep -c -w $PRINTERNAME` -gt 0 ]
	then
		echo '<td>'$LOCATION'</td><td><input type="checkbox" name="_LOCATION_" value="'$LOCATION'" checked></td>'
	else
		echo '<td>'$LOCATION'</td><td><input type="checkbox" name="_LOCATION_" value="'$LOCATION'"></td>'
	fi
	let COUNTER=$COUNTER+1
	let COLCOUNT=$COLCOUNT+2

	if [ "$COLCOUNT" = "$MAXCOLS" ]
	then
		echo "</tr>"
		COLCOUNT=0
	fi
done
echo '</tbody></table><br><br>'

echo '<input value="'$"Submit"'" class="button" type="submit"></div></div></form></div></body></html>'
exit
