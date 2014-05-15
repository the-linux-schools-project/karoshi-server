#!/bin/bash
#Copyright (C) 2008 Paul Sharrad

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
#  _GROUP_      This is the primary group for the new user eg yr2000, staff, officestaff.
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/bulk_user_creation ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/bulk_user_creation
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE3'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox">
<B>'$TITLE3'</B>
<br><br>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#GROUP=`echo $DATA | cut -d'_' -f3`

function show_status {

echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/bulk_user_creation_import_enrollment_numbers_fm.cgi"'
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
#Check input file
[ -d /var/www/karoshi/bulk_user_creation_enrollment_numbers ] || mkdir -p /var/www/karoshi/bulk_user_creation_enrollment_numbers
chmod 0700 /var/www/karoshi/
chmod 0700 /var/www/karoshi/bulk_user_creation_enrollment_numbers
if [ `dir /var/www/karoshi/bulk_user_creation_enrollment_numbers --format=single-column | wc -l` != 1 ]
then
MESSAGE=$ERRORMSG12
show_status
fi
CSVFILE=`ls /var/www/karoshi/bulk_user_creation_enrollment_numbers`
echo >> /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE"
cat /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE" | tr -cd 'A-Za-z0-9\.,_:\-\n' > /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE"2
rm -f /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE"
mv /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE"2 /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE"
sed -i '/^$/d' /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE"
CSVFILE_LINES=`cat /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE" | wc -l`
[ -f /var/www/karoshi/bulk_user_creation_enrollment_numbers/karoshi_enrollmentnumbers.csv ] && rm -f /var/www/karoshi/bulk_user_creation_enrollment_numbers/karoshi_enrollmentnumbers.csv
COUNTER=1
while [ $COUNTER -le $CSVFILE_LINES ]
do
USERNAME=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE" | cut -s -d, -f1`
ENROLLMENT_NO=`sed -n $COUNTER,$COUNTER'p' /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE" | cut -s -d, -f2`
if [ $USERNAME'null' = null ] || [ $ENROLLMENT_NO'null' = null ]
then
echo Error on line $COUNTER'<br>'
MESSAGE=`echo $ERRORMSG13`
show_status
fi
echo "$USERNAME","$ENROLLMENT_NO" >> /var/www/karoshi/bulk_user_creation_enrollment_numbers/karoshi_enrollmentnumbers.csv
let COUNTER=$COUNTER+1
done
CSVMDSUM=`md5sum /var/www/karoshi/bulk_user_creation_enrollment_numbers/karoshi_enrollmentnumbers.csv | cut -d' ' -f1`
rm -f /var/www/karoshi/bulk_user_creation_enrollment_numbers/"$CSVFILE"
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/bulk_user_creation_import_enrollment_numbers_process.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$CSVMDSUM:" | sudo -H /opt/karoshi/web_controls/exec/bulk_user_creation_import_enrollment_numbers

echo "</div></div></body></html>"
