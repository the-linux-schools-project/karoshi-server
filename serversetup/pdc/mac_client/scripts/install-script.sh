#!/bin/bash

#This script only needs to be run once from the client as root.
#The purpose of this script is to copy the necessary files from netlogon and then delete the temporary folder created.
#Once this script has been downloaded to /tmp/ and run as root you just need to reboot and login as a domain user to test the drive mappings
if [ ! -d /Library/Scripts/LoginScripts/ ]
then
	mkdir -p /Library/Scripts/LoginScripts/
	chmod 0755 /Library/Scripts/LoginScripts/
fi

if [ ! -d /tmp/tmpnetlogon/ ]
	then
		mkdir -p /tmp/tmpnetlogon/
		mount -t smbfs -o nobrowse "//CHANGETHISDOMAIN/netlogon/" /tmp/tmpnetlogon/
		cp -f /tmp/tmpnetlogon/mac_client/scripts/detect-user.sh /Library/Scripts/LoginScripts/
		chown root /Library/Scripts/LoginScripts/detect-user.sh
		chmod 0755 /Library/Scripts/LoginScripts/detect-user.sh
		cp -f /tmp/tmpnetlogon/mac_client/scripts/detect-user.sh.plist /Library/LaunchAgents/
		chown root /Library/LaunchAgents/detect-user.sh.plist
		chmod 0644 /Library/LaunchAgents/detect-user.sh.plist
		diskutil unmount force /tmp/tmpnetlogon/
		rmdir /tmp/tmpnetlogon/
fi
