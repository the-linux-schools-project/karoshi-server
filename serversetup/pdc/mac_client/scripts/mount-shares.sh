#!/bin/bash
#Copyright (C) 2015 Jonathan Hosier

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

#First get the username
LoggedInUser=$(whoami)
echo "LoggedInUser is ... "$LoggedInUser

#Next get the AD record and copy in a variable
ADRecord=$(dscl /'Active Directory'/DOVERGRAMBOYS/'All Domains' -read /Users/$LoggedInUser)
echo -e "ADRecord is...\n$ADRecord"

#Next grep the Primary Group
PrimaryGroup=$(echo -e "$ADRecord" | grep dsAttrTypeNative:division: | cut -c 28-)
echo -e "Primary group of $LoggedInUser is $PrimaryGroup"

#Make directory for mount points
if [ ! -d /tmp/$LoggedInUser/ ]
then
	mkdir -p /tmp/$LoggedInUser
	chmod 0700 /tmp/$LoggedInUser
fi

#Make directory for network home area
[ ! -d /tmp/$LoggedInUser/home/ ] && mkdir -p /tmp/$LoggedInUser/home/

