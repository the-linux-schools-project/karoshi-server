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
########################
#Required input variables
########################
#  _CERTTYPE_
#  _SERVER_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/apply_ssl_certificate ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/apply_ssl_certificate
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################

END_POINT=8
#Assign CERTTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CERTTYPEcheck ]
then
let COUNTER=$COUNTER+1
CERTTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign ACTIONTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ACTIONTYPEcheck ]
then
let COUNTER=$COUNTER+1
ACTIONTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
[ $ACTIONTYPE = webcert ] && WEBCERT=yes
[ $ACTIONTYPE = emailcert ] && EMAILCERT=yes

#Assign SERVER
SERVER=`echo $DATA | cut -d_ -f6`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/apply_ssl_certificate_fm.cgi";'
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

#########################
#Check data
#########################
#Check to see that SERVER is not blank
if [ $SERVER'null' = null ]
then
MESSAGE=$ERRORMSG10
show_status
fi
#Check to see that CERTTYPE is not blank
if [ $CERTTYPE'null' = null ]
then
MESSAGE=$ERRORMSG11
show_status
fi
#Check CERTTYPE is the correct value
if [ $CERTTYPE != selfsign ] && [ $CERTTYPE != commercial ]
then
MESSAGE=$ERRORMSG12
show_status
fi

TITLE="$TITLE2"
[ $CERTTYPE = commercial ] && TITLE="$TITLE3"

[ $EMAILCERT'null' = null ] && EMAILCERT=no
[ $WEBCERT'null' = null ] && WEBCERT=no
#Check to see that EMAILCERT or WEBCERT is set to yes
if [ $EMAILCERT != yes ] && [ $WEBCERT != yes ]
then
MESSAGE=$ERRORMSG13
show_status
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
#Fill in form for self sign certificate

echo '<form action="/cgi-bin/admin/apply_ssl_certificate2.cgi" method="post"><div id="actionbox"><b>'$TITLE'</b><br><br>'

if [ $WEBCERT = yes ]
then
echo "<b>"$SERVER - $WEBCERTMSG"</b><br><br>"
else
echo "<b>"$SERVER - $EMAILCERTMSG"</b><br><br>"
fi
#Get current certificate data if it has been set
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/apply_ssl_certificate.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVER" | sudo -H /opt/karoshi/web_controls/exec/view_ssl_data
STATUS=`echo $?`
if [ $STATUS = 102 ]
then
MESSAGE=$SSHWARNMSG
show_status
fi
echo '<input name="___SERVER___" value="'$SERVER'" type="hidden">'
echo '<input name="___EMAILCERT___" value="'$EMAILCERT'" type="hidden">'
echo '<input name="___WEBCERT___" value="'$WEBCERT'" type="hidden">'
echo '<input name="___CERTTYPE___" value="'$CERTTYPE'" type="hidden">'
echo '</div><div id="submitbox"><input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset"></div>'
echo '</form></body</html>'

exit
