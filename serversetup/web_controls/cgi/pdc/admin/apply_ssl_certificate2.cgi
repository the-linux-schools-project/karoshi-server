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
#  _SERVER_
#  _COUNTRYCODE_
#  _STATE_
#  _LOCALITY_
#  _INSTITUTENAME_
#  _DEPARTMENT_
#  _COMMONNAME_
#  _EMAIL_
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Apply Self Signed SSL Certificate"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%+' | sed 's/___/TRIPLESCORED/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLESCORED/_/g')
#########################
#Assign data to variables
#########################
END_POINT=22
function get_data {
COUNTER=2
DATAENTRY=""
while [[ $COUNTER -le $END_POINT ]]
do
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [[ "$DATAHEADER" = "$DATANAME" ]]
	then
		let COUNTER="$COUNTER"+1
		DATAENTRY=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
		break
	fi
	let COUNTER=$COUNTER+1
done
}

#Assign SERVER
DATANAME=SERVER
get_data
SERVER="${DATAENTRY//UNDERSCORE/_}"

#Assign COUNTRYCODE
DATANAME=COUNTRYCODE
get_data
COUNTRYCODE="${DATAENTRY//UNDERSCORE/_}"

#Assign STATE
DATANAME=STATE
get_data
STATE="${DATAENTRY//UNDERSCORE/_}"

#Assign LOCALITY
DATANAME=LOCALITY
get_data
LOCALITY="${DATAENTRY//UNDERSCORE/_}"

#Assign INSTITUTENAME
DATANAME=INSTITUTENAME
get_data
INSTITUTENAME="${DATAENTRY//UNDERSCORE/_}"

#Assign DEPARTMENT
DATANAME=DEPARTMENT
get_data
DEPARTMENT="${DATAENTRY//UNDERSCORE/_}"

#Assign COMMONNAME
DATANAME=COMMONNAME
get_data
COMMONNAME="${DATAENTRY//UNDERSCORE/_}"

#Assign EMAIL
DATANAME=EMAIL
get_data
EMAIL=$(echo "$DATAENTRY" | sed 's/%40/@/g' | sed 's/UNDERSCORE/_/g')

#Assign EMAILCERT
DATANAME=EMAILCERT
get_data
EMAILCERT="${DATAENTRY//UNDERSCORE/_}"

#Assign WEBCERT
DATANAME=WEBCERT
get_data
WEBCERT="${DATAENTRY//UNDERSCORE/_}"

#Assign CERTTYPE
DATANAME=CERTTYPE
get_data
CERTTYPE="${DATAENTRY//UNDERSCORE/_}"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/apply_ssl_certificate_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
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

if [[ $(grep -c ^"$REMOTE_USER": /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################
#Check to see that SERVER is not blank
if [ -z "$SERVER" ]
then
	MESSAGE=$"The server option cannot be blank."
	show_status
fi

#Check to see that COUNTRYCODE is not blank
if [ -z "$COUNTRYCODE" ]
then
	MESSAGE=$"The country code option cannot be blank."
	show_status
fi
#Check to see that STATE is not blank
if [ -z "$STATE" ]
then
	MESSAGE=$"The state option cannot be blank."
	show_status
fi
#Check to see that LOCALITY is not blank
if [ -z "$LOCALITY" ]
then
	MESSAGE=$"The locality option cannot be blank."
	show_status
fi
#Check to see that INSTITUTENAME is not blank
if [ -z "$INSTITUTENAME" ]
then
	MESSAGE=$"The institute name option cannot be blank."
	show_status
fi
#Check to see that DEPARTMENT is not blank
if [ -z "$DEPARTMENT" ]
then
	MESSAGE=$"The department name cannot be blank."
	show_status
fi
#Check to see that COMMONNAME is not blank
if [ -z "$COMMONNAME" ]
then
	MESSAGE=$"The common name option cannot be blank."
	show_status
fi
#Check to see that EMAIL is not blank
if [ -z "$EMAIL" ]
then
	MESSAGE=$"The e-mail option cannot be blank."
	show_status
fi

#Check to see that WEBCERT is not blank
if [ -z "$WEBCERT" ]
then
	MESSAGE=$"There was an error with the certificate option type."
	show_status
fi

#Check to see that EMAILCERT is not blank
if [ -z "$EMAILCERT" ]
then
	MESSAGE=$"There was an error with the certificate option type."
	show_status
fi

#Check to see that CERTTYPE is not blank
if [ -z "$CERTTYPE" ]
then
	MESSAGE=$"There was an error with the certificate option type."
	show_status
fi

STATE="${STATE//+/ }"
LOCALITY="${LOCALITY//+/ }"
INSTITUTENAME="${INSTITUTENAME//+/ }"
DEPARTMENT="${DEPARTMENT//+/ }"
COMMONNAME="${COMMONNAME//+/ }"
EMAIL="${EMAIL//+/ }"


Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/apply_ssl_certificate2.cgi | cut -d' ' -f1)

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">'
if [ "$WEBCERT" = yes ]
then
	echo "<b>$SERVER - "$"Web Certificate""</b><br><br>"
else
	echo "<b>$SERVER - "$"E-mail Certificate""</b><br><br>"
fi

echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$SERVER:$COUNTRYCODE:$STATE:$LOCALITY:$INSTITUTENAME:$DEPARTMENT:$COMMONNAME:$EMAIL:$EMAILCERT:$WEBCERT:$CERTTYPE" | sudo -H /opt/karoshi/web_controls/exec/apply_ssl_certificate
STATUS="$?"
if [ "$STATUS" = 101 ]
then
	MESSAGE=$"There was a problem applying the certificate. Please check the Karoshi Web Management logs."
	show_status
fi
if [ "$STATUS" = 102 ]
then
	MESSAGE=$"SSH is not enabled for this server."
	show_status
fi
MESSAGE=$"The SSL Certificate has been applied."
show_status
exit
