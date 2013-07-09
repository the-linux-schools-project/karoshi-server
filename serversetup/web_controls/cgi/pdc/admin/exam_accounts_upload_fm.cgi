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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/exam_accounts_copy_data ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/exam_accounts_copy_data
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <TITLE>'$TITLE1'</TITLE><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</HEAD>
<BODY>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<FORM ENCTYPE="multipart/form-data" ACTION="/cgi-bin/admin/exam_accounts_upload.cgi" METHOD="POST"><div id="actionbox">
<B>'$TITLE1'</B> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Copy_Data_to_Accounts"><img class="images" alt="" src="/images/help/info.png"><td><span>'$UPLOADHELP1'<br><br>'$UPLOADHELP3'</span></a>
<P>
'$OPENINGMSG':
<P>
       
        <TABLE class="standard" BORDER=0 WIDTH="500">
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 1:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-01" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 2:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-02" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 3:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-03" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 4:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-04" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 5:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-05" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 6:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-06" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 7:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-07" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 8:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-08" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 9:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-09" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 10:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-10" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 11:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-11" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 12:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-12" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 13:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-13" SIZE="35">
            </TD>
        </TR>
        <TR>
            <TD ALIGN=RIGHT>
                '$FILEMSG' 14:
            </TD>
            <TD>
                <INPUT TYPE="FILE" NAME="file-to-upload-14" SIZE="35">
            </TD>
        </TR>
		<TR>
			<TD COLSPAN=2>&nbsp;<BR></TD>
		</TR>
        </TABLE>
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div>
        </FORM>
</BODY>
</HTML>
'
exit
