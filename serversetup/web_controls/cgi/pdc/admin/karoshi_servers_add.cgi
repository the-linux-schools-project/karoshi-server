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
########################
#Required input variables
########################
#  _SERVERNAME_
# _TCPIP_
#  _PASSWORD1_  Root Password
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server


echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Add Server"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>
<SCRIPT language=JavaScript1.2>
//change 5 to another integer to alter the scroll speed. Greater is faster
var speed=1
var currentpos=-100,alt=1,curpos1=-100,curpos2=-1
function initialize(){
startit()
}
function scrollwindow(){
if (document.all &&
!document.getElementById)
temp=document.body.scrollTop
else
temp=window.pageYOffset
if (alt==0)
alt=2
else
alt=1
if (alt==0)
curpos1=temp
else
curpos2=temp
if (curpos1!=curpos2){
if (document.all)
currentpos=document.body.scrollTop+speed
else
currentpos=window.pageYOffset+speed
window.scroll(0,currentpos)
}
else{
currentpos=0
window.scroll(0,currentpos)
}
}
function startit(){
setInterval("scrollwindow()",30)
}
window.onload=initialize
</SCRIPT>
</head><body><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3">'
############################
#Show page
############################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/admin/karoshi_servers_add_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function test_connections {
echo '<SCRIPT language="Javascript">'
#echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/karoshi_servers_view.cgi";'
echo '</script>'
echo "</div></div></body></html>"
exit
}

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g')

#########################
#Assign data to variables
#########################
END_POINT=13
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

#Assign SERVERNAME
DATANAME=SERVERNAME
get_data
SERVERNAME="$DATAENTRY"

#Assign TCPIPNUMBER
DATANAME=TCPIPNUMBER
get_data
TCPIPNUMBER=$(echo "$DATAENTRY" | tr -cd '0-9.')

#Assign password1
DATANAME=PASSWORD1
get_data
PASSWORD1="$DATAENTRY"

#Assign password2
DATANAME=PASSWORD2
get_data
PASSWORD2="$DATAENTRY"

#Assign authentication
DATANAME=AUTHENTICATION
get_data
AUTHENTICATION="$DATAENTRY"

#Assign ZONE
DATANAME=ZONE
get_data
ZONE="$DATAENTRY"

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
#Check to see that servername is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The server must not be blank."
	show_status
fi

#Check to see that servername is not called proxy
if [ "$SERVERNAME" = proxy ]
then
	MESSAGE=$"The server cannot be called proxy."
	show_status
fi


#Check to see that password fields are not blank
if [ -z "$PASSWORD1" ]
then
	MESSAGE=$"The password must not be blank."
	show_status
fi
if [ -z "$PASSWORD2" ]
then
	MESSAGE=$"The password must not be blank."
	show_status
fi
#Check that password has been entered correctly
if [ "$PASSWORD1" != "$PASSWORD2" ]
then
	MESSAGE=$"The passwords do not match."
	show_status
fi

#Check to see that authentication is not blank
if [ -z "$AUTHENTICATION" ]
then
	MESSAGE=$"You have not picked an authentication type."
	show_status
fi

#Check to see that authentication is not blank
if [ -z "$ZONE" ]
then
	MESSAGE=$"You have not picked an authentication type."
	show_status
fi

function get_data {
#Send data back to form and ask for tcpip number
echo '
<body onload="submitForm()"><form action="/cgi-bin/admin/karoshi_servers_add_fm.cgi" method="post" name="form">
<input name="____SERVERNAME____" value="'"$SERVERNAME"'" type="hidden">
<input name="____PASSWORD1____" value="'"$PASSWORD1"'" type="hidden">
<input name="____PASSWORD2____" value="'"$PASSWORD2"'" type="hidden">
<input name="____AUTHENTICATION____" value="'"$AUTHENTICATION"'" type="hidden">
<input name="_ZONE_" value="'"$ZONE"'" type="hidden">
</form>
<SCRIPT LANGUAGE="JavaScript">
function submitForm(){
document.form.submit();
}
</SCRIPT></div></body></html
'
exit
}



#If tcpip is blank check to see that we know the tcpip number
if [ -z "$TCPIPNUMBER" ]
then
	host -r -t A "$SERVERNAME" 1>/dev/null
	[ "$?" != 0 ] && get_data
fi

if [ ! -z "$TCPIPNUMBER" ]
then
	########################
	#Check that the tcpip number has been entered correctly
	########################
	#Check dots
	if [[ $(echo "$TCPIPNUMBER" | sed 's/\./\n /g'  | sed /^$/d | wc -l) != 4 ]]
	then
		MESSAGE=$"You have entered in a valid TCPIP number."
		show_status
	fi

	#Check that no number is greater than 255
	HIGHESTNUMBER=$(echo "$TCPIPNUMBER" | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p)
	if [ "$HIGHESTNUMBER" -gt 255 ]
	then
		MESSAGE=$"You have entered in a valid TCPIP number."
		show_status
	fi
fi

#Check to see that this is not the tcpip number of the main server.
MAINSERVERIP=$(hostname -i | cut -d" " -f1)
if [ "$MAINSERVERIP" = "$TCPIPNUMBER" ]
then
	MESSAGE=$"You have entered in the same TCPIP address as the main server."
	show_status
fi

echo '<div id="titlebox"><div class="sectiontitle">'$"Add Server"' - '"$SERVERNAME"'</div><br></div><div id="infobox">'

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/karoshi_servers_add.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$SERVERNAME:$PASSWORD1:$TCPIPNUMBER:$AUTHENTICATION:$ZONE" | sudo -H /opt/karoshi/web_controls/exec/karoshi_servers_add
EXEC_STATUS="$?"

MESSAGE=''"$SERVERNAME"' - '$"ssh has been enabled."''
if [ "$EXEC_STATUS" = 101 ]
then
	MESSAGE=''"$SERVERNAME"' - '$"There was a problem enabling ssh for this server. Please check the web administration logs."''
	show_status
fi
test_connections
exit
