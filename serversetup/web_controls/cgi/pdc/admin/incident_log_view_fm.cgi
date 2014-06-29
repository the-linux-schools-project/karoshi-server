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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/incident_log ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/incident_log
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
  <title>'$TITLE2'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form action="/cgi-bin/admin/incident_log_view.cgi" name="selectedsites" method="post">
  <div id="actionbox"><div class="sectiontitle">'$TITLE2'</div>
  <br>
  <table class="standard" style="text-align: left; width: 100%;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td><input name="_ALPHABET_" value="A" checked="checked" type="radio">A</td>
        <td><input name="_ALPHABET_" value="B" type="radio">B</td>
        <td><input name="_ALPHABET_" value="C" type="radio">C</td>
        <td><input name="_ALPHABET_" value="D" type="radio">D</td>
        <td><input name="_ALPHABET_" value="E" type="radio">E</td>
        <td><input name="_ALPHABET_" value="F" type="radio">F</td>
        <td><input name="_ALPHABET_" value="G" type="radio">G</td>
        <td><input name="_ALPHABET_" value="H" type="radio">H</td>
        <td><input name="_ALPHABET_" value="I" type="radio">I</td>
        <td><input name="_ALPHABET_" value="J" type="radio">J</td>
        <td><input name="_ALPHABET_" value="K" type="radio">K</td>
        <td><input name="_ALPHABET_" value="L" type="radio">L</td>
      </tr>
      <tr>
        <td><input name="_ALPHABET_" value="M" type="radio">M</td>
        <td><input name="_ALPHABET_" value="N" type="radio">N</td>
        <td><input name="_ALPHABET_" value="O" type="radio">O</td>
        <td><input name="_ALPHABET_" value="P" type="radio">P</td>
        <td><input name="_ALPHABET_" value="Q" type="radio">Q</td>
        <td><input name="_ALPHABET_" value="R" type="radio">R</td>
        <td><input name="_ALPHABET_" value="S" type="radio">S</td>
        <td><input name="_ALPHABET_" value="T" type="radio">T</td>
        <td><input name="_ALPHABET_" value="U" type="radio">U</td>
        <td><input name="_ALPHABET_" value="V" type="radio">V</td>
        <td><input name="_ALPHABET_" value="W" type="radio">W</td>
        <td><input name="_ALPHABET_" value="X" type="radio">X</td>
      </tr>
      <tr>
        <td><input name="_ALPHABET_" value="Y" type="radio">Y</td>
        <td><input name="_ALPHABET_" value="Z" type="radio">Z</td>
        <td><input name="_ALPHABET_" value="0" type="radio">0</td>
        <td><input name="_ALPHABET_" value="1" type="radio">1</td>
        <td><input name="_ALPHABET_" value="2" type="radio">2</td>
        <td><input name="_ALPHABET_" value="3" type="radio">3</td>
        <td><input name="_ALPHABET_" value="4" type="radio">4</td>
        <td><input name="_ALPHABET_" value="5" type="radio">5</td>
        <td><input name="_ALPHABET_" value="6" type="radio">6</td>
        <td><input name="_ALPHABET_" value="7" type="radio">7</td>
        <td><input name="_ALPHABET_" value="8" type="radio">8</td>
        <td><input name="_ALPHABET_" value="9" type="radio">9</td>
      </tr>
      <tr>
        <td><input name="_ALPHABET_" value="ALL" type="radio">All</td>
      </tr>
    </tbody>
  </table>
  <br>
  </div>
  <div id="submitbox"> <input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"> </div>
</form>
</div></body>
</html>
'
exit
