rem test permissions.
C:
CD \
MD C:\"Program Files"\kixtest

if not exist C:\"Program Files"\kixtest goto permerror
rmdir C:\"Program Files"\kixtest

rem permissions good, proceeding.
MD C:\kix
if not exist C:\kix goto permerror2

rem remove previous files
attrib -R -S c:\kix\*.*
del c:\kix\*.* /Q

rem copy new files
COPY %LOGONSERVER%\netlogon\kix\*.* C:\kix
attrib +R +S c:\kix\*.*

rem Install
regsvr32 "C:\kix\kixforms.dll"
C:\kix\WKIX32.EXE %LOGONSERVER%\netlogon\kix\WSsetup.kix
%LOGONSERVER%\netlogon\getdll.bat
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
