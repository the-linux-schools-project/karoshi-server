#!/bin/bash
#Copyright (C) 2008  Paul Sharrad
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

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

########################
#Required input variables
########################
#  _USERNAME_
#  _SURNAME_
# _DAY_
# _MONTH_
# _YEAR_
##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo "<html><head><title>$"Student Internet Logs"</title>"
echo '<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
	<script type="text/javascript" src="/all/mobile_menu/sdmenu.js">
		/***********************************************
		* Slashdot Menu script- By DimX
		* Submitted to Dynamic Drive DHTML code library: http://www.dynamicdrive.com
		* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
		***********************************************/
	</script>
	<script type="text/javascript">
	// <![CDATA[
	var myMenu;
	window.onload = function() {
		myMenu = new SDMenu("my_menu");
		myMenu.init();
	};
	// ]]>
	</script>'
fi

echo '</head><body><div id="pagecontainer">'

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
fi

[ $MOBILE = no ] && echo '<div id="'$DIV_ID'"><div id="titlebox">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=9
SLEEPTIME=5

#Assign USERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = USERNAMEcheck ]
then
let COUNTER=$COUNTER+1
USERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign DATE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DATEcheck ]
then
let COUNTER=$COUNTER+1
DATE=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd '0-9-'`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/staff/dg_view_student_user_logs_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#########################
#Check data
#########################

#Check to see that USERNAME is not blank
if [ $USERNAME'null' = null ]
then
MESSAGE=$"The username cannot be blank."
show_status
fi

#Check to see that DATE is not blank
if [ $DATE'null' = null ]
then
MESSAGE=$"The date cannot be blank."
show_status
fi

DAY=`echo $DATE | cut -d- -f1`
MONTH=`echo $DATE | cut -d- -f2`
YEAR=`echo $DATE | cut -d- -f3`

#Check to see that DAY is not blank
if [ $DAY'null' = null ]
then
MESSAGE=$"The date cannot be blank."
show_status
fi

#Check to see that MONTH is not blank
if [ $MONTH'null' = null ]
then
MESSAGE=$"The date cannot be blank."
show_status
fi

#Check to see that YEAR is not blank
if [ $YEAR'null' = null ]
then
MESSAGE=$"The date cannot be blank."
show_status
fi

#Check that day is not greater than 31
if [ $DAY -gt 31 ]
then
MESSAGE=$"Date input error."
show_status
fi

#Check that the month is not greater than 12
if [ $MONTH -gt 12 ]
then
MESSAGE=$"Date input error."
show_status
fi

if [ $YEAR -lt 2006 ] || [ $YEAR -gt 3006 ]
then
MESSAGE=$"The year is not valid."
show_status
fi

#Check to see that the user exists
getent passwd $USERNAME 1>/dev/null
if [ `echo $?` != 0 ]
then
MESSAGE=`echo $USERNAME - $"This user does not exist."`
show_status
fi

#Check that logs being checked are for a student
STUDENTGROUP=`id -g -n $USERNAME`
if [ `echo $STUDENTGROUP | grep -c ^yr` = 0 ]
then
MESSAGE=$"You can only check the logs for a student."
show_status
fi

#Check to see that the member of staff is not restricted
if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
if [ `grep -c -w $REMOTE_USER /opt/karoshi/web_controls/staff_restrictions.txt` -gt 0 ]
then
sudo -H /opt/karoshi/web_controls/exec/record_staff_error $REMOTE_USER:$REMOTE_ADDR:$REMOTE_USER
sleep $SLEEPTIME
MESSAGE=$"You are not allowed to use this feature."
show_status
fi
fi

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$"User Internet Logs"'</span>
<a href="/cgi-bin/admin/dg_view_student_user_logs_fm.cgi">'$USERNAME'</a>
</div></div><div id="mobileactionbox3">
'
echo '<b>'$"Student Internet Logs"'</b><br><br>'
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/staff/dg_view_student_user_logs.cgi | cut -d' ' -f1`
#View logs
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$USERNAME:$DAY:$MONTH:$YEAR:$REMOTE_USER:$MOBILE" | sudo -H /opt/karoshi/web_controls/exec/dg_view_student_user_logs
EXEC_STATUS=`echo $?`
if [ $EXEC_STATUS = 101 ]
then
MESSAGE=`echo $"There was a problem with this action." $"Internet Logs for"`
show_status
fi
if [ $EXEC_STATUS = 102 ]
then
MESSAGE=`echo $USERNAME $DAY-$MONTH-$YEAR : $"No log for this date."`
show_status
fi
echo '</div></div></body></html>'
exit
