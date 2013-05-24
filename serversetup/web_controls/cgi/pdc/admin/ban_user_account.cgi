#!/bin/bash
#Copyright (C) 2007  Paul Sharrad
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/ban_user_account ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/ban_user_account
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
BANLENGTH=7
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
if [ $DATA'null' != null ]
then
END_POINT=18
#Assign HOUR
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = HOURcheck ]
then
let COUNTER=$COUNTER+1
HOUR=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign MINUTES
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = MINUTEScheck ]
then
let COUNTER=$COUNTER+1
MINUTES=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign DAY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = DAYcheck ]
then
let COUNTER=$COUNTER+1
DAY=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign MONTH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = MONTHcheck ]
then
let COUNTER=$COUNTER+1
MONTH=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign YEAR
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = YEARcheck ]
then
let COUNTER=$COUNTER+1
YEAR=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign INCIDENT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = INCIDENTcheck ]
then
let COUNTER=$COUNTER+1
INCIDENT=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/2B/ /g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign ACTIONTAKEN
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = ACTIONTAKENcheck ]
then
let COUNTER=$COUNTER+1
ACTIONTAKEN=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/2B/ /g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign STUDENTS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = STUDENTScheck ]
then
let COUNTER=$COUNTER+1
STUDENTS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/2B/ /g'`
break
fi
let COUNTER=$COUNTER+1
done
#Assign BANLENGTH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAENTRY=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAENTRY'check'` = BANLENGTHcheck ]
then
let COUNTER=$COUNTER+1
BANLENGTH=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/3F/?/g'`
break
fi
let COUNTER=$COUNTER+1
done
fi
DATE_INFO=`date +%F`
[ $DAY'null' = null ] && DAY=`echo $DATE_INFO | cut -d- -f3`
[ $MONTH'null' = null ] && MONTH=`echo $DATE_INFO | cut -d- -f2`
[ $YEAR'null' = null ] && YEAR=`echo $DATE_INFO | cut -d- -f1`

TIME_INFO=`date +%T`
[ $HOUR'null' = null ] && HOUR=`echo $TIME_INFO | cut -d: -f1`
[ $MINUTES'null' = null ] && MINUTES=`echo $TIME_INFO | cut -d: -f2`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/ban_user_account.cgi";'
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

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/ban_user_account2.cgi" method="post">'
echo '<div id="actionbox">'
echo '<b>'$TITLE'</b><br>'
echo '<table class="standard" style="text-align: left; top: 207px; left: 232px; width: 674px; height: 61px;" border="0" cellpadding="0" cellspacing="0">'
echo '<tbody><tr><td>'$DATEMSG'</td><td>'
#HOUR
echo '<input name="_HOUR_" value="'$HOUR'" size="2" maxlength="2" type="text">:'
echo '<input name="_MINUTES_" value="'$MINUTES'" size="2" maxlength="2" type="text">'
echo '</td><td>'
echo '<input name="_DAY_" value="'$DAY'" size="2" maxlength="2" type="text">'
echo '<input name="_MONTH_" value="'$MONTH'" size="2" maxlength="2" type="text">'
echo '<input name="_YEAR_" value="'$YEAR'" size="4" maxlength="4" type="text">'
echo '</td></tr><tr><td>'$DURATIONMSG'</td><td>'
echo '<input name="_BANLENGTH_" value="'$BANLENGTH'" size="2" maxlength="3" type="text"> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Acceptable_Use"><img class="images" alt="" src="/images/help/info.png"><span>'$BANLENGTHHELP'</span></a>
'
echo '</td></tr></tbody></table>'
#Students involved
echo '<br>'$USERNAMESMSG'<br><br>'
echo '<input value="'$STUDENTS'" name="_STUDENTS_" size="53" type="text">'
#Incident and action taken
echo '<br><br>Incident Report<br>'
echo '<textarea cols="77" rows="4" name="_INCIDENT_">'$INCIDENT'</textarea><br><br>Action Taken<br>'
echo '<textarea cols="77" rows="4" name="_ACTIONTAKEN_">'$ACTIONTAKEN'</textarea>'

echo '</div><div id="submitbox"> <input value="Submit" type="submit"> <input value="Reset" type="reset"> </div></form></body></html>'
exit
