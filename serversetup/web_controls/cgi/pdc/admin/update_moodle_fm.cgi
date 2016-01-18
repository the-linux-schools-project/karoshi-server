#!/bin/bash
#Copyright (C) 2008  Paul Sharrad

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <TITLE>'$"Update Moodle"'</TITLE><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</HEAD>
<BODY>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/update_moodle.cgi" METHOD="POST"><div id="actionbox">
<B>'$"Update Moodle"'</B> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"You will need to download a new version of moodle for the update. Use the link provided below."'</span></a> <br><br>
<table class="standard" style="text-align: left; width: 700px; height: 40px;"
 >
  <tbody>
    <tr>
      <td style="width: 300px;"><b>'$"Useful Links"'</b></td>
      <td><b>'$"Description"'</b></td>
    </tr>
    <tr>
      <td style="width: 300px;"><a href="http://download.moodle.org/" target="_blank">http://download.moodle.org/</a></td>
      <td>'$"Latest Moodle Versions"'</td>
    </tr>
    <tr>
      <td><a href="http://docs.moodle.org/en/Upgrading" target="_blank">http://docs.moodle.org/en/Upgrading</a></td>
      <td>'$"Moodle update guide which this feature automates."'</td>
    </tr>
  </tbody>
</table>
<br><br>
'$"IMPORTANT - Make sure that you have a working backup of the following areas on your moodle server before carrying out an upgrade"':<br><br>
/var/www/moodle-data<br>
/var/www/html/moodle<br>
moodle mysql database
<br><br>'$"Choose the moodle archive to upgrade from. The archive MUST be a .tgz."'<br><br>
        

                <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35">
  </div>
<div id="submitbox">
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
        </FORM>
</BODY>
</HTML>
'
exit
