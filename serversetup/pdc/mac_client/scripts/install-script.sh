#!/bin/bash

#This script only needs to be run once from the client.
#The purpose of this script is to copy the necessary files from netlogon called update-scripts.sh, unmount netlogon and then delete the temporary folder created.
if [ ! -d /Library/Scripts/LoginScripts/ ]
then
	mkdir -p /Library/Scripts/LoginScripts/
	chmod 0755 /Library/Scripts/LoginScripts/
fi

if [ ! -d /tmp/tmpnetlogon/ ]
	then
		mkdir -p /tmp/tmpnetlogon/
		mount_smbfs "//CHANGETHISDOMAIN/netlogon/" /tmp/tmpnetlogon/
		cp -f /tmp/tmpnetlogon/mac_client/scripts/update-scripts.sh /Library/Scripts/LoginScripts/
		cp -f /tmp/tmpnetlogon/mac_client/scripts/com.update-script.sh.plist /Library/LaunchDaemons/
		diskutil unmount force /tmp/tmpnetlogon/
		rmdir /tmp/tmpnetlogon/
fi
