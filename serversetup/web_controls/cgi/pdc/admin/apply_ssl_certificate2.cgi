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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Apply Self Signed SSL Certificate"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%+' | sed 's/___/TRIPLESCORED/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLESCORED/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=22
#Assign SERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERcheck ]
then
let COUNTER=$COUNTER+1
SERVER=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign COUNTRYCODE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = COUNTRYCODEcheck ]
then
let COUNTER=$COUNTER+1
COUNTRYCODE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign STATE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = STATEcheck ]
then
let COUNTER=$COUNTER+1
STATE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign LOCALITY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LOCALITYcheck ]
then
let COUNTER=$COUNTER+1
LOCALITY=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign INSTITUTENAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = INSTITUTENAMEcheck ]
then
let COUNTER=$COUNTER+1
INSTITUTENAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign DEPARTMENT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DEPARTMENTcheck ]
then
let COUNTER=$COUNTER+1
DEPARTMENT=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign COMMONNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = COMMONNAMEcheck ]
then
let COUNTER=$COUNTER+1
COMMONNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign EMAIL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = EMAILcheck ]
then
let COUNTER=$COUNTER+1
EMAIL=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%40/@/g' | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign EMAILCERT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = EMAILCERTcheck ]
then
let COUNTER=$COUNTER+1
EMAILCERT=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign WEBCERT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = WEBCERTcheck ]
then
let COUNTER=$COUNTER+1
WEBCERT=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign CERTTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CERTTYPEcheck ]
then
let COUNTER=$COUNTER+1
CERTTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/apply_ssl_certificate_fm.cgi";'
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
#Check to see that SERVER is not blank
if [ $SERVER'null' = null ]
then
MESSAGE=$"The server option cannot be blank."
show_status
fi

#Check to see that COUNTRYCODE is not blank
if [ $COUNTRYCODE'null' = null ]
then
MESSAGE=$"The country code option cannot be blank."
show_status
fi
#Check to see that STATE is not blank
if [ $STATE'null' = null ]
then
MESSAGE=$"The state option cannot be blank."
show_status
fi
#Check to see that LOCALITY is not blank
if [ $LOCALITY'null' = null ]
then
MESSAGE=$"The locality option cannot be blank."
show_status
fi
#Check to see that INSTITUTENAME is not blank
if [ $INSTITUTENAME'null' = null ]
then
MESSAGE=$"The institute name option cannot be blank."
show_status
fi
#Check to see that DEPARTMENT is not blank
if [ $DEPARTMENT'null' = null ]
then
MESSAGE=$"The department name cannot be blank."
show_status
fi
#Check to see that COMMONNAME is not blank
if [ $COMMONNAME'null' = null ]
then
MESSAGE=$"The common name option cannot be blank."
show_status
fi
#Check to see that EMAIL is not blank
if [ $EMAIL'null' = null ]
then
MESSAGE=$"The e-mail option cannot be blank."
show_status
fi

#Check to see that WEBCERT is not blank
if [ $WEBCERT'null' = null ]
then
MESSAGE=$"There was an error with the certificate option type."
show_status
fi

#Check to see that EMAILCERT is not blank
if [ $EMAILCERT'null' = null ]
then
MESSAGE=$"There was an error with the certificate option type."
show_status
fi

#Check to see that CERTTYPE is not blank
if [ $CERTTYPE'null' = null ]
then
MESSAGE=$"There was an error with the certificate option type."
show_status
fi

STATE=`echo $STATE | sed 's/+/ /g'`
LOCALITY=`echo $LOCALITY | sed 's/+/ /g'`
INSTITUTENAME=`echo $INSTITUTENAME | sed 's/+/ /g'`
DEPARTMENT=`echo $DEPARTMENT | sed 's/+/ /g'`
COMMONNAME=`echo $COMMONNAME | sed 's/+/ /g'`
EMAIL=`echo $EMAIL | sed 's/+/ /g'`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/apply_ssl_certificate2.cgi | cut -d' ' -f1`

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">'
if [ $WEBCERT = yes ]
then
echo "<b>"$SERVER - $"Web Certificate""</b><br><br>"
else
echo "<b>"$SERVER - $"E-mail Certificate""</b><br><br>"
fi

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVER:$COUNTRYCODE:$STATE:$LOCALITY:$INSTITUTENAME:$DEPARTMENT:$COMMONNAME:$EMAIL:$EMAILCERT:$WEBCERT:$CERTTYPE" | sudo -H /opt/karoshi/web_controls/exec/apply_ssl_certificate
STATUS=`echo $?`
if [ $STATUS = 101 ]
then
MESSAGE=$"There was a problem applying the certificate. Please check the Karoshi Web Management logs."
show_status
fi
if [ $STATUS = 102 ]
then
MESSAGE=$"SSH is not enabled for this server."
show_status
fi
MESSAGE=$"The SSL Certificate has been applied."
show_status
exit
