@echo off

if not exist c:\"Program Files"\kix\kix32.exe goto kixinstall

:normal
start c:\"Program Files"\kix\wkix32 %logonserver%\netlogon\logonform.kix $pgroup=%1
exit

:kixinstall
cls
echo Attempting to install Kixtart
echo Kixtart is needed to map drives and set permissions.
echo Kixtart is careware. Please donate to your chosen charity.

MD C:\kix
if not exist C:\kix goto kixerror1
rem remove previous files
attrib -R -S c:\kix\*.*
del c:\kix\*.* /Q

rem copy new files
COPY %LOGONSERVER%\netlogon\kix\kixinstall.bat C:\kix
COPY %LOGONSERVER%\netlogon\kix\kixinstall.lnk C:\kix
COPY %LOGONSERVER%\netlogon\kix\getdll.bat C:\kix
attrib +R +S c:\kix\*.*

START "C:\kix\kixinstall.lnk" "C:\kix\kixinstall.lnk"
C:\kix\getdll.bat
exit

:kixerror1
echo Error creating C:\kix
echo You do not have enough permissions to install Kixtart.
echo Please contact your network administrator.
echo Please logout and back in once you have done this.
pause
exit

