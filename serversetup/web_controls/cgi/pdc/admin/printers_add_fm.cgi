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
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_add ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/printer/printers_add
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#Check if timout should be disabled
if [ `echo $REMOTE_ADDR | grep -c $NOTIMEOUT` = 1 ]
then
TIMEOUT=86400
fi
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
#Check that a print server has been declared
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$PRINTSERVERERRORMSG'")';
echo 'window.location = "karoshi_servers_view.cgi";'
echo '</script>'
echo "</body></html>"
exit
}

[ ! -f /opt/karoshi/server_network/printserver ] && show_status

echo '<div id="actionbox"><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td style="vertical-align: top;"><b>'$TITLE'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$HELPMSG1"'</span></a></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers.cgi" name="printers" method="post"><a class="info" href="javascript:void(0)"><input name="SHOWPRINTERS" type="image" class="images" src="/images/submenus/printer/show_printers.png" value=""><span>'$SHOWPRINTERSMSG'</span></a></form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers_delete.cgi" name="printers" method="post"><a class="info" href="javascript:void(0)"><input name="DELETEPRINTER" type="image" class="images" src="/images/submenus/printer/delete_printer.png" value=""><span>'$DELETEPRINTERMSG'</span></a></form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/locations.cgi" name="printers" method="post"><a class="info" href="javascript:void(0)"><input name="ADDLOCATION" type="image" class="images" src="/images/submenus/client/add_location.png" value=""><span>'$ADDLOCATIONMSG'</span></a></form></td>
</tr></tbody></table><br>
'


echo '<form action="/cgi-bin/admin/printers_add.cgi" method="post">'
#Check that a print server has been assigned
if [ ! -f /opt/karoshi/server_network/printserver ]
then
echo $PRINTSERVERERRORMSG
fi

echo '<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 180px;">
'$PRINTERNAMEMSG'</td>
        <td><input name="_PRINTERNAME_" maxlength="15" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxgfx.co.uk/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$PRINTERNAMEHELP"'</span></a>
</td>
      </tr>
      <tr>
        <td>
'$LOCATIONMSG'</td>
        <td>'

###############################
#Location
###############################
if [ -f /var/lib/samba/netlogon/locations.txt ]
then
LOCATION_COUNT=`cat /var/lib/samba/netlogon/locations.txt | wc -l`
else
LOCATION_COUNT=0
fi
#Show current rooms
echo '<select name="_LOCATION_" style="width: 200px;">'
echo '<option value="'$NO_LOCATION'">'$NO_LOCATION'</option>'
COUNTER=1
while [ $COUNTER -le $LOCATION_COUNT ]
do
LOCATION=`sed -n $COUNTER,$COUNTER'p' /var/lib/samba/netlogon/locations.txt`
echo '<option value="'$LOCATION'">'$LOCATION'</option>'
let COUNTER=$COUNTER+1
done
echo '</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$LOCATIONHELP"'</span></a>
</td></tr>'
echo '<tr><td>'$ADDRESSMSG'</td><td><input name="_PRINTERADDRESS_" maxlength="15" style="width: 200px;" size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$ADDRESSHELP"'</span></a>
</td></tr>
<tr><td>'$QUEUEMSG'</td><td><input name="_PRINTERQUEUE_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$QUEUEHELP"'</span></a>
</td></tr>
<tr><td>'$DESCMSG'</td><td><input name="_PRINTERDESC_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'"$DESCHELP"'</span></a>
</td></tr>
      <tr>
        <td>'$NETTYPEMSG'</td>
        <td>
        <select name="_PRINTERTYPE_" style="width: 200px;">
        <option>'$TYPE1MSG'</option>
        <option>'$TYPE2MSG'</option>
        <option>'$TYPE3MSG'</option>
        </select></td></tr>
<tr><td>'$PORTMSG'</td><td>
        <select name="_PRINTERPORT_" style="width: 200px;">
        <option>9100</option>
        <option>9101</option>
        <option>9102</option>
        <option>631</option>
        </select>
        </td><td></td>
      </tr>
    </tbody>
  </table><br><br>
  <input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset">
</form>
</div>
</body>
</html>
'
exit
