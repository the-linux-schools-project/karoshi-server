#!/bin/bash

#The purpose of this script is to mount netlogon, copy the scripts down, and then unmount netlogon and delete the temporary folder it ran from

if [ ! -d /tmp/tmpnetlogon/ ]
	then
		mkdir -p /tmp/tmpnetlogon/
		mount_smbfs "//CHANGETHISDOMAIN/netlogon/" /tmp/tmpnetlogon/
		cp -f /tmp/tmpnetlogon/mac_client/scripts/{mount-shares.sh,detect-user.sh} /Library/Scripts/LoginScripts/
		cp -f /tmp/tmpnetlogon/mac_client/scripts/com.mount-shares.sh.plist /Library/LaunchAgents/
		diskutil unmount force /tmp/tmpnetlogon/
		rmdir /tmp/tmpnetlogon/
fi
