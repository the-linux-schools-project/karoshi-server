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
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/karoshi_servers_add ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/karoshi_servers_add
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi

function getip {
SERVERIP=`grep -w $SERVER /etc/hosts | sed -n 1,1p | cut -f1`
}


############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script>


		<script type="text/javascript"><!--
var lastDiv = "";
function showDiv(divName) {
	// hide last div
	if (lastDiv) {
		document.getElementById(lastDiv).className = "hiddenDiv";
	}
	//if value of the box is not nothing and an object with that name exists, then change the class
	if (divName && document.getElementById(divName)) {
		document.getElementById(divName).className = "visibleDiv";
		lastDiv = divName;
	}
}
//-->
</script>
		<style type="text/css" media="screen">
.hiddenDiv {
	display: none;
	}
.visibleDiv {
	display: block;
	}

</style>

</head><body onLoad="start()"'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-' | sed 's/__/_ _/g'`
ASKIP=no
#########################
#Assign data to variables
#########################
END_POINT=15

#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
then
let COUNTER=$COUNTER+1
SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign password1
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PASSWORD1check ]
then
let COUNTER=$COUNTER+1
PASSWORD1=`echo $DATA | cut -s -d'_' -f$COUNTER`
ASKIP=yes
break
fi
let COUNTER=$COUNTER+1
done
#Assign password2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PASSWORD2check ]
then
let COUNTER=$COUNTER+1
PASSWORD2=`echo $DATA | cut -s -d'_' -f$COUNTER`
ASKIP=yes
break
fi
let COUNTER=$COUNTER+1
done
#Assign AUTHENTICATION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = AUTHENTICATIONcheck ]
then
let COUNTER=$COUNTER+1
AUTHENTICATION=`echo $DATA | cut -s -d'_' -f$COUNTER`
ASKIP=yes
break
fi
let COUNTER=$COUNTER+1
done
#Assign ZONE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ZONEcheck ]
then
let COUNTER=$COUNTER+1
ZONE=`echo $DATA | cut -s -d'_' -f$COUNTER`
ASKIP=yes
break
fi
let COUNTER=$COUNTER+1
done

if [ ! -z "$AUTHENTICATION" ]
then
[ $AUTHENTICATION = adc ] && CHECKED1=checked
[ $AUTHENTICATION = rodc ] && CHECKED2=checked
[ $AUTHENTICATION = member ] && CHECKED3=checked
[ $AUTHENTICATION = users ] && CHECKED4=checked
[ $AUTHENTICATION = none ] && CHECKED5=checked
fi

ZONESELECT1=""
ZONESELECT2=""
if [ ! -z "$ZONE" ]
then
[ $ZONE = internal ] && ZONESELECT1='selected="selected"'
[ $ZONE = dmz ] && ZONESELECT2='selected="selected"'
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo '<form id="FormName" action="/cgi-bin/admin/karoshi_servers_add.cgi" method="post"><div id="actionbox"><b>'$TITLE'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>

<br><br>
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;">'$SERVERMSG'</td><td><input tabindex= "1" style="width: 200px;" name="_SERVERNAME_" value="'$SERVERNAME'" size="23" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a>
</td></tr>'

#Only ask for tcpip if it is not listed in /etc/hosts
if [ $ASKIP = yes ]
then
echo '<tr><td style="width: 180px;">'$TCPIPMSG'</td><td><input tabindex= "2" style="width: 200px;" name="_TCPIPNUMBER_" size="23" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a>

</td></tr>'
fi

echo '<tr><td style="width: 180px;">'$ROOTMSG'</td><td><input tabindex= "3" style="width: 200px;" name="_PASSWORD1_" value="'$PASSWORD1'" size="23" type="password"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG4'</span></a>
</td></tr>
<tr><td>'$CONFIRMMSG'</td><td><input tabindex= "4" style="width: 200px;" name="_PASSWORD2_" value="'$PASSWORD2'" size="23" type="password"></td></tr>
<tr><td style="width: 180px;">Zone</td><td>
<select name="_ZONE_" style="width: 200px;">
<option '$ZONESELECT1'>internal</option>
<option '$ZONESELECT2'>dmz</option>
</select>
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG10'</span></a>
</td></tr>
</tbody></table><br>
<b>'$AUTHTYPEMSG'</b> <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG11'</span></a><br><br>
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="width: 180px;">'$ADCMSG'</td><td><input type="radio" name="_AUTHENTICATION_" value="adc" '$CHECKED1' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG5'</span></a>
</td></tr>
<tr><td>'$RODCMSG'</td><td><input type="radio" name="_AUTHENTICATION_" value="rodc" '$CHECKED2' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG6'</span></a>
</td></tr>
<tr><td>'$DMMSG'</td><td><input type="radio" name="_AUTHENTICATION_" value="member" '$CHECKED3' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG7'</span></a>
</td></tr>
<tr><td>'$UAGMSG'</td><td><input type="radio" name="_AUTHENTICATION_" value="users" '$CHECKED4' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG8'</span></a>
</td></tr>
<tr><td>'$NOAUTHMSG'</td><td><input type="radio" name="_AUTHENTICATION_" value="none" '$CHECKED5' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG9'</span></a>
</td></tr></tbody></table>
<br><br>

<p id="adc" class="hiddenDiv"><b>'$MODULESMSG':</b> '$FILESERVERMSG', '$PRINTSERVERMSG', '$SQUIDSERVERMSG', '$EMAILSERVERMSG', '$HOMEACCESSSERVERMSG', '$MOODLESERVERMSG'</p>
<p id="rodc" class="hiddenDiv"><b>'$MODULESMSG':</b> '$FILESERVERMSG', '$PRINTSERVERMSG', '$SQUIDSERVERMSG', '$EMAILSERVERMSG', '$HOMEACCESSSERVERMSG', '$MOODLESERVERMSG'</p>
<p id="member" class="hiddenDiv"><b>'$MODULESMSG':</b> '$FILESERVERMSG', '$PRINTSERVERMSG', '$SQUIDSERVERMSG', '$EMAILSERVERMSG', '$HOMEACCESSSERVERMSG', '$MOODLESERVERMSG'</p>
<p id="users" class="hiddenDiv"><b>'$MODULESMSG':</b> '$EMAILSERVERMSG', '$MOODLESERVERMSG', '$WEBSERVERMSG', '$JOOMLAMSG', '$DISTRIBUTIONSERVERMSG'</p>
<p id="none" class="hiddenDiv"><b>'$MODULESMSG':</b> '$BACKUPSERVERMSG', '$MONITORSERVERMSG', '$DISTRIBUTIONSERVERMSG', '$WEBSERVERMSG', '$JOOMLAMSG'</p>

</div>
<div id="submitbox">
<input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</div>
</form>
</body></html>'
exit

