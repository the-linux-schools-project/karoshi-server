@echo off

if not exist c:\kix\kix32.exe goto kixerror

if not exist c:\kix\kixforms.upg goto kixformsupgrade

:normal
start c:\kix\wkix32 %LOGONSERVER%\netlogon\logonform.kix $pgroup=%1
exit

:kixerror
cls
echo Attempting to install Kixtart
echo Kixtart is needed to map drives and set permissions.
echo Kixtart is careware. Please donate to your chosen charity.
%LOGONSERVER%\netlogon\kixtart_install.bat
exit

:kixformsupgrade
%LOGONSERVER%\netlogon\kixforms_upgrade.bat
exit
