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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <TITLE>'$"Exam Accounts - Upload Files"'</TITLE><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</HEAD>
<body onLoad=start()><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/exam_accounts_upload.cgi" METHOD="POST"><div id="actionbox3"><div id="titlebox">

<table class="standard" style="text-align: left;" ><tbody>
<tr><td><div class="sectiontitle">'$"Exam Accounts - Upload Files"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Exam_Accounts#Copy_Data_to_Exam_Accounts"><img class="images" alt="" src="/images/help/info.png"><span>'$"The uploaded files will be copied to a folder called exam_files in each exam account."'</span></a></td></tr></tbody></table><br>
<P>
'$"Please select the files that you want to upload for the exam accounts"':
<P>
       
        <TABLE class="standard">
        <tr>
            <td>
                '$"File"' 1:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 2:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-02" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 3:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-03" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 4:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-04" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 5:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-05" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 6:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-06" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 7:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-07" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 8:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-08" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 9:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-09" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 10:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-10" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 11:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-11" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 12:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-12" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 13:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-13" SIZE="35">
            </td>
        </tr>
        <tr>
            <td>
                '$"File"' 14:
            </td>
            <td>
                <INPUT TYPE="FILE" NAME="file-to-upload-14" SIZE="35">
            </td>
        </tr>
		<tr>
			<TD COLSPAN=2>&nbsp;<BR></td>
		</tr>
        </TABLE>
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></div>
        </FORM>
        </div>
</BODY>
</HTML>
'
exit
