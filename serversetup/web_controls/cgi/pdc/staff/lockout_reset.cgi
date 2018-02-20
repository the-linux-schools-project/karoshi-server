#!/bin/bash
#Copyright (C) 2008  Paul Sharrad
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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

SLEEPTIME=5

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<html><head><title>'$"Reset User Lockout"'</title><meta http-equiv="REFRESH" content="0; URL='"$HTTP_REFERER"'">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+-')
#########################
#Assign data to variables
#########################

END_POINT=9
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


#Assign USERNAME
DATANAME=USERNAME
get_data
USERNAME="$DATAENTRY"

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Check data
#########################
#Check to see that USERNAME is not blank
if [ -z "$USERNAME" ]
then
	MESSAGE=$"The username must not be blank."
	show_status
fi

#Check to see that the user exists
echo "$Checksum:$USERNAME" | sudo -H /opt/karoshi/web_controls/exec/existcheck_user
if [ "$?" = 111 ]
then
	MESSAGE=$"This user does not exist."
	show_status
fi

#Check to see that the member of staff is not restricted
if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
	if [[ $(grep -c -w "$REMOTE_USER" /opt/karoshi/web_controls/staff_restrictions.txt) -gt 0 ]]
	then
		sudo -H /opt/karoshi/web_controls/exec/record_staff_error "$REMOTE_USER:$REMOTE_ADDR:$REMOTE_USER"
		sleep "$SLEEPTIME"
		MESSAGE=$"Your access to this feature has been restricted."
		show_status
	fi
fi

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/staff/lockout_reset.cgi | cut -d' ' -f1)
#Reset lockout
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$USERNAME:" | sudo -H /opt/karoshi/web_controls/exec/lockout_reset
if [ "$?" = 0 ]
then
	MESSAGE="$USERNAME: "$"Lockout attempts reset."
else
	MESSAGE="$USERNAME: "$"There was a problem with this action."" "$"Please check the karoshi web administration logs for more details."
fi
show_status
