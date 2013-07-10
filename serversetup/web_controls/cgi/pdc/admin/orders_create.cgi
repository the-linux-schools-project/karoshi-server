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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/orders ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/orders
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
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE1'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<link rel="stylesheet" type="text/css" href="/css/print.css" media="print" />
<script language="JavaScript" src="/all/calendar2/calendar_eu.js"></script>
        <!-- Timestamp input popup (European Format) -->

<link rel="stylesheet" href="/all/calendar2/calendar.css">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>
'
#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+-' | sed 's/+/ /g' | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORED/g' | sed 's/TRIPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
#Assign _DEPARTMENT_
DEPARTMENT=`echo $DATA | cut -s -d'_' -f3 | sed 's/UNDERSCORED/_/g'`
DATE=`echo $DATA | cut -s -d'_' -f5`
SUPPLIER=`echo $DATA | cut -s -d'_' -f7 | sed 's/UNDERSCORED/_/g'`
BHOLDER=`echo $DATA | cut -s -d'_' -f9 | sed 's/UNDERSCORED/_/g'`
REF1=`echo $DATA | cut -s -d'_' -f11 | sed 's/UNDERSCORED/_/g'`
QUANTITY1=`echo $DATA | cut -s -d'_' -f13 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC1=`echo $DATA | cut -s -d'_' -f15 | sed 's/UNDERSCORED/_/g'`
PPU1=`echo $DATA | cut -s -d'_' -f17 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF2=`echo $DATA | cut -s -d'_' -f19 | sed 's/UNDERSCORED/_/g'`
QUANTITY2=`echo $DATA | cut -s -d'_' -f21 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC2=`echo $DATA | cut -s -d'_' -f23 | sed 's/UNDERSCORED/_/g'`
PPU2=`echo $DATA | cut -s -d'_' -f25 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF3=`echo $DATA | cut -s -d'_' -f27 | sed 's/UNDERSCORED/_/g'`
QUANTITY3=`echo $DATA | cut -s -d'_' -f29 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC3=`echo $DATA | cut -s -d'_' -f31 | sed 's/UNDERSCORED/_/g'`
PPU3=`echo $DATA | cut -s -d'_' -f33 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF4=`echo $DATA | cut -s -d'_' -f35 | sed 's/UNDERSCORED/_/g'`
QUANTITY4=`echo $DATA | cut -s -d'_' -f37 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC4=`echo $DATA | cut -s -d'_' -f39 | sed 's/UNDERSCORED/_/g'`
PPU4=`echo $DATA | cut -s -d'_' -f41 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF5=`echo $DATA | cut -s -d'_' -f43 | sed 's/UNDERSCORED/_/g'`
QUANTITY5=`echo $DATA | cut -s -d'_' -f45 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC5=`echo $DATA | cut -s -d'_' -f47 | sed 's/UNDERSCORED/_/g'`
PPU5=`echo $DATA | cut -s -d'_' -f49 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF6=`echo $DATA | cut -s -d'_' -f51 | sed 's/UNDERSCORED/_/g'`
QUANTITY6=`echo $DATA | cut -s -d'_' -f53 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC6=`echo $DATA | cut -s -d'_' -f55 | sed 's/UNDERSCORED/_/g'`
PPU6=`echo $DATA | cut -s -d'_' -f57 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF7=`echo $DATA | cut -s -d'_' -f59 | sed 's/UNDERSCORED/_/g'`
QUANTITY7=`echo $DATA | cut -s -d'_' -f61 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC7=`echo $DATA | cut -s -d'_' -f63 | sed 's/UNDERSCORED/_/g'`
PPU7=`echo $DATA | cut -s -d'_' -f65 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF8=`echo $DATA | cut -s -d'_' -f67 | sed 's/UNDERSCORED/_/g'`
QUANTITY8=`echo $DATA | cut -s -d'_' -f69 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC8=`echo $DATA | cut -s -d'_' -f71 | sed 's/UNDERSCORED/_/g'`
PPU8=`echo $DATA | cut -s -d'_' -f73 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF9=`echo $DATA | cut -s -d'_' -f75 | sed 's/UNDERSCORED/_/g'`
QUANTITY9=`echo $DATA | cut -s -d'_' -f77 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC9=`echo $DATA | cut -s -d'_' -f79 | sed 's/UNDERSCORED/_/g'`
PPU9=`echo $DATA | cut -s -d'_' -f81 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF10=`echo $DATA | cut -s -d'_' -f83 | sed 's/UNDERSCORED/_/g'`
QUANTITY10=`echo $DATA | cut -s -d'_' -f85 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC10=`echo $DATA | cut -s -d'_' -f87 | sed 's/UNDERSCORED/_/g'`
PPU10=`echo $DATA | cut -s -d'_' -f89 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF11=`echo $DATA | cut -s -d'_' -f91 | sed 's/UNDERSCORED/_/g'`
QUANTITY11=`echo $DATA | cut -s -d'_' -f93 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC11=`echo $DATA | cut -s -d'_' -f95 | sed 's/UNDERSCORED/_/g'`
PPU11=`echo $DATA | cut -s -d'_' -f97 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF12=`echo $DATA | cut -s -d'_' -f99 | sed 's/UNDERSCORED/_/g'`
QUANTITY12=`echo $DATA | cut -s -d'_' -f101 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC12=`echo $DATA | cut -s -d'_' -f103 | sed 's/UNDERSCORED/_/g'`
PPU12=`echo $DATA | cut -s -d'_' -f105 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF13=`echo $DATA | cut -s -d'_' -f107 | sed 's/UNDERSCORED/_/g'`
QUANTITY13=`echo $DATA | cut -s -d'_' -f109 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC13=`echo $DATA | cut -s -d'_' -f111 | sed 's/UNDERSCORED/_/g'`
PPU13=`echo $DATA | cut -s -d'_' -f113 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF14=`echo $DATA | cut -s -d'_' -f115 | sed 's/UNDERSCORED/_/g'`
QUANTITY14=`echo $DATA | cut -s -d'_' -f117 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC14=`echo $DATA | cut -s -d'_' -f119 | sed 's/UNDERSCORED/_/g'`
PPU14=`echo $DATA | cut -s -d'_' -f121 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
REF15=`echo $DATA | cut -s -d'_' -f123 | sed 's/UNDERSCORED/_/g'`
QUANTITY15=`echo $DATA | cut -s -d'_' -f125 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
DESC15=`echo $DATA | cut -s -d'_' -f127 | sed 's/UNDERSCORED/_/g'`
PPU15=`echo $DATA | cut -s -d'_' -f129 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`
PANDP=`echo $DATA | cut -s -d'_' -f131 | sed 's/UNDERSCORED/_/g' | tr -cd '0-9\.'`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/orders_create_fm.cgi";'
echo '</script>'
echo "</body></html>"
exit
}

function completed {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '</script>'
echo "</body></html>"
exit
}

#Check to see that department is not blank
if [ `echo $DEPARTMENT'null' | sed 's/ //g;'` = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Check to see that supplier is not blank
if [ `echo $SUPPLIER'null' | sed 's/ //g'` = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that the date is not blank
if [ $DATE'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Check to see that the BHOLDER is not blank
if [ `echo $BHOLDER'null' | sed 's/ //g'` = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi

GRANDTOTAL=0
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

#Create order ref
REFDATE=`date +%d%m%y`
TIME=`date +%H%M%S`
ORDERREF=`echo $REFDATE-$TIME-$$`
echo '
<div id="noprint">
'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin


echo '</div><div id="actionbox">

<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 150px;"><b>'$DEPMSG'</b></td><td style="width: 240px;">'$DEPARTMENT'</td><td style="width: 120px;"><b>'$DATEMSG'</b></td><td style="width: 200px;">'$DATE'</td></tr>
<tr><td><b>'$SUPPLIERMSG'</b></td><td>'$SUPPLIER'</td><td><b>'$BHOLDERMSG'</b></td><td>'$BHOLDER'</td></tr>
<tr><td><b>'$ORDERREFMSG'</b></td><td>'$ORDERREF'</td></tr>
</tbody></table><br>
  <table class="standard" style="text-align: left;" border="2" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="vertical-align: top; width: 250px;"><b>'$REFMSG'</b></td><td style="vertical-align: top; width: 70px;"><b>'$QUANTITYMSG'</b></td><td style="vertical-align: top; width: 400px;"><b>'$DESCRIPTIONMSG'</b></td><td style="vertical-align: top; width: 90px;"><b>'$UNITPRICEMSG'</b></td><td style="vertical-align: top; width: 80px;"><b>'$TOTALMSG'</b></td></tr>
<tr><td>'$REF1'</td><td>'$QUANTITY1'</td><td>'$DESC1'</td><td>'$PPU1'</td><td>'$TOTAL1'</td></tr>
<tr><td>'$REF2'</td><td>'$QUANTITY2'</td><td>'$DESC2'</td><td>'$PPU2'</td><td>'$TOTAL2'</td></tr>
<tr><td>'$REF3'</td><td>'$QUANTITY3'</td><td>'$DESC3'</td><td>'$PPU3'</td><td>'$TOTAL3'</td></tr>
<tr><td>'$REF4'</td><td>'$QUANTITY4'</td><td>'$DESC4'</td><td>'$PPU4'</td><td>'$TOTAL4'</td></tr>
<tr><td>'$REF5'</td><td>'$QUANTITY5'</td><td>'$DESC5'</td><td>'$PPU5'</td><td>'$TOTAL5'</td></tr>
<tr><td>'$REF6'</td><td>'$QUANTITY6'</td><td>'$DESC6'</td><td>'$PPU6'</td><td>'$TOTAL6'</td></tr>
<tr><td>'$REF7'</td><td>'$QUANTITY7'</td><td>'$DESC7'</td><td>'$PPU7'</td><td>'$TOTAL7'</td></tr>
<tr><td>'$REF8'</td><td>'$QUANTITY8'</td><td>'$DESC8'</td><td>'$PPU8'</td><td>'$TOTAL8'</td></tr>
<tr><td>'$REF9'</td><td>'$QUANTITY9'</td><td>'$DESC9'</td><td>'$PPU9'</td><td>'$TOTAL9'</td></tr>
<tr><td>'$REF10'</td><td>'$QUANTITY10'</td><td>'$DESC10'</td><td>'$PPU10'</td><td>'$TOTAL10'</td></tr>
<tr><td>'$REF11'</td><td>'$QUANTITY11'</td><td>'$DESC11'</td><td>'$PPU11'</td><td>'$TOTAL11'</td></tr>
<tr><td>'$REF12'</td><td>'$QUANTITY12'</td><td>'$DESC12'</td><td>'$PPU12'</td><td>'$TOTAL12'</td></tr>
<tr><td>'$REF13'</td><td>'$QUANTITY13'</td><td>'$DESC13'</td><td>'$PPU13'</td><td>'$TOTAL13'</td></tr>
<tr><td>'$REF14'</td><td>'$QUANTITY14'</td><td>'$DESC14'</td><td>'$PPU14'</td><td>'$TOTAL14'</td></tr>
<tr><td>'$REF15'</td><td>'$QUANTITY15'</td><td>'$DESC15'</td><td>'$PPU15'</td><td>'$TOTAL15'</td></tr>
<tr><td></td><td></td><td></td><td><b>'$SUBTOTALMSG'</b></td><td>'$SUBTOTAL'</td></tr>
<tr><td></td><td></td><td></td><td><b>P+P</b></td><td>'$PANDP'</td></tr>
<tr><td></td><td></td><td></td><td><b>Total</b></td><td><b>'$GRANDTOTAL'</b></td></tr>
</tbody></table><br>
'
echo "
<style type=\"text/css\" media=\"print\">
.printbutton {
  visibility: hidden;
  display: none;
}
</style>
<script>
document.write(\"<input type=\'button\' \" +
\"onClick=\'window.print()\' \" +
\"class=\'printbutton\' \" +
\"value=\'Print This Page\'/>\");
</script>

"
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/orders_create.cgi | cut -d' ' -f1`
#Add order to the pending section
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$DEPARTMENT:$DATE:$SUPPLIER:$BHOLDER:$ORDERREF:$REF1:$QUANTITY1:$DESC1:$PPU1:$TOTAL1:$REF2:$QUANTITY2:$DESC2:$PPU2:$TOTAL2:$REF3:$QUANTITY3:$DESC3:$PPU3:$TOTAL3:$REF4:$QUANTITY4:$DESC4:$PPU4:$TOTAL4:$REF5:$QUANTITY5:$DESC5:$PPU5:$TOTAL5:$REF6:$QUANTITY6:$DESC6:$PPU6:$TOTAL6:$REF7:$QUANTITY7:$DESC7:$PPU7:$TOTAL7:$REF8:$QUANTITY8:$DESC8:$PPU8:$TOTAL8:$REF9:$QUANTITY9:$DESC9:$PPU9:$TOTAL9:$REF10:$QUANTITY10:$DESC10:$PPU10:$TOTAL10:$REF11:$QUANTITY11:$DESC11:$PPU11:$TOTAL11:$REF12:$QUANTITY12:$DESC12:$PPU12:$TOTAL12:$REF13:$QUANTITY13:$DESC13:$PPU13:$TOTAL13:$REF14:$QUANTITY14:$DESC14:$PPU14:$TOTAL14:$REF15:$QUANTITY15:$DESC15:$PPU15:$TOTAL15:$SUBTOTAL:$PANDP:$GRANDTOTAL" | sudo -H /opt/karoshi/web_controls/exec/orders_create
MESSAGE=$COMPLETEDMSG
completed
echo '

</div>
</body>
</html>
'
exit
