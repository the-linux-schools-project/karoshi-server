#!/bin/bash
#copy_files_upload
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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <TITLE>'$"Web Management - Upload Files"'</TITLE><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</HEAD>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/web_management_upload_files.cgi" METHOD="POST"><div id="actionbox">
<B>'$"Web Management - Upload Files"'</B> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will upload files so that they are available on a web server You can choose the server you wish to upload the files to."'<br><br>'$"Use the create subfolders option to create extra locations."'</span></a>
<P>
'$"Please choose the files that you want to upload to the web area."'
<P>

        <TABLE class="standard">
        <tr>
            <td>
                '$"File"' 1:
            </td>
            <TD>
                <input type="file" name="file-to-upload-01" SIZE="25">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 2:
            </td>
            <TD>
                <input type="file" name="file-to-upload-02" SIZE="25">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 3:
            </td>
            <TD>
                <input type="file" name="file-to-upload-03" SIZE="25">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 4:
            </td>
            <TD>
                <input type="file" name="file-to-upload-04" SIZE="25">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 5:
            </td>
            <TD>
                <input type="file" name="file-to-upload-05" SIZE="25">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 6:
            </td>
            <TD>
                <input type="file" name="file-to-upload-06" SIZE="25">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 7:
            </td>
            <TD>
                <input type="file" name="file-to-upload-07" SIZE="25">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 8:
            </td>
            <TD>
                <input type="file" name="file-to-upload-08" SIZE="25">
            </td>
        </tr>
		<tr>
			<TD COLSPAN=2>&nbsp;<BR></td>
		</tr>
        </TABLE>
</div><div id="submitbox">
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></form></div></div>
</body>
</html>
'
exit
