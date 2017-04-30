#!/bin/bash
#Copyright (C) 2008 Paul Sharrad

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
#  _USERNAME_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
#  _GROUP_      This is the primary group for the new user eg yr2000, staff, officestaff.
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER" ] && source "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Import DHCP Reservations"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox">
<div class="sectiontitle">'$"Import DHCP Reservations"'</div></div><div id="infobox">
<br><br>'

function show_status {

echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/admin/dhcp_import_reservations_fm.cgi"'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_dhcp_reservations {
echo "
<form action=\"/cgi-bin/admin/dhcp_reservations.cgi\" method=\"post\" id=\"showdns\">
<input type=\"hidden\" name=\"ShowReservations\" value=\"\">
</form>
<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('showdns').submit();
//-->
</script>
</div></div></body></html>
"
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
#Check input file
[ -d /var/www/karoshi/dhcp-static_lease_import ] || mkdir -p /var/www/karoshi/dhcp-static_lease_import
chmod 0700 /var/www/karoshi/
chmod 0700 /var/www/karoshi/dhcp-static_lease_import
if [[ $(dir /var/www/karoshi/dhcp-static_lease_import --format=single-column | wc -l) != 1 ]]
then
	MESSAGE=$"File upload error."
	show_status
fi
CSVFILE=$(ls /var/www/karoshi/dhcp-static_lease_import)
echo >> /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE"
cat /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE" | tr -cd 'A-Za-z0-9\.,_:\-\n' > /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE"2
rm -f /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE"
mv /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE"2 /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE"
sed -i '/^$/d' /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE"
CSVFILE_LINES=$(cat /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE" | wc -l)
[ -f /var/www/karoshi/dhcp-static_lease_import/karoshi_import_static_leases.csv.$$ ] && rm -f "/var/www/karoshi/dhcp-static_lease_import/karoshi_import_static_leases.csv.$$"
COUNTER=1

source /opt/karoshi/server_network/dhcp/dhcp_settings

function convert_ip_to_int {
IFS=. read -r a b c d <<< "$ip"
printf '%s%d\n' "$((a * 256 ** 3 + b * 256 ** 2 + c * 256 + d))"
}

while [ "$COUNTER" -le "$CSVFILE_LINES" ]
do
	CLIENTNAME=$(sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE" | cut -s -d, -f1)
	MAC=$(sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE" | cut -s -d, -f2)
	TCPIP=$(sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE" | cut -s -d, -f3)
	echo "$COUNTER: $CLIENTNAME $MAC $TCPIP""<br>"
	if [ -z "$CLIENTNAME" ]
	then
		MESSAGE=''$"Error on line $COUNTER"' - '$"Blank devicename."''
		show_status
	fi
	if [ -z "$MAC" ]
	then
		MESSAGE=''$"Error on line $COUNTER"' - '$"Blank Mac address."''
		show_status
	fi
	if [ -z "$TCPIP" ]
	then
		MESSAGE=''$"Error on line $COUNTER"' - '$"Blank TCPIP address"''
		show_status
	fi

	#Check that the clientname is not already in use
	if [ -f /etc/dhcp/dhcpd_reservations.conf ]
	then
		if [[ $(grep -c -w "host $CLIENTNAME" /etc/dhcp/dhcpd_reservations.conf) -gt 0 ]]
		then
			MESSAGE=''$"Error on line $COUNTER"' - '$"This client name is already in use."''
			show_status
		fi
	fi

	#Check tcpip
	#Check dots
	if [[ $(echo "$TCPIP" | sed 's/\./\n /g'  | sed /^$/d | wc -l) != 4 ]]
	then
		MESSAGE=''$"Error on line $COUNTER"' - '$"You have not entered in a correct tcpip address."''
		show_status
	fi
	#Check that no number is greater than 255
	HIGHESTNUMBER=$(echo "$TCPIP" | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p)
	if [ "$HIGHESTNUMBER" -gt 255 ]
	then
		MESSAGE=''$"Error on line $COUNTER"' - '$"You have not entered in a correct tcpip address."''
		show_status
	fi
	#Check to see that the tcpip number has not already been added
	if [ -f /etc/dhcp/dhcpd_reservations.conf ]
	then
		if [[ $(grep -c "$TCPIP;" /etc/dhcp/dhcpd_reservations.conf) -gt 0 ]]
		then
			MESSAGE=''$"Error on line $COUNTER"' - '$"This TCPIP address is already in use."''
			show_status
		fi
	fi

	#Check mac address
	#Check colons 00:13:77:b8:39:17
	if [[ $(echo "$MAC" | sed 's/:/\n/g' | wc -l) != 6 ]]
	then
		MESSAGE=''$"Error on line $COUNTER"' - '$"You have not entered in a valid mac address."''
		show_status	
	fi
	#Check max chars
	for LINEDATA in $(echo "$MAC" | sed 's/:/\n/g')
	do
		if [[ $(echo "$LINEDATA" | wc -L) != 2 ]]
		then
			MESSAGE=''$"Error on line $COUNTER"' - '$"You have not entered in a valid mac address."''
			show_status
		fi
	done
	#Check to see that the mac address has not already been added
	if [ -f /etc/dhcp/dhcpd_reservations.conf ]
	then
		if [[ $(grep -c "$MAC;" /etc/dhcp/dhcpd_reservations.conf) -gt 0 ]]
		then
			MESSAGE=''$"Error on line $COUNTER"' - '$"This mac address is already in use."''
			show_status
		fi
	fi

	#Check that the mac address is not in the dhcp range

	ip="$STARTADDRESS"
	int_range_start=$(convert_ip_to_int)

	ip="$ENDADDRESS"
	int_range_end=$(convert_ip_to_int)

	ip="$TCPIP"
	int_ip_num=$(convert_ip_to_int)


	if [ "$int_ip_num" -ge "$int_range_start" ] && [ "$int_ip_num" -le "$int_range_end" ]
	then
		MESSAGE=$"This TCPIP address is inside the DHCP reservation range."
		sshow_status

	fi

	echo "$CLIENTNAME","$MAC","$TCPIP" >> /var/www/karoshi/dhcp-static_lease_import/karoshi_import_static_leases.csv.$$
	let COUNTER=$COUNTER+1
done
CSVMDSUM=$(md5sum /var/www/karoshi/dhcp-static_lease_import/karoshi_import_static_leases.csv.$$ | cut -d' ' -f1)
rm -f /var/www/karoshi/dhcp-static_lease_import/"$CSVFILE"
MD5SUM=$(md5sum /var/www/cgi-bin_karoshi/admin/dhcp_import_reservations_process.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$CSVMDSUM:$$:" | sudo -H /opt/karoshi/web_controls/exec/dhcp_import_reservations
show_dhcp_reservations
echo "</div></div></div></body></html>"
