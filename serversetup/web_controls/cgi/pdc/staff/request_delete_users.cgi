#!/bin/bash
#Request New Users
#Copyright (C) 2009 Paul Sharrad
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

############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs

export TEXTDOMAIN=karoshi-server
############################
#Show page
############################

SLEEPTIME=5

echo "Content-type: text/html"
echo ""
echo '<html><head><title>'$"Request Delete Users"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+-'`
#########################
#Assign data to variables
#########################

FORENAME1=$(echo "$DATA" | cut -d_ -f3)
SURNAME1=$(echo "$DATA" | cut -d_ -f5)
GROUP1=$(echo "$DATA" | cut -d_ -f7)
ADNO1=$(echo "$DATA" | cut -d_ -f9)

FORENAME2=$(echo "$DATA" | cut -d_ -f11)
SURNAME2=$(echo "$DATA" | cut -d_ -f13)
GROUP2=$(echo "$DATA" | cut -d_ -f15)
ADNO2=$(echo "$DATA" | cut -d_ -f27)

FORENAME3=$(echo "$DATA" | cut -d_ -f19)
SURNAME3=$(echo "$DATA" | cut -d_ -f21)
GROUP3=$(echo "$DATA" | cut -d_ -f23)
ADNO3=$(echo "$DATA" | cut -d_ -f25)

FORENAME4=$(echo "$DATA" | cut -d_ -f27)
SURNAME4=$(echo "$DATA" | cut -d_ -f29)
GROUP4=$(echo "$DATA" | cut -d_ -f31)
ADNO4=$(echo "$DATA" | cut -d_ -f33)

FORENAME5=$(echo "$DATA" | cut -d_ -f35)
SURNAME5=$(echo "$DATA" | cut -d_ -f37)
GROUP5=$(echo "$DATA" | cut -d_ -f39)
ADNO5=$(echo "$DATA" | cut -d_ -f41)

FORENAME6=$(echo "$DATA" | cut -d_ -f43)
SURNAME6=$(echo "$DATA" | cut -d_ -f45)
GROUP6=$(echo "$DATA" | cut -d_ -f47)
ADNO6=$(echo "$DATA" | cut -d_ -f49)

FORENAME7=$(echo "$DATA" | cut -d_ -f51)
SURNAME7=$(echo "$DATA" | cut -d_ -f53)
GROUP7=$(echo "$DATA" | cut -d_ -f55)
ADNO7=$(echo "$DATA" | cut -d_ -f57)

FORENAME8=$(echo "$DATA" | cut -d_ -f59)
SURNAME8=$(echo "$DATA" | cut -d_ -f61)
GROUP8=$(echo "$DATA" | cut -d_ -f63)
ADNO8=$(echo "$DATA" | cut -d_ -f65)

FORENAME9=$(echo "$DATA" | cut -d_ -f67)
SURNAME9=$(echo "$DATA" | cut -d_ -f69)
GROUP9=$(echo "$DATA" | cut -d_ -f71)
ADNO9=$(echo "$DATA" | cut -d_ -f73)

FORENAME10=$(echo "$DATA" | cut -d_ -f75)
SURNAME10=$(echo "$DATA" | cut -d_ -f77)
GROUP10=$(echo "$DATA" | cut -d_ -f79)
ADNO10=$(echo "$DATA" | cut -d_ -f81)

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'history.go(-1);'
echo '</script>'
echo "</div></div></body></html>"
exit
}

function show_status2 {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo 'window.location = "/cgi-bin/staff/request_delete_users_fm.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_staff
echo '<div id="actionbox">'
#########################
#Check data
#########################

#Check some fornames have been entered
if [ $(echo "$FORENAME1$FORENAME2$FORENAME3$FORENAME4$FORENAME5$FORENAME6$FORENAME7$FORENAME8$FORENAME9$FORENAME10""null") = null ]
then
	MESSAGE=$"You have not enterered any forenames."
	show_status
fi

#Check some surnames have been entered
if [ $(echo "$SURNAME1$SURNAME2$SURNAME3$SURNAME4$SURNAME5$SURNAME6$SURNAME7$SURNAME8$SURNAME9$SURNAME10""null") = null ]
then
	MESSAGE=$"You have not enterered any surnames."
	show_status
fi

if [ ! -z "$FORENAME1" ]
then
	if [ -z "$SURNAME1" ]
	then
		MESSAGE="$FORENAME1 - "$"Missing surname."
		show_status
	fi
	if [ -z "$GROUP1" ]
	then
		MESSAGE="$FORENAME1 $SURNAME1 - "$"You need to set the group for this user."
		show_status
	fi
fi

if [ ! -z "$FORENAME2" ]
then
	if [ -z "$SURNAME2" ]
	then
		MESSAGE="$FORENAME2 - "$"Missing surname."
		show_status
	fi
	if [ -z "$GROUP2" ]
	then
		MESSAGE="$FORENAME2 $SURNAME2 - "$"You need to set the group for this user."
		show_status
	fi
fi

if [ ! -z "$FORENAME3" ]
then
	if [ -z "$SURNAME3" ]
	then
		MESSAGE="$FORENAME3 - "$"Missing surname."
		show_status
	fi
	if [ -z "$GROUP3" ]
	then
		MESSAGE="$FORENAME3 $SURNAME3 - "$"You need to set the group for this user."
		show_status
	fi
fi

if [ ! -z "$FORENAME4" ]
then
	if [ -z "$SURNAME4" ]
	then
		MESSAGE="$FORENAME4 - "$"Missing surname."
		show_status
	fi
	if [ -z "$GROUP4" ]
	then
		MESSAGE="$FORENAME4 $SURNAME4 - "$"You need to set the group for this user."
		show_status
	fi
fi

if [ ! -z "$FORENAME5" ]
then
	if [ -z "$SURNAME5" ]
	then
		MESSAGE="$FORENAME5 - "$"Missing surname."
		show_status
	fi
	if [ -z "$GROUP5" ]
	then
		MESSAGE="$FORENAME5 $SURNAME5 - "$"You need to set the group for this user."
		show_status
	fi
fi

if [ ! -z "$FORENAME6" ]
then
	if [ -z "$SURNAME6" ]
	then
		MESSAGE="$FORENAME6 - "$"Missing surname."
		show_status
	fi
	if [ -z "$GROUP6" ]
	then
		MESSAGE="$FORENAME6 $SURNAME6 - "$"You need to set the group for this user."
		show_status
	fi
fi

if [ ! -z "$FORENAME7" ]
then
	if [ -z "$SURNAME7" ]
	then
		MESSAGE="$FORENAME7 - "$"Missing surname."
		show_status
	fi
	if [ -z "$GROUP7" ]
	then
		MESSAGE="$FORENAME7 $SURNAME7 - "$"You need to set the group for this user."
		show_status
	fi
fi

if [ ! -z "$FORENAME8" ]
then
	if [ -z "$SURNAME8" ]
	then
		MESSAGE="$FORENAME8 - "$"Missing surname."
		show_status
	fi
	if [ -z "$GROUP8" ]
	then
		MESSAGE="$FORENAME8 $SURNAME8 - "$"You need to set the group for this user."
		show_status
	fi
fi

if [ ! -z "$FORENAME9" ]
then
	if [ -z "$SURNAME9" ]
	then
		MESSAGE="$FORENAME9 - "$"Missing surname."
		show_status
	fi
	if [ -z "$GROUP9" ]
	then
		MESSAGE="$FORENAME9 $SURNAME9 - "$"You need to set the group for this user."
		show_status
	fi
fi

#Check to see that the member of staff is not restricted
if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
	if [ $(grep -c -w "$REMOTE_USER" /opt/karoshi/web_controls/staff_restrictions.txt) -gt 0 ]
	then
		sudo -H /opt/karoshi/web_controls/exec/record_staff_error "$REMOTE_USER:$REMOTE_ADDR:$REMOTE_USER"
		sleep "$SLEEPTIME"
		MESSAGE=$"Authentication failure."
		show_status
	fi
fi

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/staff/request_delete_users.cgi | cut -d' ' -f1)
#Change student password
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$REMOTE_USER:$FORENAME1:$SURNAME1:$GROUP1:$ADNO1:$FORENAME2:$SURNAME2:$GROUP2:$ADNO2:$FORENAME3:$SURNAME3:$GROUP3:$ADNO3:$FORENAME4:$SURNAME4:$GROUP4:$ADNO4:$FORENAME5:$SURNAME5:$GROUP5:$ADNO5:$FORENAME6:$SURNAME6:$GROUP6:$ADNO6:$FORENAME7:$SURNAME7:$GROUP7:$ADNO7:$FORENAME8:$SURNAME8:$GROUP8:$ADNO8:$FORENAME9:$SURNAME9:$GROUP9:$ADNO9:$FORENAME10:$SURNAME10:$GROUP10:$ADNO10:" | sudo -H /opt/karoshi/web_controls/exec/request_delete_users
MESSAGE=`echo $"The users you have requested for deletion have been added to the list."`
show_status2
exit
