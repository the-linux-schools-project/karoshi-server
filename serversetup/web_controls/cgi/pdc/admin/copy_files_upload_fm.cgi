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
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [[ $(echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT") = 1 ]]
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
    <TITLE>'$"Copy Files - upload"'</TITLE><meta http-equiv="REFRESH" content="'"$TIMEOUT"'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/user/groups.png

echo '<FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/copy_files_upload.cgi" METHOD="POST"><div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"Copy Files"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Label_Groups"><img class="images" alt="" src="/images/help/info.png"><span>'$"This will copy files into all of the user home areas for the group that you choose."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<button class="info infonavbutton" formaction="groups.cgi" name="_ViewNewPasswords_" value="_">
			<img src="'"$ICON1"'" alt="'$"Group Management"'">
			<span>'$"Manage groups."'</span><br>
			'$"Group Management"'
		</button>
	</td>

</tr></tbody></table></div><div id="infobox">
<br>
<P>
'$"Select the files that you want to upload to a group"':
</P>
        
        <table class="tablesorter" style="text-align: left; height: 91px;" >
        <TR>
            <TD>
                '$"File"' 1:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD>
                '$"File"' 2:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-02" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD>
                '$"File"' 3:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-03" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD>
                '$"File"' 4:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-04" SIZE="35">
            </TD>
        </TR>
        </TABLE>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></div>
</FORM>
</div>
</BODY>
</HTML>
'
exit
