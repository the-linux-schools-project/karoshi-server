#!/bin/bash
#Copyright (C) 2010 Paul Sharrad
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
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/asset_register ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/asset_register
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`echo $QUERY_STRING | tr -cd 'A-Za-z0-9\._:\+-'`
#########################
#Assign data to variables
#########################
END_POINT=10
#Assign _CATEGORY_
COUNTER=1
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
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/asset_register/asset_register_view_fm.cgi";'
echo '</script>'
echo "</body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$ERRORMSG7
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
MESSAGE=$ERRORMSG8
show_status
fi
#Check to see that LOCATION is not blank
if [ $LOCATION'null' = null ]
then
MESSAGE=$ERRORMSG7
show_status
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">'

############################
#Database variables
############################
source /opt/karoshi/server_network/asset_register/config




echo '<b>'$TITLE2 $LOCATIONMSG - $LOCATION : $ASSETMSG - $CATEGORY'</b><br><br>'


#Get data


#Show data
ASSET_ID=1
#mysql -u $DBUSER -p$DBPASS $DBNAME -e 'SELECT location_id,description_id FROM '$DBNAME'.assets' 2>&1 | sed '1d'

function get_asset_data {

mysql -u $DBUSER -p$DBPASS $DBNAME -e 'SELECT assets.serial_number, categories.category, assets.purchase_date, assets.purchase_cost, descriptions.description, locations.location, assets.value, assets.assigned, suppliers.supplier, assets.tcpip1, assets.tcpip2, assets.tcpip3, assets.tcpip4 FROM asset_register.assets AS assets, asset_register.categories AS categories, asset_register.descriptions AS descriptions, asset_register.locations AS locations, asset_register.suppliers AS suppliers WHERE assets.category_id = categories.category_id AND assets.description_id = descriptions.description_id AND assets.location_id = locations.location_id AND assets.supplier_id = suppliers.supplier_id AND assets.asset_id = 1'
echo '<br>'

}
function get_asset_id_codes {
ASSET_ID_ARRAY=( `mysql -u $DBUSER -p$DBPASS $DBNAME -e 'SELECT asset_id FROM asset_register.assets AS assets' | sed '1d'` )
ASSET_ID_ARRAY_COUNT=`echo ${#ASSET_ID_ARRAY[@]}`
}

get_asset_id_codes


COUNTER=0
while [ $COUNTER -lt $ASSET_ID_ARRAY_COUNT ]
do
ASSET_ID=${ASSET_ID_ARRAY[$COUNTER]}
ASSET_DATA=`mysql -u $DBUSER -p$DBPASS $DBNAME -e 'SELECT assets.serial_number, categories.category, assets.purchase_date, assets.purchase_cost, descriptions.description, locations.location, assets.value, assets.assigned, suppliers.supplier, assets.tcpip1, assets.tcpip2, assets.tcpip3, assets.tcpip4 FROM asset_register.assets AS assets, asset_register.categories AS categories, asset_register.descriptions AS descriptions, asset_register.locations AS locations, asset_register.suppliers AS suppliers WHERE assets.category_id = categories.category_id AND assets.description_id = descriptions.description_id AND assets.location_id = locations.location_id AND assets.supplier_id = suppliers.supplier_id AND assets.asset_id = '$ASSET_ID'' | sed '1d' | sed 's/NULL//g'`
SERIAL=`echo -e "$ASSET_DATA" | cut -f1`
CATEGORY=`echo -e "$ASSET_DATA" | cut -f2`
PURCHASE_DATE=`echo -e "$ASSET_DATA" | cut -f3`
PURCHASE_COST=`echo -e "$ASSET_DATA" | cut -f4`
DESCRIPTION=`echo -e "$ASSET_DATA" | cut -f5`
LOCATION=`echo -e "$ASSET_DATA" | cut -f6`
VALUE=`echo -e "$ASSET_DATA" | cut -f7`
USERNAME=`echo -e "$ASSET_DATA" | cut -f8`
SUPPLIER=`echo -e "$ASSET_DATA" | cut -f9`
TCPIP1=`echo -e "$ASSET_DATA" | cut -f10`
TCPIP2=`echo -e "$ASSET_DATA" | cut -f11`
TCPIP3=`echo -e "$ASSET_DATA" | cut -f12`
TCPIP4=`echo -e "$ASSET_DATA" | cut -f13`
MAC1=`echo -e "$ASSET_DATA" | cut -f14`
MAC2=`echo -e "$ASSET_DATA" | cut -f15`
MAC3=`echo -e "$ASSET_DATA" | cut -f16`
MAC4=`echo -e "$ASSET_DATA" | cut -f17`

echo serial $SERIAL"<br>"
echo cat $CATEGORY"<br>"
echo date $PURCHASE_DATE"<br>"
echo cost $PURCHASE_COST"<br>"
echo desc $DESCRIPTION"<br>"
echo location $LOCATION"<br>"
echo value $VALUE"<br>"
echo assigned $USERNAME"<br>"
echo supplier $SUPPLIER"<br>"
echo tcpip1 $TCPIP1"<br>"
echo tcpip2 $TCPIP2"<br>"
echo tcpip3 $TCPIP3"<br>"
echo tcpip4 $TCPIP4"<br>"
echo mac1 $MAC1"<br>"
echo mac2 $MAC2"<br>"
echo mac3 $MAC3"<br>"
echo mac4 $MAC4"<br>"
echo "<br>"
let COUNTER=$COUNTER+1
done

# <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$USERHELP1'</span></a>




echo "</div>"
echo "</body></html>"
exit
