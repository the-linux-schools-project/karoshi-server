C:
CD \
MD C:\kix
if not exist C:\kix goto createerror1
COPY %LOGONSERVER%\netlogon\kix\*.* C:\kix

attrib +R +S c:\kix\*.*
rem Install
regsvr32 "C:\kix\kixforms.dll"
C:\kix\WKIX32.EXE %LOGONSERVER%\netlogon\kix\WSsetup.kix
%LOGONSERVER%\netlogon\getdll.bat
exit
:createerror1
echo Error creating C:\kix
echo Please create the kix folder manually or change your permissions.
echo Please logout and back in once you have done this.
pause
exit
