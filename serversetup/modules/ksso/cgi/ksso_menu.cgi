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
<title>KSSO</title>
<link rel="stylesheet" href="/ksso/smbwc.css">
<link rel="icon" type="image/png" href="/ksso/images/logo.png">
</head><body>
<div id="page">
<div id="headerbox">
<div id="headertextbox"></div>
</div>
<div id="linksbox">
</div>
<div id="linksbox2">
'

#########################
#Get data input
#########################
END_POINT=11

DATA=`echo $HTTP_COOKIE | tr -cd 'A-Za-z0-9\._:%\-+'`
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


#########################
#Check data
#########################


#Check to see that sessionid is not blank
if [ $SESSIONID'null' = null ]
then
echo "<form action=\"ksso_logon.cgi\" method=\"post\" id=\"kssoconnect\">
</form>
<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('kssoconnect').submit();
//-->
</script>"
fi

#Check to see that sessionname is not blank
if [ $SESSIONNAME'null' = null ]
then
echo "<form action=\"ksso_logon.cgi\" method=\"post\" id=\"kssoconnect\">
</form>
<script language=\"JavaScript\" type=\"text/javascript\">
<!--
document.getElementById('kssoconnect').submit();
//-->
</script>"
fi

#Show available pages

