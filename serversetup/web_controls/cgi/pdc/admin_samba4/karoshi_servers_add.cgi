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
########################
#Required input variables
########################
#  _SERVERNAME_
# _TCPIP_
#  _PASSWORD1_  Root Password
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/karoshi_servers_add ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/karoshi_servers_add
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox"><b>'$TITLE'</b><br><br>'
############################
#Show page
############################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/karoshi_servers_add_fm.cgi";'
echo '</script>'
echo "</body></html>"
exit
}

function test_connections {
echo '<SCRIPT language="Javascript">'
#echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/karoshi_servers_view.cgi";'
echo '</script>'
echo "</body></html>"
exit
}

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-' | sed 's/__/_ _/g'`
#########################
#Assign data to variables
#########################
END_POINT=13

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

#Assign TCPIPNUMBER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TCPIPNUMBERcheck ]
then
let COUNTER=$COUNTER+1
TCPIPNUMBER=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9.'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign password1
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PASSWORD1check ]
then
let COUNTER=$COUNTER+1
PASSWORD1=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign password2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PASSWORD2check ]
then
let COUNTER=$COUNTER+1
PASSWORD2=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign authentication
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = AUTHENTICATIONcheck ]
then
let COUNTER=$COUNTER+1
AUTHENTICATION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign ZONE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ZONEcheck ]
then
let COUNTER=$COUNTER+1
ZONE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

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
#Check to see that servername is not blank
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Check to see that password fields are not blank
if [ $PASSWORD1'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
if [ $PASSWORD2'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check that password has been entered correctly
if [ $PASSWORD1 != $PASSWORD2 ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Check to see that authentication is not blank
if [ $AUTHENTICATION'null' = null ]
then
MESSAGE=$ERRORMSG7
show_status
fi

#Check to see that authentication is not blank
if [ $ZONE'null' = null ]
then
MESSAGE=$ERRORMSG7
show_status
fi




function get_data {
#Send data back to form and ask for tcpip number
echo '
<body onload="submitForm()"><form action="/cgi-bin/admin/karoshi_servers_add_fm.cgi" method="post" name="form">
<input name="_SERVERNAME_" value="'$SERVERNAME'" type="hidden">
<input name="_PASSWORD1_" value="'$PASSWORD1'" type="hidden">
<input name="_PASSWORD2_" value="'$PASSWORD2'" type="hidden">
<input name="_AUTHENTICATION_" value="'$AUTHENTICATION'" type="hidden">
<input name="_ZONE_" value="'$ZONE'" type="hidden">
</form>
<SCRIPT LANGUAGE="JavaScript">
function submitForm(){
document.form.submit();
}
</SCRIPT></body></html
'
exit
}



#If tcpip is blank check to see that we know the tcpip number
if [ $TCPIPNUMBER'null' = null ]
then
host -r -t A $SERVERNAME 1>/dev/null
if [ `echo $?` != 0 ]
then
get_data
fi
fi

if [ $TCPIPNUMBER'null' != null ]
then
########################
#Check that the tcpip number has been entered correctly
########################
#Check dots
if [ `echo $TCPIPNUMBER | sed 's/\./\n /g'  | sed /^$/d | wc -l` != 4 ]
then
get_data
fi
#Check that no number is greater than 255
HIGHESTNUMBER=`echo $TCPIPNUMBER | sed 's/\./\n /g'  | sed /^$/d | sort -g -r | sed -n 1,1p`
if [ $HIGHESTNUMBER -gt 255 ]
then
get_data
fi
fi

#Check to see that this is not the tcpip number of the main server.
MAINSERVERIP=`net lookup $HOSTNAME`
if [ $MAINSERVERIP = $TCPIPNUMBER ]
then
MESSAGE=$ERRORMSG6
show_status
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/karoshi_servers_add.cgi | cut -d' ' -f1`
sudo -H /opt/karoshi/web_controls/exec/karoshi_servers_add $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$PASSWORD1:$TCPIPNUMBER:$AUTHENTICATION:$ZONE
EXEC_STATUS=`echo $?`

MESSAGE=`echo $SERVERNAME - $COMPLETEDMSG`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $SERVERNAME - $ERRORMSG5`
show_status
fi
test_connections
exit
