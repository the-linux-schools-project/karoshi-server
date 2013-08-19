#!/bin/bash
#Copyright (C) 2007 Paul Sharrad

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
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk

############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>HTML & CSS Avery White Heavy Duty Laser Labels, 99.1 x 38.1 mm, L7063-20/L7063</title>
    <style>
    body {
        width: 210mm;
        margin: 2mm;
        }
    .label{
        /*Square Self-Adhesive Paper Labels 37mm, 35 per Shet, L7063-20/L7063 */
        width:96.5mm; 
        height: 38.1mm;
        padding: 0mm 0mm 0mm 0mm;
        margin-right: 1mm; 

        float: center;

        text-align: center;
        overflow: hidden;

        outline: 1px dotted; /* outline doesnt occupy space like border does */
        }
    .page-break  {
        clear: left;
        display:block;
        page-break-after:always;
        }
    </style>

</head>
<body>'

#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-+%'`
#echo $DATA"<br>"

END_POINT=14

#Assign LOCATION
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = LOCATIONcheck ]
then
let COUNTER=$COUNTER+1
LOCATION=`echo $DATA | cut -s -d'_' -f$COUNTER  | sed 's/%2F/\//g' | sed "s/Z%25%25%25%25%25Z/_/g"`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo '                window.location = "/cgi-bin/admin/view_karoshi_web_admin_log.cgi";'
echo '</script>'
echo "</body></html>"
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

MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/asset_register_show_qrcodes.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$LOCATION:" | sudo -H /opt/karoshi/web_controls/exec/asset_register_show_qrcodes

echo '</body></html>'
exit
