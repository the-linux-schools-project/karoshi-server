#!/bin/bash
#Copyright (C) 2011 Paul Sharrad
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


#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
#########################
#Assign data to variables
#########################
END_POINT=11
#Assign SERVICE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVICEcheck ]
then
let COUNTER=$COUNTER+1
SERVICE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

DATA=`echo $HTTP_COOKIE | tr -cd 'A-Za-z0-9\._:%\-+'`
#Assign USERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
then
let COUNTER=$COUNTER+1
USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign SESSIONID
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SESSIONIDcheck ]
then
let COUNTER=$COUNTER+1
SESSIONID=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign SESSIONNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SESSIONNAMEcheck ]
then
let COUNTER=$COUNTER+1
SESSIONNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">
alert("'$MESSAGE'");
window.location = "ksso_logon.cgi"
</script>
</body></html>'
exit
}
#########################
#Check https access
#########################
#if [ https_$HTTPS != https_on ]
#then
#export MESSAGE=$HTTPS_ERROR
#show_status
#fi

#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html;
charset=utf-8">
<title>KSSO - '$SERVICE'</title>
<meta http-equiv="REFRESH" content="1;url=ksso_menu.cgi">
</head><body>'

#########################
#Check data
#########################
#Check to see that username is not blank
if [ $SERVICE'null' = null ]
then
MESSAGE="Blank service"
show_status
fi

#Check to see that sessionid is not blank
if [ $SESSIONID'null' = null ]
then
MESSAGE="Blank sessionid"
show_status
fi

#Check to see that sessionname is not blank
if [ $SESSIONNAME'null' = null ]
then
MESSAGE="Blank session name"
show_status
fi

source /opt/karoshi/server_network/ksso/config

PASSWORD=`echo "SELECT encryptedpass from userdata WHERE sessionname = '$SESSIONNAME';" | mysql -u$MYSQLUSERNAME -p$MYSQLPASS -h127.0.0.1 ksso | sed -n 2,2p`

PASSWORD=`echo "$PASSWORD" | base64 -d | gpg --passphrase "$SESSIONID"`


