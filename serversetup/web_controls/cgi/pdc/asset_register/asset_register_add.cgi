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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/asset_register ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/asset_register
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><meta http-equiv="REFRESH" content="100; URL='$HTTP_REFERER'"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js\" type="text/javascript\"></script></head><body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\+%-'`
#########################
#Assign data to variables
#########################
END_POINT=36
#Assign _CATEGORY_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CATEGORYcheck ]
then
let COUNTER=$COUNTER+1
CATEGORY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _LOCATION_
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
#Assign _TCPIP1_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPIP1check ]
then
let COUNTER=$COUNTER+1
TCPIP1=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9.\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _TCPIP2_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPIP2check ]
then
let COUNTER=$COUNTER+1
TCPIP2=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9.\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _TCPIP3_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPIP3check ]
then
let COUNTER=$COUNTER+1
TCPIP3=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9.\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _TCPIP4_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPIP4check ]
then
let COUNTER=$COUNTER+1
TCPIP4=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9.\n'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _MACADDRESS1_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MACADDRESS1check ]
then
let COUNTER=$COUNTER+1
MACADDRESS1=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _MACADDRESS2_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MACADDRESS2check ]
then
let COUNTER=$COUNTER+1
MACADDRESS2=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _MACADDRESS3_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MACADDRESS3check ]
then
let COUNTER=$COUNTER+1
MACADDRESS3=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _MACADDRESS4_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MACADDRESS4check ]
then
let COUNTER=$COUNTER+1
MACADDRESS4=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign _SERIALKEY_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERIALKEYcheck ]
then
let COUNTER=$COUNTER+1
SERIALKEY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _PURCHASEDATE_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DATEcheck ]
then
let COUNTER=$COUNTER+1
DATE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _IDENTITY_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = IDENTITYcheck ]
then
let COUNTER=$COUNTER+1
IDENTITY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _DESCRIPTION_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DESCRIPTIONcheck ]
then
let COUNTER=$COUNTER+1
DESCRIPTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign _USERNAME_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
then
let COUNTER=$COUNTER+1
USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign _VALUE_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = VALUEcheck ]
then
let COUNTER=$COUNTER+1
VALUE=`echo $DATA | cut -s -d'_' -f$COUNTER  | tr -cd '0-9'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign _SUPPLIER_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SUPPLIERcheck ]
then
let COUNTER=$COUNTER+1
SUPPLIER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign _BUDGET_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = BUDGETcheck ]
then
let COUNTER=$COUNTER+1
BUDGET=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {

echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/asset_register/asset_register_add_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
show_status
fi
#########################
#Check user accessing this script
#########################
#if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
#then
#MESSAGE=$ACCESS_ERROR1
#show_status
#fi

#if [ `grep -c $REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
#then
#MESSAGE=$ACCESS_ERROR1
#show_status
#fi
#########################
#Check data
#########################
#Check to see that CATEGORY is not blank
if [ $CATEGORY'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that LOCATION is not blank
if [ $LOCATION'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that TCPIP number has correct dots
if [ $TCPIP1'null' != null ]
then
if [ `echo $TCPIP1 | sed 's/\./\n/g'  | sed /^$/d | wc -l` != 4 ]
then
MESSAGE=$ERRORMSG3
show_status
fi
fi
#Check to see that MAC address has correct colons
if [ $MACADDRESS1 != N.A. ]
then
if [ `echo $MACADDRESS1 | sed 's/%3A/\n/g'  | sed /^$/d | wc -l` != 6 ]
then
MESSAGE=$ERRORMSG4
show_status
fi
fi

#Add asset to the database

source /opt/karoshi/server_network/asset_register/config

mysql -u $DBUSER -p$DBPASS $DBNAME -e 'INSERT INTO '$DBNAME'.assets (category_id, location_id, description_id, supplier_id, budget_id, tcpip1, tcpip2, tcpip3, tcpip4, purchase_date, identity, serial_number, assigned, purchase_cost, mac1, mac2, mac3, mac4) VALUES ("'$CATEGORY'", "'$LOCATION'", "'$DESCRIPTION'", "'$SUPPLIER'", "'$BUDGET'", "'$TCPIP1'", "'$TCPIP2'", "'$TCPIP3'", "'$TCPIP4'", "'$DATE'", "'$IDENTITY'", "'$SERIALKEY'", "'$USERNAME'", "'$VALUE'", "'$MACADDRESS1'", "'$MACADDRESS2'", "'$MACADDRESS3'", "'$MACADDRESS4'")' 2>&1

MESSAGE=$COMPLETEDMSG
show_status
exit

