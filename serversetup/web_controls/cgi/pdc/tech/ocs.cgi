#!/bin/bash
#Copyright (C) 2009  Paul Sharrad
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
##########################
#Language
##########################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
TEXTDOMAIN=karoshi-server


#Check to see if OCS is enabled
OCSENABLED=no
[ -d /var/www/html_karoshi/tech/ocs ] && OCSENABLED=yes

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo "<html><head><title>$"OCS"</title>"
[ $OCSENABLED = yes ] && echo '<meta http-equiv="REFRESH" content="0;url=/tech/ocs/">'

echo '<link rel="stylesheet" href="/css/'$STYLESHEET'?d='$VERSION'"></head><body><div id="pagecontainer">'

if [ $OCSENABLED = no ]
then
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_tech
echo '<div id="actionbox"><b>'$"OCS"'</b><br><br>'$"The OCS module has not been installed. You can install it in the modules section."''
fi

echo '</div></body></html>'
exit
