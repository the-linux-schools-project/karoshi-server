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
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Configure Off-Site Backup"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"><script src="/all/stuHover.js" type="text/javascript"></script>
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
el.innerHTML = "<input tabindex= \"6\" value=\"'$AWSACCESSKEYID'\" name=\"____AWSACCESSKEYID____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";
	var el = document.getElementById("extraoptions3");
el.innerHTML = "AWS Secret Access Key";
	var el = document.getElementById("extraoptions4");
el.innerHTML = "<input tabindex= \"6\" value=\"'$AWSSECRETACCESSKEY'\" name=\"____AWSSECRETACCESSKEY____\" style=\"width: 200px\;\" size=\"20\" type=\"password\">";
	var el = document.getElementById("extraoptions5");
el.innerHTML = "Bucket Name";
	var el = document.getElementById("extraoptions6");
el.innerHTML = "<input tabindex= \"6\" value=\"'$AWSBUCKETNAME'\" name=\"____AWSBUCKETNAME____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";
	var el = document.getElementById("extraoptions7");
el.innerHTML = "Bucket Location";
	var el = document.getElementById("extraoptions8");
el.innerHTML = "<select name=\"____AWSBUCKETLOCATION____\" style=\"width: 200px\;\"><option value=\"europe\">Europe</option><option value=\"america\">America</option></select>";
}
if (selectedstyle == "scp") {
	var el = document.getElementById("extraoptions1");
el.innerHTML = "Backup Server";
	var el = document.getElementById("extraoptions2");
el.innerHTML = "<input tabindex= \"6\" value=\"'$BACKUPSERVERNAME'\" name=\"____BACKUPSERVERNAME____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";
	var el = document.getElementById("extraoptions3");
el.innerHTML = "Username to connect as";
	var el = document.getElementById("extraoptions4");
el.innerHTML = "<input tabindex= \"6\" value=\"'$BACKUPUSERNAME'\" name=\"____BACKUPUSERNAME____\" style=\"width: 200px\;\" size=\"20\" type=\"text\">";
	var el = document.getElementById("extraoptions5");
el.innerHTML = "Password";
	var el = document.getElementById("extraoptions6");
el.innerHTML = "<input tabindex= \"6\" value=\"'$BACKUPPASSWORD'\" name=\"____BACKUPPASSWORD____\" style=\"width: 200px\;\" size=\"20\" type=\"password\">";
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
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g'`

#########################
#Assign data to variables
#########################
END_POINT=26

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

if [ "$ACTION" = deletebackupfolder ] || [ "$ACTION" = reallydeletebackupfolder ] || [ "$ACTION" = reallyaddbackupfolder ] || [ "$ACTION" = addbackupfolder ] || [ "$ACTION" = editbackupfolder ] || [ "$ACTION" = delete ] || [ "$ACTION" = edit ]
then
	#Assign BACKUPNAME
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPNAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign BACKUPFOLDER
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPFOLDERcheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPFOLDER=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign DURATION
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = DURATIONcheck ]
		then
			let COUNTER=$COUNTER+1
			DURATION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign FULLBACKUP
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = FULLBACKUPcheck ]
		then
			let COUNTER=$COUNTER+1
			FULLBACKUP=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

fi 

if [ "$ACTION" = reallyadd ] || [ "$ACTION" = edit ] || [ "$ACTION" = setbackupstatus ]
then
	#Assign BACKUPUSERNAME
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPUSERNAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPUSERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
	#Assign BACKUPSERVERNAME
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPSERVERNAMEcheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPSERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

if [ "$ACTION" = reallyadd ]
then
	#Assign BACKUPTYPE
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPTYPEcheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign BACKUPPASSWORD
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPPASSWORDcheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPPASSWORD=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign ENCRYPTIONKEY
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = ENCRYPTIONKEYcheck ]
		then
			let COUNTER=$COUNTER+1
			ENCRYPTIONKEY=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign HOURS
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = HOURScheck ]
		then
			let COUNTER=$COUNTER+1
			HOURS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign MINUTES
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = MINUTEScheck ]
		then
			let COUNTER=$COUNTER+1
			MINUTES=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign STORAGEPATH
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = STORAGEPATHcheck ]
		then
			let COUNTER=$COUNTER+1
			STORAGEPATH=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign FULLBACKUP
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = FULLBACKUPcheck ]
		then
			let COUNTER=$COUNTER+1
			FULLBACKUP=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	#Assign DURATION
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = DURATIONcheck ]
		then
			let COUNTER=$COUNTER+1
			DURATION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done

	if [ "$BACKUPTYPE" = AmazonS3 ]
	then
		END_POINT=36
		#Assign AWSACCESSKEYID
		COUNTER=2
		while [ $COUNTER -le $END_POINT ]
		do
			DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			if [ `echo $DATAHEADER'check'` = AWSACCESSKEYIDcheck ]
			then
				let COUNTER=$COUNTER+1
				AWSACCESSKEYID=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
				break
			fi
			let COUNTER=$COUNTER+1
		done

		#Assign AWSSECRETACCESSKEY
		COUNTER=2
		while [ $COUNTER -le $END_POINT ]
		do
			DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			if [ `echo $DATAHEADER'check'` = AWSSECRETACCESSKEYcheck ]
			then
				let COUNTER=$COUNTER+1
				AWSSECRETACCESSKEY=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
				break
			fi
			let COUNTER=$COUNTER+1
		done

		#Assign AWSBUCKETNAME
		COUNTER=2
		while [ $COUNTER -le $END_POINT ]
		do
			DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			if [ `echo $DATAHEADER'check'` = AWSBUCKETNAMEcheck ]
			then
				let COUNTER=$COUNTER+1
				AWSBUCKETNAME=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
				break
			fi
			let COUNTER=$COUNTER+1
		done

		#Assign AWSBUCKETLOCATION
		COUNTER=2
		while [ $COUNTER -le $END_POINT ]
		do
			DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
			if [ `echo $DATAHEADER'check'` = AWSBUCKETLOCATIONcheck ]
			then
				let COUNTER=$COUNTER+1
				AWSBUCKETLOCATION=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
				break
			fi
			let COUNTER=$COUNTER+1
		done
	fi


fi

if [ "$ACTION" = setbackupstatus ]
then
	#Assign BACKUPSTATUS
	COUNTER=2
	while [ $COUNTER -le $END_POINT ]
	do
		DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
		if [ `echo $DATAHEADER'check'` = BACKUPSTATUScheck ]
		then
			let COUNTER=$COUNTER+1
			BACKUPSTATUS=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/12345UNDERSCORE12345/_/g'`
			break
		fi
		let COUNTER=$COUNTER+1
	done
fi

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
echo '<div id="actionbox3"><div id="titlebox">
<table class="standard" style="text-align: left;" ><tr><td style="vertical-align: top;"><div class="sectiontitle">'$"Configure Off-Site Backup"' - '$SERVERNAME'</div></td><td style="vertical-align: top;">
<form action="/cgi-bin/admin/backup_configure_offsite_fm.cgi" method="post">
<button class="button" name="ChooseServer_" value="_">
'$"Select server"'
</button>
</form>
</td>'

if [ "$ACTION" = view ] || [ "$ACTION" = editbackupfolder ] || [ "$ACTION" = reallyaddbackupfolder ] || [ "$ACTION" = reallydeletebackupfolder ] || [ "$ACTION" = assignbackupserver ] || [ "$ACTION" = setbackupstatus ] || [ "$ACTION" = deletebackupfolder ]
then
	echo '<td><form action="/cgi-bin/admin/backup_configure_offsite.cgi" name="testform" method="post">
	<input name="____ACTION____add____SERVERNAME____'$SERVERNAME'____" type="submit" class="button" value="'$"Add Offsite Backup"'"></form></td>'
fi

if [ "$ACTION" = edit ] || [ "$ACTION" = add ]
then
	echo '<td><form action="/cgi-bin/admin/backup_configure_offsite.cgi" name="testform" method="post">
	<input name="____SERVERNAME____'$SERVERNAME'____" type="submit" class="button" value="'$"View Offsite Backups"'"></form></td>'
fi
echo '<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Configure_Offsite_Backup"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the folders you want to backup."'</span></a></td></tr></tbody></table>
</div><br><div id="infobox">'

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/backup_configure_offsite.cgi | cut -d' ' -f1`
#View logs
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ACTION:$SERVERNAME:$BACKUPSERVERNAME:$BACKUPUSERNAME:$BACKUPTYPE:$BACKUPPASSWORD:$ENCRYPTIONKEY:$HOURS:$MINUTES:$BACKUPNAME:$BACKUPFOLDER:$DURATION:$STORAGEPATH:$FULLBACKUP:$AWSACCESSKEYID:$AWSSECRETACCESSKEY:$AWSBUCKETNAME:$AWSBUCKETLOCATION:" | sudo -H /opt/karoshi/web_controls/exec/backup_configure_offsite
echo "</div></div></div></body></html>"
exit
