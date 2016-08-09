#!/bin/bash
#Copyright (C) 2014 Paul Sharrad

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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Group Management"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/js/jquery.js"></script>
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

if [ $MOBILE = yes ]
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
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%+-' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
#echo $DATA"<br>"

function show_status {
echo '<SCRIPT language="Javascript">
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/groups.cgi"
</script>
</div></div></form></body></html>'
exit
}

#########################
#Assign data to variables
#########################
END_POINT=27
#Assign GROUPNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = GROUPNAMEcheck ]
	then
		let COUNTER=$COUNTER+1
		GROUPNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/REPLACEUNDERSCORE/_/g'`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign TYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = TYPEcheck ]
	then
		let COUNTER=$COUNTER+1
		TYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
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

[ -z "$TYPE" ] && TYPE=notset
[ -z "$ACTION" ] && ACTION=view

#Assign USERNAME
if [ "$ACTION" = removeuser ] || [ "$ACTION" = adduser ] || [ "$ACTION" = disableuser ] || [ "$ACTION" = enableuser ]
then
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
fi

if [ "$ACTION" = reallyadd ] && [ "$TYPE" = primary ]
then
	#Assign HOMESERVER
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = HOMESERVERcheck ]
		then
			let COUNTER=$COUNTER+1
			HOMESERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign CATEGORY
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = CATEGORYcheck ]
		then
			let COUNTER=$COUNTER+1
			CATEGORY=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign SECGROUP
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SECGROUPcheck ]
		then
			let COUNTER=$COUNTER+1
			SECGROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
			fi
		let COUNTER=$COUNTER+1
	done
	fi


	if [ $ACTION = editextrargroups ]
	then
	#Assign EXTRAGROUPS
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = EXTRAGROUPNAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			EXTRAGROUPS=`echo $DATA | cut -s -d'_' -f$COUNTER- | sed 's/_EXTRAGROUPNAME_/,/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

#Get install type
INSTALL_TYPE=education
if [ -f /opt/karoshi/server_network/install_type ]
then
	INSTALL_TYPE=`sed -n 1,1p /opt/karoshi/server_network/install_type`
fi

PROTECTEDLIST="itadmin exams karoshi staff nogroup"

#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
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

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

#########################
#Check data
#########################

#Check to see that GROUPNAME is not blank
TITLE=$"Group Management"
ACTIONTYPE=add
ACTIONMSG="$NEWGROUPMSG"

if [ "$ACTION" != add ] && [ $ACTION != delete ] && [ $ACTION != view ] && [ $ACTION != reallyadd ] && [ $ACTION != reallydelete ] && [ $ACTION != extragroups ] && [ $ACTION != editextrargroups ] && [ $ACTION != showusers ] && [ $ACTION != removeuser ] && [ $ACTION != adduser ] && [ $ACTION != disableuser ] && [ $ACTION != enableuser ]
then
	MESSAGE=$"An incorrect action has been entered."
	show_status
fi

if [ "$ACTION" = reallyadd ] || [ $ACTION = reallydelete ]
then
	#Check to see that GROUPNAME is not blank
	if [ -z "$GROUPNAME" ]
	then
		MESSAGE=$"The group name cannot be blank."
		show_status
	fi
fi

if [ $ACTION = add ] || [ $ACTION = delete ] || [ "$ACTION" = reallyadd ] || [ $ACTION = reallydelete ] || [ $ACTION = extragroups ] || [ $ACTION = editextrargroups ]
then
	if [ -z "$TYPE" ]
	then
		MESSAGE=$"The type cannot be blank."
		show_status
	fi
fi

if [ $ACTION = showusers ] || [ $ACTION = removeuser ] || [ $ACTION = adduser ]
then
	if [ -z "$GROUPNAME" ]
	then
		MESSAGE=$"The group cannot be blank."
		show_status
	fi
fi

if [ $ACTION = removeuser ] || [ $ACTION = adduser ] || [ $ACTION = disableuser ] || [ $ACTION = enableuser ]
then
	if [ -z "$USERNAME" ]
	then
		MESSAGE=$"The username cannot be blank."
		show_status
	fi
	#Check that the username exists
	getent passwd "$USERNAME" 1>/dev/null
	if [ $? != 0 ]
	then
		MESSAGE=$"This username does not exist."
		show_status
	fi
fi



#Generate navigation bar
if [ $MOBILE = no ]
then
	DIV_ID=actionbox3
	TABLECLASS=standard
	WIDTH1=200
	WIDTH2=90
	WIDTH3=200
	WIDTH4=70
	WIDTH5=80
	WIDTH6=192
	ICON1=/images/submenus/system/delete.png
	ICON2=/images/submenus/system/edit.png
	ICON3=/images/submenus/user/users.png
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
else
	DIV_ID=actionbox2
	TABLECLASS=mobilestandard
	WIDTH1=100
	WIDTH2=70
	WIDTH3=150
	WIDTH4=60
	WIDTH5=50
	WIDTH6=142
	ICON1=/images/submenus/system/deletem.png
	ICON2=/images/submenus/system/editm.png
	ICON3=/images/submenus/user/usersm.png
fi

function do_action {
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/groups.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$GROUPNAME:$ACTION:$TYPE:$PROFILE:$HOMESERVER:$CATEGORY:$SECGROUP:$EXTRAGROUPS:$USERNAME:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/groups
}

#Delete a user from a group
if [ "$ACTION" = removeuser ] || [ "$ACTION" = adduser ] || [ "$ACTION" = disableuser ] || [ "$ACTION" = enableuser ]
then
	do_action
	if [ "$ACTION" = disableuser ] || [ "$ACTION" = enableuser ] || [ "$ACTION" = adduser ]
	then
		USERNAME=""
	fi
	ACTION=showusers
fi

if [ $ACTION = reallyadd ]
then
	#Check that the group does not already exist
	getent group $GROUPNAME 1>/dev/null
	if [ $? = 0 ]
	then
		MESSAGE=$"A group with that name already exists."
		show_status
	fi

	#Check that a user with the same name does not already exist
	getent passwd $GROUPNAME 1>/dev/null
	if [ $? = 0 ]
	then
		MESSAGE=$"A user with that name already exists."
		show_status
	fi

	do_action
	ACTION=view
fi

if [ $ACTION = editextrargroups ]
then
	do_action
	ACTION=view
fi

if [ $ACTION = reallydelete ]
then
	do_action
	ACTION=view
fi

if [ $ACTION = add ] && [ $TYPE = primary ]
then 
	TITLE=$"New Primary Group"
fi
if [ $ACTION = add ] && [ $TYPE = secondary ]
then 
	TITLE=$"New Secondary Group"
fi
[ $ACTION = delete ] && TITLE=$"Delete Group"
[ $ACTION = extragroups ] && TITLE=$"Extra Groups"

#Show back button for mobiles
if [ $MOBILE = yes ]
then
	echo '<div style="float: center" id="my_menu" class="sdmenu">
		<div class="expanded">
		<span>'$"Group Management"'</span>
	<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
	</div></div><div id="mobileactionbox">
	'
	else
	echo '<div id="'$DIV_ID'"><div id="titlebox">'
fi

echo '<table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
	<tr>'
	if [ $MOBILE = no ]
	then
		echo '<td style="vertical-align: top;"><div class="sectiontitle">'$TITLE' '$GROUPNAME'</div></td>'
	else
		echo '<td style="vertical-align: top;"><div class="sectiontitle">'$GROUPNAME'</div></td>'
	fi

if [ $ACTION = view ] 
then
	echo '<td style="vertical-align: top;">
	<form name="myform" action="/cgi-bin/admin/categories.cgi" method="post">
	<button class="button" name="Categories" value="">
	'$"Categories"'
	</button>
	</form>
	</td>
	<td style="vertical-align: top;">
	<form name="myform" action="/cgi-bin/admin/groups.cgi" method="post">
	<button class="button" name="____NewPrimaryGroup____" value="____ACTION____add____TYPE____primary____">
	'$"New primary group"'
	</button>
	</form>
	</td><td style="vertical-align: top;">
	<form name="myform" action="/cgi-bin/admin/groups.cgi" method="post">
	<button class="button" name="____NewSecondaryGroup____" value="____ACTION____add____TYPE____secondary____">
	'$"New secondary group"'
	</button>
	</form>
	</td>'


	if [ $MOBILE = no ]
	then
		echo '<td style="vertical-align: top;">
		<form name="DynamicGroups" action="/cgi-bin/admin/dynamic_groups_fm.cgi" method="post">
		<button class="button" name="ViewGroups" value="_">
		'$"Dynamic Groups"'
		</button>
		</form>
		</td>
		<td style="vertical-align: top;">
		<form name="LabelGroups" action="/cgi-bin/admin/label_groups_fm.cgi" method="post">
		<button class="button" name="LabelGroups" value="_">
		'$"Label Groups"'
		</button>
		</form>
		</td>
		<td style="vertical-align: top;">
		<form name="CopyFiles" action="/cgi-bin/admin/copy_files_upload_fm.cgi" method="post">
		<button class="button" name="CopyFiles" value="_">
		'$"Copy Files"'
		</button>
		</form>
		</td>'
	fi
else
	echo '<td style="vertical-align: top;">
	<form name="myform" action="/cgi-bin/admin/groups.cgi" method="post">
	<button class="button" name="____ViewGroups____" value="____ACTION____view____TYPE____'$TYPE'____">
	'$"View groups"'
	</button>
	</form>	
	</td>'
fi
echo '<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management"><img class="images" alt="" src="/images/help/info.png"><span>'$"This page lets you add and remove groups from your system."'<br><br>'$"Primary groups are used when creating users. All users are assigned to a primary group."'<br><br>'$"Secondary groups can be used when creating sub folders and restricting access to certain groups."'</span></a></td></tr></tbody></table>'

if [ $MOBILE = no ]
then
	echo '</div><div id="infobox">'
fi

#Show users in a group
if [ "$ACTION" = showusers ]
then
	do_action
fi

#Show form for adding groups
if [ $ACTION = add ] && [ $TYPE = secondary ]
then
echo '<form name="myform" action="/cgi-bin/admin/groups.cgi" method="post"><input type="hidden" name="____TYPE____secondary____" value=""><input type="hidden" name="____ACTION____reallyadd____" value=""><table class="'$TABLECLASS'" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: '$WIDTH3'px;">
'$"Secondary group"'</td>
        <td><input name="____GROUPNAME____" style="width: '$WIDTH3'px;" type="text">
</td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#New_Secondary_Goup"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name of a new supplementary group that you want to create."'<br><br>'$"Secondary groups can be used for subfolders in existing shares to restrict access to memebers of the group."'</span></a>
</td>
      </tr>
    </tbody>
  </table>
  <br>
  <br>
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></form>'
fi

if [ $ACTION = add ] && [ $TYPE = primary ]
then
	echo '<form name="myform" action="/cgi-bin/admin/groups.cgi" method="post"><input type="hidden" name="____TYPE____primary____" value=""><input type="hidden" name="____ACTION____reallyadd____" value=""><table class="'$TABLECLASS'" style="text-align: left;" >
	    <tbody>
	<tr><td style="width: '$WIDTH3'px;">'$"Primary group name"'</td><td><input name="____GROUPNAME____" style="width: '$WIDTH6'px;" size="20" type="text"></td><td>
	<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#New_Primary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name of the new primary group that you want to create."'<br><br>'$"This could be used where you need different profiles for staff and require more staff groups."'</span></a>

	</td></tr>
	<tr><td>'$"Home Server"'</td><td><select name="____HOMESERVER____" style="width: '$WIDTH3'px;">'

	#Generate a list of servers for the home folders
	FILESERVERCOUNT=0
	for KAROSHI_SERVER in /opt/karoshi/server_network/servers/*
	do
		KAROSHI_SERVER=`basename $KAROSHI_SERVER`
		if [ -f /opt/karoshi/server_network/servers/$KAROSHI_SERVER/fileserver ]
		then
			SERVERARRAY[$FILESERVERCOUNT]=$KAROSHI_SERVER
			let FILESERVERCOUNT=$FILESERVERCOUNT+1
		fi
	done
	COUNTER=0
	while [ $COUNTER -lt $FILESERVERCOUNT ]
	do
		echo '<option value="'${SERVERARRAY[$COUNTER]}'">'${SERVERARRAY[$COUNTER]}'</option>'
		let COUNTER=$COUNTER+1
	done
	echo '</select></td><td>
	<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#New_Primary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the server you require for the home areas to be stored on for this group."'</span></a></td></tr>'
	#Show categories
	echo '<tr><td>'$"Category"'</td><td><select name="____CATEGORY____" style="width: '$WIDTH3'px;">
	<option value="" label="blank"></option>'
	for CATEGORY in $(ls -1 /opt/karoshi/server_network/categories/ )
	do
		source /opt/karoshi/server_network/categories/"$CATEGORY"
		echo '	<option value="'$CATEGORY'">'$CATEGORYNAME'</option>'
	done
	echo '<option value="other">'$"Other"'</option>
	</select>
	</td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the category that you want this group to be placed in."'</span></a></td></tr>
	</tbody></table><br><br><input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></form>'
fi

if [ $ACTION = view ]
then
	#Show list of groups

	[ "$TYPE" = notset ] && TYPE=primary

	#Get a list of groups
	if [ $TYPE = primary ]
	then
		GROUPTYPE=$"Primary"
		GTYPE=primary
		GROUPLIST=( `ls -1 /opt/karoshi/server_network/group_information` )
	fi

	if [ $TYPE = secondary ]
	then
		GROUPTYPE=$"Secondary"
		GTYPE=secondary
		GROUPLIST=( `ls -1 /opt/karoshi/server_network/group_information_secondary` )
	fi

	if [ $TYPE = dynamic ]
	then
		GROUPTYPE=$"Dynamic"
		GTYPE=dynamic
		GROUPLIST=( `ls -1 /opt/karoshi/server_network/group_information_dynamic` )
	fi

	if [ $TYPE = all ]
	then
		GROUPLIST=( `ls -1 /opt/karoshi/server_network/group_information` `ls -1 /opt/karoshi/server_network/group_information_secondary` `ls -1 /opt/karoshi/server_network/group_information_dynamic` )	
	fi

	#Get the number of groups in the array
	GROUPCOUNT=${#GROUPLIST[@]} 
	COUNTER=0

	echo  '<form name="myform" action="/cgi-bin/admin/groups.cgi" method="post"><table id="myTable" class="tablesorter" style="text-align: left;" >
	<thead><tr><th style="width: '$WIDTH1'px; vertical-align:top;"><b>'$"Group"'</b></th>'


	[ $MOBILE = no ] && echo '<th style="width: '$WIDTH2'px; vertical-align:top;"><b>'$"Group id"'</b></th><th style="width: '$WIDTH2'px; vertical-align:top;"><b>'$"User count"'</b></th>'

	echo '<td style="width: '$WIDTH5'px; vertical-align:top;">
	<select name="____TYPE____" onchange="this.form.submit()">
	<option value="'$TYPE'">'$"Type"'</option>
	<option class="select-dash" disabled="disabled">----------</option>
	<option value="primary">'$"Primary"'</option>
	<option value="secondary">'$"Secondary"'</option>
	<option value="dynamic">'$"Dynamic"'</option>
	<option value="all">'$"All"'</option>
	</select>
	<noscript><input type="submit" value="Submit"></noscript>
	</td>'

[ $MOBILE = no ] && echo '<th style="width: '$WIDTH3'px; vertical-align:top;"><b>'$"Associated groups"'</b></th>'
echo '<th style="width: '$WIDTH4'px; vertical-align:top;"><b>'$"Members"'</b></th><th style="width: '$WIDTH4'px; vertical-align:top;"><b>'$"Delete"'</b></th></tr></thead><tbody>'

	source /opt/karoshi/web_controls/group_dropdown_def
	

	while [ $COUNTER -lt $GROUPCOUNT ]
	do
		GROUPNAME=`echo ${GROUPLIST[$COUNTER]} | sed 's/____/ /g'`
		GROUPNAMESHORT="$GROUPNAME"
		[ $MOBILE = yes ] && GROUPNAMESHORT=${GROUPNAME:0:12}
		GROUPID=`getent group "$GROUPNAME" | cut -d: -f3`

		if [ $GROUPID -ge 1000 ] && [ $GROUPNAME != nogroup ]
		then

			UPPERGROUPNAME=${GROUPNAME^^}
			LABEL=${!UPPERGROUPNAME:+ : ${!UPPERGROUPNAME}}

			if [ $TYPE = all ]
			then
				GROUPTYPE=$"Secondary"
				GTYPE=secondary
				if [ -f /opt/karoshi/server_network/group_information/"$GROUPNAME" ]
				then
					GROUPTYPE=$"Primary"
					GTYPE=primary
				fi
				if [ -f /opt/karoshi/server_network/group_information_dynamic/"$GROUPNAME" ]
				then
					GROUPTYPE=$"Dynamic"
					GTYPE=dynamic
				fi
			fi
			#Show primary, secondary, dynamic, or all groups
			MEMBERCOUNT=`getent group $GROUPNAME | cut -d: -f4- | sed '/^$/d' | sed 's/,/\n/g' | wc -l`
			echo '<tr><td>'$GROUPNAMESHORT' '$LABEL'</td><td>'
			[ $MOBILE = no ] && echo ''$GROUPID'</td><td>'$MEMBERCOUNT'</td><td>'
		
			echo ''$GROUPTYPE'</td>'
			if [ $MOBILE = no ]
			then
				echo '<td>'
				if [ $GTYPE = primary ]
				then
					source /opt/karoshi/server_network/group_information/"$GROUPNAME"
					echo '


			<button class="info" name="____changeextragroups____" value="____ACTION____extragroups____GROUPNAME____'$GROUPNAME'____TYPE____'$GTYPE'____">
			<img src="'$ICON2'" alt="'$"changeextragroups"'">
			<span>'$"Change the extra groups associated with this group."' '$GROUPNAME'</span>
			</button> '$SECONDARYGROUP''
				fi
				echo '</td>'
			fi

			echo '<td>
			<button class="info infoleft" name="____showusers____" value="____ACTION____showusers____GROUPNAME____'$GROUPNAME'____TYPE____'$TYPE'____">
			<img src="'$ICON3'" alt="'$"Show users in this group."'">
			<span>'$GROUPNAME' - '$"Show users in this group."'</span>
			</button></td><td>'
			PROTECTED=no
			[ `echo $PROTECTEDLIST | grep -c $GROUPNAME` -gt 0 ] && PROTECTED=yes
			if [ "$PROTECTED" = no ]
			then
				if [ "$MEMBERCOUNT" = 0 ] || [ "$GTYPE" = secondary ] || [ "$GTYPE" = dynamic ] 
				then
					echo '
			<button class="info infoleft" name="____deletegroup____" value="____ACTION____delete____GROUPNAME____'$GROUPNAME'____TYPE____'$TYPE'____">
			<img src="'$ICON1'" alt="'$"delete this group."'">
			<span>'$GROUPNAME' - '$"delete this group."'</span>
			</button>'
				fi
			fi
			echo '</td></tr>'
		fi
		let COUNTER=$COUNTER+1
	done
	echo '</tbody></table></form>'
fi

if [ $ACTION = delete ]
then
	echo '<form name="myform" action="/cgi-bin/admin/groups.cgi" method="post"><input type="hidden" name="____TYPE____'$TYPE'____" value=""><input type="hidden" name="____GROUPNAME____'$GROUPNAME'____" value=""><input type="hidden" name="____ACTION____reallydelete____" value="">
	<b>'$"Group name": $GROUPNAME'</b><br><br>'$"Are you sure that you want to delete this group?"'<br><br><input value="'$"Submit"'" class="button" type="submit"></form>'
fi

if [ $ACTION = extragroups ]
then
	#Get a list of groups already asociated with this group
	source /opt/karoshi/server_network/group_information/"$GROUPNAME"

	echo '<form name="myform" action="/cgi-bin/admin/groups.cgi" method="post"><input type="hidden" name="____TYPE____'$TYPE'____" value=""><input type="hidden" name="____GROUPNAME____'$GROUPNAME'____" value=""><input type="hidden" name="____ACTION____editextrargroups____" value="">'

	#Show list of groups
	GROUPLIST=( `getent group | cut -d: -f1 | sed 's/ /____/g' | sort` )
	GROUPCOUNT=${#GROUPLIST[@]}  
	COUNTER=0

	echo  '<div class="sectiontitle">'$GROUPNAME'</div><br><table class="'$TABLECLASS'" style="text-align: left;" >
	<tbody><tr><td style="width: '$WIDTH1'px;"><b>'$"Group name"'</b></td><td><b>Select</b></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#Extra_Groups"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the extra groups that you want new users to be members of when the users are created."'</span></a></td></tr>'

	while [ $COUNTER -lt $GROUPCOUNT ]
	do
		GROUPNAMECHOICE=`echo ${GROUPLIST[$COUNTER]} | sed 's/____/ /g'`
		GROUPID=`getent group "$GROUPNAMECHOICE" | cut -d: -f3`
		if [ $GROUPID -ge 1000 ] && [ $GROUPNAMECHOICE != $GROUPNAME ] && [ $GROUPNAME != nogroup ]
		then
			echo '<tr><td>'$GROUPNAMECHOICE'</td><td>'
			CHECKED=""
			[ `echo $SECONDARYGROUP | grep -c -w $GROUPNAMECHOICE` -gt 0 ] && CHECKED=checked
			echo '<input type="checkbox" name="____EXTRAGROUPNAME____" value="'$GROUPNAMECHOICE'" '$CHECKED'>'
			echo '</td></tr>'
		fi
		let COUNTER=$COUNTER+1
	done

	echo '</tbody></table><br><br><input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset"></form>'

fi

[ $MOBILE = no ] && echo '</div>'
echo '</div></div></body></html>'
exit

