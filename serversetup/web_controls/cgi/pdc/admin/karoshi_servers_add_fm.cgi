#!/bin/bash
#Copyright (C) 2010  Paul Sharrad

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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Add Server"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>


		<script><!--
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

</head><body onLoad="start()"><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-' | sed 's/__/_ _/g'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%*+-' | sed 's/*/%1123/g' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
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
ZONESELECT3=""
if [ ! -z "$ZONE" ]
then
	[ $ZONE = internal ] && ZONESELECT1='selected="selected"'
	[ $ZONE = dmz ] && ZONESELECT2='selected="selected"'
	[ $ZONE = external ] && ZONESELECT3='selected="selected"'
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/system/computer.png

echo '<form id="FormName" action="/cgi-bin/admin/karoshi_servers_add.cgi" method="post"><div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"Add Server"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Disk_Information"><img class="images" alt="" src="/images/help/info.png"><span>'$"Setup an ssh connection to a Karoshi server so that it can be controlled by the web management."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<button class="info" formaction="karoshi_servers_view.cgi" name="ShowServers" value="_">
			<img src="'$ICON1'" alt="'$"Show Servers"'">
			<span>'$"Show the servers and roles."'</span><br>
			'$"Show Servers"'
		</button>
	</td>

</tr></tbody></table>
<br>
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">'$"Server name"'</td><td><input required="required" tabindex= "1" style="width: 200px;" name="____SERVERNAME____" value="'$SERVERNAME'" size="23" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name of the server you want to enable ssh for."'</span></a>
</td></tr><tr><td style="width: 180px;">'$"TCPIP number"'</td><td><input required="required" tabindex= "2" style="width: 200px;" name="____TCPIPNUMBER____" size="23" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the tcpip number of the server that you are connecting to."'</span></a>
</td></tr>
<tr><td style="width: 180px;">'$"Root Password"'</td><td><input required="required" tabindex= "3" style="width: 200px;" name="____PASSWORD1____" value="'$PASSWORD1'" size="23" type="password"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter the root password for the server you are setting up ssh for and confirm it in the box below."'<br><br>'$"The following special characters are allowed"'<br><br> space !	&quot;	# 	$	%	&amp; 	(	) 	*	+	, 	-	.	/ 	:
;	&lt;	=	&gt;	?	@ 	[	\	]	^	_	` 	{	|	}	~	~</span></a>
</td></tr>
<tr><td>'$"Confirm Root Password"'</td><td><input required="required" tabindex= "4" style="width: 200px;" name="____PASSWORD2____" value="'$PASSWORD2'" size="23" type="password"></td><td></td></tr>
<tr><td style="width: 180px;">Zone</td><td>
<select name="____ZONE____" style="width: 200px;">
<option '$ZONESELECT1'>internal</option>
<option '$ZONESELECT2'>dmz</option>
<option '$ZONESELECT3'>external</option>
</select>
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server#Zone"><img class="images" alt="" src="/images/help/info.png"><span>'$"Your server is in a dmz firewall zone and will be set up with a vpn tunnel to the main server."'</span></a>
</td></tr>
</tbody></table><br>
<table class="standard" style="text-align: left;" ><tbody>
<tr><td>
<div class="sectiontitle">'$"Authentication type"'</div></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server#Authentication_Type"><img class="images" alt="" src="/images/help/info.png"><span>'$"In most cases your extra server will need to recognise your network users and groups."'</span></a></td></tr></tbody></table><br>
<table class="standard" style="text-align: left;" ><tbody>
<tr><td style="width: 180px;">'$"Additional domain controller"'</td><td><input type="radio" name="____AUTHENTICATION____" value="adc" '$CHECKED1' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server#Authentication_Type"><img class="images" alt="" src="/images/help/info.png"><span>'$"Reduncancy in the case of failure of your main domain controller and for additional file servers."'</span></a>
</td></tr>
<tr><td>'$"Read only domain controller"'</td><td><input type="radio" name="____AUTHENTICATION____" value="rodc" '$CHECKED2' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server#Authentication_Type"><img class="images" alt="" src="/images/help/info.png"><span>'$"Useful in dmz firewall zones."'</span></a>
</td></tr>
<tr><td>'$"Domain member"'</td><td><input type="radio" name="____AUTHENTICATION____" value="member" '$CHECKED3' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server#Authentication_Type"><img class="images" alt="" src="/images/help/info.png"><span>'$"Used for file servers."'</span></a>
</td></tr>
<tr><td>'$"Users and groups"'</td><td><input type="radio" name="____AUTHENTICATION____" value="usersandgroups" '$CHECKED4' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server#Authentication_Type"><img class="images" alt="" src="/images/help/info.png"><span>'$"Your server will recognise all of your users and groups but will not be joined to the domain."'</span></a>
</td></tr>
<tr><td>'$"None"'</td><td><input type="radio" name="____AUTHENTICATION____" value="none" '$CHECKED5' onchange="showDiv(this.value);"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Extra_Server#Authentication_Type"><img class="images" alt="" src="/images/help/info.png"><span>'$"The server will not recognise any of your users. This is suitable for a backup server role."'</span></a>
</td></tr></tbody></table>
<br><br>

<p id="adc" class="hiddenDiv"><b>'$"Suggested modules"':</b> '$"File Server"', '$"Print Server"', '$"Squid Internet Proxy"', '$"E-Mail Server"', '$"Home Access Server"', '$"Moodle Server"'</p>
<p id="rodc" class="hiddenDiv"><b>'$"Suggested modules"':</b> '$"File Server"', '$"Print Server"', '$"Squid Internet Proxy"', '$"E-Mail Server"', '$"Home Access Server"', '$"Moodle Server"'</p>
<p id="member" class="hiddenDiv"><b>'$"Suggested modules"':</b> '$"File Server"', '$"Print Server"', '$"Squid Internet Proxy"', '$"E-Mail Server"', '$"Home Access Server"', '$"Moodle Server"'</p>
<p id="usersandgroups" class="hiddenDiv"><b>'$"Suggested modules"':</b> '$"Squid Internet Proxy"', '$"E-Mail Server"', '$"Home Access Server"', '$"Moodle Server"', '$"Web Server"', '$"Joomla"', '$"Distribution Server"'</p>
<p id="none" class="hiddenDiv"><b>'$"Suggested modules"':</b> '$"Backup Server"', '$"Monitor Server"', '$"Reverse Proxy Server"', '$"Distribution Server"', '$"Web Server"', '$"Joomla"'</p>

<br><br>
<input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</div></div>
</form>
</div></body></html>'
exit

