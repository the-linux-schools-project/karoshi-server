#!/bin/bash
#Copyright (C) 2010  Paul Sharrad
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
DATE_INFO=`date +%F`
DAY=`echo $DATE_INFO | cut -d- -f3`
MONTH=`echo $DATE_INFO | cut -d- -f2`
YEAR=`echo $DATE_INFO | cut -d- -f1`

[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/samba_view_logs ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/samba_view_logs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE2'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'">
<script language="JavaScript" src="/all/calendar2/calendar_eu.js" type="text/javascript"></script>
        <!-- Timestamp input popup (European Format) -->

<link rel="stylesheet" href="/all/calendar2/calendar.css">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/samba_logs_computer.cgi" name="testform" method="post"><b></b>
  <div id="actionbox"><b>'$TITLE2'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>
<br><br>

<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 180px;">'$COMPUTERMSG'</td><td><input tabindex= "1" name="_MACHINE_" size="14" type="text"></td><td style="vertical-align: top; text-align: center;"><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG4'</span></a></td></tr>'
echo "<tr><td>$LOGDATE</td><td>
<!-- calendar attaches to existing form element -->
	<input type=\"text\" value=\"$DAY-$MONTH-$YEAR\" size=14 maxlength=10 name=\"_DATE_\"></td><td style=\"vertical-align: top; text-align: center;\">
	<script language=\"JavaScript\" type=\"text/javascript\">
	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': '_DATE_'
	});

	</script></td></tr>"

echo '<tr><td>'$LOGCOUNTMSG'</td><td><input tabindex= "1" name="_DAYCOUNT_" maxlength="2" size="2" value="1" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a></td></tr>
</tbody></table>
  </div>
  <div id="submitbox">
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
  </div>
</form>
</body>
</html>
'
exit
