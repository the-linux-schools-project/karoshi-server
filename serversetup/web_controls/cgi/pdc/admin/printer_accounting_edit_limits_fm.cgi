#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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

##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printer_accounting ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printer_accounting
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=11
#Assign NAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = NAMEcheck ]
then
let COUNTER=$COUNTER+1
NAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign LIMIT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LIMITcheck ]
then
let COUNTER=$COUNTER+1
LIMIT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign GROUPLIMIT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = GROUPLIMITcheck ]
then
let COUNTER=$COUNTER+1
GROUPLIMIT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign TOTAL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TOTALcheck ]
then
let COUNTER=$COUNTER+1
TOTAL=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

TYPE=group
STARTCGI=printer_accounting_group_limits_fm.cgi
#Assign TYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TYPEcheck ]
then
let COUNTER=$COUNTER+1
TYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

if [ $TYPE'null' != null ]
then
if [ $TYPE = user ]
then
STARTCGI=printer_accounting_user_limits_fm.cgi
fi
fi


function show_status {
echo '<script type="text/javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/'$STARTCGI'";'
echo '</script>'
echo "</div></body></html>"
exit
}


##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE3'</title><link rel="stylesheet" href="/css/'$STYLESHEET'">
</head><body onLoad="start()">'

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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi
#########################
#Check data
#########################
#Check to see that NAME is not blank
if [ $NAME'null' = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi
#Check to see that LIMIT is not blank
if [ $LIMIT'null' = null ]
then
MESSAGE=$ERRORMSG5
show_status
fi

MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
fi
echo '<form name="myform" id="myform" action="/cgi-bin/admin/printer_accounting_edit_limits.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE3'</b></a></td></tr></tbody></table>'
else
echo '<b>'$TITLE3'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'<br><br>'$HELPMSG4'</span></a><br><br>'
fi

echo '
<input name="_NAME_" value="'$NAME'" type="hidden">
<input name="_TYPE_" value="'$TYPE'" type="hidden">'

if [ $TYPE != userdelete ] && [ $TYPE = user ]
then
echo '
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;">'$USERNAMEMSG'</td><td>'$NAME'</td></tr>
<tr><td>'$USERLIMITMSG'</td><td>'$LIMIT'</td></tr>
<tr><td>'$GROUPLIMITMSG'</td><td>'$GROUPLIMIT'</td></tr>
<tr><td>'$TOTALMSG'</td><td>'$TOTAL'</td></tr>
<tr><td>'$ADDITIONALCREDITSMSG'</td><td><input maxlength="10" size="10" name="_LIMIT_" value=""> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG11'<br><br>'$HELPMSG4'</span></a></td></tr></tbody></table>
'
fi

if [ $TYPE != userdelete ] && [ $TYPE = group ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;"><b>'$PRIMARYGROUPMSG2'</b></td><td><b>'$LIMITMSG'</b></td></tr>
<tr><td>'$NAME'</td><td><input maxlength="10" size="10" name="_LIMIT_" value="'$LIMIT'"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG5'</span></a></td></tr></tbody></table>
'
fi


if [ $TYPE = userdelete ]
then
echo
echo '<input name="_LIMIT_" value="'$LIMIT'" type="hidden"></form>'
echo "<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('myform').submit();
//-->
</script>"

fi

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi
echo '<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
</div></form></body></html>
'
exit
