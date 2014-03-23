#!/bin/bash
#Copyright (C) 2014 Paul Sharrad

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

########################
#Required input variables
########################
#  _USERNAME_

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

########################
#Language
########################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/groups ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/groups
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
#########################
#Show page
#########################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE1'</title><link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'"><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->'

if [ $MOBILE = yes ]
then
echo '<link rel="stylesheet" type="text/css" href="/all/mobile_menu/sdmenu.css">
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

echo '</head><body onLoad="start()"><div id="pagecontainer">'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
#DATA=`cat | tr -cd 'A-Za-z0-9\._:\-'`
DATA=`cat | tr -cd 'A-Za-z0-9\._:\-%+-' | sed 's/____/QUADRUPLEUNDERSCORE/g' | sed 's/_/REPLACEUNDERSCORE/g' | sed 's/QUADRUPLEUNDERSCORE/_/g'`
#echo $DATA"<br>"

function show_status {
echo '<SCRIPT language="Javascript">
alert("'$MESSAGE'");
window.location = "/cgi-bin/admin/groups.cgi"
</script>
</div></div></form></body></html>'
exit
}

#########################
#Assign data to variables
#########################
END_POINT=27
#Assign GROUPNAME
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = GROUPNAMEcheck ]
then
let COUNTER=$COUNTER+1
GROUPNAME=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign TYPE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = TYPEcheck ]
then
let COUNTER=$COUNTER+1
TYPE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

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

[ -z "$TYPE" ] && TYPE=notset
[ -z "$ACTION" ] && ACTION=view

if [ $ACTION = reallyadd ] && [ $TYPE = primary ]
then
#Assign PROFILE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = PROFILEcheck ]
then
let COUNTER=$COUNTER+1
PROFILE=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign HOMESERVER
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = HOMESERVERcheck ]
then
let COUNTER=$COUNTER+1
HOMESERVER=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign CATEGORY
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = CATEGORYcheck ]
then
let COUNTER=$COUNTER+1
CATEGORY=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done

#Assign SECGROUP
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = SECGROUPcheck ]
then
let COUNTER=$COUNTER+1
SECGROUP=`echo $DATA | cut -s -d'_' -f$COUNTER`
break
fi
let COUNTER=$COUNTER+1
done
fi


if [ $ACTION = editextrargroups ]
then
#Assign EXTRAGROUPS
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = EXTRAGROUPNAMEcheck ]
then
let COUNTER=$COUNTER+1
EXTRAGROUPS=`echo $DATA | cut -s -d'_' -f$COUNTER- | sed 's/_EXTRAGROUPNAME_/,/g'`
break
fi
let COUNTER=$COUNTER+1
done
fi

PROTECTEDLIST="itadmin exams karoshi staff nogroup"

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

#########################
#Check data
#########################

#Check to see that GROUPNAME is not blank
TITLE="$TITLE1"
ACTIONTYPE=add
ACTIONMSG="$NEWGROUPMSG"

if [ "$ACTION" != add ] && [ $ACTION != delete ] && [ $ACTION != view ] && [ $ACTION != reallyadd ] && [ $ACTION != reallydelete ] && [ $ACTION != extragroups ] && [ $ACTION != editextrargroups ]
then
MESSAGE=$ERRORMSG1
show_status
fi

if [ "$ACTION" = reallyadd ] || [ $ACTION = reallydelete ]
then
#Check to see that GROUPNAME is not blank
if [ -z "$GROUPNAME" ]
then
MESSAGE="$ERRORMSG2"
show_status
fi
fi

if [ $ACTION = add ] || [ $ACTION = delete ] || [ "$ACTION" = reallyadd ] || [ $ACTION = reallydelete ] || [ $ACTION = extragroups ] || [ $ACTION = editextrargroups ]
then
if [ -z "$TYPE" ]
then
MESSAGE="$ERRORMSG3"
show_status
fi
fi



#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox3
TABLECLASS=standard
WIDTH1=200
WIDTH2=90
WIDTH3=300
ICON1=/images/submenus/system/delete.png
ICON2=/images/submenus/system/edit.png
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=actionbox2
TABLECLASS=mobilestandard
WIDTH1=120
WIDTH2=70
WIDTH3=200
ICON1=/images/submenus/system/deletem.png
ICON2=/images/submenus/system/editm.png
fi

function do_action {
MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/groups.cgi | cut -d' ' -f1`
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$GROUPNAME:$ACTION:$TYPE:$PROFILE:$HOMESERVER:$CATEGORY:$SECGROUP:$EXTRAGROUPS:" | sudo -H /opt/karoshi/web_controls/exec/groups
}

if [ $ACTION = reallyadd ]
then
#Check that the group does not already exist
getent group $GROUPNAME 1>/dev/null
if [ $? = 0 ]
then
MESSAGE=$ERRORMSG4
show_status
fi

#Check that a user with the same name does not already exist
getent passwd $GROUPNAME 1>/dev/null
if [ $? = 0 ]
then
MESSAGE=$ERRORMSG5
show_status
fi

do_action
ACTION=view
fi

if [ $ACTION = editextrargroups ]
then
do_action
ACTION=view
fi

if [ $ACTION = reallydelete ]
then
do_action
ACTION=view
fi

if [ $ACTION = add ] && [ $TYPE = primary ]
then 
TITLE="$TITLE3"
fi
if [ $ACTION = add ] && [ $TYPE = secondary ]
then 
TITLE="$TITLE2"
fi
[ $ACTION = delete ] && TITLE="$TITLE4"
[ $ACTION = extragroups ] && TITLE="$EXTRAGROUPSMSG"
echo '<form name="myform" action="/cgi-bin/admin/groups.cgi" method="post">'

#Show back button for mobiles
if [ $MOBILE = yes ]
then
echo '<div style="float: center" id="my_menu" class="sdmenu">
	<div class="expanded">
	<span>'$TITLE1'</span>
<a href="/cgi-bin/admin/mobile_menu.cgi">'$USERMENUMSG'</a>
</div></div><div id="mobileactionbox">
'
else
echo '<div id="'$DIV_ID'"><div id="titlebox">
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr>
<td style="vertical-align: top;"><div class="sectiontitle">'$TITLE'</div></td>'

if [ $ACTION = view ] 
then
echo '<td style="vertical-align: top;"><input name="____ACTION____add____TYPE____primary____" type="submit" class="button" value="'$NEWPRIGROUPMSG'"></td>
<td style="vertical-align: top;"><input name="____ACTION____add____TYPE____secondary____" type="submit" class="button" value="'$NEWSECGROUPMSG'"></td>
<td style="vertical-align: top;"><a href="/cgi-bin/admin/label_groups_fm.cgi"><input class="button" type="button" name="" value="'$LABELGROUPSMSG'"></a></td>
<td style="vertical-align: top;"><a href="/cgi-bin/admin/copy_files_upload_fm.cgi"><input class="button" type="button" name="" value="'$COPYFILESMSG'"></a></td>
'
else
echo '<td style="vertical-align: top;"><input name="____ACTION____view____TYPE____notset____" type="submit" class="button" value="'$VIEWGROUPSMSG'"></td>'
fi
echo '<td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG7'<br><br>'$HELPMSG8'<br><br>'$HELPMSG9'</span></a></td></tr></tbody></table></div><div id="infobox">'
fi

#Show form for adding groups
if [ $ACTION = add ] && [ $TYPE = secondary ]
then
echo '<input type="hidden" name="____TYPE____secondary____" value=""><input type="hidden" name="____ACTION____reallyadd____" value=""><table class="standard" style="text-align: left; height: 34px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: '$WIDTH1'px;">
'$NEWSECGROUPMSG'</td>
        <td><input name="____GROUPNAME____" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#New_Secondary_Goup"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1a'<br><br>'$HELPMSG1b'</span></a>
</td>
      </tr>
    </tbody>
  </table>
  <br>
  <br>
  <input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">'
fi

if [ $ACTION = add ] && [ $TYPE = primary ]
then
echo '<input type="hidden" name="____TYPE____primary____" value=""><input type="hidden" name="____ACTION____reallyadd____" value=""><table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: '$WIDTH1'px;">'$PRIGROUPNAMEMSG'</td><td><input name="____GROUPNAME____" style="width: '$WIDTH1'px;" size="20" type="text"></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#New_Primary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2a'<br><br>'$HELPMSG2b'</span></a>

</td></tr>

<tr><td>'$PROFILEMSG'</td><td>'
#Generate list of profiles
echo '<select name="____PROFILE____" style="width: 200px;"><option value=""></option>'
for PROFILES in `ls -1 /home/applications/profiles | grep -v .V2`
do
PROFILE=`basename $PROFILES`
if [ $PROFILE != default_roaming_profile ]
then
echo '<option value="'$PROFILE'">'$PROFILE'</option>'
fi
done
echo '</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#New_Primary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a>
</td></tr>
<tr><td>'$HOMESERVERMSG'</td><td><select name="____HOMESERVER____" style="width: '$WIDTH1'px;">'

#Generate a list of servers for the home folders
FILESERVERCOUNT=0
for KAROSHI_SERVER in /opt/karoshi/server_network/servers/*
do
KAROSHI_SERVER=`basename $KAROSHI_SERVER`
if [ -f /opt/karoshi/server_network/servers/$KAROSHI_SERVER/fileserver ]
then
SERVERARRAY[$FILESERVERCOUNT]=$KAROSHI_SERVER
let FILESERVERCOUNT=$FILESERVERCOUNT+1
fi
done
COUNTER=0
while [ $COUNTER -le $FILESERVERCOUNT ]
do
echo '<option value="'${SERVERARRAY[$COUNTER]}'">'${SERVERARRAY[$COUNTER]}'</option>'
let COUNTER=$COUNTER+1
done
echo '</select></td><td>
<a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#New_Primary_Group"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG4'</span></a></td></tr>'
#Show categories
echo '<tr><td>'$CATEGORYMSG'</td><td><select name="____CATEGORY____" style="width: '$WIDTH1'px;">
<option value=""></option>
<option value="students">'$STUDENTMSG'</option>
<option value="personnel">'$PERSONNELMSG'</option>
<option value="other">'$OTHERMSG'</option>
<option value="trustees">'$TRUSTEESMSG'</option></select>
</td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG5'</span></a></td></tr>
</tbody></table><br><br><input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">'
fi

if [ $ACTION = view ]
then
#Show list of groups
GROUPLIST=( `getent group | cut -d: -f1 | sed 's/ /____/g' | sort` )
GROUPCOUNT=${#GROUPLIST[@]}  
COUNTER=0

echo  '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: '$WIDTH1'px;"><b>'$GROUPNAMEMSG'</b></td>'


[ $MOBILE = no ] && echo '<td style="width: '$WIDTH2'px;"><b>'$GROUPIDMSG'</b></td><td style="width: '$WIDTH2'px;"><b>'$MEMBERCOUNTMSG'</b></td>'

echo '<td style="width: '$WIDTH2'px;"><b>'$TYPEMSG'</b></td><td style="width: '$WIDTH3'px;"><b>'$EXTRAGROUPSMSG'</b></td><td><b>'$EDITMSG'</b></td><td><b>'$DELETEMSG'</b></td></tr>'

while [ $COUNTER -lt $GROUPCOUNT ]
do
GROUPNAME=`echo ${GROUPLIST[$COUNTER]} | sed 's/____/ /g'`
GROUPID=`getent group "$GROUPNAME" | cut -d: -f3`
MEMBERCOUNT=`getent group $GROUPNAME | cut -d: -f4- | sed '/^$/d' | sed 's/,/\n/g' | wc -l`
if [ $GROUPID -ge 1000 ] && [ $GROUPNAME != nogroup ]
then
echo '<tr><td>'$GROUPNAME'</td><td>'
[ $MOBILE = no ] && echo ''$GROUPID'</td><td>'$MEMBERCOUNT'</td><td>'
GROUPTYPE="$TYPE2MSG"
TYPE=secondary
if [ -f /opt/karoshi/server_network/group_information/"$GROUPNAME" ]
then
GROUPTYPE="$TYPE1MSG"
TYPE=primary
fi
echo ''$GROUPTYPE'</td><td>'

if [ $TYPE = primary ]
then
source /opt/karoshi/server_network/group_information/"$GROUPNAME"
echo ''$SECONDARYGROUP'</td><td><a class="info" href="javascript:void(0)"><input name="____ACTION____extragroups____GROUPNAME____'$GROUPNAME'____TYPE____'$TYPE'____" type="image" class="images" src="'$ICON2'" value=""><span>'$EXTRAGROUPSMSG' '$GROUPNAME'</span></a>'
else
echo '</td><td>'
fi

echo '</td><td>'

PROTECTED=no
[ `echo $PROTECTEDLIST | grep -c $GROUPNAME` -gt 0 ] && PROTECTED=yes
if [ $MEMBERCOUNT = 0 ] || [ $TYPE = secondary ] && [ $PROTECTED = no ]
then
echo '<a class="info" href="javascript:void(0)"><input name="____ACTION____delete____GROUPNAME____'$GROUPNAME'____TYPE____'$TYPE'____" type="image" class="images" src="'$ICON1'" value=""><span>'$DELETEMSG' '$GROUPNAME'</span></a>'
fi
echo '</td></tr>'
fi
let COUNTER=$COUNTER+1
done
echo '</tbody></table>'
fi

if [ $ACTION = delete ]
then
echo '<input type="hidden" name="____TYPE____'$TYPE'____" value=""><input type="hidden" name="____GROUPNAME____'$GROUPNAME'____" value=""><input type="hidden" name="____ACTION____reallydelete____" value="">
<b>'$GROUPNAMEMSG: $GROUPNAME'</b><br><br>'$CONFIRMDELETEMSG'<br><br><input value="'$SUBMITMSG'" class="button" type="submit">'
fi

if [ $ACTION = extragroups ]
then
#Get a list of groups already asociated with this group
source /opt/karoshi/server_network/group_information/"$GROUPNAME"

echo '<input type="hidden" name="____TYPE____'$TYPE'____" value=""><input type="hidden" name="____GROUPNAME____'$GROUPNAME'____" value=""><input type="hidden" name="____ACTION____editextrargroups____" value="">'

#Show list of groups
GROUPLIST=( `getent group | cut -d: -f1 | sed 's/ /____/g' | sort` )
GROUPCOUNT=${#GROUPLIST[@]}  
COUNTER=0

echo  '<table class="'$TABLECLASS'" style="text-align: left;" border="0" cellpadding="2" cellspacing="2">
<tbody><tr><td style="width: '$WIDTH1'px;"><b>'$GROUPNAMEMSG'</b></td><td><b>Select</b></td><td><a class="info" target="_blank" href="http://www.linuxschools.com/karoshi/documentation/wiki/index.php?title=Group_Management#Extra_Groups"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG10'</span></a></td></tr>'

while [ $COUNTER -lt $GROUPCOUNT ]
do
GROUPNAMECHOICE=`echo ${GROUPLIST[$COUNTER]} | sed 's/____/ /g'`
GROUPID=`getent group "$GROUPNAMECHOICE" | cut -d: -f3`
if [ $GROUPID -ge 1000 ] && [ $GROUPNAMECHOICE != $GROUPNAME ] && [ $GROUPNAME != nogroup ]
then
echo '<tr><td>'$GROUPNAMECHOICE'</td><td>'
CHECKED=""
[ `echo $SECONDARYGROUP | grep -c -w $GROUPNAMECHOICE` -gt 0 ] && CHECKED=checked
echo '<input type="checkbox" name="____EXTRAGROUPNAME____" value="'$GROUPNAMECHOICE'" '$CHECKED'>'
echo '</td></tr>'
fi
let COUNTER=$COUNTER+1
done

echo '</tbody></table><br><br><input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">'

fi

[ $MOBILE = no ] && echo '</div>'
echo '</div></form></div></body></html>'
exit

