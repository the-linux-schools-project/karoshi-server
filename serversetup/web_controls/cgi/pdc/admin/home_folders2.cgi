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
########################
#Required input variables
########################
#  _SERVERNAME_
#  _CURRENTSERVER_
#  _PRIGROUP_
#  _COPYHOMEAREAS_
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
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Change Home Server"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Generate navigation bar
#########################
/opt/karoshi/web_controls/generate_navbar_admin
echo '<div id="actionbox3"><div id="titlebox"><b>'$"Change Home Server"'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$"Change the home server for this group of users."'</span></a><br><br></div><div id="infobox">'

#########################
#Assign data to variables
#########################
END_POINT=12
#Assign CURRENTSERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = CURRENTSERVERcheck ]
	then
		let COUNTER=$COUNTER+1
		CURRENTSERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
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

#Assign PRIGROUP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = PRIGROUPcheck ]
	then
		let COUNTER=$COUNTER+1
		PRIGROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

#Assign COPYHOMEAREAS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = COPYHOMEAREAScheck ]
	then
		let COUNTER=$COUNTER+1
		COPYHOMEAREAS=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/home_folders_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

function completed {
echo '<SCRIPT language="Javascript">'
echo 'window.location = "/cgi-bin/admin/home_folders_fm.cgi";'
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
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
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
#Check to see that SERVERNAME is not blank
if [ -z "$SERVERNAME" ]
then
	MESSAGE=$"The new server you have chosen is not configured as a Karoshi file server."
	show_status
fi
#Check to see that CURRENTSERVER is not blank
if [ -z "$CURRENTSERVER" ]
then
	MESSAGE=$"The home server cannot be blank."
	show_status
fi
#Check to see that PRIGROUP is not blank
if [ -z "$PRIGROUP" ]
then
	MESSAGE=$"The primary group cannot be blank."
	show_status
fi

GLUSTER=no

#Check to see that the new server is available
if [ $SERVERNAME != `hostname-fqdn` ]
then
	if [ ! -f /opt/karoshi/server_network/servers/$SERVERNAME/fileserver ]
	then
		#Check to see if this is a gluster volume
		VOLUME=`echo $SERVERNAME | cut -d. -f1`
		if [ ! -d /opt/karoshi/server_network/gluster-volumes/$VOLUME ]
		then
			MESSAGE=$"The new server you have chosen is not configured as a Karoshi file server."
			show_status
		else
			GLUSTER=yes
		fi
	fi
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/home_folders2.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$CURRENTSERVER:$SERVERNAME:$PRIGROUP:$COPYHOMEAREAS:$GLUSTER" | sudo -H /opt/karoshi/web_controls/exec/home_folders

if [ $? = 101 ]
then
	MESSAGE=`echo $"There was a problem with this action." $"Please check the karoshi web administration logs for more details."`
	show_status
fi
completed
echo '</div></div></div></body></html>'
exit


