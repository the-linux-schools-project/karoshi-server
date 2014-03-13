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

############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/ssl_certs ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/ssl_certs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%+' | sed 's/___/TRIPLESCORED/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLESCORED/_/g'`
#########################
#Assign data to variables
#########################

BACKMSG=Back


END_POINT=26
#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
then
let COUNTER=$COUNTER+1
SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
then
let COUNTER=$COUNTER+1
ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign COUNTRYCODE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = COUNTRYCODEcheck ]
then
let COUNTER=$COUNTER+1
COUNTRYCODE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign STATE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = STATEcheck ]
then
let COUNTER=$COUNTER+1
STATE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign LOCALITY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LOCALITYcheck ]
then
let COUNTER=$COUNTER+1
LOCALITY=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign INSTITUTENAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = INSTITUTENAMEcheck ]
then
let COUNTER=$COUNTER+1
INSTITUTENAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign DEPARTMENT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DEPARTMENTcheck ]
then
let COUNTER=$COUNTER+1
DEPARTMENT=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign COMMONNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = COMMONNAMEcheck ]
then
let COUNTER=$COUNTER+1
COMMONNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign EMAIL
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = EMAILcheck ]
then
let COUNTER=$COUNTER+1
EMAIL=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

#Assign CERTTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CERTTYPEcheck ]
then
let COUNTER=$COUNTER+1
CERTTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/UNDERSCORE/_/g'`
break
fi
let COUNTER=$COUNTER+1
done

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

#Assign CACERT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CACERTcheck ]
then
let COUNTER=$COUNTER+1
CACERT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign SSLCERT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SSLCERTcheck ]
then
let COUNTER=$COUNTER+1
SSLCERT=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/ssl_commercial_certs_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
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

if [ -z "$SERVERNAME" ]
then
MESSAGE=$ERRORMSG1
show_status
fi

if [ $ACTION = createcert ]
then
#Check to see that COUNTRYCODE is not blank
if [ $COUNTRYCODE'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Check to see that STATE is not blank
if [ $STATE'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi
#Check to see that LOCALITY is not blank
if [ $LOCALITY'null' = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi
#Check to see that INSTITUTENAME is not blank
if [ $INSTITUTENAME'null' = null ]
then
MESSAGE=$ERRORMSG5
show_status
fi
#Check to see that DEPARTMENT is not blank
if [ $DEPARTMENT'null' = null ]
then
MESSAGE=$ERRORMSG6
show_status
fi
#Check to see that COMMONNAME is not blank
if [ $COMMONNAME'null' = null ]
then
MESSAGE=$ERRORMSG7
show_status
fi
#Check to see that EMAIL is not blank
if [ $EMAIL'null' = null ]
then
MESSAGE=$ERRORMSG8
show_status
fi

STATE=`echo $STATE | sed 's/+/ /g'`
LOCALITY=`echo $LOCALITY | sed 's/+/ /g'`
INSTITUTENAME=`echo $INSTITUTENAME | sed 's/+/ /g'`
DEPARTMENT=`echo $DEPARTMENT | sed 's/+/ /g'`
COMMONNAME=`echo $COMMONNAME | sed 's/+/ /g'`
EMAIL=`echo $EMAIL | sed 's/+/ /g'`

fi

if [ $ACTION = installcertinfo ]
then
#Check to see that CERTTYPE is not blank
if [ -z "$CERTTYPE" ]
then
MESSAGE=$ERRORMSG17
show_status
fi
if [ -z "$CACERT" ]
then
MESSAGE=$ERRORMSG15
show_status
fi
if [ -z "$SSLCERT" ]
then
MESSAGE=$ERRORMSG16
show_status
fi
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/ssl_commercial_certs.cgi | cut -d' ' -f1`

if [ $ACTION = getcertdetails ]
then
echo "<b>"$TITLE1 - $SERVERNAME"</b><br><br>"
#Get current certificate data if it has been set
source /etc/default/locale
source /opt/karoshi/server_network/domain_information/domain_name

COUNTRYCODE=`echo $LANG | cut -d_ -f2 | cut -d. -f1`
STATE=`cat /etc/timezone | cut -d/ -f1`
LOCALITY=`cat /etc/timezone | cut -d/ -f2`
UNITNAME=$SERVERNAME
ORGANISATIONNAME=$REALM

if [ -f /opt/karoshi/server_network/aliases/$SERVERNAME ] 
then
ALIAS=`sed -n 1,1p /opt/karoshi/server_network/aliases/$SERVERNAME`
LOCALNAME=$ALIAS.$REALM
COMMONNAME=$ALIAS.$REALM
else
LOCALNAME=$SERVERNAME
COMMONNAME=$SERVERNAME
fi

CONTACTEMAIL=administrator@$REALM

if [ -f /opt/karoshi/server_network/ssl/cert_data/$SERVERNAME ]
then
COUNTRYCODE=`sed -n 1,1p /opt/karoshi/server_network/ssl/cert_data/$SERVERNAME`
STATE=`sed -n 2,2p /opt/karoshi/server_network/ssl/cert_data/$SERVERNAME`
LOCALITY=`sed -n 3,3p /opt/karoshi/server_network/ssl/cert_data/$SERVERNAME`
ORGANISATIONNAME=`sed -n 4,4p /opt/karoshi/server_network/ssl/cert_data/$SERVERNAME`
UNITNAME=`sed -n 5,5p /opt/karoshi/server_network/ssl/cert_data/$SERVERNAME`
COMMONNAME=`sed -n 6,6p /opt/karoshi/server_network/ssl/cert_data/$SERVERNAME`
CONTACTEMAIL=`sed -n 7,7p /opt/karoshi/server_network/ssl/cert_data/$SERVERNAME`
fi

#Check to see if a ca cert has already been created and show warning message.
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:checkservercsr:" | sudo -H /opt/karoshi/web_controls/exec/ssl_commercial_certs
if [ $? = 105 ]
then
echo '<font color="red"><b>'$WARNINGMSG'<br><br>
'$ERRORMSG18'<br>'$ERRORMSG19'</b></font><br><br>'
fi

echo '<form action="/cgi-bin/admin/ssl_commercial_certs.cgi" name="selectservers" method="post">
<input type="hidden" name="___ACTION___" value="createcert"><input name="___SERVERNAME___" value="'$SERVERNAME'" type="hidden">
<table class="standard"><tbody>'
echo '<tr><td style="width: 180px;">'$COUNTRYCODEMSG'</td><td><input tabindex= "1" value="'$COUNTRYCODE'" name="___COUNTRYCODE___" maxlength="2" size="30" type="text"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$COUNTRYCODEHELP'<br><br>'$COMMONNAMEHELP2'</span></a></td>
</tr>
<tr><td>'$STATEMSG'</td><td><input tabindex= "2" value="'$STATE'" name="___STATE___" size="30" type="text"></td></tr>
<tr><td>'$CITYMSG'</td><td><input tabindex= "3" value="'$LOCALITY'" name="___LOCALITY___" size="30" type="text"></td></tr>
<tr><td>'$SCHOOLMSG'</td><td><input tabindex= "4" value="'$ORGANISATIONNAME'" name="___INSTITUTENAME___" size="30" type="text"></td></tr>
<tr><td>'$DEPTNAMEMSG'</td><td><input tabindex= "5" value="'$UNITNAME'" name="___DEPARTMENT___" size="30" type="text"></td></tr>
<tr><td>'$COMMONNAMEMSG'</td><td><input tabindex= "6" value="'$COMMONNAME'" name="___COMMONNAME___" size="30" type="text"></td>
<td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$COMMONNAMEHELP'<br><br>'$COMMONNAMEHELP2'</span></a></td>
</tr>
<tr><td>'$EMAILMSG'</td><td><input tabindex= "7" value="'$CONTACTEMAIL'" name="___EMAIL___" size="30" type="text"></td></tr>
</tbody></table><br><br>
<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"> <a href="ssl_commercial_certs_fm.cgi"><input class="button" type="button" name="" value="'$BACKMSG'"></a>
</form></div></div></div></body></html>'

exit
fi

if [ $ACTION = copycertinfo ]
then
echo "<b>"$TITLE5 - $SERVERNAME"</b><br><br>$HELPMSG5<br><br>"
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$ACTION:" | sudo -H /opt/karoshi/web_controls/exec/ssl_commercial_certs
echo '<br><br><a href="ssl_commercial_certs_fm.cgi"><input class="button" type="button" name="" value="'$BACKMSG'"></a></div></div></div></body></html>'
exit
fi

if [ $ACTION = getinstallcertinfo ]
then
echo '<form action="/cgi-bin/admin/ssl_commercial_certs.cgi" name="selectservers" method="post"><b>'$TITLE7' - '$SERVERNAME'</b><br><br>'$HELPMSG6'<br><br></div><div id="infobox">'

#Drop down choice for cert types

echo '<input type="hidden" name="___ACTION___" value="installcertinfo"><input name="___SERVERNAME___" value="'$SERVERNAME'" type="hidden"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 360px;"><b>'$CERTTYPEMSG'</b></td><td>
<select name="___CERTTYPE___" style="width: 200px;">
	<option></option>
        <option value="intcert">'$INTERMEDIATECERTMSG'</option>
        <option value="bundle">'$CERTBUNDLEMSG'</option>
</select></td></tr></tbody></table>
'

echo '<textarea cols="80" rows="14" name="___CACERT___"></textarea><br><br>'
echo "<b>"$SSLCERTMSG"</b><br><br>"
echo '<textarea cols="80" rows="14" name="___SSLCERT___"></textarea><br><br><input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
<a href="ssl_commercial_certs_fm.cgi"><input class="button" type="button" name="" value="'$BACKMSG'"></a>
'
echo '</div></form></div></body></html>'
exit
fi

if [ $ACTION = installcertinfo ]
then
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$ACTION::::::::$CERTTYPE:$CACERT:$SSLCERT:" | sudo -H /opt/karoshi/web_controls/exec/ssl_commercial_certs
MESSAGE="$COMPLETEDMSG"
show_status
exit
fi

echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$ACTION:$COUNTRYCODE:$STATE:$LOCALITY:$INSTITUTENAME:$DEPARTMENT:$COMMONNAME:$EMAIL:" | sudo -H /opt/karoshi/web_controls/exec/ssl_commercial_certs

if [ $ACTION = createcert ]
then
MESSAGE="$HELPMSG3"
show_status
fi

#STATUS=`echo $?`
#if [ $STATUS = 101 ]
#then
#MESSAGE=$ERRORMSG9
#show_status
#fi
#if [ $STATUS = 102 ]
#then
#MESSAGE=$SSHWARNMSG
#show_status
#fi
#MESSAGE=$COMPLETEDMSG2
#show_status
exit
