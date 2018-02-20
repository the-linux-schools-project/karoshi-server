#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

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

<!DOCTYPE html>
<html>
<head>
  <title>'$"Web Management - Upload Files"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-.'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
then
let COUNTER=$COUNTER+1
SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "web_management_upload_files_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}



echo '<form action="/cgi-bin/admin/web_management_upload_files_select.cgi" method="post"><div id="actionbox"><span style="font-weight: bold;">
'$"Web Management - Upload Files"' - '$SERVERNAME'</span><br>
  <br>
  <br>
'

#########################
#Check data
#########################
#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
MESSAGE=$"The server cannot be blank."
show_status
fi

#Check to see if any files have been uploaded
if [ `ls -1 /var/www/karoshi/webfiles | wc -l` = 0 ]
then
MESSAGE=$"You have not uploaded any files"
show_status
else
###########################
#Write in indentifier check
###########################
echo $$ > /var/www/karoshi/webfiles/web_management_upload_id
UPLOADID=`echo $$`
Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/web_management_upload_files_select_fm.cgi | cut -d' ' -f1`

echo '<input name="___SERVERNAME___" value="'$SERVERNAME'" type="hidden">'
echo '<input name="___UPLOADID___" value="'$UPLOADID'" type="hidden">'

echo '<table class="standard" style="text-align: left;" >
<tbody><tr><td style="width: 180px;">'$"Web Folder"'</td><td><select name="___UPLOADFOLDER___" style="width: 185px;">'

#Create folder list
echo '<option>/var/www/html</option>'
sudo -H /opt/karoshi/web_controls/exec/web_management_create_folder_list $REMOTE_USER:$REMOTE_ADDR:$Checksum:$SERVERNAME:

echo '
</select></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Please select the folder that you want to upload the files to."'</span></a></td></tr></tbody></table>
</div>
<div id="submitbox">
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></form>
</div></body>
</html>
'
fi
exit
