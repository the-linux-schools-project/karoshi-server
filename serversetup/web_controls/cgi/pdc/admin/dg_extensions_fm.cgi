#!/bin/bash
#Copyright (C) 2011  Paul Sharrad

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
#Website: http://www.karoshi.org.uk
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
TIMEOUT=300
NOTIMEOUT=127.0.0.1
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_extensions ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/internet/dg_extensions
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
  <link rel="stylesheet" href="/css/'$STYLESHEET'?d='`date +%F`'">

  
  <script type="text/javascript">
<!--
function SetAllCheckBoxes(FormName, FieldName, CheckValue)
{
	if(!document.forms[FormName])
		return;
	var objCheckBoxes = document.forms[FormName].elements[FieldName];
	if(!objCheckBoxes)
		return;
	var countCheckBoxes = objCheckBoxes.length;
	if(!countCheckBoxes)
		objCheckBoxes.checked = CheckValue;
	else
		// set the check value for all check boxes
		for(var i = 0; i < countCheckBoxes; i++)
			objCheckBoxes[i].checked = CheckValue;
}
// -->
  </script>
<script src="/all/stuHover.js" type="text/javascript"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <!--480-->
</head>
<body onLoad="start()"><div id="pagecontainer">'

#Detect mobile browser
MOBILE=no
source /opt/karoshi/web_controls/detect_mobile_browser

#Generate navigation bar
if [ $MOBILE = no ]
then
DIV_ID=actionbox
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin
else
DIV_ID=menubox
fi

echo '<form action="/cgi-bin/admin/dg_extensions.cgi" name="selectedsites" method="post"><b></b><div id="'$DIV_ID'">'

#Show back button for mobiles
if [ $MOBILE = allow ]
then
echo '<table class="standard" style="text-align: left;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top;"><a href="/cgi-bin/admin/mobile_menu.cgi"><img border="0" src="/images/submenus/mobile/back.png" alt="'$BACKMSG'"></a></td>
<td style="vertical-align: middle;"><a href="/cgi-bin/admin/dg_extensions.cgi"><b>'$TITLE'</b></a></td><td><a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td></tr></tbody></table><br>'
else
echo '<b>'$TITLE'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a>
<br><br>'
fi

echo '<input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset"><br><br>'

echo '<table class="standard" style="text-align:" border="0" cellpadding="2" cellspacing="2">
    <tbody><tr><td><b>'$EXTENSIONMSG'</b></td><td><b>'$DESCRIPTIONMSG'</b></td><td><b>'$STUDENTSTITLE'</b></td><td><b>'$STAFFTITLE'</b></td></tr>'

source /opt/karoshi/server_network/dansguardian/allowed_file_extensions

# Microsoft Access project extension
STATUS1=""
STATUS2=""

[ $STUDENT_ADE = allow ] && STATUS1='checked="checked"'
[ $STAFF_ADE = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.ade</td><td>Microsoft Access project extension</td>
<td><input name="students_ade_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_ade_" value="" '$STATUS2' type="checkbox"></td></tr>'
# Microsoft Access project
STATUS1=""
STATUS2=""
[ $STUDENT_ADP = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_ADP = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.adp</td><td>Microsoft Access project</td>
<td><input name="students_adp_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_adp_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows Media Audio / Video
STATUS1=""
STATUS2=""
[ $STUDENT_ASX = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_ASX = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.asx</td><td>Windows Media Audio / Video</td>
<td><input name="students_asx_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_asx_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Visual Basic class module
STATUS1=""
STATUS2=""
[ $STUDENT_BAS = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_BAS = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.bas</td><td>Microsoft Visual Basic class module</td>
<td><input name="students_bas_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_bas_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Batch file
STATUS1=""
STATUS2=""
[ $STUDENT_BAT = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_BAT = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.bat</td><td>Batch file</td>
<td><input name="students_bat_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_bat_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows setup file
STATUS1=""
STATUS2=""
[ $STUDENT_CAB = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_CAB = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.cab</td><td>Windows setup file</td>
<td><input name="students_cab_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_cab_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Compiled HTML Help file
STATUS1=""
STATUS2=""
[ $STUDENT_CHM = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_CHM = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.chm</td><td>Compiled HTML Help file</td>
<td><input name="students_chm_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_chm_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Windows NT Command script
STATUS1=""
STATUS2=""
[ $STUDENT_CMD = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_CMD = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.cmd</td><td>Microsoft Windows NT Command script</td>
<td><input name="students_cmd_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_cmd_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft MS-DOS program
STATUS1=""
STATUS2=""
[ $STUDENT_COM = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_COM = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.com</td><td>Microsoft MS-DOS program</td>
<td><input name="students_com_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_com_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Control Panel extension
STATUS1=""
STATUS2=""
[ $STUDENT_CPL = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_CPL = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.cpl</td><td>Control Panel extension</td>
<td><input name="students_cpl_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_cpl_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Security certificate 
STATUS1=""
STATUS2=""
[ $STUDENT_CRT = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_CRT = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.crt</td><td>Security certificate </td>
<td><input name="students_crt_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_crt_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows system file
STATUS1=""
STATUS2=""
[ $STUDENT_DLL = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_DLL = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.dll</td><td>Windows system file</td>
<td><input name="students_dll_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_dll_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Program
STATUS1=""
STATUS2=""
[ $STUDENT_EXE = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_EXE = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.exe</td><td>Program</td>
<td><input name="students_exe_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_exe_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Help file
STATUS1=""
STATUS2=""
[ $STUDENT_HLP = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_HLP = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.hlp</td><td>Help file</td>
<td><input name="students_hlp_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_hlp_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows system file
SSTATUS1=""
STATUS2=""
[ $STUDENT_INI = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_INI = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.ini</td><td>Windows system file</td>
<td><input name="students_ini_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_ini_" value="" '$STATUS2' type="checkbox"></td></tr>'

# HTML program
STATUS1=""
STATUS2=""
[ $STUDENT_HTA = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_HTA = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.hta</td><td>HTML program</td>
<td><input name="students_hta_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_hta_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Setup Information
STATUS1=""
STATUS2=""
[ $STUDENT_INF = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_INF = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.hta</td><td>Setup Information</td>
<td><input name="students_inf_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_inf_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Internet Naming Service
STATUS1=""
STATUS2=""
[ $STUDENT_INS = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_INS = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.ins</td><td>Internet Naming Service</td>
<td><input name="students_ins_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_ins_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Internet Communication settings
STATUS1=""
STATUS2=""
[ $STUDENT_ISP = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_ISP = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.ins</td><td>Internet Communication settings</td>
<td><input name="students_isp_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_isp_" value="" '$STATUS2' type="checkbox"></td></tr>'

# JScript file - often needed in web pages
STATUS1=""
STATUS2=""
[ $STUDENT_JS = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_JS = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.js</td><td>JScript file - often needed in web pages</td>
<td><input name="students_js_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_js_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Jscript Encoded Script file - often needed in web pages
STATUS1=""
STATUS2=""
[ $STUDENT_JSE = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_JSE = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.jse</td><td>Jscript Encoded Script file - often needed in web pages</td>
<td><input name="students_jse_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_jse_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Jscript Encoded Script file - often needed in web pages
STATUS1=""
STATUS2=""
[ $STUDENT_JSE = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_JSE = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.jse</td><td>Jscript Encoded Script file - often needed in web pages</td>
<td><input name="students_jse_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_jse_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows Shortcut
STATUS1=""
STATUS2=""
[ $STUDENT_LNK = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_LNK = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.lnk</td><td>Windows Shortcut</td>
<td><input name="students_lnk_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_lnk_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Access add-in program
STATUS1=""
STATUS2=""
[ $STUDENT_LNK = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_LNK = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mda</td><td>Microsoft Access add-in program</td>
<td><input name="students_mda_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mda_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Access program
STATUS1=""
STATUS2=""
[ $STUDENT_MDB = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MDB = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mdb</td><td>Microsoft Access program</td>
<td><input name="students_mdb_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mdb_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Access MDE database
STATUS1=""
STATUS2=""
[ $STUDENT_MDE = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MDE = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mde</td><td>Microsoft Access MDE database</td>
<td><input name="students_mde_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mde_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Access workgroup information 
STATUS1=""
STATUS2=""
[ $STUDENT_MDT = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MDT = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mdt</td><td>Microsoft Access workgroup information</td>
<td><input name="students_mdt_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mdt_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Access workgroup information 
STATUS1=""
STATUS2=""
[ $STUDENT_MDW = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MDW = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mdw</td><td>Microsoft Access workgroup information</td>
<td><input name="students_mdw_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mdw_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Access wizard program 
STATUS1=""
STATUS2=""
[ $STUDENT_MDZ = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MDZ = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mdz</td><td>Microsoft Access wizard program </td>
<td><input name="students_mdz_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mdz_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Access wizard program 
STATUS1=""
STATUS2=""
[ $STUDENT_MSC = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MSC = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.msc</td><td>Microsoft Access wizard program </td>
<td><input name="students_msc_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_msc_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Windows Installer package
STATUS1=""
STATUS2=""
[ $STUDENT_MSI = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MSI = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.msi</td><td>Microsoft Windows Installer package</td>
<td><input name="students_msi_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_msi_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Windows Installer patch
STATUS1=""
STATUS2=""
[ $STUDENT_MSP = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MSP = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.msp</td><td>Microsoft Windows Installer patch</td>
<td><input name="students_msp_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_msp_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Visual Test source files
STATUS1=""
STATUS2=""
[ $STUDENT_MST = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MST = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mst</td><td>Microsoft Visual Test source files</td>
<td><input name="students_mst_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mst_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Photo CD image, Microsoft Visual compiled script
STATUS1=""
STATUS2=""
[ $STUDENT_PCD = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_PCD = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.pcd</td><td>Photo CD image, Microsoft Visual compiled script</td>
<td><input name="students_pcd_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_pcd_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Shortcut to MS-DOS program
STATUS1=""
STATUS2=""
[ $STUDENT_PIF = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_PIF = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.pif</td><td>Shortcut to MS-DOS program</td>
<td><input name="students_pif_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_pif_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Microsoft Outlook profile settings
STATUS1=""
STATUS2=""
[ $STUDENT_PRF = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_PRF = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.prf</td><td>Microsoft Outlook profile settings</td>
<td><input name="students_prf_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_prf_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows registry entries
STATUS1=""
STATUS2=""
[ $STUDENT_REG = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_REG = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.reg</td><td>Microsoft Outlook profile settings</td>
<td><input name="students_reg_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_reg_" value="" '$STATUS2' type="checkbox"></td></tr>'

 # Windows Explorer command
STATUS1=""
STATUS2=""
[ $STUDENT_SCF = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SCF = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.scf</td><td>Windows Explorer command</td>
<td><input name="students_scf_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_scf_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Screen saver
STATUS1=""
STATUS2=""
[ $STUDENT_SCR = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SCR = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.scr</td><td>Screen saver</td>
<td><input name="students_scr_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_scr_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows Script Component
STATUS1=""
STATUS2=""
[ $STUDENT_SCT = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SCT = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.sct</td><td>Windows Script Component</td>
<td><input name="students_sct_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_sct_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Shell script
STATUS1=""
STATUS2=""
[ $STUDENT_SH = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SH = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.sh</td><td>Shell script</td>
<td><input name="students_sh_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_sh_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Shell Scrap object
STATUS1=""
STATUS2=""
[ $STUDENT_SHS = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SHS = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.shs</td><td>Shell Scrap object</td>
<td><input name="students_shs_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_shs_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Shell Scrap object
STATUS1=""
STATUS2=""
[ $STUDENT_SHB = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SHB = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.shb</td><td>Shell Scrap object</td>
<td><input name="students_shb_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_shb_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows system file
STATUS1=""
STATUS2=""
[ $STUDENT_SYS = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SYS = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.sys</td><td>Windows system file</td>
<td><input name="students_sys_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_sys_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Internet shortcut
STATUS1=""
STATUS2=""
[ $STUDENT_URL = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_URL = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.url</td><td>Internet shortcut</td>
<td><input name="students_url_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_url_" value="" '$STATUS2' type="checkbox"></td></tr>'

# VBScript file
STATUS1=""
STATUS2=""
[ $STUDENT_VB = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_VB = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.vb</td><td>VBScript file</td>
<td><input name="students_vb_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_vb_" value="" '$STATUS2' type="checkbox"></td></tr>'

 # VBScript Encoded script file
STATUS1=""
STATUS2=""
[ $STUDENT_VBE = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_VBE = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.vbe</td><td>VBScript Encoded script file</td>
<td><input name="students_vbe_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_vbe_" value="" '$STATUS2' type="checkbox"></td></tr>'

# VBScript file
STATUS1=""
STATUS2=""
[ $STUDENT_VBS = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_VBS = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.vbs</td><td>VBScript file</td>
<td><input name="students_vbs_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_vbs_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows system file
STATUS1=""
STATUS2=""
[ $STUDENT_VXD = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_VXD = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.vxd</td><td>Windows system file</td>
<td><input name="students_vxd_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_vxd_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows Script Component
STATUS1=""
STATUS2=""
[ $STUDENT_WSC = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_WSC = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.wsc</td><td>Windows Script Component</td>
<td><input name="students_wsc_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_wsc_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows Script file
STATUS1=""
STATUS2=""
[ $STUDENT_WSF = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_WSF = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.wsf</td><td>Windows Script Component</td>
<td><input name="students_wsf_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_wsf_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows Script Host Settings file
STATUS1=""
STATUS2=""
[ $STUDENT_WSH = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_WSH = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.wsh</td><td>Windows Script Host Settings file</td>
<td><input name="students_wsh_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_wsh_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows Script Host Settings file
STATUS1=""
STATUS2=""
[ $STUDENT_WSH = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_WSH = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.wsh</td><td>Windows Script Host Settings file</td>
<td><input name="students_wsh_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_wsh_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Font file - can be used to instant reboot 2k and xp
STATUS1=""
STATUS2=""
[ $STUDENT_OTF = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_OTF = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.otf</td><td>Font file - can be used to instant reboot 2k and xp</td>
<td><input name="students_otf_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_otf_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Office XP settings 
STATUS1=""
STATUS2=""
[ $STUDENT_OPS = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_OPS = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.ops</td><td>Office XP settings</td>
<td><input name="students_ops_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_ops_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Word document 
STATUS1=""
STATUS2=""
[ $STUDENT_DOC = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_DOC = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.doc</td><td>Word document</td>
<td><input name="students_doc_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_doc_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Excel document
STATUS1=""
STATUS2=""
[ $STUDENT_XLS = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_XLS = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.xls</td><td>Excel document</td>
<td><input name="students_xls_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_xls_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Gziped file
STATUS1=""
STATUS2=""
[ $STUDENT_GZ = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_GZ = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.gz</td><td>Gziped file</td>
<td><input name="students_gz_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_gz_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Tape ARchive file
STATUS1=""
STATUS2=""
[ $STUDENT_TAR = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_TAR = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.tar</td><td>Tape ARchive file</td>
<td><input name="students_tar_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_tar_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Windows compressed file
STATUS1=""
STATUS2=""
[ $STUDENT_ZIP = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_ZIP = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.zip</td><td>Windows compressed file</td>
<td><input name="students_zip_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_zip_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Unix compressed file
STATUS1=""
STATUS2=""
[ $STUDENT_TGZ = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_TGZ = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.tgz</td><td>Unix compressed file</td>
<td><input name="students_tgz_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_tgz_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Unix compressed file
STATUS1=""
STATUS2=""
[ $STUDENT_BZ2 = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_BZ2 = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.bz2</td><td>Unix compressed file</td>
<td><input name="students_bz2_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_bz2_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Mac disk image
STATUS1=""
STATUS2=""
[ $STUDENT_CDR = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_CDR = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.cdr</td><td>Mac disk image</td>
<td><input name="students_cdr_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_cdr_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Mac disk image
STATUS1=""
STATUS2=""
[ $STUDENT_DMG = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_DMG = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.dmg</td><td>Mac disk image</td>
<td><input name="students_dmg_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_dmg_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Mac self mounting disk image
STATUS1=""
STATUS2=""
[ $STUDENT_SMI = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SMI = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.smi</td><td>Mac self mounting disk image</td>
<td><input name="students_smi_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_smi_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Mac compressed file
STATUS1=""
STATUS2=""
[ $STUDENT_SIT = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SIT = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.sit</td><td>Mac compressed file</td>
<td><input name="students_sit_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_sit_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Mac compressed file, self extracting
STATUS1=""
STATUS2=""
[ $STUDENT_SEA = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_SEA = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.sea</td><td>Mac compressed file, self extracting</td>
<td><input name="students_sea_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_sea_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Mac binary compressed file
STATUS1=""
STATUS2=""
[ $STUDENT_BIN = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_BIN = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.bin</td><td>Mac binary compressed file</td>
<td><input name="students_bin_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_bin_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Mac binhex encoded file
STATUS1=""
STATUS2=""
[ $STUDENT_HQX = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_HQX = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.hqx</td><td>Mac binhex encoded file</td>
<td><input name="students_hqx_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_hqx_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Rar Similar to zip
STATUS1=""
STATUS2=""
[ $STUDENT_RAR = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_RAR = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.rar</td><td>Rar Similar to zip</td>
<td><input name="students_rar_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_rar_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Music file
STATUS1=""
STATUS2=""
[ $STUDENT_MP3 = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MP3 = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mp3</td><td>Music file</td>
<td><input name="students_mp3_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mp3_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Movie file
STATUS1=""
STATUS2=""
[ $STUDENT_MPEG = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MPEG = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mpeg</td><td>Movie file</td>
<td><input name="students_mpeg_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mpeg_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Movie file
STATUS1=""
STATUS2=""
[ $STUDENT_MPG = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_MPG = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.mpg</td><td>Movie file</td>
<td><input name="students_mpg_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_mpg_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Movie file
STATUS1=""
STATUS2=""
[ $STUDENT_AVI = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_AVI = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.avi</td><td>Movie file</td>
<td><input name="students_avi_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_avi_" value="" '$STATUS2' type="checkbox"></td></tr>'

 # this can also exploit a security hole allowing virus infection
STATUS1=""
STATUS2=""
[ $STUDENT_ASF = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_ASF = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.asf</td><td>this can also exploit a security hole allowing virus infection</td>
<td><input name="students_asf_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_asf_" value="" '$STATUS2' type="checkbox"></td></tr>'

# CD ISO image
STATUS1=""
STATUS2=""
[ $STUDENT_ISO = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_ISO = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.iso</td><td>CD ISO image</td>
<td><input name="students_iso_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_iso_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Music file
STATUS1=""
STATUS2=""
[ $STUDENT_OGG = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_OGG = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.ogg</td><td>Music file</td>
<td><input name="students_ogg_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_ogg_" value="" '$STATUS2' type="checkbox"></td></tr>'

# Music file
STATUS1=""
STATUS2=""
[ $STUDENT_WMF = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_WMF = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.wmf</td><td>Music file</td>
<td><input name="students_wmf_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_wmf_" value="" '$STATUS2' type="checkbox"></td></tr>'

# CD ISO image
STATUS1=""
STATUS2=""
[ $STUDENT_CUE = allow ] &&  STATUS1='checked="checked"'
[ $STAFF_CUE = allow ] && STATUS2='checked="checked"'

echo '<tr><td>.cue</td><td>CD ISO image</td>
<td><input name="students_cue_" value="" '$STATUS1' type="checkbox"></td>
<td><input name="staff_cue_" value="" '$STATUS2' type="checkbox"></td></tr>'

echo '</tbody></table>'



echo '<br><input value="'$SUBMITMSG'" class="button" type="submit"> <input value="'$RESETMSG'" class="button" type="reset">
  </div></form></div></body></html>'
exit
