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
#Database variables
############################
source /opt/karoshi/server_network/asset_register/config
############################
#Show page
############################
echo "Content-type: text/html"
echo ""

echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><script language="JavaScript" type="text/javascript" src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) --><link rel="stylesheet" href="/all/calendar2/calendar.css"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head><body>'


#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/asset_register_add.cgi";'
echo '</script>'
echo "</body></html>"
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
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

DATE_INFO=`date +%F`
DAY=`echo $DATE_INFO | cut -d- -f3`
MONTH=`echo $DATE_INFO | cut -d- -f2`
YEAR=`echo $DATE_INFO | cut -d- -f1`

echo '<form action="/cgi-bin/asset_register/asset_register_add.cgi" name="testform" method="post"><div id="actionbox"><b>'$TITLE1'</b><br><br>'
###############################
#Categories
###############################
echo '<table style="text-align: left;" border="0" cellpadding="2" cellspacing="2" class="standard"><tbody><tr><td style="width: 180px;">'$ASSETTYPEMSG'</td><td>'

echo '<select name="_CATEGORY_" style="width: 185px;">'
CATEGORIES=`mysql -u $DBUSER -p$DBPASS $DBNAME -e 'SELECT category_id, category FROM '$DBNAME'.categories'`
echo -e "$CATEGORIES" | sed 's/^/<option value="/g' | sed 's/\t/">/g' | sed 's/$/<\/option>/g' | sed '1d'
echo '</select></td>'

#Asset Purchase date
echo '<td style="width: 30px;"></td><td style="width: 180px;">'$PURCHASEDATE'</td><td>'


echo "	<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$DAY-$MONTH-$YEAR\" size=20 maxlength=10 name=\"_DATE_\"></td><td style=\"vertical-align: top; text-align: center;\">
	<script type=\"text/javascript\" language=\"JavaScript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script></tr>"


###############################
#Location
###############################

echo '<tr><td><a href="/cgi-bin/admin/locations.cgi">'$LOCATIONMSG'</a></td><td>'

echo '<select name="_LOCATION_" style="width: 185px;">'
LOCATIONS=`mysql -u $DBUSER -p$DBPASS $DBNAME -e 'SELECT location_id, location FROM '$DBNAME'.locations'`
echo -e "$LOCATIONS" | sed 's/^/<option value="/g' | sed 's/\t/">/g' | sed 's/$/<\/option>/g' | sed '1d'
echo '</select>'

#Identifying name
echo '<td></td><td>'$IDENTITYNAME'</td><td><input size="20" name="_IDENTITY_" value="N.A."></td></tr>'

#Description
echo '<tr><td><a href="/cgi-bin/admin/asset_register_add_description_fm.cgi">'$DESCRIPTION'</a></td><td>'

echo '<select name="_DESCRIPTION_" style="width: 185px;">'
DESCRIPTIONS=`mysql -u $DBUSER -p$DBPASS $DBNAME -e 'SELECT description_id, description FROM '$DBNAME'.descriptions'`
echo -e "$DESCRIPTIONS" | sed 's/^/<option value="/g' | sed 's/\t/">/g' | sed 's/$/<\/option>/g' | sed '1d'
echo '</select></td>'

#Serial Code
echo '<td></td><td>'$SERIALKEY'</td><td><input size="20" name="_SERIALKEY_" value="N.A."></td></tr>'

#Supplier
echo '<tr><td><a href="/cgi-bin/admin/asset_register_add_supplier_fm.cgi">'$SUPPLIERMSG'</a></td><td>'
echo '<select name="_SUPPLIER_" style="width: 185px;">'
SUPPLIERS=`mysql -u $DBUSER -p$DBPASS $DBNAME -e 'SELECT supplier_id, supplier FROM '$DBNAME'.suppliers'`
echo -e "$SUPPLIERS" | sed 's/^/<option value="/g' | sed 's/\t/">/g' | sed 's/$/<\/option>/g' | sed '1d'
echo '</select></td>'

#Assigned to
echo '<td></td><td>'$USERNAME'</td><td><input size="20" name="_USERNAME_" value="N.A."></td></tr>'

#Budget
echo '<tr><td><a href="/cgi-bin/admin/asset_register_add_budget_fm.cgi">'$BUDGETMSG'</a></td><td>'
echo '<select name="_BUDGET_" style="width: 185px;">'
BUDGETS=`mysql -u $DBUSER -p$DBPASS $DBNAME -e 'SELECT budget_id, budget FROM '$DBNAME'.budgets'`
echo -e "$BUDGETS" | sed 's/^/<option value="/g' | sed 's/\t/">/g' | sed 's/$/<\/option>/g' | sed '1d'
echo '</select></td>'


#Value
echo '<td></td><td>'$VALUEMSG'</td><td><input size="20" name="_VALUE_" value="N.A."></td></tr>'





echo '<td>'$TCPIP'</td><td><input maxlength="15" size="20" name="_TCPIP1_" value=""></td><td></td><td>'$MACADDRESS'</td><td><input maxlength="17" size="20" name="_MACADDRESS1_" value=""></td></tr>
<td></td><td><input maxlength="15" size="20" name="_TCPIP2_" value=""></td><td></td><td></td><td><input maxlength="20" size="20" name="_MACADDRESS2_" value=""></td></tr>
<td></td><td><input maxlength="15" size="20" name="_TCPIP3_" value=""></td><td></td><td></td><td><input maxlength="20" size="20" name="_MACADDRESS3_" value=""></td></tr>
<td></td><td><input maxlength="15" size="20" name="_TCPIP4_" value=""></td><td></td><td></td><td><input maxlength="20" size="20" name="_MACADDRESS4_" value=""></td></tr>

'

echo '</tbody></table>'

echo "</div>"
echo '<div id="submitbox"><input value="Submit" type="submit"> <input value="Reset" type="reset"></div>'
echo '</form></body></html>'
exit

