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

STYLESHEET=monstyle.css
export LANG="en_UK"
export LC_ALL=""
TEXTDOMAIN=karoshi-server
source /opt/karoshi/web_controls/language/$LANGCHOICE/menus/menu

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$"System Status"'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><META HTTP-EQUIV="refresh" CONTENT="120">
<style type="text/css">
 #hide1{height:15px !important; width:100px !important; padding-top:6px !important; color: #000 !important }
 #show1{height:15px !important; width:100px !important; padding-top:6px !important; color: #000 !important }
 #show1:hover{color: #fff !important }
 #hide1:hover{color: #fff !important } 
 .row { vertical-align: top; height:auto !important; }
 .list {display:none; }
 .show {display: none; }
 .hide:target + .show {display: inline-block; }
 .hide:target {display: none; }
 .hide:target ~ .list {display:inline; }
 @media print { .hide, .show { display: none; } }
 </style>
</head><body><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_mon

#Show title
echo '<div id="actionbox3"><div id="infobox">'

#Create table
echo '<table class="mon" style="text-align: left;" border="0" cellpadding="1" cellspacing="1"><tbody><tr><td style="width: 180px;"><b>Host Group</b></td><td></td><td style="width: 100px;"><b>ping</b></td><td style="width: 100px;"><b>smb</b></td><td style="width: 100px;"><b>http</b></td><td style="width: 100px;"><b>https</b></td><td style="width: 100px;"><b>pop3</b></td><td style="width: 100px;"><b>pop3s</b></td><td style="width: 100px;"><b>imap</b></td><td style="width: 100px;"><b>imaps</b></td><td style="width: 100px;"><b>smtp</b></td><td style="width: 100px;"><b>dg</b></td><td style="width: 100px;"><b>dns</b></td><td style="width: 100px;"><b>cups</b></td></tr>'

if [ -f  /opt/karoshi/server_network/mon/mon_data_html ]
then
	cat /opt/karoshi/server_network/mon/mon_data_html
else
	echo "<tr><td>No Data</td></tr></tbody></table>"
fi 

echo '</div></div></div></body></html>'
exit
