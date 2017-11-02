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
DATE=`echo $DAY-$MONTH-$YEAR`
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
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script language="JavaScript" src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) -->

<link rel="stylesheet" href="/all/calendar2/calendar.css">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+' | sed 's/+/ /g' | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORED/g' | sed 's/TRIPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
#Assign _DEPARTMENT_
DEPARTMENT=`echo $DATA | cut -s -d'_' -f3 | sed 's/UNDERSCORED/_/g'`
DATE1=`echo $DATA | cut -s -d'_' -f5`
[ $DATE1'null' != null ] && DATE=$DATE1
SUPPLIER=`echo $DATA | cut -s -d'_' -f7 | sed 's/UNDERSCORED/_/g'`
BHOLDER=`echo $DATA | cut -s -d'_' -f9 | sed 's/UNDERSCORED/_/g'`
REF1=`echo $DATA | cut -s -d'_' -f11 | sed 's/UNDERSCORED/_/g'`
QUANTITY1=`echo $DATA | cut -s -d'_' -f13 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC1=`echo $DATA | cut -s -d'_' -f15 | sed 's/UNDERSCORED/_/g'`
PPU1=`echo $DATA | cut -s -d'_' -f17 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF2=`echo $DATA | cut -s -d'_' -f19 | sed 's/UNDERSCORED/_/g'`
QUANTITY2=`echo $DATA | cut -s -d'_' -f21 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC2=`echo $DATA | cut -s -d'_' -f23 | sed 's/UNDERSCORED/_/g'`
PPU2=`echo $DATA | cut -s -d'_' -f25 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF3=`echo $DATA | cut -s -d'_' -f27 | sed 's/UNDERSCORED/_/g'`
QUANTITY3=`echo $DATA | cut -s -d'_' -f29 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC3=`echo $DATA | cut -s -d'_' -f31 | sed 's/UNDERSCORED/_/g'`
PPU3=`echo $DATA | cut -s -d'_' -f33 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF4=`echo $DATA | cut -s -d'_' -f35 | sed 's/UNDERSCORED/_/g'`
QUANTITY4=`echo $DATA | cut -s -d'_' -f37 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC4=`echo $DATA | cut -s -d'_' -f39 | sed 's/UNDERSCORED/_/g'`
PPU4=`echo $DATA | cut -s -d'_' -f41 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF5=`echo $DATA | cut -s -d'_' -f43 | sed 's/UNDERSCORED/_/g'`
QUANTITY5=`echo $DATA | cut -s -d'_' -f45 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC5=`echo $DATA | cut -s -d'_' -f47 | sed 's/UNDERSCORED/_/g'`
PPU5=`echo $DATA | cut -s -d'_' -f49 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF6=`echo $DATA | cut -s -d'_' -f51 | sed 's/UNDERSCORED/_/g'`
QUANTITY6=`echo $DATA | cut -s -d'_' -f53 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC6=`echo $DATA | cut -s -d'_' -f55 | sed 's/UNDERSCORED/_/g'`
PPU6=`echo $DATA | cut -s -d'_' -f57 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF7=`echo $DATA | cut -s -d'_' -f59 | sed 's/UNDERSCORED/_/g'`
QUANTITY7=`echo $DATA | cut -s -d'_' -f61 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC7=`echo $DATA | cut -s -d'_' -f63 | sed 's/UNDERSCORED/_/g'`
PPU7=`echo $DATA | cut -s -d'_' -f65 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF8=`echo $DATA | cut -s -d'_' -f67 | sed 's/UNDERSCORED/_/g'`
QUANTITY8=`echo $DATA | cut -s -d'_' -f69 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC8=`echo $DATA | cut -s -d'_' -f71 | sed 's/UNDERSCORED/_/g'`
PPU8=`echo $DATA | cut -s -d'_' -f73 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF9=`echo $DATA | cut -s -d'_' -f75 | sed 's/UNDERSCORED/_/g'`
QUANTITY9=`echo $DATA | cut -s -d'_' -f77 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC9=`echo $DATA | cut -s -d'_' -f79 | sed 's/UNDERSCORED/_/g'`
PPU9=`echo $DATA | cut -s -d'_' -f81 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF10=`echo $DATA | cut -s -d'_' -f83 | sed 's/UNDERSCORED/_/g'`
QUANTITY10=`echo $DATA | cut -s -d'_' -f85 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC10=`echo $DATA | cut -s -d'_' -f87 | sed 's/UNDERSCORED/_/g'`
PPU10=`echo $DATA | cut -s -d'_' -f89 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF11=`echo $DATA | cut -s -d'_' -f91 | sed 's/UNDERSCORED/_/g'`
QUANTITY11=`echo $DATA | cut -s -d'_' -f93 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC11=`echo $DATA | cut -s -d'_' -f95 | sed 's/UNDERSCORED/_/g'`
PPU11=`echo $DATA | cut -s -d'_' -f97 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF12=`echo $DATA | cut -s -d'_' -f99 | sed 's/UNDERSCORED/_/g'`
QUANTITY12=`echo $DATA | cut -s -d'_' -f101 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC12=`echo $DATA | cut -s -d'_' -f103 | sed 's/UNDERSCORED/_/g'`
PPU12=`echo $DATA | cut -s -d'_' -f105 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF13=`echo $DATA | cut -s -d'_' -f107 | sed 's/UNDERSCORED/_/g'`
QUANTITY13=`echo $DATA | cut -s -d'_' -f109 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC13=`echo $DATA | cut -s -d'_' -f111 | sed 's/UNDERSCORED/_/g'`
PPU13=`echo $DATA | cut -s -d'_' -f113 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF14=`echo $DATA | cut -s -d'_' -f115 | sed 's/UNDERSCORED/_/g'`
QUANTITY14=`echo $DATA | cut -s -d'_' -f117 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC14=`echo $DATA | cut -s -d'_' -f119 | sed 's/UNDERSCORED/_/g'`
PPU14=`echo $DATA | cut -s -d'_' -f121 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF15=`echo $DATA | cut -s -d'_' -f123 | sed 's/UNDERSCORED/_/g'`
QUANTITY15=`echo $DATA | cut -s -d'_' -f125 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9'`
DESC15=`echo $DATA | cut -s -d'_' -f127 | sed 's/UNDERSCORED/_/g'`
PPU15=`echo $DATA | cut -s -d'_' -f129 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
PANDP=`echo $DATA | cut -s -d'_' -f131 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
GRANDTOTAL=0

[ $PPU1'null' != null ] && PPU1=`echo "scale=2; ${PPU1} / 1" | bc`
[ $PPU2'null' != null ] && PPU2=`echo "scale=2; ${PPU2} / 1" | bc`
[ $PPU3'null' != null ] && PPU3=`echo "scale=2; ${PPU3} / 1" | bc`
[ $PPU4'null' != null ] && PPU4=`echo "scale=2; ${PPU4} / 1" | bc`
[ $PPU5'null' != null ] && PPU5=`echo "scale=2; ${PPU5} / 1" | bc`
[ $PPU6'null' != null ] && PPU6=`echo "scale=2; ${PPU6} / 1" | bc`
[ $PPU7'null' != null ] && PPU7=`echo "scale=2; ${PPU7} / 1" | bc`
[ $PPU8'null' != null ] && PPU8=`echo "scale=2; ${PPU8} / 1" | bc`
[ $PPU9'null' != null ] && PPU9=`echo "scale=2; ${PPU9} / 1" | bc`
[ $PPU10'null' != null ] && PPU10=`echo "scale=2; ${PPU10} / 1" | bc`
[ $PPU11'null' != null ] && PPU11=`echo "scale=2; ${PPU11} / 1" | bc`
[ $PPU12'null' != null ] && PPU12=`echo "scale=2; ${PPU12} / 1" | bc`
[ $PPU13'null' != null ] && PPU13=`echo "scale=2; ${PPU13} / 1" | bc`
[ $PPU14'null' != null ] && PPU14=`echo "scale=2; ${PPU14} / 1" | bc`
[ $PPU15'null' != null ] && PPU15=`echo "scale=2; ${PPU15} / 1" | bc`
[ $PANDP'null' != null ] && PANDP=`echo "scale=2; ${PANDP} / 1" | bc`


if [ $QUANTITY1'null' != null ] && [ $PPU1'null' != null ]
then
TOTAL1=`echo "$QUANTITY1 * $PPU1" | bc`
GRANDTOTAL=`echo "$TOTAL1 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY2'null' != null ] && [ $PPU2'null' != null ]
then
TOTAL2=`echo "$QUANTITY2 * $PPU2" | bc`
GRANDTOTAL=`echo "$TOTAL2 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY3'null' != null ] && [ $PPU3'null' != null ]
then
TOTAL3=`echo "$QUANTITY3 * $PPU3" | bc`
GRANDTOTAL=`echo "$TOTAL3 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY4'null' != null ] && [ $PPU4'null' != null ]
then
TOTAL4=`echo "$QUANTITY4 * $PPU4" | bc`
GRANDTOTAL=`echo "$TOTAL4 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY5'null' != null ] && [ $PPU5'null' != null ]
then
TOTAL5=`echo "$QUANTITY5 * $PPU5" | bc`
GRANDTOTAL=`echo "$TOTAL5 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY6'null' != null ] && [ $PPU6'null' != null ]
then
TOTAL6=`echo "$QUANTITY6 * $PPU6" | bc`
GRANDTOTAL=`echo "$TOTAL6 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY7'null' != null ] && [ $PPU7'null' != null ]
then
TOTAL7=`echo "$QUANTITY7 * $PPU7" | bc`
GRANDTOTAL=`echo "$TOTAL7 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY8'null' != null ] && [ $PPU8'null' != null ]
then
TOTAL8=`echo "$QUANTITY8 * $PPU8" | bc`
GRANDTOTAL=`echo "$TOTAL8 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY9'null' != null ] && [ $PPU9'null' != null ]
then
TOTAL9=`echo "$QUANTITY9 * $PPU9" | bc`
GRANDTOTAL=`echo "$TOTAL9 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY10'null' != null ] && [ $PPU10'null' != null ]
then
TOTAL10=`echo "$QUANTITY10 * $PPU10" | bc`
GRANDTOTAL=`echo "$TOTAL10 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY11'null' != null ] && [ $PPU11'null' != null ]
then
TOTAL11=`echo "$QUANTITY11 * $PPU11" | bc`
GRANDTOTAL=`echo "$TOTAL11 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY12'null' != null ] && [ $PPU12'null' != null ]
then
TOTAL12=`echo "$QUANTITY12 * $PPU12" | bc`
GRANDTOTAL=`echo "$TOTAL12 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY13'null' != null ] && [ $PPU13'null' != null ]
then
TOTAL13=`echo "$QUANTITY13 * $PPU13" | bc`
GRANDTOTAL=`echo "$TOTAL13 + $GRANDTOTAL" | bc`
fi
if [ $QUANTITY14'null' != null ] && [ $PPU14'null' != null ]
then
TOTAL14=`echo "$QUANTITY14 * $PPU14" | bc`
fi
if [ $QUANTITY15'null' != null ] && [ $PPU15'null' != null ]
then
TOTAL15=`echo "$QUANTITY15 * $PPU15" | bc`
GRANDTOTAL=`echo "$TOTAL15 + $GRANDTOTAL" | bc`
fi
SUBTOTAL=$GRANDTOTAL
if [ $PANDP'null' != null ]
then
GRANDTOTAL=`echo "$PANDP + $GRANDTOTAL" | bc`
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><form name="testform" action="/cgi-bin/admin/orders_create_fm.cgi" method="post">
<table class="standard" style="text-align: left;" >
    <tbody>
<tr><td style="width: 90px;"><b>'$"Department"'</b></td><td style="width: 300px;"><input value="'$DEPARTMENT'" maxlength="20" size="20" name="___DEPARTMENT___"></td><td style="width: 120px;"><b>'$"Date"'</b></td><td style="width: 200px;">'

echo "
<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$DATE\" size=14 maxsize=10 name=\"___DATE___\" />
	<script language=\"JavaScript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '___DATE___'
	});

	</script></td></tr>"


echo '</td></tr>
<tr><td><b>'$"Supplier"'</b></td><td><input value="'$SUPPLIER'" maxlength="20" size="20" name="___SUPPLIER___"></td><td><b>'$"Budget Holder"'</b></td><td><input value="'$BHOLDER'" maxlength="16" size="16" name="___BHOLDER___"></td></tr></tbody></table><br>
  <table class="standard" style="text-align: left;" >
    <tbody>
<tr><td><b>'$"Ref"'</b></td><td><b>'$"Qty"'</b></td><td><b>'$"Description"'</b></td><td><b>'$"Unit Price"'</b></td><td><b>'$"Total"'</b></td></tr>
<tr><td><input value="'$REF1'" maxlength="20" size="20" name="___REF1___"></td><td><input value="'$QUANTITY1'" maxlength="4" size="4" name="___QUANTITY1___"></td><td><input value="'$DESC1'" maxlength="30" size="30" name="___DESC1___"></td><td><input value="'$PPU1'" maxlength="8" size="8" name="___PPU1___"></td><td>'$TOTAL1'</td></tr>
<tr><td><input value="'$REF2'" maxlength="20" size="20" name="___REF2___"></td><td><input value="'$QUANTITY2'" maxlength="4" size="4" name="___QUANTITY2___"></td><td><input value="'$DESC2'" maxlength="30" size="30" name="___DESC2___"></td><td><input value="'$PPU2'" maxlength="8" size="8" name="___PPU2___"></td><td>'$TOTAL2'</td></tr>
<tr><td><input value="'$REF3'" maxlength="20" size="20" name="___REF3___"></td><td><input value="'$QUANTITY3'" maxlength="4" size="4" name="___QUANTITY3___"></td><td><input value="'$DESC3'" maxlength="30" size="30" name="___DESC3___"></td><td><input value="'$PPU3'" maxlength="8" size="8" name="___PPU3___"></td><td>'$TOTAL3'</td></tr>
<tr><td><input value="'$REF4'" maxlength="20" size="20" name="___REF4___"></td><td><input value="'$QUANTITY4'" maxlength="4" size="4" name="___QUANTITY4___"></td><td><input value="'$DESC4'" maxlength="30" size="30" name="___DESC4___"></td><td><input value="'$PPU4'" maxlength="8" size="8" name="___PPU4___"></td><td>'$TOTAL4'</td></tr>
<tr><td><input value="'$REF5'" maxlength="20" size="20" name="___REF5___"></td><td><input value="'$QUANTITY5'" maxlength="4" size="4" name="___QUANTITY5___"></td><td><input value="'$DESC5'" maxlength="30" size="30" name="___DESC5___"></td><td><input value="'$PPU5'" maxlength="8" size="8" name="___PPU5___"></td><td>'$TOTAL5'</td></tr>
<tr><td><input value="'$REF6'" maxlength="20" size="20" name="___REF6___"></td><td><input value="'$QUANTITY6'" maxlength="4" size="4" name="___QUANTITY6___"></td><td><input value="'$DESC6'" maxlength="30" size="30" name="___DESC6___"></td><td><input value="'$PPU6'" maxlength="8" size="8" name="___PPU6___"></td><td>'$TOTAL6'</td></tr>
<tr><td><input value="'$REF7'" maxlength="20" size="20" name="___REF7___"></td><td><input value="'$QUANTITY7'" maxlength="4" size="4" name="___QUANTITY7___"></td><td><input value="'$DESC7'" maxlength="30" size="30" name="___DESC7___"></td><td><input value="'$PPU7'" maxlength="8" size="8" name="___PPU7___"></td><td>'$TOTAL7'</td></tr>
<tr><td><input value="'$REF8'" maxlength="20" size="20" name="___REF8___"></td><td><input value="'$QUANTITY8'" maxlength="4" size="4" name="___QUANTITY8___"></td><td><input value="'$DESC8'" maxlength="30" size="30" name="___DESC8___"></td><td><input value="'$PPU8'" maxlength="8" size="8" name="___PPU8___"></td><td>'$TOTAL8'</td></tr>
<tr><td><input value="'$REF9'" maxlength="20" size="20" name="___REF9___"></td><td><input value="'$QUANTITY9'" maxlength="4" size="4" name="___QUANTITY9___"></td><td><input value="'$DESC9'" maxlength="30" size="30" name="___DESC9___"></td><td><input value="'$PPU9'" maxlength="8" size="8" name="___PPU9___"></td><td>'$TOTAL9'</td></tr>
<tr><td><input value="'$REF10'" maxlength="20" size="20" name="___REF10___"></td><td><input value="'$QUANTITY10'" maxlength="4" size="4" name="___QUANTITY10___"></td><td><input value="'$DESC10'" maxlength="30" size="30" name="___DESC10___"></td><td><input value="'$PPU10'" maxlength="8" size="8" name="___PPU10___"></td><td>'$TOTAL10'</td></tr>
<tr><td><input value="'$REF11'" maxlength="20" size="20" name="___REF11___"></td><td><input value="'$QUANTITY11'" maxlength="4" size="4" name="___QUANTITY11___"></td><td><input value="'$DESC11'" maxlength="30" size="30" name="___DESC11___"></td><td><input value="'$PPU11'" maxlength="8" size="8" name="___PPU11___"></td><td>'$TOTAL11'</td></tr>
<tr><td><input value="'$REF12'" maxlength="20" size="20" name="___REF12___"></td><td><input value="'$QUANTITY12'" maxlength="4" size="4" name="___QUANTITY12___"></td><td><input value="'$DESC12'" maxlength="30" size="30" name="___DESC12___"></td><td><input value="'$PPU12'" maxlength="8" size="8" name="___PPU12___"></td><td>'$TOTAL12'</td></tr>
<tr><td><input value="'$REF13'" maxlength="20" size="20" name="___REF13___"></td><td><input value="'$QUANTITY13'" maxlength="4" size="4" name="___QUANTITY13___"></td><td><input value="'$DESC13'" maxlength="30" size="30" name="___DESC13___"></td><td><input value="'$PPU13'" maxlength="8" size="8" name="___PPU13___"></td><td>'$TOTAL13'</td></tr>
<tr><td><input value="'$REF14'" maxlength="20" size="20" name="___REF14___"></td><td><input value="'$QUANTITY14'" maxlength="4" size="4" name="___QUANTITY14___"></td><td><input value="'$DESC14'" maxlength="30" size="30" name="___DESC14___"></td><td><input value="'$PPU14'" maxlength="8" size="8" name="___PPU14___"></td><td>'$TOTAL14'</td></tr>
<tr><td><input value="'$REF15'" maxlength="20" size="20" name="___REF15___"></td><td><input value="'$QUANTITY15'" maxlength="4" size="4" name="___QUANTITY15___"></td><td><input value="'$DESC15'" maxlength="30" size="30" name="___DESC15___"></td><td><input value="'$PPU15'" maxlength="8" size="8" name="___PPU15___"></td><td>'$TOTAL15'</td></tr>

<tr><td></td><td></td><td></td><td><b>'$"Subtotal"'</b></td><td>'$SUBTOTAL'</td></tr>
<tr><td></td><td></td><td></td><td><b>P+P</b></td><td><input value="'$PANDP'" maxlength="4" size="4" name="___PANDP___"></td></tr>
<tr><td></td><td></td><td></td><td><b>Total</b></td><td><b>'$GRANDTOTAL'</b></td></tr>
</tbody></table><br>
<input value="'$"Calculate"'" type="submit"> </form><form action="/cgi-bin/admin/orders_create.cgi" method="post">
<input name="___DEPARTMENT___" value="'$DEPARTMENT'" type="hidden">
<input name="___DATE___" value="'$DATE'" type="hidden">
<input name="___SUPPLIER___" value="'$SUPPLIER'" type="hidden">
<input name="___BHOLDER___" value="'$BHOLDER'" type="hidden">

<input name="___REF1___" value="'$REF1'" type="hidden">
<input name="___QUANTITY1___" value="'$QUANTITY1'" type="hidden">
<input name="___DESC1___" value="'$DESC1'" type="hidden">
<input name="___PPU1___" value="'$PPU1'" type="hidden">
<input name="___REF2___" value="'$REF2'" type="hidden">
<input name="___QUANTITY2___" value="'$QUANTITY2'" type="hidden">
<input name="___DESC2___" value="'$DESC2'" type="hidden">
<input name="___PPU2___" value="'$PPU2'" type="hidden">
<input name="___REF3___" value="'$REF3'" type="hidden">
<input name="___QUANTITY3___" value="'$QUANTITY3'" type="hidden">
<input name="___DESC3___" value="'$DESC3'" type="hidden">
<input name="___PPU3___" value="'$PPU3'" type="hidden">
<input name="___REF4___" value="'$REF4'" type="hidden">
<input name="___QUANTITY4___" value="'$QUANTITY4'" type="hidden">
<input name="___DESC4___" value="'$DESC4'" type="hidden">
<input name="___PPU4___" value="'$PPU4'" type="hidden">
<input name="___REF5___" value="'$REF5'" type="hidden">
<input name="___QUANTITY5___" value="'$QUANTITY5'" type="hidden">
<input name="___DESC5___" value="'$DESC5'" type="hidden">
<input name="___PPU5___" value="'$PPU5'" type="hidden">
<input name="___REF6___" value="'$REF6'" type="hidden">
<input name="___QUANTITY6___" value="'$QUANTITY6'" type="hidden">
<input name="___DESC6___" value="'$DESC6'" type="hidden">
<input name="___PPU6___" value="'$PPU6'" type="hidden">
<input name="___REF7___" value="'$REF7'" type="hidden">
<input name="___QUANTITY7___" value="'$QUANTITY7'" type="hidden">
<input name="___DESC7___" value="'$DESC7'" type="hidden">
<input name="___PPU7___" value="'$PPU7'" type="hidden">
<input name="___REF8___" value="'$REF8'" type="hidden">
<input name="___QUANTITY8___" value="'$QUANTITY8'" type="hidden">
<input name="___DESC8___" value="'$DESC8'" type="hidden">
<input name="___PPU8___" value="'$PPU8'" type="hidden">
<input name="___REF9___" value="'$REF9'" type="hidden">
<input name="___QUANTITY9___" value="'$QUANTITY9'" type="hidden">
<input name="___DESC9___" value="'$DESC9'" type="hidden">
<input name="___PPU9___" value="'$PPU9'" type="hidden">
<input name="___REF10___" value="'$REF10'" type="hidden">
<input name="___QUANTITY10___" value="'$QUANTITY10'" type="hidden">
<input name="___DESC10___" value="'$DESC10'" type="hidden">
<input name="___PPU10___" value="'$PPU10'" type="hidden">
<input name="___REF11___" value="'$REF11'" type="hidden">
<input name="___QUANTITY11___" value="'$QUANTITY11'" type="hidden">
<input name="___DESC11___" value="'$DESC11'" type="hidden">
<input name="___PPU11___" value="'$PPU11'" type="hidden">
<input name="___REF12___" value="'$REF12'" type="hidden">
<input name="___QUANTITY12___" value="'$QUANTITY12'" type="hidden">
<input name="___DESC12___" value="'$DESC12'" type="hidden">
<input name="___PPU12___" value="'$PPU12'" type="hidden">
<input name="___REF13___" value="'$REF13'" type="hidden">
<input name="___QUANTITY13___" value="'$QUANTITY13'" type="hidden">
<input name="___DESC13___" value="'$DESC13'" type="hidden">
<input name="___PPU13___" value="'$PPU13'" type="hidden">
<input name="___REF14___" value="'$REF14'" type="hidden">
<input name="___QUANTITY14___" value="'$QUANTITY14'" type="hidden">
<input name="___DESC14___" value="'$DESC14'" type="hidden">
<input name="___PPU14___" value="'$PPU14'" type="hidden">
<input name="___REF15___" value="'$REF15'" type="hidden">
<input name="___QUANTITY15___" value="'$QUANTITY15'" type="hidden">
<input name="___DESC15___" value="'$DESC15'" type="hidden">
<input name="___PPU15___" value="'$PPU15'" type="hidden">
<input name="___PANDP___" value="'$PANDP'" type="hidden">'

if [ $GRANDTOTAL != 0 ] && [ `echo $SUPPLIER'null' | sed 's/ //g'` != null ] && [ `echo $BHOLDER'null' | sed 's/ //g'` != null ] && [ `echo $DEPARTMENT'null' | sed 's/ //g'` != null ]
then
echo '<input value="'$"Submit"'" class="button" type="submit">'
fi
echo '
</div>
</form>
</div></body>
</html>
'
exit
