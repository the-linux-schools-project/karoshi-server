#!/bin/bash
#Copyright (C) 2011 Paul Sharrad

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

########################
#Language
########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/ksso ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/ksso
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
#########################
#Assign data to variables
#########################
END_POINT=9
#Assign LOGONPAGE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LOGONPAGEcheck ]
then
let COUNTER=$COUNTER+1
LOGONPAGE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3A/:/g' | sed 's/%2F/\//g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign ENTRYNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ENTRYNAMEcheck ]
then
let COUNTER=$COUNTER+1
ENTRYNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3A/:/g' | sed 's/%2F/\//g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign ICON
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ICONcheck ]
then
let COUNTER=$COUNTER+1
ICON=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%3A/:/g' | sed 's/%2F/\//g'`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/ksso_add1_fm.cgi"
</script>
</body></html>'
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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/admin/ksso_add2.cgi" method="post"><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE1'</b></a></td></tr></tbody></table><br>'
else
echo '<b>'$TITLE1'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a><br><br>'
fi

#########################
#Check data
#########################
#Check to see that LOGONPAGE is not blank
if [ $LOGONPAGE'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Check to see that ENTRYNAME is not blank
if [ $ENTRYNAME'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that ICON is not blank
if [ $ICON'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi

########################
#Process the data
########################

#Convert special chars in the address
LOGONPAGE=`echo $LOGONPAGE | sed 's/%3F/?/g' | sed 's/%3D/=/g'`

echo '<b>'$ENTRYNAME - $LOGONPAGE'</b><br><br>'

PROCESSFOLDER=/tmp/processfolder.$$

[ -d $PROCESSFOLDER ] && rm -f -R $PROCESSFOLDER
mkdir $PROCESSFOLDER

#Get raw data
cd $PROCESSFOLDER

wget --no-check-certificate "$LOGONPAGE"

#Check that 1 file has been downloaded

FILECOUNTER=`ls -1 $PROCESSFOLDER | wc -l`

if [ $FILECOUNTER != 1 ]
then
exit 102
fi

#Get filename

FILENAME=`ls -1 $PROCESSFOLDER`

#Check that filename exists
[ ! -f /$PROCESSFOLDER/$FILENAME ] && exit 103

#Get form destination
DATA=`cat /$PROCESSFOLDER/$FILENAME | grep -i '<form '`
DESTINATION=`echo $DATA | sed 's/ /\\n/g' | grep ^action= | cut -d\" -f2 | sed 's/"//g' | sed 's/>//g' | sed -n 1,1p`

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 120px;"><span style="color: red;"><b>'$DESTINATIONMSG'</b></span></td>
<td><input tabindex= "1" value="'$DESTINATION'" name="___DESTINATION___" style="width: 450px;" size="20" type="text">
</td>
<td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images//warnings/warning.png"><span>'$HELPMSG6'</span></a>
</td>
</tr></tbody></table><br>'

#Process raw file
cat /$PROCESSFOLDER/$FILENAME | tr 'A-Z' 'a-z' | grep '<input ' > /$PROCESSFOLDER/data.$$

echo '<input name="___ENTRYNAME___" value="'$ENTRYNAME'" type="hidden"><input name="___ICON___" value="'$ICON'" type="hidden"><input name="___LOGONPAGE___" value="'$LOGONPAGE'" type="hidden"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 120px;"><b>'$FIELDNAMEMSG'</b></td><td style="width: 120px;"><b>'$FIELDIDMSG'</b></td><td style="width: 120px;"><b>'$FIELDVALUEMSG'</b></td></tr>
'

#Display a list of fields

COUNTER=1
LINECOUNT=`cat /$PROCESSFOLDER/data.$$ | wc -l`

while [ $COUNTER -lt $LINECOUNT ]
do
DATA=`sed -n $COUNTER,$COUNTER'p' /$PROCESSFOLDER/data.$$`

NAME=`echo $DATA | sed 's/ /\\n/g' | grep ^name= | cut -d\" -f2 | sed 's/"//g' | sed 's/>//g'`
ID=`echo $DATA | sed 's/ /\\n/g' | grep ^id= | cut -d\" -f2 | sed 's/"//g' | sed 's/>//g'`
VALUE=`echo $DATA | sed 's/ /\\n/g' | grep ^value= | cut -d\" -f2 | sed 's/"//g' | sed 's/>//g'`
if [ $NAME'null' != null ]
then
echo '<tr><td>'"$NAME"'</td><td>'"$ID"'</td><td>'"$VALUE"'</td>
<td>
<select name="___FORMDATA___">
<option value="___NAME___'$NAME'___ID___'$ID'___VALUE___EXCLUDE"___>'$EXCLUDEMSG'</option>
<option value="___NAME___'$NAME'___ID___'$ID'___VALUE___'$VALUE'___">'$INCLUDECURVALMSG'</option>
<option value="___NAME___'$NAME'___ID___'$ID'___VALUE___USERNAME___">'$INLUDEWUSNAMEMSG'</option>
<option value="___NAME___'$NAME'___ID___'$ID'___VALUE___PASSWORD___">'$INCLUDEWPASSMSG'</option>
<option value="___NAME___'$NAME'___ID___'$ID'___VALUE___BROWSERSTRING___">'$INCLUDEWBSTRINGMSG'</option>
</select>
</td></tr>'
fi
let COUNTER=$COUNTER+1
done

echo '</tbody></table><br><br><input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">'

#rm -f -R $PROCESSFOLDER

echo '</div></body></html>'

exit
