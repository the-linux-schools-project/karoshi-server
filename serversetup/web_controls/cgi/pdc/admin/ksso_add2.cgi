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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><meta http-equiv="REFRESH" content="0;url=ksso_view_fm.cgi"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`
DATA=`echo $DATA | sed 's/___/TRIPLEUNDERSCORE/g' | sed 's/_/UNDERSCORE/g' | sed 's/TRIPLEUNDERSCORE/_/g'`
#Assign data to array
DATAARRAY=( `echo $DATA | sed 's/_FORMDATA_/ /g'` )
ARRAYCOUNT=${#DATAARRAY[@]}

#########################
#Assign data to variables
#########################
END_POINT=13
#Assign ENTRYNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ENTRYNAMEcheck ]
then
let COUNTER=$COUNTER+1
ENTRYNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign LOGONPAGE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LOGONPAGEcheck ]
then
let COUNTER=$COUNTER+1
LOGONPAGE=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
ICON=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign DESTINATION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DESTINATIONcheck ]
then
let COUNTER=$COUNTER+1
DESTINATION=`echo $DATA | cut -s -d'_' -f$COUNTER`
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
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/ksso_add2.cgi | cut -d' ' -f1`
#########################
#Check data
#########################

#Check to see that ENTRYNAME is not blank
if [ $ENTRYNAME'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that LOGONPAGE is not blank
if [ $LOGONPAGE'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Check to see that ICON is not blank
if [ $ICON'null' = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Check to see that Destination is not blank
if [ $DESTINATION'null' = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi

#Add entry
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ENTRYNAME:$ICON:$DESTINATION:$LOGONPAGE:${DATAARRAY[@]:0}:" | sudo -H /opt/karoshi/web_controls/exec/ksso_add

exit



