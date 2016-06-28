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

##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Network Shares"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
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
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
#########################
#Assign data to variables
#########################
END_POINT=47

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

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = delete ] || [ "$ACTION" = reallydelete ]
then
	END_POINT=26
	#Assign SHARENAME
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SHARENAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			SHARENAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

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

	#Assign SERVERTYPE
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SERVERTYPEcheck ]
		then
			let COUNTER=$COUNTER+1
			SERVERTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign SERVERMASTER
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SERVERMASTERcheck ]
		then
			let COUNTER=$COUNTER+1
			SERVERMASTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

fi

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = edit ] || [ "$ACTION" = reallyedit ]
then
	END_POINT=47
	#Assign COMMENT
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = COMMENTcheck ]
		then
			let COUNTER=$COUNTER+1
			COMMENT=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign SHARENAME
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SHARENAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			SHARENAME=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd "0-9A-Za-z"`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign SHAREPATH
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SHAREPATHcheck ]
		then
			let COUNTER=$COUNTER+1
			SHAREPATH=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%2F/\//g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign GROUP1
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUP1check ]
		then
			let COUNTER=$COUNTER+1
			GROUP1=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUP2
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUP2check ]
		then
			let COUNTER=$COUNTER+1
			GROUP2=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUP3
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUP3check ]
		then
			let COUNTER=$COUNTER+1
			GROUP3=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUP4
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUP4check ]
		then
			let COUNTER=$COUNTER+1
			GROUP4=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUPPERMS1
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUPPERMS1check ]
		then
			let COUNTER=$COUNTER+1
			GROUPPERMS1=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUPPERMS2
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUPPERMS2check ]
		then
			let COUNTER=$COUNTER+1
			GROUPPERMS2=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUPPERMS3
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUPPERMS3check ]
		then
			let COUNTER=$COUNTER+1
			GROUPPERMS3=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign GROUPPERMS4
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = GROUPPERMS4check ]
		then
			let COUNTER=$COUNTER+1
			GROUPPERMS4=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign ALLPERMS
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = ALLPERMScheck ]
		then
			let COUNTER=$COUNTER+1
			ALLPERMS=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign MAPDRIVE1
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = MAPDRIVE1check ]
		then
			let COUNTER=$COUNTER+1
			MAPDRIVE1=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign MAPDRIVE2
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = MAPDRIVE2check ]
		then
			let COUNTER=$COUNTER+1
			MAPDRIVE2=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign MAPDRIVE3
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = MAPDRIVE3check ]
		then
			let COUNTER=$COUNTER+1
			MAPDRIVE3=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign MAPDRIVE4
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = MAPDRIVE4check ]
		then
			let COUNTER=$COUNTER+1
			MAPDRIVE4=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign MAPDRIVEALL
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = MAPDRIVEALLcheck ]
		then
			let COUNTER=$COUNTER+1
			MAPDRIVEALL=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done


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


	#Assign SERVERTYPE
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SERVERTYPEcheck ]
		then
			let COUNTER=$COUNTER+1
			SERVERTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign SERVERMASTER
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = SERVERMASTERcheck ]
		then
			let COUNTER=$COUNTER+1
			SERVERMASTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign DRIVELETTER
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = DRIVELETTERcheck ]
		then
			let COUNTER=$COUNTER+1
			DRIVELETTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

function show_status {
echo '<script>'
echo 'alert("'$MESSAGE'");'
echo 'window.location = "/cgi-bin/admin/samba_shares.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

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
		if [ -f /opt/karoshi/server_network/network_shares/$SERVERNAME/"$SHARENAME" ]
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
	SHAREPATH=`echo $SHAREPATH | sed 's/\/$//g'`
	if [ `echo "$PROTECTEDPATHS" | grep -c "$SHAREPATH"` -gt 0 ]
	then
		MESSAGE=$"This is a protected path and cannot be added as a share."
		show_status
	fi

	for CHECKPATH in $PROTECTEDPATHS2
	do
		if [ `echo "$SHAREPATH" | grep -c "$CHECKPATH"` -gt 0 ]
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
			if [ `grep -r 'DRIVELETTER="'$DRIVELETTER'"' /opt/karoshi/server_network/network_shares | wc -l` -gt 0 ]
			then
				MESSAGE=$"This drive letter is already in use."
				show_status
			fi
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
	BUTTONTXT=$"View Network Shares"
	TITLETXT=$"Add Network Share"
	[ "$ACTION" = edit ] && TITLETXT=$"Edit Network Share"
	[ "$ACTION" = delete ] && TITLETXT=$"Delete Network Share"
fi

if [ "$ACTION" = view ] || [ "$ACTION" = reallyadd ] || [ "$ACTION" = reallydelete ] || [ "$ACTION" = reallyedit ] 
then
	ACTION2=add
	BUTTONTXT=$"Add Network Share"
	TITLETXT=$"View Network Shares"
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
echo '<form action="/cgi-bin/admin/samba_shares.cgi" method="post"><table class="'$TABLECLASS'" style="text-align: left;" ><tbody>
<tr><td style="height:30px;"><div class="sectiontitle">'$TITLETXT'</div></td>
<td>
<input name="____ACTION____'$ACTION2'____" type="submit" class="button" value="'$BUTTONTXT'">
</td>
<td>
<button class="button" formaction="gluster_control.cgi" name="GlusterControl" value="_">
'$"Gluster Volume Control"'
</button>
</td>
<td>
<button class="button" formaction="home_folders_fm.cgi" name="HomeFolders" value="_">
'$"Home Folders"'
</button>
</td>
<td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Network_Shares"><img class="images" alt="" src="/images/help/info.png"><span>'$"Network Shares"'</span></a>
</td></tr></tbody></table></form>
'
[ "$MOBILE" = no ] && echo '</div><div id="infobox">' 

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/samba_shares.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$COMMENT:$SHARENAME:$SHAREPATH:$GROUP1:$GROUP2:$GROUP3:$GROUP4:$GROUPPERMS1:$GROUPPERMS2:$GROUPPERMS3:$GROUPPERMS4:$ALLPERMS:$MAPDRIVE1:$MAPDRIVE2:$MAPDRIVE3:$MAPDRIVE4:$MAPDRIVEALL:$DRIVELETTER:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$MOBILE:" | sudo -H /opt/karoshi/web_controls/exec/samba_shares
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
