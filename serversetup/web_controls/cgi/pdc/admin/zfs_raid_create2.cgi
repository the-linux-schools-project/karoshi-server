#!/bin/bash
#Copyright (C) 2010  Paul Sharrad
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

##########################
#Language
##########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/software_raid ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/software_raid
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE1'</title>
  <link rel="stylesheet" href="/css/'$STYLESHEET'"></head><body>'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\_\-%'`
#########################
#Assign data to variables
#########################
END_POINT=30
#Assign SERVERNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERNAMEcheck ]
then
let COUNTER=$COUNTER+1
SERVERNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign SERVERTYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERTYPEcheck ]
then
let COUNTER=$COUNTER+1
SERVERTYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign SERVERMASTER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SERVERMASTERcheck ]
then
let COUNTER=$COUNTER+1
SERVERMASTER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign ACTION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ACTIONcheck ]
then
let COUNTER=$COUNTER+1
ACTION=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
#Assign DRIVES
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = DRIVEcheck ]
then
let COUNTER=$COUNTER+1
DRIVE=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%2F/\//g'`
DRIVES=`echo $DRIVES,$DRIVE`
fi
let COUNTER=$COUNTER+1
done
DRIVES=`echo $DRIVES | sed 's/^,//g'`
#Assign PARITY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PARITYcheck ]
then
let COUNTER=$COUNTER+1
PARITY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign CREATETYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CREATETYPEcheck ]
then
let COUNTER=$COUNTER+1
CREATETYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign MOUNTPOINT
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = MOUNTPOINTcheck ]
then
let COUNTER=$COUNTER+1
MOUNTPOINT=`echo $DATA | cut -s -d'_' -f$COUNTER | sed 's/%2F/\//g' | sed 's/%2F/\//g'`
break
fi
let COUNTER=$COUNTER+1
done


function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'");'
echo '</script>
<form METHOD=POST ACTION="/cgi-bin/admin/zfs_raid_create.cgi" target="_top" name = "frm">
<input type="hidden" name="_SERVERNAME_" value="'$SERVERNAME'">
<input type="hidden" name="_SERVERTYPE_" value="'$SERVERTYPE'">
<input type="hidden" name="_SERVERMASTER_" value="'$SERVERMASTER'">
</form>
<script>
document.frm.submit();
</script>
'
echo "</div></body></html>"
exit
}

function control_raid {
echo '
<form METHOD=POST ACTION="/cgi-bin/admin/zfs_raid_control.cgi" target="_top" name = "frm">
<input type="hidden" name="_SERVERNAME_" value="'$SERVERNAME'">
<input type="hidden" name="_SERVERTYPE_" value="'$SERVERTYPE'">
<input type="hidden" name="_SERVERMASTER_" value="'$SERVERMASTER'">
</form>
<script>
document.frm.submit();
</script>
'
echo "</div></body></html>"
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

#Check to see that SERVERNAME is not blank
if [ $SERVERNAME'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

#Check to see that SERVERTYPE is not blank
if [ $SERVERTYPE'null' = null ]
then
MESSAGE=$ERRORMSG15
show_status
fi

#Check to see that SERVERMASTER is not blank
if [ $SERVERTYPE = federatedslave ]
then
if [ $SERVERMASTER'null' = null ]
then
MESSAGE=$ERRORMSG16
show_status
fi
fi

#Check to see that CREATETYPE is not blank
if [ $CREATETYPE'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi

if [ $CREATETYPE = create ]
then
#Check to see that PARITY is not blank
if [ $PARITY'null' = null ]
then
MESSAGE="You have not chosen a parity level."
show_status
fi

if [ $DRIVES'null' = null ]
then
MESSAGE=$ERRORMSG2
show_status
fi


if [ $PARITY'null' = null ]
then
MESSAGE="You have not chosen a create type."
show_status
fi

#Check to see that MOUNTPOINT is not blank
if [ $MOUNTPOINT'null' = null ]
then
MESSAGE=$ERRORMSG5
show_status
fi


#Check that MOUNTPOINT is in an allowed area
if [ `echo $MOUNTPOINT | grep -c ^/home` = 0 ] && [ `echo $MOUNTPOINT | grep -c ^/media/` = 0 ] && [ `echo $MOUNTPOINT | grep -c ^/mnt/` = 0 ] && [ `echo $MOUNTPOINT | grep -c ^/var/` = 0 ]
then
MESSAGE=$ERRORMSG6
show_status
fi


#Sort out drives and spare drives

SPAREDRIVES=`echo -e $DRIVES | sed "s/,/\n/g" | grep spare`
DRIVES=`echo -e $DRIVES | sed "s/,/\n/g" | grep use`

SPAREDRIVES=`echo $SPAREDRIVES | sed "s/ /,/g" | sed "s/spare//g"`
DRIVES=`echo $DRIVES | sed "s/ /,/g" | sed "s/use//g"`

#Check that enough drives have been selected
MINDRIVES=2
[ $PARITY = 2 ] && MINDRIVES=3
[ $PARITY = 3 ] && MINDRIVES=4

if [ `echo $DRIVES | sed 's/,/\n/g' | wc -l` -lt $MINDRIVES ]
then
MESSAGE=$ERRORMSG7
show_status
fi
fi

MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
fi

echo '<div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/mobile_menu.cgi"><b>'$TITLE1 - $SERVER'</b></a></td></tr></tbody></table>'
else
echo '<b>'$TITLE1 - $SERVERNAME'</b><br><br>'
fi

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/zfs_raid_create2.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$SERVERNAME:$SERVERTYPE:$SERVERMASTER:$ACTION:$PARITY:$DRIVES:$SPAREDRIVES:$MOUNTPOINT:$CREATETYPE" | sudo -H /opt/karoshi/web_controls/exec/zfs_raid_create2
control_raid
exit
