#!/bin/bash
#Delete User
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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

############################
#Language
############################
SHUTDOWN_CODE=`echo ${RANDOM:0:3}`
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/delete_user ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/delete_user
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
  <title>'$TITLE'</title><META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE"><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script type="text/javascript" src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
		***********************************************/
	</script>
	<script type="text/javascript">
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head>
<body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=5
#Assign username
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
then
let COUNTER=$COUNTER+1
USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#FILE
COUNTER=2
END_POINT=8
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
then
let COUNTER=$COUNTER+1
FILE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
fi


echo '
<form action="/cgi-bin/admin/delete_user.cgi" method="post">
<input name="_FORMCODE_" value="'$SHUTDOWN_CODE'" type="hidden">'

[ $MOBILE = no ]  && echo '<div id="'$DIV_ID'"><div id="titlebox">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$USERMENUMSG'</a>
</div></div>
'
else
echo '<div class="sectiontitle">'$TITLE'</div><br></div><div id="infobox">'
fi

#Check that this server is not part of a federated setup
if [ -f /opt/karoshi/server_network/servers/$HOSTNAME/federated_server ]
then
echo $ERRORMSG9 '</div></div></body></html>'
exit
fi


#Get request data if asked
if [ $FILE'null' != null ]
then
if [ -f /opt/karoshi/user_requests/delete_users/$FILE ]
then
NEW_USER_DATA=`sed -n 1,1p /opt/karoshi/user_requests/delete_users/$FILE`
FORENAME=`echo $NEW_USER_DATA | cut -d: -f1`
SURNAME=`echo $NEW_USER_DATA | cut -d: -f2`
GROUP=`echo $NEW_USER_DATA | cut -d: -f3`
echo '<input name="_REQUESTFILE_" value="'$FILE'" type="hidden">'
#Try and get username

if [ `echo $GROUP | grep -c ^yr` -gt 0 ]
then
GROUPCHARCOUNT=`echo $GROUP | wc -c`
let GROUPCHARCOUNT=$GROUPCHARCOUNT-1
let GROUPSTARTCHAR=$GROUPCHARCOUNT-2
USERNAME=`echo ${FORENAME:0:1}$SURNAME${GROUP:$GROUPSTARTCHAR:$GROUPCHARCOUNT} | tr 'A-Z' 'a-z'`
else
USERNAME=`echo ${FORENAME:0:1}$SURNAME | tr 'A-Z' 'a-z'`
fi
fi
fi

if [ $MOBILE = yes ]
then
echo '<div id="mobileactionbox">'
echo '<div id="suggestions"></div>
'$USERNAMEMSG'<br>
<input tabindex= "1" style="width: 160px;" name="_USERNAME_" value="'$USERNAME'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"><br><br>
'$CODEMSG' '$SHUTDOWN_CODE'<br><br>
'$CONFIRMMSG'<br>
<input tabindex= "2" name="_SHUTDOWNCODE_" maxlength="3" size="3" type="text"><br><br>
'$VIEWIMAGEMSG'<br>
<a class="info" href="javascript:void(0)"><input name="_VIEWIMAGE_yes_" type="image" class="images" src="/images/submenus/user/user_photo.png" value=""><span>'$VIEWIMAGEMSG'</span></a>
<br>
'
else

echo '
  <table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$USERNAMEMSG'</td>
        <td><span style="font-weight: bold;"><div id="suggestions"></div><input tabindex= "1" style="width: 200px;" name="_USERNAME_" value="'$USERNAME'" size="20" type="text" id="inputString" onkeyup="lookup(this.value);"></span></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Delete_User"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG'</span></a>
      </td></tr>
<tr><td>'$CONFIRMMSG'</td>
        <td style="vertical-align: top; text-align: left;"><input tabindex= "2" name="_SHUTDOWNCODE_" maxlength="3" size="3" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Delete_User"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>
</td></tr>
<tr><td>'$CODEMSG'</td>
        <td style="vertical-align: top; text-align: left;"><b>'$SHUTDOWN_CODE'</b></td></tr>
<tr><td>'$ARCHIVEMSG'</td><td><input type="checkbox" name="_ARCHIVE_" value="yes"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Delete_User"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a>
      </td></tr>
<tr><td>'$VIEWIMAGEMSG'</td><td>
<a class="info" href="javascript:void(0)"><input name="_VIEWIMAGE_yes_" type="image" class="images" src="/images/submenus/user/user_photo.png" value=""><span>'$VIEWIMAGEMSG'</span></a>
</td></tr>
    </tbody>
  </table>'

fi
#Get user image
if [ $USERNAME'blank' != blank ]
then
echo '<br>'
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:" | sudo -H /opt/karoshi/web_controls/exec/show_user_image
fi
if [ $MOBILE = no ]
then
echo '</div><div id="submitbox">'
else
echo '<br>'
fi
echo '<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"></div>'
[ $MOBILE = no ] && echo '</div>'
echo '</form></div></body></html>'
exit
