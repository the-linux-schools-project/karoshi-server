#!/bin/bash

#For ease of testing output line breaks
#echo -e "\n\n\n"

#First get the username
LoggedInUser=$(whoami)
echo "LoggedInUser is ... "$LoggedInUser

#Next get the AD record and copy in a variable
ADRecord=$(dscl /'Active Directory'/DOVERGRAMBOYS/'All Domains' -read /Users/$LoggedInUser)
echo -e "ADRecord is...\n$ADRecord"

#Next grep the Primary Group
PrimaryGroup=$(echo -e "$ADRecord" | grep dsAttrTypeNative:division: | cut -c 28-)
echo -e "Primary group of $LoggedInUser is $PrimaryGroup"

#Make directory for mount point and then mount to tmp/sharename, one share for each server
if [ ! -d /tmp/$LoggedInUser/ ]
then
	mkdir -p /tmp/$LoggedInUser
	chmod 0700 /tmp/$LoggedInUser
fi

