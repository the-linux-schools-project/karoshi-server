#!/bin/bash
#Copyright (C) 2009  Paul Sharrad

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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/file/file_manager ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/file/file_manager
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
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body><div id="pagecontainer">'
TCPIP_ADDR=$REMOTE_ADDR

DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+*'`
#CONVERT STAR
DATA=`echo "$DATA" | sed 's/*/%99/g'`

#########################
#Assign data to variables
#########################
SERVER=`echo "$DATA" | cut -d'_' -f7`
ACTION=`echo "$DATA" | cut -d'_' -f8`
LOCATION=`echo "$DATA" | cut -d'_' -f9- | sed 's/%2F/\//g'`

if [ $DATA'null' != null ]
then
if [ `echo ${DATA:0:8}` = ITEMCOPY ]
then
DATA=`echo $DATA | sed 's/+++++/:/g'`
ITEMMOVE=`echo $DATA | cut -d: -f2`
fi
fi

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/file_manager.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

if [ $ACTION'null' = null ]
then
ACTION=ENTER
fi

if [ $SERVER'null' = null ]
then
SERVER=$HOSTNAME
fi

if [ $ACTION = REALLYSETPERMS ]
then
PERMISSIONS=`echo "$DATA" | cut -d'_' -f1`
END_POINT=5
#Assign owner
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $PERMISSIONS | cut -s -d'+' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = OWNERcheck ]
then
let COUNTER=$COUNTER+1
OWNER=`echo $DATA | cut -s -d'+' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign group
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $PERMISSIONS | cut -s -d'+' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = GROUPcheck ]
then
let COUNTER=$COUNTER+1
GROUP=`echo $DATA | cut -s -d'+' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Check to see that owner is not blank
if [ $OWNER'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Check to see that group is not blank
if [ $GROUP'null' = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi
#Check that the owner exists
#getent passwd "$OWNER" 1>/dev/null
#if [ `echo $?` != 0 ]
#then
#MESSAGE=$ERRORMSG5
#show_status
#fi
#Check that the group exists
#getent group "$GROUP" 1>/dev/null
#if [ `echo $?` != 0 ]
#then
#MESSAGE=$ERRORMSG6
#show_status
#fi
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
SERVER2=$SERVER
[ $SERVER2 = pdc ] && SERVER2=$HOSTNAME
echo '<form action="/cgi-bin/admin/file_manager.cgi" method="post"><div id="actionbox"><b>'$TITLE' - '$SERVER2'</b><br><br>'
#########################
#Check data
#########################
if [ $ACTION != ENTER ] && [ $ACTION != DELETE ] && [ $ACTION != REALLYDELETE ] && [ $ACTION != SETPERMS ] && [ $ACTION != REALLYSETPERMS ] && [ $ACTION != MOVE ] && [ $ACTION != REALLYMOVE ] && [ $ACTION != REALLYCOPY ] && [ $ACTION != CANCELCOPY ] && [ $ACTION != RENAME ] && [ $ACTION != REALLYRENAME ] && [ $ACTION != EDIT ] && [ $ACTION != REALLYEDIT ] && [ $ACTION != CREATEDIR ] && [ $ACTION != REALLYCREATEDIR ] && [ $ACTION != RESTORE ] && [ $ACTION != REALLYRESTORE ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#echo $DATA'<br>'
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/file_manager.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVER:$LOCATION:$FILENAME:$ACTION:$PERMISSIONS:$OWNER:$GROUP:$ITEMMOVE:" | sudo -H /opt/karoshi/web_controls/exec/file_manager

echo '

</div>
</form>
</div></body>
</html>
'
exit
