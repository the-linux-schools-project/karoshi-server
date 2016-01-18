#!/bin/bash

#The purpose of this script is to determine if you are a local or domain user. If local then exit, if domain then copy down mount-shares.sh to /tmp/

UserID=$(id -u)
if [ $UserID -lt 1000 ]
then
	exit
else
	if [ ! -d /tmp/tmpnetlogon/ ]
	then
		mkdir -p /tmp/tmpnetlogon/
		mount -t smbfs -o nobrowse "//CHANGETHISDOMAIN/netlogon/" /tmp/tmpnetlogon/
		cp -f /tmp/tmpnetlogon/mac_client/scripts/mount-shares.sh /tmp/
		chmod 0755 /tmp/mount-shares.sh
		diskutil unmount force /tmp/tmpnetlogon/
		rmdir /tmp/tmpnetlogon/
		sh /tmp/mount-shares.sh
		rm -f /tmp/mount-shares.sh
	fi
fi
