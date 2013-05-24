C:
CD \
REM Try to change security attributes
attrib -R -S c:\kix\kixforms.dll
move c:\kix\kixforms.dll c:\

REM if not successful then exit
rem echo error code is: %errorlevel%
IF ERRORLEVEL 1 GOTO permerror

echo Copying new files
REM Copy new dll file
COPY /Y \\CHANGETHISHOSTNAME\netlogon\kix\kixforms.dll C:\kix

REM Copy new graphic files
COPY /Y \\CHANGETHISHOSTNAME\netlogon\kix\bgnd.bmp C:\kix
COPY /Y \\CHANGETHISHOSTNAME\netlogon\kix\logov513.bmp C:\kix
COPY /Y \\CHANGETHISHOSTNAME\netlogon\kix\tick.bmp C:\kix

REM Copy successful upgrade marker file
COPY /Y \\CHANGETHISHOSTNAME\netlogon\kix\kixforms.upg C:\kix

REM Reapply security attributes
attrib +R +S c:\kix\kixforms.dll

echo Registering new kixfroms dll File
regsvr32 /s "C:\kix\kixforms.dll"

\\CHANGETHISHOSTNAME\netlogon\logon.bat
exit
:permerror
echo You do not have enough permissions to upgrade Kixforms.
echo Please contact your network administrator.
\\CHANGETHISHOSTNAME\netlogon\logonoldgui.bat
exit

