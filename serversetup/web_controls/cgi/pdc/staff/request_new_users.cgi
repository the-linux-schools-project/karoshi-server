#!/bin/bash
#Request New Users
#Copyright (C) 2009 Paul Sharrad
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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk

############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/request_new_users ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/request_new_users
############################
#Show page
############################

SLEEPTIME=5

echo "Content-type: text/html"
echo ""
echo '<html><head><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+-'`
#########################
#Assign data to variables
#########################
MYUSERNAME=`echo $DATA | cut -d_ -f3`
MYPASSWORD=`echo $DATA | cut -d_ -f5`

FORENAME1=`echo $DATA | cut -d_ -f3`
SURNAME1=`echo $DATA | cut -d_ -f5`
GROUP1=`echo $DATA | cut -d_ -f7`
ADNO1=`echo $DATA | cut -d_ -f9`

FORENAME2=`echo $DATA | cut -d_ -f11`
SURNAME2=`echo $DATA | cut -d_ -f13`
GROUP2=`echo $DATA | cut -d_ -f15`
ADNO2=`echo $DATA | cut -d_ -f17`

FORENAME3=`echo $DATA | cut -d_ -f19`
SURNAME3=`echo $DATA | cut -d_ -f21`
GROUP3=`echo $DATA | cut -d_ -f23`
ADNO3=`echo $DATA | cut -d_ -f25`

FORENAME4=`echo $DATA | cut -d_ -f27`
SURNAME4=`echo $DATA | cut -d_ -f29`
GROUP4=`echo $DATA | cut -d_ -f31`
ADNO4=`echo $DATA | cut -d_ -f33`

FORENAME5=`echo $DATA | cut -d_ -f35`
SURNAME5=`echo $DATA | cut -d_ -f37`
GROUP5=`echo $DATA | cut -d_ -f39`
ADNO5=`echo $DATA | cut -d_ -f41`

FORENAME6=`echo $DATA | cut -d_ -f43`
SURNAME6=`echo $DATA | cut -d_ -f45`
GROUP6=`echo $DATA | cut -d_ -f47`
ADNO6=`echo $DATA | cut -d_ -f49`

FORENAME7=`echo $DATA | cut -d_ -f51`
SURNAME7=`echo $DATA | cut -d_ -f53`
GROUP7=`echo $DATA | cut -d_ -f55`
ADNO7=`echo $DATA | cut -d_ -f57`

FORENAME8=`echo $DATA | cut -d_ -f59`
SURNAME8=`echo $DATA | cut -d_ -f61`
GROUP8=`echo $DATA | cut -d_ -f63`
ADNO8=`echo $DATA | cut -d_ -f65`

FORENAME9=`echo $DATA | cut -d_ -f67`
SURNAME9=`echo $DATA | cut -d_ -f69`
GROUP9=`echo $DATA | cut -d_ -f71`
ADNO9=`echo $DATA | cut -d_ -f73`

FORENAME10=`echo $DATA | cut -d_ -f75`
SURNAME10=`echo $DATA | cut -d_ -f77`
GROUP10=`echo $DATA | cut -d_ -f79`
ADNO10=`echo $DATA | cut -d_ -f81`

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'history.go(-1);'
echo '</script>'
echo "</div></body></html>"
exit
}

function show_status2 {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/staff/request_new_users_fm.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_staff
echo '<div id="actionbox">'
#########################
#Check data
#########################

#Check some fornames have been entered
if [ `echo $FORENAME1$FORENAME2$FORENAME3$FORENAME4$FORENAME5$FORENAME6$FORENAME7$FORENAME8$FORENAME9$FORENAME10'null'` = null ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Check some surnames have been entered
if [ `echo $SURNAME1$SURNAME2$SURNAME3$SURNAME4$SURNAME5$SURNAME6$SURNAME7$SURNAME8$SURNAME9$SURNAME10'null'` = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi

if [ $FORENAME1'null' != null ]
then
if [ $SURNAME1'null' = null ]
then
MESSAGE=`echo $FORENAME1 - $ERRORMSG5`
show_status
fi
if [ $GROUP1'null' = null ]
then
MESSAGE=`echo $FORENAME1 $SURNAME1 - $ERRORMSG6`
show_status
fi
fi

if [ $FORENAME2'null' != null ]
then
if [ $SURNAME2'null' = null ]
then
MESSAGE=`echo $FORENAME2 - $ERRORMSG5`
show_status
fi
if [ $GROUP2'null' = null ]
then
MESSAGE=`echo $FORENAME2 $SURNAME2 - $ERRORMSG6`
show_status
fi
fi

if [ $FORENAME3'null' != null ]
then
if [ $SURNAME3'null' = null ]
then
MESSAGE=`echo $FORENAME3 - $ERRORMSG5`
show_status
fi
if [ $GROUP3'null' = null ]
then
MESSAGE=`echo $FORENAME3 $SURNAME3 - $ERRORMSG6`
show_status
fi
fi

if [ $FORENAME4'null' != null ]
then
if [ $SURNAME4'null' = null ]
then
MESSAGE=`echo $FORENAME4 - $ERRORMSG5`
show_status
fi
if [ $GROUP4'null' = null ]
then
MESSAGE=`echo $FORENAME4 $SURNAME4 - $ERRORMSG6`
show_status
fi
fi

if [ $FORENAME5'null' != null ]
then
if [ $SURNAME5'null' = null ]
then
MESSAGE=`echo $FORENAME5 - $ERRORMSG5`
show_status
fi
if [ $GROUP5'null' = null ]
then
MESSAGE=`echo $FORENAME5 $SURNAME5 - $ERRORMSG6`
show_status
fi
fi

if [ $FORENAME6'null' != null ]
then
if [ $SURNAME6'null' = null ]
then
MESSAGE=`echo $FORENAME6 - $ERRORMSG5`
show_status
fi
if [ $GROUP6'null' = null ]
then
MESSAGE=`echo $FORENAME6 $SURNAME6 - $ERRORMSG6`
show_status
fi
fi

if [ $FORENAME7'null' != null ]
then
if [ $SURNAME7'null' = null ]
then
MESSAGE=`echo $FORENAME7 - $ERRORMSG5`
show_status
fi
if [ $GROUP7'null' = null ]
then
MESSAGE=`echo $FORENAME7 $SURNAME7 - $ERRORMSG6`
show_status
fi
fi

if [ $FORENAME8'null' != null ]
then
if [ $SURNAME8'null' = null ]
then
MESSAGE=`echo $FORENAME8 - $ERRORMSG5`
show_status
fi
if [ $GROUP8'null' = null ]
then
MESSAGE=`echo $FORENAME8 $SURNAME8 - $ERRORMSG6`
show_status
fi
fi

if [ $FORENAME9'null' != null ]
then
if [ $SURNAME9'null' = null ]
then
MESSAGE=`echo $FORENAME9 - $ERRORMSG5`
show_status
fi
if [ $GROUP9'null' = null ]
then
MESSAGE=`echo $FORENAME9 $SURNAME9 - $ERRORMSG6`
show_status
fi
fi

#Check to see that the member of staff is not restricted
if [ -f /opt/karoshi/web_controls/staff_restrictions.txt ]
then
if [ `grep -c -w $REMOTE_USER /opt/karoshi/web_controls/staff_restrictions.txt` -gt 0 ]
then
sudo -H /opt/karoshi/web_controls/exec/record_staff_error $REMOTE_USER:$REMOTE_ADDR:$MYUSERNAME
sleep $SLEEPTIME
MESSAGE=$ERRORMSG10
show_status
fi
fi


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/staff/request_new_users.cgi | cut -d' ' -f1`
#Change student password
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$REMOTE_USER:$FORENAME1:$SURNAME1:$GROUP1:$ADNO1:$FORENAME2:$SURNAME2:$GROUP2:$ADNO2:$FORENAME3:$SURNAME3:$GROUP3:$ADNO3:$FORENAME4:$SURNAME4:$GROUP4:$ADNO4:$FORENAME5:$SURNAME5:$GROUP5:$ADNO5:$FORENAME6:$SURNAME6:$GROUP6:$ADNO6:$FORENAME7:$SURNAME7:$GROUP7:$ADNO7:$FORENAME8:$SURNAME8:$GROUP8:$ADNO8:$FORENAME9:$SURNAME9:$GROUP9:$ADNO9:$FORENAME10:$SURNAME10:$GROUP10:$ADNO10:" | sudo -H /opt/karoshi/web_controls/exec/request_new_users
MESSAGE=`echo $COMPLETEDMSG`
show_status2
exit
