#!/bin/bash
#Copyright (C) 2011  Paul Sharrad
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
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>KSSO</title>
<link rel="stylesheet" href="/ksso/smbwc.css">
<meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
<link rel="icon" type="image/png" href="/ksso/images/logo.png">
</head>
<body>'


#Create session id


function passgen {
PASSCHOICE=( A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y x 1 2 3 4 5 6 7 8 9 0 )

RANGE=`echo ${#PASSCHOICE[@]}`
let RANGE=$RANGE-1 

COUNTER=1
while [ $COUNTER -le 18 ]
do
ARRAYCHOICE=$RANDOM
let "ARRAYCHOICE %= $RANGE"
PASSWORD[$COUNTER]=`echo ${PASSCHOICE[$ARRAYCHOICE]} `
let COUNTER=COUNTER+1
done
}
passgen
SESSIONID=`echo ${PASSWORD[@]:0} | sed 's/ //g'`
passgen
SESSIONNAME=`echo ${PASSWORD[@]:0} | sed 's/ //g'`

echo '
<div id="page">
  <div id="headerbox">
    <div id="headertextbox"></div>
</div>
<div id="logonbox">
<form action="ksso.cgi" method="post">
<input type="hidden" name="_SESSIONNAME_" value="'$SESSIONNAME'">
<input type="hidden" name="_SESSIONID_" value="'$SESSIONID'">


    <div id="logonboxusr">
     	<input tabindex= "1" style="width: 150px;" name="_USERNAME_"  size="20" type="text">
    </div>
    <div id="logonboxpwd">
    	<input tabindex= "2" style="width: 150px;" name="_PASSWORD_" size="20" type="password">
    </div>
    <div id="logonboxbtn">
      <input name="_Submit_" type="submit" class="btnSubmit" id="btnSubmit" value="LOGON" />
    </div>

  </form></div>
</div>
</body>
</html>'
exit
