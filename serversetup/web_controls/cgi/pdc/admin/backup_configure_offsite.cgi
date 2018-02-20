#!/bin/bash
#Copyright (C) 20016 Paul Sharrad

#This file is part of Karoshi SERVERNAME.
#
#Karoshi SERVERNAME is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Karoshi SERVERNAME is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Karoshi SERVERNAME.  If not, see <http://www.gnu.org/licenses/>.

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
[ -f /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER" ] && source /opt/karoshi/web_controls/user_prefs/"$REMOTE_USER"
export TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Configure Off-Site Backup"'</title><link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/stuHover.js" type="text/javascript"></script>
<script src="/all/js/jquery.js"></script>
<script src="/all/js/jquery.tablesorter/jquery.tablesorter.js"></script>
<script id="js">
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
);
</script>
<script>
function rewriteselect() {
document.myform.____BACKUPTYPE____.options.selectedIndex.length=0;
var el = document.getElementById("extraoptions1");
el.innerHTML = "";

var el = document.getElementById("extraoptions2");
el.innerHTML = "";

var el = document.getElementById("extraoptions3");
el.innerHTML = "";

var el = document.getElementById("extraoptions4");
el.innerHTML = "";

var el = document.getElementById("extraoptions5");
el.innerHTML = "";

var el = document.getElementById("extraoptions6");
el.innerHTML = "";

var el = document.getElementById("extraoptions7");
el.innerHTML = "";

var el = document.getElementById("extraoptions8");
el.innerHTML = "";

var selectedstyle = document.myform.____BACKUPTYPE____.value;

if (selectedstyle == "AmazonS3") {
	var el = document.getElementById("extraoptions1");
el.innerHTML = "AWS Access Key ID";
	var el = document.getElementById("extraoptions2");
el.innerHTML = "<input tabindex= \"6\" value=\"'"$AWSACCESSKEYID"'\" name=\"____AWSACCESSKEYID____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";
	var el = document.getElementById("extraoptions3");
el.innerHTML = "AWS Secret Access Key";
	var el = document.getElementById("extraoptions4");
el.innerHTML = "<input tabindex= \"6\" value=\"'"$AWSSECRETACCESSKEY"'\" name=\"____AWSSECRETACCESSKEY____\" style=\"width: 200px\;\" size=\"20\" type=\"password\">";
	var el = document.getElementById("extraoptions5");
el.innerHTML = "Bucket Name";
	var el = document.getElementById("extraoptions6");
el.innerHTML = "<input tabindex= \"6\" value=\"'"$AWSBUCKETNAME"'\" name=\"____AWSBUCKETNAME____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";
	var el = document.getElementById("extraoptions7");
el.innerHTML = "Bucket Location";
	var el = document.getElementById("extraoptions8");
el.innerHTML = "<select name=\"____AWSBUCKETLOCATION____\" style=\"width: 200px\;\"><option value=\"europe\">Europe</option><option value=\"america\">America</option></select>";
}
if (selectedstyle == "scp") {
	var el = document.getElementById("extraoptions1");
el.innerHTML = "Backup Server";
	var el = document.getElementById("extraoptions2");
el.innerHTML = "<input tabindex= \"6\" value=\"'"$BACKUPSERVERNAME"'\" name=\"____BACKUPSERVERNAME____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";
	var el = document.getElementById("extraoptions3");
el.innerHTML = "Username to connect as";
	var el = document.getElementById("extraoptions4");
el.innerHTML = "<input tabindex= \"6\" value=\"'"$BACKUPUSERNAME"'\" name=\"____BACKUPUSERNAME____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";
	var el = document.getElementById("extraoptions5");
el.innerHTML = "Password";
	var el = document.getElementById("extraoptions6");
el.innerHTML = "<input tabindex= \"6\" value=\"'"$BACKUPPASSWORD"'\" name=\"____BACKUPPASSWORD____\" style=\"width: 200px\;\" size=\"20\" type=\"password\">";
}
if (selectedstyle == "local") {
	var el = document.getElementById("extraoptions1");
el.innerHTML = "Partition Label";
	var el = document.getElementById("extraoptions2");
el.innerHTML = "<input tabindex= \"6\" value=\"offsite-backup\" name=\"____LABEL____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";
}
}
</script>
</head><body><div id="pagecontainer">'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/backup_configure_offsite_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}


#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g')

#########################
#Assign data to variables
#########################
END_POINT=26
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


#Assign SERVERNAME
DATANAME=SERVERNAME
get_data
SERVERNAME="$DATAENTRY"

#Assign ACTION
DATANAME=ACTION
get_data
ACTION="$DATAENTRY"

[ -z "$ACTION" ] && ACTION=view

if [ "$ACTION" = deletebackupfolder ] || [ "$ACTION" = reallydeletebackupfolder ] || [ "$ACTION" = reallyaddbackupfolder ] || [ "$ACTION" = addbackupfolder ] || [ "$ACTION" = editbackupfolder ] || [ "$ACTION" = delete ] || [ "$ACTION" = edit ]
then
	#Assign BACKUPNAME
	DATANAME=BACKUPNAME
	get_data
	BACKUPNAME=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign BACKUPFOLDER
	DATANAME=BACKUPFOLDER
	get_data
	BACKUPFOLDER=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign DURATION
	DATANAME=DURATION
	get_data
	DURATION=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign FULLBACKUP
	DATANAME=FULLBACKUP
	get_data
	FULLBACKUP=${DATAENTRY//12345UNDERSCORE12345/_}
fi 

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = edit ] || [ "$ACTION" = setbackupstatus ]
then
	#Assign BACKUPUSERNAME
	DATANAME=BACKUPUSERNAME
	get_data
	BACKUPUSERNAME=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign BACKUPSERVERNAME
	DATANAME=BACKUPSERVERNAME
	get_data
	BACKUPSERVERNAME=${DATAENTRY//12345UNDERSCORE12345/_}
fi

if [ "$ACTION" = reallyadd ]
then
	#Assign BACKUPTYPE
	DATANAME=BACKUPTYPE
	get_data
	BACKUPTYPE=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign BACKUPPASSWORD
	DATANAME=BACKUPPASSWORD
	get_data
	BACKUPPASSWORD=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign ENCRYPTIONKEY
	DATANAME=ENCRYPTIONKEY
	get_data
	ENCRYPTIONKEY=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign HOURS
	DATANAME=HOURS
	get_data
	HOURS=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign MINUTES
	DATANAME=MINUTES
	get_data
	MINUTES=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign STORAGEPATH
	DATANAME=STORAGEPATH
	get_data
	STORAGEPATH=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign FULLBACKUP
	DATANAME=FULLBACKUP
	get_data
	FULLBACKUP=${DATAENTRY//12345UNDERSCORE12345/_}

	#Assign DURATION
	DATANAME=DURATION
	get_data
	DURATION=${DATAENTRY//12345UNDERSCORE12345/_}

	if [ "$BACKUPTYPE" = local ]
	then
		#Assign LABEL
		DATANAME=LABEL
		get_data
		LABEL=${DATAENTRY//12345UNDERSCORE12345/_}
	fi

	if [ "$BACKUPTYPE" = AmazonS3 ]
	then
		END_POINT=36
		#Assign AWSACCESSKEYID
		DATANAME=AWSACCESSKEYID
		get_data
		AWSACCESSKEYID=${DATAENTRY//12345UNDERSCORE12345/_}

		#Assign AWSSECRETACCESSKEY
		DATANAME=AWSSECRETACCESSKEY
		get_data
		AWSSECRETACCESSKEY=${DATAENTRY//12345UNDERSCORE12345/_}

		#Assign AWSBUCKETNAME
		DATANAME=AWSBUCKETNAME
		get_data
		AWSBUCKETNAME=${DATAENTRY//12345UNDERSCORE12345/_}

		#Assign AWSBUCKETLOCATION
		DATANAME=AWSBUCKETLOCATION
		get_data
		AWSBUCKETLOCATION=${DATAENTRY//12345UNDERSCORE12345/_}
	fi


fi

if [ "$ACTION" = setbackupstatus ]
then
	#Assign BACKUPSTATUS
	DATANAME=BACKUPSTATUS
	get_data
	BACKUPSTATUS=${DATAENTRY//12345UNDERSCORE12345/_}
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

if [[ $(grep -c ^"$REMOTE_USER:" /opt/karoshi/web_controls/web_access_admin) != 1 ]]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi
#########################
#Check data
#########################
#Check to see that a SERVERNAME has been chosen
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"You must choose a server."
	show_status
fi

if [ "$ACTION" = reallyaddbackupfolder ]
then
	if [ -z "$BACKUPFOLDER" ]
	then
		MESSAGE=$"You have not entered a backup folder."
		show_status
	fi

	if [ -z "$DURATION" ]
	then
		MESSAGE=$"You have not entered a duration."
		show_status
	fi

	if [ -z "$BACKUPNAME" ]
	then
		MESSAGE=$"You have not chosen a backup name."
		show_status
	fi
fi

if [ "$ACTION" = reallyadd ]
then
	if [ -z "$BACKUPTYPE" ]
	then
		MESSAGE=$"You have not chosen a backup type."
		show_status
	fi

	if [ "$BACKUPTYPE" = scp ]
	then
		if [ -z "$BACKUPSERVERNAME" ]
		then
			MESSAGE=$"You have not entered a backup server name."
			show_status
		fi

		if [ -z "$BACKUPUSERNAME" ]
		then
			MESSAGE=$"You have not entered a backup user name."
			show_status
		fi
	fi

	if [ "$BACKUPTYPE" = AmazonS3 ]
	then
		if [ -z "$AWSACCESSKEYID" ]
		then
			MESSAGE=$"You have not entered your AWS secret key ID."
			show_status
		fi

		if [ -z "$AWSSECRETACCESSKEY" ]
		then
			MESSAGE=$"You have not entered your AWS secret access key."
			show_status
		fi

		if [ -z "$AWSBUCKETNAME" ]
		then
			MESSAGE=$"You have not entered your AWS bucket name."
			show_status
		fi

		if [ -z "$AWSBUCKETLOCATION" ]
		then
			MESSAGE=$"You have not entered your AWS bucket location."
			show_status
		fi
	fi



	if [ -z "$ENCRYPTIONKEY" ]
	then
		MESSAGE=$"You have not entered an encryption key."
		show_status
	fi

	if [ -z "$STORAGEPATH" ]
	then
		MESSAGE=$"You have not entered a storage path."
		show_status
	fi
fi

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

WIDTH=100
ICON1=/images/submenus/system/computer.png
ICON2=/images/submenus/system/add.png
ICON3=/images/submenus/system/backup.png

echo '<div id="actionbox3"><div id="titlebox">

<div class="sectiontitle">'$"Configure Off-Site Backup"' - '"$SERVERNAME"' <a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Configure_Offsite_Backup"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the folders you want to backup."'</span></a></div>
<table class="tablesorter"><tbody><tr>

	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/backup_configure_offsite_fm.cgi" method="post">
			<button class="info infonavbutton" name="SelectServer" value="_">
				<img src="'"$ICON1"'" alt="'$"Select server"'">
				<span>'$"Select the server you want to view."'</span><br>
				'$"Select Server"'
			</button>
		</form>
	</td>
'

if [ "$ACTION" = view ] || [ "$ACTION" = editbackupfolder ] || [ "$ACTION" = reallyaddbackupfolder ] || [ "$ACTION" = reallydeletebackupfolder ] || [ "$ACTION" = assignbackupserver ] || [ "$ACTION" = setbackupstatus ] || [ "$ACTION" = deletebackupfolder ]
then
	echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/backup_configure_offsite.cgi" name="testform" method="post">
			<button class="info infonavbutton" name="____AddOffsiteBackup____" value="____ACTION____add____SERVERNAME____'"$SERVERNAME"'____">
				<img src="'"$ICON2"'" alt="'$"Add Offsite Backup"'">
				<span>'$"Add an offsite backup."'</span><br>
				'$"Add Offsite Backup"'
			</button>
		</form>
	</td>
	'
fi

if [ "$ACTION" = edit ] || [ "$ACTION" = add ]
then
	echo '
	<td style="vertical-align: top; height: 30px; white-space: nowrap; min-width: '"$WIDTH"'px; text-align:center;">
		<form action="/cgi-bin/admin/backup_configure_offsite.cgi" name="testform" method="post">
			<button class="info infonavbutton" name="____ViewOffsiteBackup____" value="____SERVERNAME____'"$SERVERNAME"'____">
				<img src="'"$ICON3"'" alt="'$"View Offsite Backups"'">
				<span>'$"View configured offsite backups."'</span><br>
				'$"View Offsite Backups"'
			</button>
		</form>
	</td>
	'
fi
echo '</tr></tbody></table></div><br><div id="infobox">'

Checksum=$(sha256sum /var/www/cgi-bin_karoshi/admin/backup_configure_offsite.cgi | cut -d' ' -f1)
#View logs
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$ACTION:$SERVERNAME:$BACKUPSERVERNAME:$BACKUPUSERNAME:$BACKUPTYPE:$BACKUPPASSWORD:$ENCRYPTIONKEY:$HOURS:$MINUTES:$BACKUPNAME:$BACKUPFOLDER:$DURATION:$STORAGEPATH:$FULLBACKUP:$AWSACCESSKEYID:$AWSSECRETACCESSKEY:$AWSBUCKETNAME:$AWSBUCKETLOCATION:$LABEL:" | sudo -H /opt/karoshi/web_controls/exec/backup_configure_offsite
echo "</div></div></div></body></html>"
exit
