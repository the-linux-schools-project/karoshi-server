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
<TITLE>'$"Windows Desktop Icons - Upload"'</TITLE><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</HEAD>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox">
<B>'$"Windows Desktop Icons - Upload"'</B> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Upload_Desktop_Icons"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the icons that you want to upload."'</span></a>
<P>
'$"Select the icons that you want to upload."':
<P>
        <FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/windows_client_icon_upload.cgi" METHOD="POST">
        <TABLE class="standard">
        <TR>
            <TD style="width: 200px;" ALIGN=left>
                '$"Icon"' 1:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=left>
                '$"Icon"' 2:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-02" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=left>
                '$"Icon"' 3:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-03" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=left>
                '$"Icon"' 4:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-04" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=left>
                '$"Icon"' 5:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-05" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=left>
                '$"Icon"' 6:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-06" SIZE="35">
            </TD>
        <TR>
            <TD ALIGN=left>
                '$"Icon"' 7:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-07" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=left>
                '$"Icon"' 8:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-08" SIZE="35">
            </TD>
        </TR>
        </TR>
        </TABLE>
</div>
<div id="submitbox">
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
</form></BODY>
</HTML>
'
exit
