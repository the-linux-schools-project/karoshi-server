#!/bin/bash
#Statistics
#Copyright (C) 2007 Paul Sharrad

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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
#Language
TITLE="$TITLE"
ACCESS_ERROR1="You must be a Karoshi Management User to complete this action."

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title></head>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
UPTIME=`uptime`
TCPIPNUMBER=`ifconfig eth0 | grep "inet addr" | tr -s ' ' ' ' | sed 's/ /:/g' | cut -d: -f4`
MACCADDRESS=`ifconfig | grep eth0 | tr -s ' ' ' ' | cut -d' ' -f 5 | sed 's/:/-/g'`
CPUSPEED=`cat /proc/cpuinfo | sed -n 7,7p | sed 's/ /./g' | cut -d. -f3`
BOGOMIPS=`cat /proc/cpuinfo | sed -n 18,18p | sed 's/ /./g' | cut -d. -f2`
CPUTYPE=`cat /proc/cpuinfo | sed -n 5,5p | cut -d' ' -f3-`
TOTAL_MEMORY=`free -m | sed -n 2,2p | tr -s ' ' ' ' | cut -d' ' -f2`
HARD_DISK_SIZE=`fdisk -l | sed -n 2,2p | sed 's/,//g' | cut -d' ' -f3,4`
KERNEL=`uname -r`

echo Up Time: $UPTIME '<br>'
echo TCPIP Number: $TCPIPNUMBER '<br>'
echo Mac Address: $MACCADDRESS '<br>'
echo CPUSPEED: $CPUSPEED '<br>'
echo BOGOMIPS: $BOGOMIPS '<br>'
echo CPU: $CPUTYPE '<br>'
echo Memory: $TOTAL_MEMORY '<br>'
echo Hard Disk size: $HARD_DISK_SIZE '<br>'
echo Kernel: $KERNEL '<br>'
echo "</body></html>"
