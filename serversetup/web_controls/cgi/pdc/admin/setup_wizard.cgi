#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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

#
#Website: http://www.karoshi.org.uk
############################
#Language
############################

STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server
INSTALL_TYPE=`sed -n 1,1p /opt/karoshi/server_network/install_type`

#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
	TIMEOUT=86400
fi

#Change default page to stop recursion problem
if [ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ]
then
	sed -i 's/DEFAULTPAGE=setup_wizard.cgi/DEFAULTPAGE=change_password_fm.cgi/g' /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"Setup Wizard"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi"><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480--></head>
<body>'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
#########################
#Assign data to variables
#########################
END_POINT=12
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

#Assign VIEWEDPAGES
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
	DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
	if [ `echo $DATAHEADER'check'` = VIEWEDPAGEScheck ]
	then
		let COUNTER=$COUNTER+1
		VIEWEDPAGES=`echo $DATA | cut -s -d'_' -f$COUNTER`
		break
	fi
	let COUNTER=$COUNTER+1
done
IMAGE1=incomplete.png
IMAGE2=incomplete.png
IMAGE3=incomplete.png
IMAGE4=incomplete.png
IMAGE5=incomplete.png
IMAGE6=incomplete.png
IMAGE7=incomplete.png
IMAGE8=incomplete.png
IMAGE9=incomplete.png
IMAGEa=incomplete.png
IMAGEb=incomplete.png
IMAGEc=incomplete.png
IMAGEd=incomplete.png

[ -f /opt/karoshi/server_network/web_controls/setup_wizard ] && source /opt/karoshi/server_network/web_controls/setup_wizard

SITEURL=welcome.cgi
if [ ! -z "$ACTION" ]
then
[ $ACTION = 1 ] && SITEURL=karoshi_servers_add_fm.cgi
[ $ACTION = 2 ] && SITEURL=karoshi_servers_view.cgi
[ $ACTION = 3 ] && SITEURL=remote_management_add_fm.cgi
[ $ACTION = 4 ] && SITEURL=label_groups_fm.cgi
[ $ACTION = 5 ] && SITEURL=add_user_fm.cgi
[ $ACTION = 6 ] && SITEURL=locations.cgi
[ $ACTION = 7 ] && SITEURL=setup_wizard_clients_fm.cgi
[ $ACTION = 8 ] && SITEURL=setup_wizard_profiles_fm.cgi
[ $ACTION = 9 ] && SITEURL=asset_register_view.cgi
[ $ACTION = a ] && SITEURL=setup_wizard_printers_fm.cgi
[ $ACTION = b ] && SITEURL=default_user_settings_fm.cgi
[ $ACTION = c ] && SITEURL=bulk_user_creation_upload_fm.cgi
[ $ACTION = d ] && SITEURL=set_default_page_fm.cgi

VIEWEDPAGES=`echo $VIEWEDPAGES$ACTION`

[ `echo $VIEWEDPAGES | grep -c 1` -gt 0 ] && IMAGE1=complete.png
[ `echo $VIEWEDPAGES | grep -c 2` -gt 0 ] && IMAGE2=complete.png
[ `echo $VIEWEDPAGES | grep -c 3` -gt 0 ] && IMAGE3=complete.png
[ `echo $VIEWEDPAGES | grep -c 4` -gt 0 ] && IMAGE4=complete.png
[ `echo $VIEWEDPAGES | grep -c 5` -gt 0 ] && IMAGE5=complete.png
[ `echo $VIEWEDPAGES | grep -c 6` -gt 0 ] && IMAGE6=complete.png
[ `echo $VIEWEDPAGES | grep -c 7` -gt 0 ] && IMAGE7=complete.png
[ `echo $VIEWEDPAGES | grep -c 8` -gt 0 ] && IMAGE8=complete.png
[ `echo $VIEWEDPAGES | grep -c 9` -gt 0 ] && IMAGE9=complete.png
[ `echo $VIEWEDPAGES | grep -c a` -gt 0 ] && IMAGEa=complete.png
[ `echo $VIEWEDPAGES | grep -c b` -gt 0 ] && IMAGEb=complete.png
[ `echo $VIEWEDPAGES | grep -c c` -gt 0 ] && IMAGEc=complete.png
[ `echo $VIEWEDPAGES | grep -c d` -gt 0 ] && IMAGEd=complete.png

echo IMAGE1=$IMAGE1 > /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE2=$IMAGE2 >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE3=$IMAGE3 >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE4=$IMAGE4 >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE5=$IMAGE5 >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE6=$IMAGE6 >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE7=$IMAGE7 >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE8=$IMAGE8 >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGE9=$IMAGE9 >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGEa=$IMAGEa >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGEb=$IMAGEb >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGEc=$IMAGEc >> /opt/karoshi/server_network/web_controls/setup_wizard
echo IMAGEd=$IMAGEd >> /opt/karoshi/server_network/web_controls/setup_wizard

fi



echo '<div id="wizard">
<form action="/cgi-bin/admin/setup_wizard.cgi" method="post">
<input type="hidden" id="age" name="_VIEWEDPAGES_'$VIEWEDPAGES'_" value="">

<table class="standard" style="text-align: left;">
<tbody>
<tr><td style="width: 20px; height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_2_" type="image" class="images"  src="/images/submenus/system/'$IMAGE2'" value=""></a>
</td><td style="width: 140px;">
<input name="_ACTION_2_" value="'$"Add Server Roles"'" class="button wizardbutton" type="submit">
</td></tr>

<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_4_" type="image" class="images" src="/images/submenus/system/'$IMAGE3'" value=""></a>
</td><td>
<input name="_ACTION_3_" value="'$"Management Users"'" class="button wizardbutton" type="submit">
</td></tr>'


if [ "$INSTALL_TYPE" != home ]
then
	echo '<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_4_" type="image" class="images" src="/images/submenus/system/'$IMAGE4'" value=""></a>
</td><td>
<input name="_ACTION_4_" value="'$"Label Groups"'" class="button wizardbutton" type="submit">
</td></tr>'
fi

echo '<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_5_" type="image" class="images" src="/images/submenus/system/'$IMAGE5'" value=""></a>
</td><td>
<input name="_ACTION_5_" value="'$"Add a User"'" class="button wizardbutton" type="submit">
</td></tr>'

if [ "$INSTALL_TYPE" != home ]
then
	echo '<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_6_" type="image" class="images" src="/images/submenus/system/'$IMAGE6'" value=""></a>
</td><td>
<input name="_ACTION_6_" value="'$"Room Locations"'" class="button wizardbutton" type="submit">
</td></tr>

<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_7_" type="image" class="images" src="/images/submenus/system/'$IMAGE7'" value=""></a>
</td><td>
<input name="_ACTION_7_" value="'$"Join Clients"'" class="button wizardbutton" type="submit">
</td></tr>

<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_8_" type="image" class="images" src="/images/submenus/system/'$IMAGE8'" value=""></a>
</td><td>
<input name="_ACTION_8_" value="'$"Profiles"'" class="button wizardbutton" type="submit">
</td></tr>

<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_9_" type="image" class="images" src="/images/submenus/system/'$IMAGE9'" value=""></a>
</td><td>
<input name="_ACTION_9_" value="'$"Add Assets"'" class="button wizardbutton" type="submit">
</td></tr>'
fi

echo '<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_a_" type="image" class="images" src="/images/submenus/system/'$IMAGEa'" value=""></a>
</td><td>
<input name="_ACTION_a_" value="'$"Setup Printers"'" class="button wizardbutton" type="submit">
</td></tr>

<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_b_" type="image" class="images" src="/images/submenus/system/'$IMAGEb'" value=""></a>
</td><td>
<input name="_ACTION_b_" value="'$"User Settings"'" class="button wizardbutton" type="submit">
</td></tr>'

if [ "$INSTALL_TYPE" != home ]
then
	echo '<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_c_" type="image" class="images" src="/images/submenus/system/'$IMAGEc'" value=""></a>
</td><td>
<input name="_ACTION_c_" value="'$"Bulk User Creation"'" class="button wizardbutton" type="submit">
</td></tr>'
fi

echo '<tr><td style="height: 35px;">
<a class="info" href="javascript:void(0)"><input name="_ACTION_d_" type="image" class="images" src="/images/submenus/system/'$IMAGEd'" value=""></a>
</td><td>
<input name="_ACTION_d_" value="'$"Set Default Page"'" class="button wizardbutton" type="submit">
</td></tr>
</tbody></table>
</form></div>
<iframe src="'$SITEURL'" name="setupwizard" width="100%" height="100%" frameborder="0">
  <p>Your browser does not support iframes.</p>
</iframe>
</body></html>
'
exit


