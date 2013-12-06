#!/bin/bash
#Copyright (C) 2007 Paul Sharrad
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
STYLESHEET=monstyle.css
LANGCHOICE=englishuk

source /opt/karoshi/web_controls/language/$LANGCHOICE/menus/menu

[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/system/mon_status ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/system/mon_status
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><META HTTP-EQUIV="refresh" CONTENT="120"></head><body>'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_mon
echo '<div id="actionbox">'


#Show title
echo '<hr style="width: 100%; height: 2px;"><b>'$TITLE'</b>'

#Create table
echo '<br><br>
<table class="mon" style="text-align: left;" border="0" cellpadding="1" cellspacing="1"><tbody><tr><td style="width: 180px;"><b>Host Group</b></td><td></td><td style="width: 80px;"><b>ping</b></td><td style="width: 80px;"><b>smb</b></td><td style="width: 80px;"><b>http</b></td><td style="width: 80px;"><b>https</b></td><td style="width: 80px;"><b>pop3</b></td><td style="width: 80px;"><b>pop3s</b></td><td style="width: 80px;"><b>imap</b></td><td style="width: 80px;"><b>imaps</b></td><td style="width: 80px;"><b>smtp</b></td><td style="width: 80px;"><b>dg</b></td><td style="width: 80px;"><b>dns</b></td><td style="width: 80px;"><b>cups</b></td></tr>'

if [ -f  /opt/karoshi/server_network/mon/mon_data_html ]
then
cat /opt/karoshi/server_network/mon/mon_data_html
else
echo "<tr><td>No Data</td></tr></tbody></table>"
fi 

echo '</div></body></html>'
exit
