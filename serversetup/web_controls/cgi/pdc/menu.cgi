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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
############################
#Language
############################

STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<META HTTP-EQUIV="refresh" CONTENT="300; URL=/cgi-bin/blank.cgi">
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
  <title>'$"Web Management"'</title>
<link href="/css/'$STYLESHEET'?d=`date +%F`" rel="stylesheet" type="text/css">
<script src="/all/stuHover.js" type="text/javascript"></script>'


if [ $MOBILE = yes ]
then
echo '	<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
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
/opt/karoshi/web_controls/generate_navbar_top
else
source /opt/karoshi/web_controls/version
echo '<div style="float: center" id="my_menu" class="sdmenu">

      <div class="expanded">
       <span>TLSP '$"DE"'</span>
        <a href="/cgi-bin/all/change_my_password_fm.cgi">'$"All"'</a>
        <a href="/cgi-bin/staff/mobile_menu.cgi">'$"Staff"'</a>
        <a href="/cgi-bin/tech/mobile_menu.cgi">'$"Technician"'</a>
        <a href="/cgi-bin/admin/mobile_menu.cgi">'$"Administrator"'</a>
     <div class="a.current">
<small><small>
'$"Version"' : '$VERSION'
</small></small>
</div>
</div>
</div>'


fi

if [ $MOBILE = no ]
then
echo '<div id="actionbox">'
[ -f /var/www/html_karoshi/statistics.html ] && cat /var/www/html_karoshi/statistics.html
echo '<br><br><br><img src="/images/valid-html401-blue.png" alt="Valid HTML 4.01 Transitional"></div>'
else
echo "<br><br>"
fi
echo '</div></body></html>'
exit
