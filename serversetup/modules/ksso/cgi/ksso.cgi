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
END_POINT=9
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
#Assign PASSWORD
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PASSWORDcheck ]
then
let COUNTER=$COUNTER+1
PASSWORD=`echo $DATA | cut -s -d'_' -f$COUNTER`
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

#Set cookie date Friday, 31-Dec-2014 23:59:59
NOW=`date +%s`
VALIDHOURS=7
let VALIDSECS=$VALIDHOURS*60*60
let VALIDUNTIL=$NOW+$VALIDSECS
EXPIRES=`date +%A,' '%d-%b-%Y' '%H:%M:%S -d @$VALIDUNTIL`

#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html;
charset=utf-8">
<META HTTP-EQUIV="Set-Cookie" CONTENT="ksso=_USERNAME_'$USERNAME'_SESSIONNAME_'$SESSIONNAME'_SESSIONID_'$SESSIONID'_;expires='$EXPIRES' GMT; path=/">
<title>KSSO</title>
</head><body>'

#########################
#Check data
#########################
#Check to see that username is not blank
if [ $USERNAME'null' = null ]
then
MESSAGE="Blank Username"
show_status
fi

#Check to see that password is not blank
if [ $PASSWORD'null' = null ]
then
MESSAGE="Blank Password"
show_status
fi

#Check to see that sessionid is not blank
if [ $SESSIONID'null' = null ]
then
MESSAGE="Blank Session-id"
show_status
fi

#Check to see that sessionname is not blank
if [ $SESSIONNAME'null' = null ]
then
MESSAGE="Blank Session-name"
show_status
fi

#Save encrypted password to mysql database
source /opt/karoshi/server_network/ksso/config
ENCRYPTEDPASS=`echo "$PASSWORD" | gpg -c --passphrase "$SESSIONID" | openssl enc -base64`
echo "INSERT INTO userdata (sessionname,encryptedpass) VALUES ('$SESSIONNAME','$ENCRYPTEDPASS');" | mysql -u$MYSQLUSERNAME -p$MYSQLPASS -h127.0.0.1 ksso
if [ `echo $?` != 0 ]
then
MESSAGE="Database Error"
show_status
fi

echo "<form action=\"ksso_menu.cgi\" method=\"post\" id=\"kssoconnect\">
</form>
<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('kssoconnect').submit();
//-->
</script>"

echo "</body></html>"
exit


CREATE TABLE kssodata (
         id INT,
         data VARCHAR(100)
       );

create table userdata ( sessionname varchar(20) , sessionpass varchar(20) );


`echo "$PASSWORD" | gpg -c --passphrase "$SESSIONID"`
