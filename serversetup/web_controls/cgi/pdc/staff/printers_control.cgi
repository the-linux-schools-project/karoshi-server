#!/bin/bash
#Copyright (C) 2007 paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jsharrad@karoshi.org.uk

#
#Website: http://www.karoshi.org.uk

#Language
STYLESHEET=defaultstyle.css

TITLE="Manage Print Queues"
ERRORMSG10="Authentication failure."


SLEEPTIME=5

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'"$MESSAGE"'")';
echo '                window.location = "/cgi-bin/staff/printers.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Get data input
#########################
DATA=$(cat | tr -cd 'A-Za-z0-9\._:%\-+' | sed 's/____/QUADUNDERSCORE/g' | sed 's/_/12345UNDERSCORE12345/g' | sed 's/QUADUNDERSCORE/_/g')
echo "Content-type: text/html"
echo ""
echo '<html><head><title>'"$TITLE"'</title><meta http-equiv='"'REFRESH'"' content='"'0; URL=printers.cgi'"'></head>'
echo '<link rel="stylesheet" href="/css/'"$STYLESHEET"'?d='"$VERSION"'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'
echo '</head>'
echo '<body><div id="pagecontainer">'
#########################
#Assign data
########################

PRINTDATA="$DATA"


#Check to see that the member of staff is not restricted
if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
	if [[ $(grep -c -w "$REMOTE_USER" /opt/karoshi/web_controls/staff_restrictions.txt) -gt 0 ]]
	then
		sudo -H /opt/karoshi/web_controls/exec/record_staff_error "$REMOTE_USER:$REMOTE_ADDR:$REMOTE_USER"
		sleep "$SLEEPTIME"
		MESSAGE="$ERRORMSG10"
		show_status
	fi
fi


Checksum=$(sha256sum /var/www/cgi-bin_karoshi/staff/printers_control.cgi | cut -d' ' -f1)

PRINTER_ACTION=none
#Get printer name
PRINTERNAME=$(echo "$PRINTDATA" | cut -d_ -f2  | sed 's/12345UNDERSCORE12345/_/g')
#Check to see what action needs to be carried out
if [[ $(echo "$PRINTDATA" | grep -c _enable_) = 1 ]]
then
	PRINTER_ACTION=enable
fi
if [[ $(echo "$PRINTDATA" | grep -c _disable_) = 1 ]]
then
	PRINTER_ACTION=disable
fi
if [[ $(echo "$PRINTDATA" | grep -c _test_) = 1 ]]
then
	PRINTER_ACTION=test
fi
if [[ $(echo "$PRINTDATA" | grep -c _clearqueue_) = 1 ]]
then
	PRINTER_ACTION=clearqueue
fi
if [[ $(echo "$PRINTDATA" | grep -c _removejobid_) = 1 ]]
then
	END_POINT=6
	#Assign jobid
	JOBCOUNTER=2
	while [ "$JOBCOUNTER" -le "$END_POINT" ]
	do
	if [[ $(echo "$DATA" | cut -s -d'_' -f"$JOBCOUNTER") = jobid"$PRINTERNAME" ]]
	then
		let JOBCOUNTER="$JOBCOUNTER"+1
		JOBID=$(echo "$DATA" | cut -s -d'_' -f"$JOBCOUNTER")
		PRINTER_ACTION=removejobid
		break
	fi
	let JOBCOUNTER="$JOBCOUNTER"+1
	done
fi
#Show action to be taken
if [ "$PRINTER_ACTION" != none ]
then
	sudo -H /opt/karoshi/web_controls/exec/printers_control "$REMOTE_USER:$REMOTE_ADDR:$Checksum:$PRINTERNAME:$PRINTER_ACTION:$JOBID"
fi

echo "</div></body></html>"
exit
