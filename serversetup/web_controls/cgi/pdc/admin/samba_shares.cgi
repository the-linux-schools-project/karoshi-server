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
source /opt/karoshi/web_controls/version

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER" ] && source "/opt/karoshi/web_controls/user_prefs/$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Network Shares"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'">
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
</head><body><div id="pagecontainer">'
#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g')
#########################
#Assign data to variables
#########################
END_POINT=$(echo "$DATA" | sed 's/_/\n/g' | wc -l)
let ENDPOINT="$ENDPOINT"+1

function get_data {
COUNTER=2
DATAENTRY=""
while [[ $COUNTER -le $END_POINT ]]
do
	DATAHEADER=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
	if [[ "$DATAHEADER" = "$DATANAME" ]]
	then
		let COUNTER="$COUNTER"+1
		DATAENTRY=$(echo "$DATA" | cut -s -d'_' -f"$COUNTER")
		break
	fi
	let COUNTER=$COUNTER+1
done
}

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = delete ] || [ "$ACTION" = reallydelete ]
then
	#Assign SHARENAME
	DATANAME=SHARENAME
	get_data
	SHARENAME="$DATAENTRY"

	#Assign SERVERNAME
	DATANAME=SERVERNAME
	get_data
	SERVERNAME="$DATAENTRY"

	#Assign SERVERTYPE
	DATANAME=SERVERTYPE
	get_data
	SERVERTYPE="$DATAENTRY"

	#Assign SERVERMASTER
	DATANAME=SERVERMASTER
	get_data
	SERVERMASTER="$DATAENTRY"
fi

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = edit ] || [ "$ACTION" = reallyedit ]
then
	#Assign COMMENT
	DATANAME=COMMENT
	get_data
	COMMENT="$DATAENTRY"

	#Assign SHARENAME
	DATANAME=SHARENAME
	get_data
	SHARENAME=$(echo "$DATAENTRY" | tr -cd "0-9A-Za-z")

	#Assign SHAREPATH
	DATANAME=SHAREPATH
	get_data
	SHAREPATH=$(echo "$DATAENTRY" | sed 's/%2F/\//g')

	#Assign GROUP1
	DATANAME=GROUP1
	get_data
	GROUP1="$DATAENTRY"

	#Assign GROUP2
	DATANAME=GROUP2
	get_data
	GROUP2="$DATAENTRY"

	#Assign GROUP3
	DATANAME=GROUP3
	get_data
	GROUP3="$DATAENTRY"

	#Assign GROUP4
	DATANAME=GROUP4
	get_data
	GROUP4="$DATAENTRY"

	#Assign GROUP5
	DATANAME=GROUP5
	get_data
	GROUP5="$DATAENTRY"

	#Assign GROUP6
	DATANAME=GROUP6
	get_data
	GROUP6="$DATAENTRY"

	#Assign GROUP7
	DATANAME=GROUP7
	get_data
	GROUP7="$DATAENTRY"

	#Assign GROUP8
	DATANAME=GROUP8
	get_data
	GROUP8="$DATAENTRY"

	#Assign GROUP9
	DATANAME=GROUP9
	get_data
	GROUP9="$DATAENTRY"

	#Assign GROUP10
	DATANAME=GROUP10
	get_data
	GROUP10="$DATAENTRY"

	#Assign GROUP11
	DATANAME=GROUP11
	get_data
	GROUP11="$DATAENTRY"

	#Assign GROUP12
	DATANAME=GROUP12
	get_data
	GROUP12="$DATAENTRY"

	#Assign GROUPPERMS1
	DATANAME=GROUPPERMS1
	get_data
	GROUPPERMS1="$DATAENTRY"

	#Assign GROUPPERMS2
	DATANAME=GROUPPERMS2
	get_data
	GROUPPERMS2="$DATAENTRY"

	#Assign GROUPPERMS3
	DATANAME=GROUPPERMS3
	get_data
	GROUPPERMS3="$DATAENTRY"

	#Assign GROUPPERMS4
	DATANAME=GROUPPERMS4
	get_data
	GROUPPERMS4="$DATAENTRY"

	#Assign GROUPPERMS5
	DATANAME=GROUPPERMS5
	get_data
	GROUPPERMS5="$DATAENTRY"

	#Assign GROUPPERMS6
	DATANAME=GROUPPERMS6
	get_data
	GROUPPERMS6="$DATAENTRY"

	#Assign GROUPPERMS7
	DATANAME=GROUPPERMS7
	get_data
	GROUPPERMS7="$DATAENTRY"

	#Assign GROUPPERMS8
	DATANAME=GROUPPERMS8
	get_data
	GROUPPERMS8="$DATAENTRY"

	#Assign GROUPPERMS9
	DATANAME=GROUPPERMS9
	get_data
	GROUPPERMS9="$DATAENTRY"

	#Assign GROUPPERMS10
	DATANAME=GROUPPERMS10
	get_data
	GROUPPERMS10="$DATAENTRY"

	#Assign GROUPPERMS11
	DATANAME=GROUPPERMS11
	get_data
	GROUPPERMS11="$DATAENTRY"

	#Assign GROUPPERMS12
	DATANAME=GROUPPERMS12
	get_data
	GROUPPERMS12="$DATAENTRY"

	#Assign ALLPERMS
	DATANAME=ALLPERMS
	get_data
	ALLPERMS="$DATAENTRY"

	#Assign MAPDRIVE1
	DATANAME=MAPDRIVE1
	get_data
	MAPDRIVE1="$DATAENTRY"

	#Assign MAPDRIVE2
	DATANAME=MAPDRIVE2
	get_data
	MAPDRIVE2="$DATAENTRY"

	#Assign MAPDRIVE3
	DATANAME=MAPDRIVE3
	get_data
	MAPDRIVE3="$DATAENTRY"

	#Assign MAPDRIVE4
	DATANAME=MAPDRIVE4
	get_data
	MAPDRIVE4="$DATAENTRY"

	#Assign MAPDRIVE5
	DATANAME=MAPDRIVE5
	get_data
	MAPDRIVE5="$DATAENTRY"

	#Assign MAPDRIVE6
	DATANAME=MAPDRIVE6
	get_data
	MAPDRIVE6="$DATAENTRY"

	#Assign MAPDRIVE7
	DATANAME=MAPDRIVE7
	get_data
	MAPDRIVE7="$DATAENTRY"

	#Assign MAPDRIVE8
	DATANAME=MAPDRIVE8
	get_data
	MAPDRIVE8="$DATAENTRY"

	#Assign MAPDRIVE9
	DATANAME=MAPDRIVE9
	get_data
	MAPDRIVE9="$DATAENTRY"

	#Assign MAPDRIVE10
	DATANAME=MAPDRIVE10
	get_data
	MAPDRIVE10="$DATAENTRY"

	#Assign MAPDRIVE11
	DATANAME=MAPDRIVE11
	get_data
	MAPDRIVE11="$DATAENTRY"

	#Assign MAPDRIVE12
	DATANAME=MAPDRIVE12
	get_data
	MAPDRIVE12="$DATAENTRY"

	#Assign MAPDRIVEALL
	DATANAME=MAPDRIVEALL
	get_data
	MAPDRIVEALL="$DATAENTRY"

	#Assign SERVERNAME
	DATANAME=SERVERNAME
	get_data
	SERVERNAME="$DATAENTRY"

	#Assign SERVERTYPE
	DATANAME=SERVERTYPE
	get_data
	SERVERTYPE="$DATAENTRY"

	#Assign SERVERMASTER
	DATANAME=SERVERMASTER
	get_data
	SERVERMASTER="$DATAENTRY"

	#Assign DRIVELETTER
	DATANAME=DRIVELETTER
	get_data
	DRIVELETTER="$DATAENTRY"

	#Assign RECYCLEBIN
	DATANAME=RECYCLEBIN
	get_data
	RECYCLEBIN="$DATAENTRY"

	#Assign FULLAUDIT
	DATANAME=FULLAUDIT
	get_data
	FULLAUDIT="$DATAENTRY"

	#Assign RECBINDURATION
	DATANAME=RECBINDURATION
	get_data
	RECBINDURATION="$DATAENTRY"

	#Assign SETPERMISSIONS
	DATANAME=SETPERMISSIONS
	get_data
	SETPERMISSIONS="$DATAENTRY"
	[ -z "$SETPERMISSIONS" ] && SETPERMISSIONS=no
fi

function show_status {
echo '<script>'
echo 'alert("'"$MESSAGE"'");'
echo 'window.location = "/cgi-bin/admin/samba_shares.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

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

if [[ $(grep -c ^"$REMOTE_USER": /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallyedit ]
then
	#Check to see that SHAREPATH is not blank
	if [ -z "$SHAREPATH" ]
	then
		MESSAGE=$"You have not entered a folder name."
		show_status
	fi

	#Check to see that SHARENAME is not blank
	if [ -z "$SHARENAME" ]
	then
		MESSAGE=$"You have not entered a sharename."
		show_status
	fi

	#Check that this sharename does not already exist.
	if [ "$ACTION" = reallyadd ]
	then
		if [ -f "/opt/karoshi/server_network/network_shares/$SERVERNAME/$SHARENAME" ]
		then
			MESSAGE=''$SHARENAME' - '$"A share with this name already exists."''
			show_status
		fi
	fi

	#Check to see that GROUP1 is not blank
	if [ -z "$GROUP1" ]
	then
		MESSAGE=$"You have not entered a group."
		show_status
	fi
	#Check to see that GROUPPERMS is not blank
	if [ -z "$GROUPPERMS1" ]
	then
		MESSAGE=$"You have not chosen any group permissions."
		show_status
	fi
	#Check to see that SERVERNAME is not blank
	if [ -z "$SERVERNAME" ]
	then
		MESSAGE=$"You have not chosen a server name."
		show_status
	fi
	#Check to see that SERVERTYPE is not blank
	if [ -z "$SERVERTYPE" ]
	then
		MESSAGE=$"You have not chosen a server type."
		show_status
	fi

	if [ "$SERVERTYPE" = federatedslave ]
	then
		if [ -z "$SERVERMASTER" ]
		then
			MESSAGE=$"You have not chosen a server master."
			show_status
		fi
	fi

	#Check that the SHAREPATH is something sensible.

	#These folders cannot be assigned as network shares.
	PROTECTEDPATHS="/bin /boot /dev /etc /media /mnt /home /home/applications /home/users /initrd /lib /root /opt/karoshi /usr /proc /sbin /sys /var/lib /var/www /var/www/html /var/www/html_karoshi /var/www/cgi-bin /var/www/cgi-bin_karoshi /tmp /root"
	#Sub folders in here cannot be assigned as shares.
	PROTECTEDPATHS2="/usr /boot /bin /etc /lib /sbin /sys /root /dev /tmp"

	#Strip trailing slash for SHAREPATH
	SHAREPATH=$(echo "$SHAREPATH" | sed 's/\/$//g')
	if [[ $(echo "$PROTECTEDPATHS" | grep -c "$SHAREPATH") -gt 0 ]]
	then
		MESSAGE=$"This is a protected path and cannot be added as a share."
		show_status
	fi

	for CHECKPATH in $PROTECTEDPATHS2
	do
		if [[ $(echo "$SHAREPATH" | grep -c "$CHECKPATH") -gt 0 ]]
		then
			MESSAGE=$"This is a protected path and cannot be added as a share."
			show_status
		fi
	done

	#Check that the network drive letter has not already been allocated to a share.
	if [ "$ACTION" = reallyadd ]
	then
		if [ ! -z "$DRIVELETTER" ]
		then

			function check_drive_letter {
			if [ "$GROUP" = all ]
			then
				SHARELIST=$(grep -l -r 'SERVER=' /opt/karoshi/server_network/network_shares/)
			else
				SHARELIST=$(grep -l -w -r "$GROUP" /opt/karoshi/server_network/network_shares/)
			fi

			for SHARE in $SHARELIST
			do
				EXISTINGSHARE=$(basename "$SHARE")
				if [[ $(grep 'DRIVELETTER="'"$DRIVELETTER"'"' "$SHARE" | wc -l) -gt 0 ]]
				then
					MESSAGE=''$"This drive letter is already in use for"' '$EXISTINGSHARE''
					show_status
				fi
			done
			}

			GROUP="$GROUP1"
			check_drive_letter

			GROUP="$GROUP2"
			check_drive_letter

			GROUP="$GROUP3"
			check_drive_letter

			GROUP="$GROUP4"
			check_drive_letter

			GROUP="$GROUP5"
			check_drive_letter

			GROUP="$GROUP6"
			check_drive_letter

			GROUP="$GROUP7"
			check_drive_letter

			GROUP="$GROUP8"
			check_drive_letter

			GROUP="$GROUP9"
			check_drive_letter

			GROUP="$GROUP10"
			check_drive_letter

			GROUP="$GROUP11"
			check_drive_letter

			GROUP="$GROUP12"
			check_drive_letter
		fi
	fi
fi

#Generate navigation bar
if [ "$MOBILE" = no ]
then
	TABLECLASS=standard
	DIV_ID=actionbox3
	#Generate navigation bar
	/opt/karoshi/web_controls/generate_navbar_admin
	echo '<div id="'$DIV_ID'"><div id=titlebox>'
else
	TABLECLASS=mobilestandard
fi


if [ "$ACTION" = add ] || [ "$ACTION" = edit ] || [ "$ACTION" = delete ]
then
	ACTION2=view
	BUTTONTXT=$"View Shares"
	TITLETXT=$"Add Network Share"
	[ "$ACTION" = edit ] && TITLETXT=$"Edit Network Share"
	[ "$ACTION" = delete ] && TITLETXT=$"Delete Network Share"
	ICON1="/images/submenus/system/network-server.png"
fi

if [ "$ACTION" = view ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ] || [ "$ACTION" = reallyedit ] 
then
	ACTION2=add
	BUTTONTXT=$"Add Share"
	TITLETXT=$"View Network Shares"
	ICON1="/images/submenus/system/add.png"
fi

#Show back button for mobiles
if [ "$MOBILE" = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLETXT'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$"Menu"'</a>
</div></div><div id="mobileactionbox">
'
fi

WIDTH=100

ICON3="/images/submenus/file/folder.png"
ICON2="/images/submenus/system/gluster.png"

echo '<form action="/cgi-bin/admin/samba_shares.cgi" method="post">

<div class="sectiontitle">'$TITLETXT' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Network_Shares"><img class="images" alt="" src="/images/help/info.png"><span>'$"Network Shares"'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<button class="info infonavbutton" name="____SambaAction____" value="____ACTION____'$ACTION2'____">
			<img src="'$ICON1'" alt="'$BUTTONTXT'">
			<span>'$BUTTONTXT'</span><br>
			'$BUTTONTXT'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<button class="info infonavbutton" formaction="gluster_control.cgi" name="GlusterVolumeControl" value="_">
			<img src="'$ICON2'" alt="'$"Gluster Volumes"'">
			<span>'$"Configure gluster volumes"'</span><br>
			'$"Gluster Volumes"'
		</button>
	</td>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '$WIDTH'px; text-align:center;">
		<button class="info infonavbutton" formaction="home_folders_fm.cgi" name="ViewHomeFolders" value="_">
			<img src="'$ICON3'" alt="'$"Home Folders"'">
			<span>'$"Configure user home folders"'</span><br>
			'$"Home Folders"'
		</button>
	</td>

</tr></tbody></table>
</form>'

[ "$MOBILE" = no ] && echo '</div><div id="infobox">' 

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/samba_shares.cgi | cut -d' ' -f1)
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ACTION:$COMMENT:$SHARENAME:$SHAREPATH:$GROUP1:$GROUP2:$GROUP3:$GROUP4:$GROUP5:$GROUP6:$GROUP7:$GROUP8:$GROUP9:$GROUP10:$GROUP11:$GROUP12:$GROUPPERMS1:$GROUPPERMS2:$GROUPPERMS3:$GROUPPERMS4:$GROUPPERMS5:$GROUPPERMS6:$GROUPPERMS7:$GROUPPERMS8:$GROUPPERMS9:$GROUPPERMS10:$GROUPPERMS11:$GROUPPERMS12:$ALLPERMS:$MAPDRIVE1:$MAPDRIVE2:$MAPDRIVE3:$MAPDRIVE4:$MAPDRIVE5:$MAPDRIVE6:$MAPDRIVE7:$MAPDRIVE8:$MAPDRIVE9:$MAPDRIVE10:$MAPDRIVE11:$MAPDRIVE12:$MAPDRIVEALL:$DRIVELETTER:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$RECYCLEBIN:$FULLAUDIT:$RECBINDURATION:$SETPERMISSIONS:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/samba_shares
EXIT_STATUS=$?

if [ $EXIT_STATUS = 102 ]
then
	MESSAGE=$"A folder with this name already exists."
	show_status	
fi

if [ $EXIT_STATUS = 103 ]
then
	MESSAGE=$"This share already exits in samba."
	show_status	
fi

[ "$MOBILE" = no ] && echo '</div>'
echo '</div></div></body></html>'
exit
