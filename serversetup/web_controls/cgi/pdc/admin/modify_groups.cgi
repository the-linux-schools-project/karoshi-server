#!/bin/bash
#Copyright (C) 2007  Paul Sharrad
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
########################
#Required input variables
########################
#  _OPTIONCHOICE_ enable,disable,changepasswords,resetpasswords,deleteaccounts
#  _GROUP_ All the users in this group will be affected

############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/modify_groups ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/modify_groups
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script>
<SCRIPT language=JavaScript1.2>
//change 5 to another integer to alter the scroll speed. Greater is faster
var speed=1
var currentpos=0,alt=1,curpos1=0,curpos2=-1
function initialize(){
startit()
}
function scrollwindow(){
if (document.all &&
!document.getElementById)
temp=document.body.scrollTop
else
temp=window.pageYOffset
if (alt==0)
alt=2
else
alt=1
if (alt==0)
curpos1=temp
else
curpos2=temp
if (curpos1!=curpos2){
if (document.all)
currentpos=document.body.scrollTop+speed
else
currentpos=window.pageYOffset+speed
window.scroll(0,currentpos)
}
else{
currentpos=0
window.scroll(0,currentpos)
}
}
function startit(){
setInterval("scrollwindow()",30)
}
window.onload=initialize
</SCRIPT> 

</head><body>'



#########################
#Get data input
#########################
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=15
#Assign OPTIONCHOICE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = OPTIONCHOICEcheck ]
then
let COUNTER=$COUNTER+1
OPTIONCHOICE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PASSWORD1
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PASSWORD1check ]
then
let COUNTER=$COUNTER+1
PASSWORD1=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign PASSWORD2
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PASSWORD2check ]
then
let COUNTER=$COUNTER+1
PASSWORD2=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign GROUP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = GROUPcheck ]
then
let COUNTER=$COUNTER+1
GROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign MODCODE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MODCODEcheck ]
then
let COUNTER=$COUNTER+1
MODCODE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign FORMCODE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = FORMCODEcheck ]
then
let COUNTER=$COUNTER+1
FORMCODE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign EXCEPTIONLIST
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = EXCEPTIONLISTcheck ]
then
let COUNTER=$COUNTER+1
EXCEPTIONLIST=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/modify_groups_fm.cgi";'
echo '</script>'
echo "</body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi
#########################
#Check data
#########################
#Check to see that optionchoice is not blank
if [ $OPTIONCHOICE'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi
#Check to see that the group is not blank
if [ $GROUP'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

#Check to see that the group exists
if [ `grep -c $GROUP: /etc/group` = 0 ]
then
MESSAGE=$ERRORMSG6
show_status
fi
#Check to see that the option choice is correct
if [ $OPTIONCHOICE != enable ] && [ $OPTIONCHOICE != disable ] && [ $OPTIONCHOICE != changepasswords ] && [ $OPTIONCHOICE != resetpasswords ] && [ $OPTIONCHOICE != deleteaccounts ]
then
MESSAGE=$ERRORMSG3
show_status
fi

#Check to see that MODCODE is not blank
if [ $MODCODE'null' = null ]
then
MESSAGE=$ERRORMSG7
show_status
fi
#Check to see that FORMCODE is not blank
if [ $FORMCODE'null' = null ]
then
MESSAGE=$ERRORMSG8
show_status
fi
#Make sure that FORMCODE and MODCODE matches
if [ $FORMCODE != $MODCODE ]
then
MESSAGE=$ERRORMSG9
show_status
fi

#Check to see that passwords have been entered and are correct
if [ $OPTIONCHOICE = changepasswords ]
then
if [ $PASSWORD1'null' = null ] || [ $PASSWORD2'null' = null ]
then
MESSAGE=$ERRORMSG4
show_status
fi
if [ $PASSWORD1 != $PASSWORD2 ]
then
MESSAGE=$ERRORMSG5
show_status
fi
fi

if [ $OPTIONCHOICE = enable ]
then
MESSAGE=`echo $ACTION1 $GROUP`
fi
if [ $OPTIONCHOICE = disable ]
then
MESSAGE=`echo $ACTION2 $GROUP`
fi
if [ $OPTIONCHOICE = changepasswords ]
then
MESSAGE=`echo $ACTION3 $GROUP`
fi
if [ $OPTIONCHOICE = resetpasswords ]
then
MESSAGE=`echo $ACTION4 $GROUP`
fi
if [ $OPTIONCHOICE = deleteaccounts ]
then
MESSAGE=`echo $ACTION5 $GROUP`
fi
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
echo "<div id="actionbox">"
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/modify_groups.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$OPTIONCHOICE:$GROUP:$PASSWORD1:$EXCEPTIONLIST:" | sudo -H /opt/karoshi/web_controls/exec/modify_groups
MODIFY_STATUS=`echo $?`
if [ $MODIFY_STATUS = 102 ]
then
MESSAGE=$ERRORMSG8
show_status
fi

if [ $OPTIONCHOICE != resetpasswords ]
then
MESSAGE=`echo $COMPLETEDMSG $GROUP.`
show_status
else
echo '<br><br>'$COMPLETEDMSG $GROUP'<br>'
echo "</div>"
fi
exit
