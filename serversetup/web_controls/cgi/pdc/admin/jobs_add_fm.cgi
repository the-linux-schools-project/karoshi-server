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
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/add_user ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/add_user
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi


TITLE="Work Request"
REFERREDMSG="Referred to"

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'

echo '<script type="text/javascript" language="JavaScript"><!--
function activate(field) {
  field.disabled=false;
  if(document.styleSheets)field.style.visibility  = "visible";
  field.focus(); }
function last_choice(selection) {
  return selection.selectedIndex==selection.length - 1; }
function process_choice(selection,textfield) {
  if(last_choice(selection)) {
    activate(textfield); }
  else {
    textfield.disabled = true;    
    if(document.styleSheets)textfield.style.visibility  = "hidden";
    textfield.value = ""; }}
function valid(menu,txt) {
  if(menu.selectedIndex == 0) {
    alert("You must make a selection from the menu");
    return false;} 
  if(txt.value == "") {
    if(last_choice(menu)) {
      alert("You need to type your choice into the text box");
      return false; }
    else {
      return true; }}
  else {
    if(!last_choice(menu)) {
      alert("Incompatible selection");
      return false; }
    else {
      return true; }}}
function check_choice() {
  if(!last_choice(document.demoform.menu)) {
    document.demoform.choicetext.blur();
    alert("Please check your menu selection first");
    document.demoform.menu.focus(); }}
//--></script>'


#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form name="demoform" onsubmit="return valid(this.menu,this.choicetext)" action="/cgi-bin/admin/add_user.cgi" method="post"><div id="actionbox"><div class="sectiontitle">'$TITLE'</div><br><form action="/cgi-bin/admin/add_user.cgi" method="post">'

echo '
  <table class="standard" style="text-align: left; height: 91px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$REFERREDMSG'</td>
        <td>
<select name="menu" onchange=
 "process_choice(this,document.demoform.choicetext)">
<option value="0" selected>(please select:)</option>
<option value="1">one</option>
<option value="2">two</option>
<option value="3">three</option>
<option value="other">other, please specify:</option>

</select>
<noscript>
<input type="text" name="choicetext">
</noscript>

<script type="text/javascript" language="JavaScript"><!--disa = " disabled";
if(last_choice(document.demoform.menu)) disa = "";
document.write("<input type="text" name="choicetext""+disa+" onfocus="check_choice()">");
if(disa && document.styleSheets)
   document.demoform.choicetext.style.visibility  = "hidden";
//--></script>



<select name="s" size="1" onchange="document.ex.state.value = document.ex.s.options[document.ex.s.selectedIndex].value;document.ex.s.value=&#39;&#39;">
 <option value="" selected="selected">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>
             '

#Get list of admins
PERSONNEL1=( `cat /opt/karoshi/web_controls/web_access_admin | cut -d: -f1` )
PERSONNEL2=( `cat /opt/karoshi/web_controls/web_access_tech | cut -d: -f1` )

PERSONNEL=( `echo -e "${PERSONNEL1[@]:0} ${PERSONNEL2[@]:0}"` )

PERSONNEL_COUNT=${#PERSONNEL[@]}
COUNTER=0

while [ $COUNTER -lt $PERSONNEL_COUNT ]
do
echo '<option value="'${PERSONNEL[$COUNTER]}'">'${PERSONNEL[$COUNTER]}'</option>'
let COUNTER=$COUNTER+1
done

echo '</select></div>

      </td></tr>
      <tr>
        <td>
'$SURNAMEMSG'</td>
        <td><input tabindex= "2" value="'$SURNAME'" name="_SURNAME_" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$USERHELP2'</span></a>
      </td></tr>
      <tr>
        <td>
'$PASSWORDMSG'</td>
        <td><input tabindex= "3" name="_PASSWORD1_" size="20" type="password"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$PASSWORDHELP'</span></a>
      </td></tr>
      <tr>
        <td>
'$CONFIRMMSG'</td>
        <td><input tabindex= "4" name="_PASSWORD2_" size="20" type="password"></td>
      </tr>
<tr>
        <td>
'$ENROLLMENTNUMBERMSG'</td>
        <td><input tabindex= "5" value="'$ENROLLMENTNUMBER'" name="_ENROLLMENTNUMBER_" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$ENROLLHELP'</span></a>
      </td></tr>
      <tr>
        <td>'$PRIGROUPMSG'</td>
        <td>'
if [ $FILE'null' = null ]
then
/opt/karoshi/web_controls/group_dropdown_list
else
/opt/karoshi/web_controls/group_dropdown_list | sed 's/<select name="_GROUP_">/<select name="_GROUP_"><option selected="selected">'$GROUP'<\/option>/g'
fi

echo '
        </td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$GROUPHELPMSG'</span></a>
      </td></tr>
<tr>
        <td>'$USERSTYLEMSG'</td>
        <td>
        <select name="_USERNAMESTYLE_">
        <option value="userstyleS1">'$DEFAULTMSG'</option>
        <option value="userstyleS2">'$YRFIRSTMSG'</option>
        <option value="userstyleS3">'$SNAMEFIRSTMSG'</option>
        <option value="userstyleS4">'$FULLNAMEMSG'</option>
        <option value="userstyleS5">'$FNSNAMEFIRSTMSG'</option>
	<option value="">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </option></select>
        </select>
        </td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$USERNAMESTYLEHELP1'<br><br>'$USERNAMESTYLEHELP2'<br><br>'$DEFAULTMSG' - jjones09<br><br>'$YRFIRSTMSG' - 09jjones<br><br>'$SNAMEFIRSTMSG' - jonesj09<br><br>'$FULLNAMEMSG' - john.jones09<br><br>'$FNSNAMEFIRSTMSG' - jones.john09</span></a>
      </td></tr>
    </tbody>
  </table><br><br>
</div>
<div id="submitbox">
<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
</div>
</form>
</div></body>
</html>
'
exit
