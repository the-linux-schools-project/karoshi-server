#!/bin/bash
#Copyright (C) 2007  Paul Sharrad

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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$"Add Network Printer"'</title><meta http-equiv="REFRESH" content="'$TIMEOUT'; URL=/cgi-bin/admin/logout.cgi">
<link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body onLoad="start()"><div id="pagecontainer">'

#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
#Check that a print server has been declared
function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$"A print server has not yet been set up."'")';
echo 'window.location = "karoshi_servers_view.cgi";'
echo '</script>'
echo "</div></body></html>"
exit
}

[ ! -f /opt/karoshi/server_network/printserver ] && show_status

echo '<div id="actionbox"><table class="standard" style="text-align: left;" ><tbody>
<tr><td style="vertical-align: top;"><b>'$"Add Network Printer"'</b></td>
<td style="vertical-align: top;"><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Add a network printer for your client computers."'</span></a></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers.cgi" name="printers" method="post">
<input name="SHOWPRINTERS" type="submit" class="button" value="'$"Show Printers"'">
</form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/printers_delete.cgi" name="printers" method="post">
<input name="DELETEPRINTER" type="submit" class="button" value="'$"Delete Printer"'">
</form></td>
<td style="vertical-align: top;"><form action="/cgi-bin/admin/locations.cgi" name="printers" method="post">
<input name="ADDLOCATION" type="submit" class="button" value="'$"Add Location"'">
</form></td>
</tr></tbody></table><br>
'


echo '<form action="/cgi-bin/admin/printers_add.cgi" method="post">'
#Check that a print server has been assigned
if [ ! -f /opt/karoshi/server_network/printserver ]
then
echo $"A print server has not yet been set up."
fi

echo '<table class="standard" style="text-align: left;" >
    <tbody>
      <tr>
        <td style="width: 180px;">
'$"Printer Name"'</td>
        <td><input name="_PRINTERNAME_" maxlength="15" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxgfx.co.uk/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the name that you want for this printer."'</span></a>
</td>
      </tr>
      <tr>
        <td>
'$"Location"'</td>
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
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Choose the location of this printer. Click on the add locations icon above to add locations."'</span></a>
</td></tr>'
echo '<tr><td>'$"Printer Address"'</td><td><input name="_PRINTERADDRESS_" maxlength="15" style="width: 200px;" size="20" type="text"></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the tcpip number of the printer."'</span></a>
</td></tr>
<tr><td>'$"Queue - LPD only"'</td><td><input name="_PRINTERQUEUE_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in the network queue."'</span></a>
</td></tr>
<tr><td>'$"Description"'</td><td><input name="_PRINTERDESC_" style="width: 200px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Add_Network_Printer"><img class="images" alt="" src="/images/help/info.png"><span>'$"Enter in a description of the printer hardware."'</span></a>
</td></tr>
      <tr>
        <td>'$"Network Type"'</td>
        <td>
        <select name="_PRINTERTYPE_" style="width: 200px;">
        <option>'$"Network Printer TCP"'</option>
        <option>'$"Network Printer IPP"'</option>
        <option>'$"Remote LPD queue"'</option>
        </select></td></tr>
<tr><td>'$"Port"'</td><td>
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
  <input value="'$"Submit"'" class="button" type="submit"> <input value="'$"Reset"'" class="button" type="reset">
</form>
</div>
</div></body>
</html>
'
exit
