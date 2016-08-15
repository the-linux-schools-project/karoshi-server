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
# _LOCKOUTDURATION_
# _LOCKOUTTHRESHOLD_
# _LOCKOUTOBS_
##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Default User Settings"'</title><meta http-equiv="REFRESH" content="0; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=28
#Assign LOCKOUTDURATION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = LOCKOUTDURATIONcheck ]
	then
		let COUNTER=$COUNTER+1
		LOCKOUTDURATION=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9'`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign LOCKOUTTHRESHOLD
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = LOCKOUTTHRESHOLDcheck ]
	then
		let COUNTER=$COUNTER+1
		LOCKOUTTHRESHOLD=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9'`
		break
	fi
	let COUNTER=$COUNTER+1
done
#Assign LOCKOUTOBS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = LOCKOUTOBScheck ]
	then
		let COUNTER=$COUNTER+1
		LOCKOUTOBS=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9'`
		break
	fi
	let COUNTER=$COUNTER+1
	done

#Assign MAXIMUMPASSWORDAGE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = MAXIMUMPASSWORDAGEcheck ]
	then
		let COUNTER=$COUNTER+1
		MAXIMUMPASSWORDAGE=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign USERNAMESTYLE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = USERNAMESTYLEcheck ]
	then
		let COUNTER=$COUNTER+1
		USERNAMESTYLE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign PASSWORDCOMPLEXITY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PASSWORDCOMPLEXITYcheck ]
	then
		let COUNTER=$COUNTER+1
		PASSWORDCOMPLEXITY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign MINPASSWORDLENGTH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = MINPASSWORDLENGTHcheck ]
	then
		let COUNTER=$COUNTER+1
		MINPASSWORDLENGTH=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign PASSWORDHISTORYLENGTH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PASSWORDHISTORYLENGTHcheck ]
	then
		let COUNTER=$COUNTER+1
		PASSWORDHISTORYLENGTH=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9'`
		break
	fi
	let COUNTER=$COUNTER+1
done


#Assign CHANGEPASSFIRSTLOGIN
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = CHANGEPASSFIRSTLOGINcheck ]
	then
		let COUNTER=$COUNTER+1
		CHANGEPASSFIRSTLOGIN=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign PASSWORDEXPIRY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PASSWORDEXPIRYcheck ]
	then
		let COUNTER=$COUNTER+1
		PASSWORDEXPIRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign HOMEDRIVE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = HOMEDRIVEcheck ]
	then
		let COUNTER=$COUNTER+1
		HOMEDRIVE=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Make sure that only numbers are entered
LOCKOUTDURATION=`echo $LOCKOUTDURATION | tr -cd '0-9\n'`
LOCKOUTTHRESHOLD=`echo $LOCKOUTTHRESHOLD | tr -cd '0-9\n'`
LOCKOUTOBS=`echo $LOCKOUTOBS | tr -cd '0-9\n'`
MAXIMUMPASSWORDAGE=`echo $MAXIMUMPASSWORDAGE | tr -cd '0-9\n'`

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><div class="sectiontitle">'$"Default User Settings"'</div><br>'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '</script>'
echo "</div></div></body></html>"
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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
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

#Check to see that LOCKOUTDURATION is not blank
if [ -z "$LOCKOUTDURATION" ]
then
	MESSAGE=$"The lockout duration cannot be blank."
	show_status
fi
#Check to see that LOCKOUTTHRESHOLD is not blank
if [ -z "$LOCKOUTTHRESHOLD" ]
then
	MESSAGE=$"The lockout threshold cannot be blank."
	show_status
fi
#Check to see that LOCKOUTOBS is not blank
if [ -z "$LOCKOUTOBS" ]
then
	MESSAGE=$"The lockout observation period cannot be blank."
	show_status
fi

#Check to see that PASSWORDHISTORYLENGTH is not blank
if [ -z "$PASSWORDHISTORYLENGTH" ]
then
	PASSWORDHISTORYLENGTH=24
fi

#Check that PASSWORDHISTORYLENGTH is between 0 and 24
if [ "$PASSWORDHISTORYLENGTH" -gt 24 ] || [ "$PASSWORDHISTORYLENGTH" -lt 0 ]
then
	MESSAGE=$"The password history length must be between 0 and 24."
	show_status
fi

#Check to see that PASSWORDCOMPLEXITYis not blank
if [ -z "$PASSWORDCOMPLEXITY" ]
then
	PASSWORDCOMPLEXITY=off
fi

#Make sure that password complexity is either on or off
if [ "$PASSWORDCOMPLEXITY" != on ] && [ "$PASSWORDCOMPLEXITY" != off ]
then
	MESSAGE=$"The password complexity must be either on or off."
	show_status
fi

#Check to see that PASSWORDEXPIRY is not blank
if [ -z "$PASSWORDEXPIRY" ]
then
	PASSWORDEXPIRY=yes
fi

#Make sure that PASSWORDEXPIRY is either yes or no
if [ "$PASSWORDEXPIRY" != yes ] && [ "$PASSWORDEXPIRY" != no ]
then
	MESSAGE=$"The password expiry must be either yes or no."
	show_status
fi

#Check to see that CHANGEPASSFIRSTLOGIN is not blank
if [ -z "$CHANGEPASSFIRSTLOGIN" ]
then
	CHANGEPASSFIRSTLOGIN=no
fi

#Check to see that MINPASSWORDLENGTH is not blank
if [ -z "$MINPASSWORDLENGTH" ]
then
	MINPASSWORDLENGTH=5
fi

#Check that MINPASSWORDLENGTH is between 0 and 14
if [ "$MINPASSWORDLENGTH" -gt 14 ] || [ "$PASSWORDHISTORYLENGTH" -lt 0 ]
then
	MESSAGE=$"The minimum password length must be between 0 and 14."
	show_status
fi

#Check to see that MAXIMUMPASSWORDAGE is not blank
if [ -z "$MAXIMUMPASSWORDAGE" ]
then
	MAXIMUMPASSWORDAGE=999
fi

#Check to see that USERNAMESTYLE is not blank
if [ -z "$USERNAMESTYLE" ]
then
	MESSAGE=$"The username style cannot be blank."
	show_status
fi

#Make sure that HOMEDRIVE is not already in use
if [ -z "$HOMEDRIVE" ]
then
	MESSAGE=$"The homedrive cannot be blank."
	show_status
fi

if [ `grep -r 'DRIVELETTER="'$HOMEDRIVE'"' /opt/karoshi/server_network/network_shares | wc -l` -gt 0 ]
then
	MESSAGE=''$"Home Drive"': '$HOMEDRIVE' - '$"This drive letter is already in use."''
	show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/default_user_settings.cgi | cut -d' ' -f1`
#Modify settings
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:SETDATA:$LOCKOUTDURATION:$LOCKOUTTHRESHOLD:$LOCKOUTOBS:$MAXIMUMPASSWORDAGE:$USERNAMESTYLE:$MINPASSWORDLENGTH:$PASSWORDCOMPLEXITY:$PASSWORDHISTORYLENGTH:$CHANGEPASSFIRSTLOGIN:$PASSWORDEXPIRY:$HOMEDRIVE:" | sudo -H /opt/karoshi/web_controls/exec/default_user_settings
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS != 0 ]
then
	MESSAGE=`echo $"There was a problem with this action." $"Please check the karoshi web administration logs for more details."`
	show_status
fi
exit
