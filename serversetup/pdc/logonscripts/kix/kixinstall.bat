@echo off

MD C:\"Program Files"\kix
if not exist C:\"Program Files"\kix goto kixerror1
rem remove previous files
attrib -R -S C:\"Program Files"\kix\*.*
del C:\"Program Files"\kix\*.* /Q
goto install

:kixerror1
echo Error creating C:\"Program Files"\kix
echo You do not have enough permissions to install Kixtart.
echo Please contact your network administrator.
echo Please logout and back in once you have done this.
pause
exit

rem copy new files
:install
COPY \\CHANGETHISSERVER\netlogon\kix\*.* C:\"Program Files"\kix
attrib +R +S c:\kix\*.*
attrib -R -S c:\kix\*.*
rem register kixforms.dll
regsvr32 "C:\Program Files\kix\kixforms.dll"
rem run WSsetup
C:\"Program Files"\kix\WKIX32.EXE \\CHANGETHISSERVER\netlogon\kix\WSsetup.kix


