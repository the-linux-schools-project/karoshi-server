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
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
DATE_INFO=`date +%F`
DAY=`echo $DATE_INFO | cut -d- -f3`
MONTH=`echo $DATE_INFO | cut -d- -f2`
YEAR=`echo $DATE_INFO | cut -d- -f1`
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

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
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Create Order"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script language="JavaScript" src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) -->
<link rel="stylesheet" href="/all/calendar2/calendar.css">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=9
#Assign DATE
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

#Assign ORDERNO
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ORDERNOcheck ]
then
let COUNTER=$COUNTER+1
ORDERNO=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign PERSON
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PERSONcheck ]
then
let COUNTER=$COUNTER+1
PERSON=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign BUDGET
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

#Assign SUPPLIER
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

#Assign PANDP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PANDPcheck ]
then
let COUNTER=$COUNTER+1
PANDP=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign NEWITEM
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = NEWITEMcheck ]
then
let COUNTER=$COUNTER+1
NEWITEM=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign QUANTITY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = QUANTITYcheck ]
then
let COUNTER=$COUNTER+1
QUANTITY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign UNITCOST
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = UNITCOSTcheck ]
then
let COUNTER=$COUNTER+1
UNITCOST=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/helpdesk_create_order.cgi" name="testform" method="post"><div id="actionbox"><div class="sectiontitle">'$"Create Order"'</div><br>'$DATA''

#Show calendar
echo "<table class=\"standard\" style=\"text-align: left; width: 100%;\" border=\"0\" cellpadding=\"2\" cellspacing=\"2\"><tr><td>$"Date"</td><td>
<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$DAY-$MONTH-$YEAR\" size=14 maxsize=10 name=\"_DATE_\" />
	<script language=\"JavaScript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script></td><td>$"Order Number"</td><td><input tabindex= \"1\" name=\"_ORDERNO_\" size=\"14\" type=\"text\"></td></tr><tr><td>$"Person"</td><td><input tabindex= \"1\" name=\"_PERSON_\" size=\"14\" type=\"text\"></td><td>$"Budget"</td><td><input tabindex= \"1\" name=\"_BUDGET_\" size=\"14\" type=\"text\"></td></tr><tr><td>$"Supplier"</td><td><input tabindex= \"1\" name=\"_SUPPLIER_\" size=\"14\" type=\"text\"></td><td>$"Post and Packaging"</td><td><input tabindex= \"1\" name=\"_PANDP_\" size=\"14\" type=\"text\"></td></tr><tr><td></td><td></td><td>$TOTALMSG</td><td><b>$TOTAL</b></td></tr></tbody></table>"


echo '<table class="standard" style="text-align: left; width: 100%;" ><tbody>
<tr><td style="vertical-align: top;">'$"Add item"'</td>
<td style="vertical-align: top; width: 80px;">'$"Quantity"'</td>
<td style="vertical-align: top; width: 80px;">Unit Price</td>
<td style="vertical-align: top; width: 80px;"></td></tr>
<tr><td><input tabindex= "2" name="_NEWITEM_" size="60" type="text"></td>
<td><input tabindex= "3" name="_QUANTITY_" size="4" type="text"></td>
<td><input tabindex= "4" name="_UNITCOST_" size="6" type="text"></td><td><input type="image" title="add" src="/images/submenus/user/helpdesk/add.png" name="_ADD_"></td></tr></tbody></table></form>

</div>
</div></body>
</html>
'
exit
