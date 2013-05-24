#!/bin/bash
#Copyright (C) 2008  Paul Sharrad
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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/label_groups ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/label_groups
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
source /opt/karoshi/web_controls/group_dropdown_def
#Check if timout should be disabled
if [ `echo $REMOTE___ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi

YEAR=`date +%Y`
let STARTYEAR=$YEAR-9
let ENDYEAR=$YEAR+2

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/label_groups.cgi" method="post"><div id="actionbox"><b>'$TITLE'</b> 
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Label_Groups"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>

<br><br>
<table class="standard" style="text-align: left;" border="0"
 cellpadding="2" cellspacing="2">
<tbody><tr><td style="vertical-align: top; width: 200px;">'

#Student groups
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>'

while [ $STARTYEAR -lt $ENDYEAR ]
do
eval LABEL=\$YR${STARTYEAR}
echo '<tr><td>yr'$STARTYEAR'</td><td><input maxlength="20" size="10" name="____YR'$STARTYEAR':" value="'$LABEL'"></td></tr>'
let STARTYEAR=$STARTYEAR+1
done 
echo '</tbody></table>'
echo '</td><td style="vertical-align: top; width: 200px;">'

#Personnel
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td>guests</td><td><input maxlength="20" size="10" name="____GUESTS:" value="'$GUESTS'"></td></tr>
<tr><td>staff</td><td><input maxlength="20" size="10" name="____STAFF:" value="'$STAFF'"></td></tr>
<tr><td>staff2</td><td><input maxlength="20" size="10" name="____STAFF2:" value="'$STAFF2'"></td></tr>
<tr><td>staff3</td><td><input maxlength="20" size="10" name="____STAFF3:" value="'$STAFF3'"></td></tr>
<tr><td>staff4</td><td><input maxlength="20" size="10" name="____STAFF4:" value="'$STAFF4'"></td></tr>
<tr><td>nonteachingstaff</td><td><input maxlength="20" size="10" name="____NONTEACHINGSTAFF:" value="'$NONTEACHINGSTAFF'"></td></tr>
<tr><td>officestaff</td><td><input maxlength="20" size="10" name="____OFFICESTAFF:" value="'$OFFICESTAFF'"></td></tr>
<tr><td>studentstaff</td><td><input maxlength="20" size="10" name="____STUDENTSTAFF:" value="'$STUDENTSTAFF'"></td></tr>
<tr><td>guardians</td><td><input maxlength="20" size="10" name="____GUARDIANS:" value="'$GUARDIANS'"></td></tr>
<tr><td>tech</td><td><input maxlength="20" size="10" name="____TECH:" value="'$TECH'"></td></tr>
<tr><td>itadmin</td><td><input maxlength="20" size="10" name="____ITADMIN:" value="'$ITADMIN'"></td></tr>
</tbody></table>
'

#Custom groups
echo '</td><td style="vertical-align: top; width: 200px;">'
if [ -d /opt/karoshi/server_network/group_information/optional_groups/ ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>'
for OPTGROUPS in /opt/karoshi/server_network/group_information/optional_groups/*
do
OPTGROUP=`basename $OPTGROUPS`
eval LABEL=\$OPT${OPTGROUP}
echo '<tr><td>'$OPTGROUP'</td><td><input maxlength="20" size="10" name="____OPT'$OPTGROUP':" value="'$LABEL'"></td></tr>'
done
echo '</tbody></table>'
fi


echo '</tbody></table>'

echo '</div>
<div id="submitbox">
<input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div>
</form>
</body>
</html>
'
exit

