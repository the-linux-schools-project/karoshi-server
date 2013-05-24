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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/web/upload_files ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/web/upload_files
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

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign WEBSERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = WEBSERVERcheck ]
then
let COUNTER=$COUNTER+1
WEBSERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "web_management_upload_files_fm.cgi";'
echo '</script>'
echo "</body></html>"
exit
}



echo '<div id="actionbox">
<form action="/cgi-bin/admin/web_management_upload_files_select.cgi" method="post"><span style="font-weight: bold;">
'$TITLE' - '$WEBSERVER'</span><br>
  <br>
  <br>
'

#########################
#Check data
#########################
#Check to see that WEBSERVER is not blank
if [ $WEBSERVER'null' = null ]
then
MESSAGE=$ERRORMSG5
show_status
fi

#Check to see if any files have been uploaded
if [ `ls -1 /var/www/karoshi/webfiles | wc -l` = 0 ]
then
MESSAGE=$ERRORMSG1
show_status
else
###########################
#Write in indentifier check
###########################
echo $$ > /var/www/karoshi/webfiles/web_management_upload_id
UPLOADID=`echo $$`
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/web_management_upload_files_select_fm.cgi | cut -d' ' -f1`

echo '<input name="___WEBSERVER___" value="'$WEBSERVER'" type="hidden">'
echo '<input name="___UPLOADID___" value="'$UPLOADID'" type="hidden">'

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: 180px;">'$FOLDERMSG'</td><td><select name="___UPLOADFOLDER___" style="width: 185px;">'

#Create folder list
sudo -H /opt/karoshi/web_controls/exec/web_management_create_folder_list $REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$WEBSERVER:

echo '
</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$FOLDERHELPMSG'</span></a></td></tr></tbody></table>
</div>
<div id="submitbox">
<input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div>
</body>
</html>
'
fi
exit
