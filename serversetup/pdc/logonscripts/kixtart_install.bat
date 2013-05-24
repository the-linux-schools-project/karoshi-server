C:
CD \
MD C:\"Program Files"\kixtest
if not exist C:\"Program Files"\kixtest goto permerror
rmdir C:\"Program Files"\kixtest
MD C:\kix
if not exist C:\kix goto permerror2
COPY \\CHANGETHISHOSTNAME\netlogon\kix\*.* C:\kix

attrib +R +S c:\kix\*.*
rem Install
regsvr32 "C:\kix\kixforms.dll"
C:\kix\WKIX32.EXE \\CHANGETHISHOSTNAME\netlogon\kix\WSsetup.kix
\\CHANGETHISHOSTNAME\netlogon\getdll.bat
exit
:permerror
echo You do not have enough permissions to install Kixtart.
echo Please contact your network administrator.
logoff
exit
:permerror2
echo Error creating C:\kix
echo Please create the kix folder manually or change your permissions.
echo Please logout and back in once you have done this.
pause
exit
