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
<body onLoad=start() ">div id=pagecontainer>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/exam_accounts_upload.cgi" METHOD="POST"><div id="actionbox">
<B>'$"Exam Accounts - Upload Files"'</B> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Copy_Data_to_Exam_Accounts"><img class="images" alt="" src="/images/help/info.png"><td><span>'$"The uploaded files will be copied to a folder called exam_files in each exam account."'<br><br>'$"Any .zip or .tar.gz files will automatically be extracted in each exam home folder."'</span></a>
<P>
'$"Please select the files that you want to upload for the exam accounts"':
<P>
       
        <TABLE class="standard" BORDER=0 WIDTH="500">
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 1:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 2:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-02" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 3:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-03" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 4:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-04" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 5:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-05" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 6:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-06" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 7:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-07" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 8:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-08" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 9:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-09" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 10:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-10" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 11:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-11" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 12:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-12" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 13:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-13" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$"File"' 14:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-14" SIZE="35">
            </TD>
        </TR>
		<TR>
			<TD COLSPAN=2>&nbsp;<BR></TD>
		</TR>
        </TABLE>
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div>
        </FORM>
        </div>
</BODY>
</HTML>
'
exit
