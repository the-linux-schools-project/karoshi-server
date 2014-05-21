#!/bin/bash
#Copyright (C) 2014 Paul Sharrad

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
#Required input variables
########################
#  _USERNAME_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

########################
#Language
########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitorix ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/monitorix
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=12
#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
then
let COUNTER=$COUNTER+1
SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign INTERVAL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = INTERVALcheck ]
then
let COUNTER=$COUNTER+1
INTERVAL=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/monitorix_fm.cgi"
</script>
</div></body></html>'
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

#########################
#Check data
#########################

#Check to see that username is not blank
if [ -z "$SERVERNAME" ]
then
MESSAGE=$ERRORMSG1
show_status
fi

if [ -z "$GRAPHTYPE" ]
then
MESSAGE=$ERRORMSG2
show_status
fi

if [ -z "$INTERVAL" ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox4
TABLECLASS=standard
WIDTH=180
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
WIDTH=160
fi

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'

#echo HTTP_REFERER is $HTTP_REFERER"<br>"
ACCESSPORT=50001
[ `echo $HTTP_REFERER | grep -c ":50002"` -gt 0 ] && ACCESSPORT=50002
source /opt/karoshi/server_network/domain_information/domain_name
echo '<div class="sectiontitle">'$TITLE'</div></div><div id="infobox">'
#Show monitorix data

echo '<iframe src="https://manage.'$REALM':'$ACCESSPORT'/monitorix-'$SERVERNAME'/monitorix.cgi?mode=localhost&graph=all&when='$INTERVAL'&color=black" frameborder="0" width="1200" height="5000" scrolling="no"></iframe>'

#Get data
#MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/monitorix.cgi | cut -d' ' -f1`
#echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$GRAPHTYPE:$INTERVAL:" | sudo -H /opt/karoshi/web_controls/exec/monitorix

echo '</div></div></div></body></html>'
exit
