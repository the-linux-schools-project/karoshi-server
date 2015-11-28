#!/bin/bash
#Copyright (C) 2015  Paul Sharrad

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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

#Check if timout should be disabled
if [ `echo "$REMOTE_ADDR" | grep -c "$NOTIMEOUT"` = 1 ]
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
  <title>'$"Internet Usage Trends"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
<script type="text/javascript" src="/all/js/jquery.js"></script>
<script type="text/javascript" src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script type="text/javascript" id="js">
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
echo '</head><body onLoad="start()"><div id="pagecontainer">'
TCPIP_ADDR=$REMOTE_ADDR

DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`

ICON1=/images/submenus/system/edit.png
ICON2=/images/submenus/system/delete.png
ICON3=/images/submenus/internet/detailed_logs.png
#########################
#Assign data to variables
#########################
END_POINT=15
#Assign CATEGORY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo "$DATA" | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = CATEGORYcheck ]
	then
		let COUNTER=$COUNTER+1
		CATEGORY=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/+*+/+/g' | sed 's/^+//g' | sed 's/+$//g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign SEARCHTERMS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = SEARCHTERMScheck ]
	then
		let COUNTER=$COUNTER+1
		SEARCHTERMS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/+*+/+/g' | sed 's/^+//g' | sed 's/+$//g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
	then
		let COUNTER=$COUNTER+1
		ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<script language="Javascript">
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/ist.cgi";
</script></div></body></html>'
exit
}

function check_categories {
	if [  -d /opt/karoshi/server_network/ist/categories/ ]
	then
		if [ $(ls -1 /opt/karoshi/server_network/ist/categories/ | wc -l) = 0 ]
		then
			ACTION=addcategory
			CATEGORY=""
		fi
	else
		ACTION=addcategory
		CATEGORY=""
	fi
}

if [ -z "$ACTION" ]
then
	ACTION=viewcategories
	check_categories
fi

if [ -z "$SERVERNAME" ]
then
	SERVERNAME=notset
fi
if [ -z "$SERVERTYPE" ]
then
	SERVERTYPE=notset
fi

#########################
#Check data
#########################
if [ $ACTION != viewcategories ] && [ $ACTION != addcategory ] && [ $ACTION != reallyaddcategory ] && [ $ACTION != editcategory ] && [ $ACTION != deletecategory ] && [ $ACTION != reallydeletecategory ] && [ $ACTION != viewdata ]
then
	MESSAGE=$"You have not entered a correct action."
	show_status
fi


#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=mobileactionbox
fi

echo '<form action="/cgi-bin/admin/ist.cgi" method="post">'

if [ $ACTION = viewcategories ] || [ $ACTION = reallyaddcategory ] || [ $ACTION = reallydeletecategory ]
then
	ACTION2=addcategory
	ACTIONTEXT=$"Add Category"
else
	ACTION2=viewcategories
	ACTIONTEXT=$"View Categories"
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"Internet Usage Trends"' '$SERVER2'</span>'
	if [ $SERVERNAME != notset ]
	then
		echo '<a href="/cgi-bin/admin/file_manager.cgi">'$"Select Server"'</a>'
	else
		echo '<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>'
	fi
	echo '</div></div>
	<div id="'$DIV_ID'">
	'

	else
	echo '<div id="'$DIV_ID'"><div id="titlebox">
	<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
	<tr>
	<td style="vertical-align: top;"><div class="sectiontitle">'$"Internet Usage Trends"'</div></td>
	<td><input name="_ACTION_'$ACTION2'_" type="submit" class="button" value="'$ACTIONTEXT'"></td>
	<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=File_Manager"><img class="images" alt="" src="/images/help/info.png"><span>'$"Internet Usage Trends"'</span></a></td>
	</tr>
	</tbody></table>
	</div><div id="infobox">'
fi

if [ $ACTION = deletecategory ]
then
	#Prompt to delete the category
	CATEGORY=$(echo "$CATEGORY" | sed 's/%2B/ /g')
	echo '<input type="hidden" name="_ACTION_" value="reallydeletecategory"><input type="hidden" name="_CATEGORY_" value="'$CATEGORY'">
	'"$CATEGORY"': Are you sure you want to delete this category?<br><br><input value="'$"Submit"'" class="button" type="submit">'
	
fi

if [ $ACTION = reallyaddcategory ] || [ $ACTION = reallydeletecategory ]
then
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/ist.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$ACTION:$CATEGORY:$SEARCHTERMS:" | sudo -H /opt/karoshi/web_controls/exec/ist
	ACTION=viewcategories
	check_categories
fi

if [ $ACTION = addcategory ] || [ $ACTION = editcategory ]
then
	if [ ! -z "$CATEGORY" ]
	then
		CATEGORY=$(echo "$CATEGORY" | sed 's/%2B/+/g')
		SEARCHTERMS=$(cat /opt/karoshi/server_network/ist/categories/"$CATEGORY" | sed 's/\\|/ /g')
		CATEGORY=$(echo "$CATEGORY" | sed 's/+/ /g')
	fi

	#Show for for adding catergories
	echo '<input type="hidden" name="_ACTION_" value="reallyaddcategory"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
	<tr><td style="width: 180px;" colspan="2"><b>'$"Add an Internet Trend Category"'</b></td><td></td></tr>
	<tr><td>'$"Category"'</td><td>'
	if [ -z "$CATEGORY" ]
	then
		echo '<input tabindex= "1" value="'$CATEGORY'" name="_CATEGORY_" style="width: 200px;" size="20" type="text">'
	else
		echo ''$CATEGORY'<input type="hidden" name="_CATEGORY_" value="'$CATEGORY'">'
	fi
	echo '</td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Username_Styles"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a name for the category you want to add."'</span></a></td></tr>
	<tr><td style="width: 180px;">'$"Search Criteria"'</td><td><input tabindex= "2" value="'$SEARCHTERMS'" name="_SEARCHTERMS_" style="width: 200px;" size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_User#Username_Styles"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the key words to be searched for separated by spaces."'</span></a></td></tr>
	</tbody></table><br>
	<input value="'$"Submit"'" class="button" type="submit">
	'
fi

if [ $ACTION = viewcategories ]
then
	echo '<table id="myTable" class="tablesorter" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><thead>
<tr><th style="width: 180px;"><b>'$"Category"'</b></th><th style="width: 250px;"><b>'$"Search Criteria"'</b></th><th style="width: 60px;"><b>'$"Edit"'</b></th><th style="width: 60px;"><b>'$"Delete"'</b></th><th style="width: 60px;"><b>'$"View"'</b></th></tr></thead><tbody>'
	for CATEGORY in $(ls -1 /opt/karoshi/server_network/ist/categories/)
	do
		CATEGORY2=$(echo $CATEGORY | sed 's/+/ /g')
		SEARCH=$(cat /opt/karoshi/server_network/ist/categories/"$CATEGORY" | sed 's/\\|/ /g')
		echo '<tr><td>'"$CATEGORY2"'</td><td>'"$SEARCH"'</td><td><a class="info" href="javascript:void(0)"><input name="_ACTION_editcategory_CATEGORY_'$CATEGORY'_" type="image" class="images" src="'$ICON1'" value=""><span>'$"Edit"'<br>'$CATEGORY2'</span></a></td><td><a class="info" href="javascript:void(0)"><input name="_ACTION_deletecategory_CATEGORY_'$CATEGORY'_" type="image" class="images" src="'$ICON2'" value=""><span>'$"Delete"'<br>'$CATEGORY2'</span></a></td><td><a class="info" href="javascript:void(0)"><input name="_ACTION_viewdata_CATEGORY_'$CATEGORY'_" type="image" class="images" src="'$ICON3'" value=""><span>'$"View"'<br>'$CATEGORY2'</span></a></td></tr>'
	done
	echo '</tbody></table>'
fi

if [ $ACTION = viewdata ]
then
	MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/ist.cgi | cut -d' ' -f1`
	echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$MOBILE:$ACTION:$CATEGORY:$SEARCHTERMS:" | sudo -H /opt/karoshi/web_controls/exec/ist
fi

[ $MOBILE = no ] && echo '</div>'
echo '</div></form></div></body></html>'
exit

