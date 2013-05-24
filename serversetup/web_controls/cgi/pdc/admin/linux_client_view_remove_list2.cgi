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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_view_remove_list ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/linux_client_view_remove_list
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
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">'
echo '<link rel="stylesheet" href="/css/'$STYLESHEET'">'
echo '<script type="text/javascript">'
echo '<!--'
echo 'function SetAllCheckBoxes(FormName, FieldName, CheckValue)'
echo '{'
echo '	if(!document.forms[FormName])'
echo '		return;'
echo '	var objCheckBoxes = document.forms[FormName].elements[FieldName];'
echo '	if(!objCheckBoxes)'
echo '		return;'
echo '	var countCheckBoxes = objCheckBoxes.length;'
echo '	if(!countCheckBoxes)'
echo '		objCheckBoxes.checked = CheckValue;'
echo '	else'
echo '		// set the check value for all check boxes'
echo '		for(var i = 0; i < countCheckBoxes; i++)'
echo '			objCheckBoxes[i].checked = CheckValue;'
echo '}'
echo '// -->'
echo '</script><script src="/all/stuHover.js" type="text/javascript"></script>'
echo "</head><body>"
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=4
#Assign LINUXVERSION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LINUXVERSIONcheck ]
then
let COUNTER=$COUNTER+1
LINUXVERSION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done


function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/linux_client_view_remove_list.cgi";'
echo '</script>'
echo "</body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$ERRORMSG1
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
#Check to see that LINUXVERSION is not blank
if [ $LINUXVERSION'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/linux_client_view_remove_list3.cgi" name="selectedsoftware" method="post"><b></b>'
echo '<div id="actionbox">'
echo '<input type="hidden" name="_LINUXVERSION_" value="'$LINUXVERSION'">'
echo '<b>'$TITLE' - '$LINUXVERSION'</b><br><br>'
if [ -f /var/lib/samba/netlogon/linuxclient/$LINUXVERSION/remove_list ]
then
INSTALLCOUNT=`cat /var/lib/samba/netlogon/linuxclient/$LINUXVERSION/remove_list | wc -l`
COUNTER=1
if [ $INSTALLCOUNT -gt 0 ]
then
#Show table of sites
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td style="width: 250px;"><b>'$INSTALLMSG'</b></td><td><b>'$REMOVEMSG'</b></td></tr>'
while [ $COUNTER -le $INSTALLCOUNT ]
do
SOFTWAREDATA=`sed -n $COUNTER,$COUNTER"p" /var/lib/samba/netlogon/linuxclient/$LINUXVERSION/remove_list`
echo '<tr><td>'$SOFTWAREDATA'</td><td><input name="_REMOVENAME_" value="'$SOFTWAREDATA'" type="checkbox"></td></tr>'
let COUNTER=$COUNTER+1
done
echo "</tbody>"
echo "</table>"
echo '<input value="Submit" type="submit">'
echo '<input value="Reset" type="reset">'
echo '<input type="button" onclick="SetAllCheckBoxes('"'"selectedsoftware"'", "'"_REMOVENAME_"'", true');" value="Select all">'
else
echo $ERRORMSG2'<br>'
fi
else
echo $ERRORMSG2'<br>'
fi
echo '</div>'
echo '</form>'
echo "</body></html>"
exit
