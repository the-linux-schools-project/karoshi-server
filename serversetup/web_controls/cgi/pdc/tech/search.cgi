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
#  _SEARCH_
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/search ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/search
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/tech/search_fm.cgi";'
echo '</script>'
echo "</body></html>"
exit
}
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\%._:\-+'`
#########################
#Assign data to variables
#########################
END_POINT=3
#Assign SEARCH
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SEARCHcheck ]
then
let COUNTER=$COUNTER+1
SEARCH=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

echo "Content-type: text/html"
echo ""
echo "<html><head><title>$TITLE</title></head>"
echo "<link rel="stylesheet" href="/css/$STYLESHEET">"
echo "</head>"
echo "<body>"
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
if [ ! -f /opt/karoshi/web_controls/web_access_tech ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c $REMOTE_USER: /opt/karoshi/web_controls/web_access_tech` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi
#########################
#Check data
#########################

#Check to see that SEARCH is not blank
if [ $SEARCH'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#make sure that the search criteria has at least three spaces
if [ ${#SEARCH} -le 2 ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Sort out spaces
SEARCH=`echo $SEARCH | sed 's/+/ /g'`

echo "<div id="menubox">"
echo "<iframe src="/cgi-bin/tech/menu.cgi" name="main" frameborder="0" width="950" height="150" scrolling="no" marginwidth="0" marginheight="0">"
echo "</iframe><br><br>"

echo '<b>'$TITLE - "$SEARCH"'</b><br><br>'

#Do search
#User
/var/www/cgi-bin_karoshi/tech/user.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#System
/var/www/cgi-bin_karoshi/tech/system.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Client
/var/www/cgi-bin_karoshi/tech/client.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Printer
/var/www/cgi-bin_karoshi/tech/printer.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#File
/var/www/cgi-bin_karoshi/tech/file.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Email
#/var/www/cgi-bin_karoshi/tech/email.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Exams
#/var/www/cgi-bin_karoshi/tech/exams.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Internet
/var/www/cgi-bin_karoshi/tech/internet.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Web
/var/www/cgi-bin_karoshi/tech/web_management.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Bulk user creation
#/var/www/cgi-bin_karoshi/tech/bulk_user_creation.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Backup controls
/var/www/cgi-bin_karoshi/tech/backup.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Monitoring
#/var/www/cgi-bin_karoshi/tech/monitoring.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Linux Client
#/var/www/cgi-bin_karoshi/tech/linux_client.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Windows Client
#/var/www/cgi-bin_karoshi/tech/windows_client.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Asset Register
/var/www/cgi-bin_karoshi/tech/asset_register.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
#Remote Management
/var/www/cgi-bin_karoshi/tech/remote_management.cgi | grep -i "$SEARCH" | grep -i -v html | grep -i -v table
echo "</div>"
echo "</body></html>"
exit
