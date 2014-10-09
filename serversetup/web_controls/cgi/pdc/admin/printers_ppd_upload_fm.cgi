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
if [ `echo $REMOTE_ADDR | grep -c "$NOTIMEOUT"` = 1 ]
then
TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <TITLE>'$"Upload PPD file"'</TITLE><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/printers.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}
#Get printer details
if [ ! -f /var/www/karoshi/uploadppd ]
then
MESSAGE=$"No Printer details found."
show_status
fi
source /var/www/karoshi/uploadppd

echo '<div id="actionbox">
<B>'$"Upload PPD file"'</B> <a target="_blank" href="http://openprinting.org/printer_list.cgi"><img src="/images/help/info.png" border="0"></a>
<br><br>
<table class="standard" style="text-align: left; height: 120px;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: middle; width: 180px;">'$"Printer"'</td><td>'$PRINTERNAME'</td></tr>
<tr><td style="vertical-align: middle;">'$"Default Page Size"'</td><td>'$PAGESIZE'</td></tr>
<tr><td style="vertical-align: middle;">'$"Print in Colour?"'</td><td>'$COLOUR'</td></tr>
<tr><td style="vertical-align: top;">'$"Printer PPD"'</td><td style="vertical-align: middle;"><FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/printers_ppd_upload.cgi" METHOD="POST">
 <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="25">
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"If you are using a Linux client with cups installed you can find ppd files in /usr/share/cups/models or /usr/share/ppd."'</span></a></td></tr>
</tbody></table><br>
  </div>
<div id="submitbox">
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
        </form>
</div></body>
</html>
'
exit
