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
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/ocs ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/ocs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all

#Check to see if OCS is enabled
OCSENABLED=no
[ -d /var/www/html_karoshi/tech/ocs ] && OCSENABLED=yes

##########################
#Show page
##########################
echo "Content-type: text/html"
echo ""
echo "<html><head><title>$TITLE</title>"
[ $OCSENABLED = yes ] && echo '<meta http-equiv="REFRESH" content="0;url=/tech/ocs/">'

echo '<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"></head><body><div id="pagecontainer">'

if [ $OCSENABLED = no ]
then
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_tech
echo '<div id="actionbox"><b>'$TITLE'</b><br><br>'$ERRORMSG1''
fi

echo '</div></body></html>'
exit
