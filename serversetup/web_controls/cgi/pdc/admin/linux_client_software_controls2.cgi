#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

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
########################
#Required input variables
########################
#  _VERSION_
#  _INSTALL_
#  _UPDATES_
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Linux Client Software Controls"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

#########################
#Assign data to variables
#########################
END_POINT=17
#Assign VERSION
VERSION=""
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = VERSIONcheck ]
	then
		let COUNTER=$COUNTER+1
		VERSION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign SOFTWARE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SOFTWAREcheck ]
	then
		let COUNTER=$COUNTER+1
		SOFTWARE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign LOCATION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = LOCATIONcheck ]
	then
		let COUNTER=$COUNTER+1
		LOCATION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign GRAPHICS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = GRAPHICScheck ]
	then
		let COUNTER=$COUNTER+1
		GRAPHICS=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign AUTO
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = AUTOcheck ]
	then
		let COUNTER=$COUNTER+1
		AUTO=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign RESTRICTED
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = RESTRICTEDcheck ]
	then
		let COUNTER=$COUNTER+1
		RESTRICTED=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
	done

#Assign FIRMWARE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = FIRMWAREcheck ]
	then
		let COUNTER=$COUNTER+1
		FIRMWARE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SOFTWARE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SOFTWAREcheck ]
	then
		let COUNTER=$COUNTER+1
		SOFTWARE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign UPDATES
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = UPDATEScheck ]
	then
		let COUNTER=$COUNTER+1
		UPDATES=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "linux_client_software_controls_fm.cgi"'
echo '</script>'
echo "</div></body></html>"
exit
}

function completed {
echo '<form name="myForm" id="myForm" action="/cgi-bin/admin/linux_client_software_controls.cgi" method="post"><input name="_VERSION_" value="'$VERSION'" type="hidden"></form>'
echo "<script type='text/javascript'>document.myForm.submit();</script></div></body></html>"
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
#Check to see that VERSION is not blank
if [ -z "$VERSION" ]
then
	MESSAGE=$"The version has not been set."
	show_status
fi

#Check to see that VERSION is not blank
if [ -z "$LOCATION" ]
then
	MESSAGE=$"The location has not been set."
	show_status
fi

Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/linux_client_software_controls2.cgi | cut -d' ' -f1`
#Set software control options
sudo -H /opt/karoshi/web_controls/exec/linux_client_software_controls $REMOTE_USER:$REMOTE_ADDR:$Checksum:$VERSION:$SOFTWARE:$UPDATES:$AUTO:$GRAPHICS:$RESTRICTED:$FIRMWARE:$LOCATION:
completed
exit

