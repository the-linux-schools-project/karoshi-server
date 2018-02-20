#!/bin/bash
#Copyright (C) 2016 Paul Sharrad

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

########################
#Required input variables
########################
#  _USERNAME_

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser
source /opt/karoshi/web_controls/version

########################
#Language
########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Quick Links"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/js/jquery.js"></script>
<script src="/all/js/script.js"></script>
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>

<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ "$MOBILE" = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: www.dynamicdrive.com
		* Visit Dynamic Drive at www.dynamicdrive.com for full source code
		***********************************************/
	</script>
	<script>
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################

DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%+-' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g')

function show_status {
echo '<SCRIPT language="Javascript">
alert("'"$MESSAGE"'");
window.location = "/cgi-bin/admin/mylinks.cgi"
</script>
</div></div></form></body></html>'
exit
}

#########################
#Assign data to variables
#########################
END_POINT=15
MAX_SUB_LINKS=20
MAX_INLINE_LINKS=5
MAX_QUICK_LINKS=200
#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/REPLACEUNDERSCORE/_/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = add ] || [ "$ACTION" = delete ] || [ "$ACTION" = up ] || [ "$ACTION" = down ]
then
	#Assign HYPERLINK
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = HYPERLINKcheck ]
		then
			let COUNTER=$COUNTER+1
			HYPERLINK=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign QUICKLINKSTYLE
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = QUICKLINKSTYLEcheck ]
		then
			let COUNTER=$COUNTER+1
			QUICKLINKSTYLE=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

#########################
#Check https access
#########################
if [ https_"$HTTPS" != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ -z "$REMOTE_USER" ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#########################
#Check data
#########################

#Check to see that GROUPNAME is not blank
TITLE=$"Quick Links"

if [ "$ACTION" != add ] && [ "$ACTION" != delete ] && [ "$ACTION" != view ] && [ "$ACTION" != up ] && [ "$ACTION" != down ]
then
	MESSAGE=$"An incorrect action has been entered."
	show_status
fi

if [ "$ACTION" = add ] || [ $ACTION = delete ] || [ "$ACTION" = UP ] || [ "$ACTION" = down ]
then
	#Check to see that HYPERLINK is not blank
	if [ -z "$HYPERLINK" ]
	then
		MESSAGE=$"The hyperlink cannot be blank."
		show_status
	fi
fi

if [ "$ACTION" = add ]
then
	if [ -f "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER.links.$QUICKLINKSTYLE" ]
	then
		#Check how many links we already have
		if [ $QUICKLINKSTYLE = sub ]
		then
			MAX_LINKS=$MAX_SUB_LINKS
		elif [ $QUICKLINKSTYLE = inline ]
		then
			MAX_LINKS=$MAX_INLINE_LINKS
		else
			MAX_LINKS=$MAX_QUICK_LINKS
		fi
		LINK_COUNT=$(cat "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER.links.$QUICKLINKSTYLE" | wc -l)
		if [ $LINK_COUNT -ge $MAX_LINKS ]
		then
			MESSAGE=$"The maximum links for this section has been reached."
			show_status	
		fi
	fi
fi

if [ "$ACTION" = add ] || [ "$ACTION" = delete ] || [ "$ACTION" = up ] || [ "$ACTION" = down ]
then
	Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/mylinks.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ACTION:$HYPERLINK:$QUICKLINKSTYLE:" | sudo -H /opt/karoshi/web_controls/exec/mylinks
	#Reload page
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH1=200
	WIDTH2=210
	WIDTH3=130
	WIDTH4=375
	WIDTH5=80
	HEIGHT1=25
	ICON1=/images/submenus/file/moveup.png
	ICON2=/images/submenus/file/movedown.png
	ICON3=/images/submenus/file/delete.png
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
	WIDTH1=80
	WIDTH2=210
	WIDTH3=80
	WIDTH4=200
	WIDTH5=40
	HEIGHT1=30
	ICON1=/images/submenus/file/moveupm.png
	ICON2=/images/submenus/file/movedownm.png
	ICON3=/images/submenus/file/deletem.png
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"Quick Links"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="mobileactionbox">
	'
	else
	echo '<div id="'"$DIV_ID"'"><div id="titlebox">'
fi

echo '<div class="sectiontitle">'$"Quick Links"'</div>'

#Show box to add link
echo '<form name="myform" action="/cgi-bin/admin/mylinks.cgi" method="post"><table id="myTable" class="tablesorter" style="text-align: left;"><tbody>
<tr><td style="width: '"$WIDTH1"'px;">'$"Link Style"'</td>
<td style="width: '"$WIDTH2"'px; text-align:center">
<select name="____QUICKLINKSTYLE" style="width: 200px; height: '"$HEIGHT1"'px;">
<option value="____sub____">'$"Sub Link"'</option>
<option value="____inline____">'$"Main Link"'</option>
<option value="____quick____">'$"Bookmark"'</option>
</select>
</td><td></td></tr>
<tr><td style="width: '"$WIDTH1"'px;">'$"Add link"'</td>
<td style="width: '"$WIDTH2"'px; text-align:center">'
#Show a drop down of all available links
echo '<select name="____ACTION____add________HYPERLINK____" style="width: 200px; height: '"$HEIGHT1"'px;">'
/opt/karoshi/web_controls/generate_navbar_admin | grep -v ^singletext | grep -v '<li class="top"' |  grep -v '<li class="mid"' | grep 'a href=' | sed 's/\t//g' | sed 's/<li>//g' | sed 's%</li>%%g' | sed 's$<a href=$<option value=$g' | sed 's$</a>$</option>$g' | sed 's$;$$g' | sed 's%target="_blank"%%g' | sort --unique
echo '</select></td><td style="width: '"$WIDTH3"'px; text-align:center"><input value="'$"Submit"'" class="button" type="submit"></td></tr>
</tbody></table></form>
'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">'

function show_current_links {
#Show current sub links
if [ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER".links.$QUICKLINKSTYLE ]
then
	if [ "$QUICKLINKSTYLE" = sub ]
	then
		MAX_LINKS="$MAX_SUB_LINKS"
	elif [ "$QUICKLINKSTYLE" = inline ]
	then
		MAX_LINKS="$MAX_INLINE_LINKS"
	else
		MAX_LINKS="$MAX_QUICK_LINKS"
	fi
	LINK_COUNT=$(cat "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER.links.$QUICKLINKSTYLE" | wc -l)

	COUNTER=1
	echo '<a name="'"$QUICKLINKSTYLE"'"></a><form name="myform" action="/cgi-bin/admin/mylinks.cgi#'"$QUICKLINKSTYLE"'" method="post"> <input type="hidden" name="____Quicklinks____" value="____QUICKLINKSTYLE____'"$QUICKLINKSTYLE"'____"><table class="tablesorter" style="text-align: left;" >
	<thead><tr><th style="width: '$WIDTH4'px;">'"$QUICKLNKTITLE"' '"$LINK_COUNT"'/'"$MAX_LINKS"'</th><th style="width: '"$WIDTH5"'px;text-align:center">'$"Move"'</th><th style="width: '"$WIDTH5"'px; text-align:center">'$"Delete"'</th></tr></thead><tbody>'
	LINKCOUNT=$(cat /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER.links.$QUICKLINKSTYLE" | wc -l)
	for LINKDATA in $(cat /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER.links.$QUICKLINKSTYLE" | sed 's% %SPACE%g')
	do
		HYPERLINK=$(echo "$LINKDATA" | cut -d, -f1)
		LINKTITLE=$(echo "$LINKDATA" | cut -d, -f2 | sed 's%SPACE% %g')
		echo '<tr><td><a href="'"$HYPERLINK"'">'"$LINKTITLE"'</a></td><td style="text-align:center">'
		if [ $COUNTER != 1 ]
		then
			echo '<button class="info" name="____Up____" value="____ACTION____up____HYPERLINK____'"$HYPERLINK"'____">
			<img src="'"$ICON1"'" alt="'$"Up"'">
			<span>'$"Move Up"'<br>'"$LINKTITLE"'</span>
			</button>'
		fi
		if [ "$COUNTER" != "$LINKCOUNT" ]
		then
			echo '<button class="info" name="____Down____" value="____ACTION____down____HYPERLINK____'"$HYPERLINK"'____">
			<img src="'"$ICON2"'" alt="'$"Down"'">
			<span>'$"Move Down"'<br>'"$LINKTITLE"'</span>
			</button>'
		fi

		echo '</td><td style="text-align:center">
		<button class="info" name="____Delete____" value="____ACTION____delete____HYPERLINK____'"$HYPERLINK"'____">
		<img src="'"$ICON3"'" alt="'$"Delete"'">
		<span>'$"Delete"'<br>'"$LINKTITLE"'</span>
		</button>
		</td></tr>'
		let COUNTER="$COUNTER"+1
	done
	echo '</tbody></table></form>'
fi
}

QUICKLNKTITLE=$"Bookmarks"
QUICKLINKSTYLE=quick
show_current_links

QUICKLNKTITLE=$"Main Links"
QUICKLINKSTYLE=inline
show_current_links

QUICKLNKTITLE=$"Sub Links"
QUICKLINKSTYLE=sub
show_current_links

echo '</div></div></div></body></html>'

exit

