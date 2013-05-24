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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/file/quotas_set ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/file/quotas_set
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
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<form action="/cgi-bin/admin/quotas_set.cgi" name="selectservers" method="post"><b></b>
  <div id="actionbox"><b>'$TITLE'</b>
  <br>
  <br>
<table class="standard" style="text-align: left;" border="0"
 cellpadding="2" cellspacing="2">
  <tbody>
 <tr>
      <td style="width: 180px;">'$USERNAMEMSG'</td>
      <td style="width: 120px;"><input size="20" name="_USERNAME_" style="width: 200px;"></td><td>  <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG6'<br><br>'$HELPMSG7'</span></a></td>
    </tr>
    <tr>
      <td style="width: 180px;">'$GROUPMSG'</td>
      <td style="width: 120px;">'

#Show groups
/opt/karoshi/web_controls/group_dropdown_list

echo '</td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG5'</span></a></td>
    </tr>

<tr><td>Unit</td><td>
<select name="_UNIT_" style="width: 200px;">
<option value="MB" selected="selected">MB</option> 
<option>GB</option>
<option>TB</option>
</select>
</td></tr>
<tr><td style="width: 180px;">'$SIZEMSG'</td><td style="width: 120px;"><input maxlength="3" size="9" name="_SIZE_" style="width: 200px;" value="300"></td>
<td> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'<br><br>'$HELPMSG3'<br><br>'$HELPMSG4'</span></a></td></tr>
<tr>
      <td style="width: 180px;">'$MAXFILESMSG'</td>
      <td style="width: 120px;"><input maxlength="7" size="20" name="_MAXFILES_" style="width: 200px;"
 value="1000"></td><td>  <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'<br><br>'$HELPMSG3'<br><br>'$HELPMSG4'</span></a></td>
    </tr>
  </tbody>
</table>
  </div>
  <div id="submitbox">
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
  </div>
</form>
</body>
</html>
'
exit


<option value="allstudents">'$ALLSTUDENTSMSG'</option>
