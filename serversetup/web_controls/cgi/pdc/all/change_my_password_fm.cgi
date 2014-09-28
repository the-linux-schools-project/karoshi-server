#!/bin/bash
#Change my password
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
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Change My Password"'</title>
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<META HTTP-EQUIV="refresh" CONTENT="300; URL=/cgi-bin/blank.cgi">
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head><body><div id="pagecontainer">'

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_all
else
DIV_ID=actionbox2
fi

echo '<form action="/cgi-bin/all/change_my_password.cgi" method="post"><div id="'$DIV_ID'">'

#Get password strength settings
source /opt/karoshi/server_network/security/password_settings

if [ $STAFF_UPPER_AND_LOWER_CASE = yes ]
then
STAFFCASECHECKMSG=$"Upper and lower case characters required."
else
STAFFCASECHECKMSG=$"Upper and lower case characters not required."
fi

if [ $STUDENT_UPPER_AND_LOWER_CASE = yes ]
then
STUDENTCASECHECKMSG=$"Upper and lower case characters required."
else
STUDENTCASECHECKMSG=$"Upper and lower case characters not required."
fi

if [ $STAFF_CHARS_AND_NUMBERS = yes ]
then
STAFFCHARCHECKMSG=$"Characters and numbers required."
else
STAFFCHARCHECKMSG=$"Characters and numbers not required."
fi

if [ $STUDENT_CHARS_AND_NUMBERS = yes ]
then
STUDENTCHARCHECKMSG=$"Characters and numbers required."
else
STUDENTCHARCHECKMSG=$"Characters and numbers not required."
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$"Back"MSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/menu.cgi"><b>'$"Change My Password"'</b></a></td></tr></tbody></table><br>'
else
echo '<b>'$"Change My Password"'</b><br><br>'
fi

if [ $MOBILE = yes ]
then

echo ''$"Username"'<br>
<input tabindex= "1" name="_USERNAME_" size="20" type="text"><br>
'$"Current Password"'<br>
<input tabindex= "2" name="_PASSWORD1_" size="20" type="password"><br>
'$"New Password"'<br>
<input tabindex= "3" name="_PASSWORD2_" size="20" type="password"><br><br>
'

else

echo '<table class="standard" style="text-align: left; width: 399px; height: 76px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td>
'$"Username"'</td>

        <td><input tabindex= "1" name="____USERNAME____" size="20" type="text"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Please enter in your username."'</span></a></td>
      </tr>
      <tr>
        <td>
'$"Current Password"'</td>
        <td><input tabindex= "2" name="____PASSWORD1____" size="20" type="password"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the password that you use to log into the system."'</span></a></td>
      </tr>
      <tr>
        <td>
'$"New Password"'</td>
        <td><input tabindex= "3" name="____PASSWORD2____" size="20" type="password"></td><td><a class="info2" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the new password that you want to have."'<br><br><b>'$"Student Password Requirements"'</b><br><br>'$"Required password length"': '$STUDENT_MINPASSLENGTH'<br>'$STUDENTCASECHECKMSG'<br>'$STUDENTCHARCHECKMSG'<br><br><b>'$"Staff Password Requirements"'</b><br><br>'$"Required password length"': '$STAFF_MINPASSLENGTH'<br>'$STAFFCASECHECKMSG'<br>'$STAFFCHARCHECKMSG'<br><br><b>'$"Allowed Special Characters"'</b><br><br>'$"The following special characters are allowed"'<br><br> space !	"	# 	$	%	& 	(	) 	*	+	, 	-	.	/ 	:
;	<	=	>	?	@ 	[	\	]	^	_	` 	{	|	}	~</span></a></td>
      </tr>
       <tr>
        <td>
'$"Confirm New Password"'</td>
        <td><input tabindex= "4" name="____PASSWORD3____" size="20" type="password"></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in your new password again here."'</span></a></td>
      </tr>
    </tbody>
  </table>
  <br>'
fi

if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
fi

echo '<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></div></form></div></body></html>'
exit
