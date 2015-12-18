#!/bin/bash

#The purpose of this script is to determine if you are a local or domain user. If local then exit, if domain then run the mount-shares.sh script

#If statement to determine if user is local and then exit if they are or run the script Mount-Home-Areas.sh if not local.
UserID=$(id -u)
if [ $UserID -lt 1000 ]
then
	exit
else
	/bin/bash /Library/Scripts/LoginScripts/mount-shares.sh
fi
