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
#  _TCPADDRESS_
#  _ACTION_
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Restrict access to Karoshi Remote Management"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
       $("#myTable").tablesorter({
	headers: {
	0: { sorter: "ipAddress" }
    		}
		});
       $("#myTable2").tablesorter({
	headers: {
	0: { sorter: "ipAddress" }
    		}
		});
    } 
);
</script>
</head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\%+-'`
#########################
#Assign data to variables
#########################
END_POINT=12
#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAENTRY'check'` = ACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign TCPADDRESS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAENTRY'check'` = ADDTCPADDRESScheck ]
	then
		let COUNTER=$COUNTER+1
		ADDTCPADDRESS=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign TCPCOMMENT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAENTRY'check'` = TCPCOMMENTcheck ]
	then
		let COUNTER=$COUNTER+1
		TCPCOMMENT=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign PRIMARYADMIN
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAENTRY'check'` = PRIMARYADMINcheck ]
	then
		let COUNTER=$COUNTER+1
		PRIMARYADMIN=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAENTRY'check'` = DELTCPADDRESScheck ]
	then
		let COUNTER=$COUNTER+1
		DELTCPADDRESS=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function view_tcpip {
echo '<SCRIPT language="Javascript">'
echo '                window.location = "/cgi-bin/admin/remote_management_restrict.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/remote_management_restrict_fm.cgi";'
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
#Check to see that ACTION is not blank
if [ -z "$ACTION" ]
then
	ACTION=view
fi

#Check to see that action is correct
if [ $ACTION != add ] && [ $ACTION != remove ] && [ $ACTION != view ]
then
	MESSAGE=$"Incorrect action."
	show_status
fi
#Check to see that TCPADDRESS is not blank
if [ $ACTION = add ]
then
	TCPADDRESS=$ADDTCPADDRESS
fi
if [ $ACTION = remove ]
then
	TCPADDRESS=$DELTCPADDRESS
	if [ $TCPADDRESS = $REMOTE_ADDR ]
	then
		MESSAGE=$"You cannot remove your own TCPIP address."
		show_status
	fi
fi
if [ $ACTION = add ] || [ $ACTION = remove ]
then
	#Check to see that PRIMARYADMIN is not blank
	if [ -z "$PRIMARYADMIN" ]
	then
		MESSAGE=$"The admin level must not be blank."
		show_status
	fi
	if [ -z "$TCPADDRESS" ]
	then
		MESSAGE=$"The TCPIP address must not be blank."
		show_status
	fi
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo "<div id="actionbox">"
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/remote_management_restrict.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/remote_management_restrict $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$TCPADDRESS:$TCPCOMMENT:$PRIMARYADMIN
EXEC_STATUS=`echo $?`
echo "</div>"
if [ $EXEC_STATUS = 100 ]
then
	MESSAGE=$"There was an error processing this request. Please view the Karoshi remote management logs."
	show_status
fi
if [ $EXEC_STATUS = 101 ]
then
	MESSAGE=$"The TCPIP address was already added."
	show_status
fi
if [ $EXEC_STATUS = 102 ]
then
	MESSAGE=$"The TCPIP address was not in the list."
	show_status
fi
if [ $EXEC_STATUS = 103 ]
then
	MESSAGE=$"The list is empty. All TCPIP addresses are allowed."
	show_status
fi
if [ $EXEC_STATUS = 104 ]
then
	view_tcpip
fi
echo "</div></body></html>"
exit
