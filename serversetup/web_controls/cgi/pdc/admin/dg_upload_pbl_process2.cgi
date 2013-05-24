#!/bin/bash
#Copyright (C) 2007 Paul Sharrad
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
#  _USERNAME_
#  _PASSWORD1_  Password used for new user
#  _PASSWORD2_  Checked against PASSWORD1 for typos.
#  _GROUP_      This is the primary group for the new user eg yr2000, staff, officestaff.
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_pbl ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_pbl
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="0; URL=/cgi-bin/admin/dg_upload_pbl_fm.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body><div id="actionbox">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=3
#Assign _OVERWRITE_
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = OVERWRITEcheck ]
then
let COUNTER=$COUNTER+1
OVERWRITE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {

echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
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

if [ $OVERWRITE'null' = null ]
then
MESSAGE=$OVERWRITERROR
show_status
fi

if [ $OVERWRITE != no ] && [ $OVERWRITE != yes ]
then
MESSAGE=$OVERWRITERROR
show_status
fi

#########################
#Check data
#########################
#Check input file
[ -d /var/www/karoshi/pbl ] || mkdir -p /var/www/karoshi/pbl
chmod 0700 /var/www/karoshi/
chmod 0700 /var/www/karoshi/pbl
#Check that a file has been uploaded
if [ `dir /var/www/karoshi/pbl --format=single-column | wc -l` != 1 ]
then
MESSAGE=$ERRORMSG1
show_status
fi

PBLFILE=`ls -1 /var/www/karoshi/pbl | sed -n 1,1p`

#Check that the file is a .txt file
if [ `echo "$PBLFILE" | grep -c .txt$` != 1 ]
then
MESSAGE=$ERRORMSG2
show_status
fi
#Remove all spaces and special characters
cat /var/www/karoshi/pbl/"$PBLFILE" | tr -cd 'A-Za-z0-9\._:\-\n' | sed 's/^http://g' > /var/www/karoshi/pbl/pbl1.$$
#Remove http:// and www.
sed 's/^www.//g' /var/www/karoshi/pbl/pbl1.$$ > /var/www/karoshi/pbl/pbl2.$$
echo >> /var/www/karoshi/pbl/pbl2.$$
#Remove empty lines
sed -i '/^$/d' /var/www/karoshi/pbl/pbl2.$$

PBLMD5SUM=`md5sum /var/www/karoshi/pbl/pbl2.$$ | cut -d' ' -f1`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/dg_upload_pbl_process2.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$OVERWRITE:$PBLMD5SUM:pbl2.$$" | sudo -H /opt/karoshi/web_controls/exec/dg_upload_pbl
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 0 ]
then
MESSAGE=`echo $COMPLETEDMSG1`
else
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
fi
show_status
echo "</div></body></html>"
