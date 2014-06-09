@echo off

if not exist c:\kix\kix32.exe goto kixerror

:normal
start c:\kix\kix32 %LOGONSERVER%\netlogon\logonform.kix $pgroup=%1
exit

:kixerror
cls
echo Attempting to install Kixtart
echo Kixtart is needed to map drives and set permissions.
echo Kixtart is careware. Please donate to your chosen charity.
%LOGONSERVER%\netlogon\kixtart_install.bat
exit

