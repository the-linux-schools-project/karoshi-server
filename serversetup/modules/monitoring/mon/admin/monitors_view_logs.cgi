#!/bin/bash
#Copyright (C) 2010  Paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
########################
#Required input variables
########################
#  _GROUPNAME_ The name of the mon monitor group to add
#  _SERVICE_  IP numbers of the devices in the group to check
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=monstyle.css

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Monitor Logs"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\+-'`
#########################
#Assign data to variables
#########################
END_POINT=9
#Assign GROUPNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = GROUPNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		GROUPNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign SERVICE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SERVICEcheck ]
	then
		let COUNTER=$COUNTER+1
		SERVICE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "mon_status.cgi"'
echo '</script>'
echo "</body></html>"
exit
}


#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_mon
echo '<div id="actionbox">'
#Show title
echo '<hr style="width: 100%; height: 2px;">'
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td style="vertical-align: top;">
<form action="/cgi-bin/admin/mon_status.cgi" method="post"><a class="info" href="javascript:void(0)"><input name="_SHOWMONITORS_" type="image" class="images" src="'$ICON'" value=""><span>'$VIEWMONITORS'</span></a></form></td><td style="vertical-align: top;"><b>'$"View Monitor Logs"' : '$GROUPNAME' - '$SERVICE'</b></td></tr></tbody></table>'
f


#Show monitor logs

if [ -f /opt/karoshi/server_network/mon/events/$GROUPNAME/$SERVICE.log ]
then
	echo '<pre style="font-size: 10pt; font-family:Arial, Times, Georgia, serif">'
	cat /opt/karoshi/server_network/mon/events/$GROUPNAME/$SERVICE.log
	echo "</pre>"
	else
	echo No Logs available
fi
echo "</div></body></html>"
