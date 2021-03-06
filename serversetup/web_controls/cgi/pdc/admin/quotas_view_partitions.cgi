#!/bin/bash
#Copyright (C) 2008  Paul Sharrad

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
########################
#Required input variables
########################
#  _SERVER_
##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"View Quota Enabled Partitions"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head><body><div id="pagecontainer">'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox3"><div id="titlebox"><form action="/cgi-bin/admin/quotas_view_partitions.cgi" name="selectservers" method="post"><table class="standard" style="text-align: left;" ><tbody><tr>
<td style="height:30px;"><div class="sectiontitle">'$"View Quota Enabled Partitions"'</div></td>
<td>
<button class="button" formaction="quotas_enable_fm.cgi" name="_QuotaSettings_" value="_">
'$"Enable Quotas"'
</button>
</td>
<td>
<button class="button" formaction="quotas_set_fm.cgi" name="_QuotaSettings_" value="_">
'$"Quota Settings"'
</button>
</td>
<td>
<button class="button" formaction="quotas_view_usage_fm.cgi" name="_QuotaUsage_" value="_">
'$"Quota Usage"'
</button>
</td>
</tr></tbody></table></form></div><div id="infobox">
<br>'

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '</script>'
echo "</div></div></body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
	export MESSAGE=$"You must access this page via https."
	show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
	MESSAGE=$"You must be a Karoshi Management User to complete this action."
	show_status
fi

Checksum=`sha256sum /var/www/cgi-bin_karoshi/admin/quotas_view_partitions.cgi | cut -d' ' -f1`
#Add user
echo "$REMOTE_USER:$REMOTE_ADDR:$Checksum:" | sudo -H /opt/karoshi/web_controls/exec/quotas_view_partitions
echo "</div></div></body></html>"
exit

