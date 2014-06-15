echo off

If not exist %LOGONSERVER%\applications\cups_print\pscript5.dll (
if exist C:\windows\"Driver Cache"\i386\driver.cab (
cd C:\windows\"Driver Cache"\i386\
expand driver.cab %LOGONSERVER%\applications\cups_print -F:pscript.hlp
)

rem Windows 2000 drivers
if exist C:\winnt\"Driver Cache"\i386\sp4.cab (
date /T > %LOGONSERVER%\applications\cups_print\dll_version.txt
echo DLLs obtained from: >> %LOGONSERVER%\applications\cups_print\dll_version.txt
echo Windows 2000 Service pack 4 >> %LOGONSERVER%\applications\cups_print\dll_version.txt
cd C:\winnt\"Driver Cache"\i386\
expand sp4.cab %LOGONSERVER%\applications\cups_print -F:pscript.hlp
expand sp4.cab %LOGONSERVER%\applications\cups_print -F:pscript5.dll
expand sp4.cab %LOGONSERVER%\applications\cups_print -F:pscript.ntf
expand sp4.cab %LOGONSERVER%\applications\cups_print -F:ps5ui.dll
)

rem Windows XP SP1 drivers
if exist C:\windows\"Driver Cache"\i386\sp1.cab (
date /T > %LOGONSERVER%\applications\cups_print\dll_version.txt
echo DLLs obtained from: >> %LOGONSERVER%\applications\cups_print\dll_version.txt
echo Windows XP Service Pack 1 >> %LOGONSERVER%\applications\cups_print\dll_version.txt
cd C:\windows\"Driver Cache"\i386\
expand sp1.cab %LOGONSERVER%\applications\cups_print -F:pscript5.dll
expand sp1.cab %LOGONSERVER%\applications\cups_print -F:pscript.ntf
expand sp1.cab %LOGONSERVER%\applications\cups_print -F:ps5ui.dll
)

rem Windows XP SP2 drivers
if exist C:\windows\"Driver Cache"\i386\sp2.cab (
date /T > %LOGONSERVER%\applications\cups_print\dll_version.txt
echo DLLs obtained from: >> %LOGONSERVER%\applications\cups_print\dll_version.txt
echo Windows XP Service Pack 2 >> %LOGONSERVER%\applications\cups_print\dll_version.txt
cd C:\windows\"Driver Cache"\i386\
expand sp2.cab %LOGONSERVER%\applications\cups_print -F:pscript5.dll
expand sp2.cab %LOGONSERVER%\applications\cups_print -F:pscript.ntf
expand sp2.cab %LOGONSERVER%\applications\cups_print -F:ps5ui.dll
)

rem Windows XP SP3 drivers
if exist C:\windows\"Driver Cache"\i386\sp3.cab (
date /T > %LOGONSERVER%\applications\cups_print\dll_version.txt
echo DLLs obtained from: >> %LOGONSERVER%\applications\cups_print\dll_version.txt
echo Windows XP Service Pack 3 >> %LOGONSERVER%\applications\cups_print\dll_version.txt
cd C:\windows\"Driver Cache"\i386\
expand sp3.cab %LOGONSERVER%\applications\cups_print -F:pscript5.dll
expand sp3.cab %LOGONSERVER%\applications\cups_print -F:pscript.ntf
expand sp3.cab %LOGONSERVER%\applications\cups_print -F:ps5ui.dll
)

rem Windows 7 32bit drivers
if exist C:\Windows\System32\spool\drivers\W32x86\PCC\ntprint.inf*.cab (
date /T > %LOGONSERVER%\applications\cups_print\dll_version.txt
echo DLLs obtained from: >> %LOGONSERVER%\applications\cups_print\dll_version.txt
echo Windows 7 System >> %LOGONSERVER%\applications\cups_print\dll_version.txt
C:\Windows\System32\expand.exe -I C:\Windows\System32\spool\drivers\W32x86\PCC\ntprint.inf*.cab %LOGONSERVER%\applications\cups_print -F:ps5ui.dll
C:\Windows\System32\expand.exe -I C:\Windows\System32\spool\drivers\W32x86\PCC\ntprint.inf*.cab %LOGONSERVER%\applications\cups_print -F:pscript.hlp
C:\Windows\System32\expand.exe -I C:\Windows\System32\spool\drivers\W32x86\PCC\ntprint.inf*.cab %LOGONSERVER%\applications\cups_print -F:pscript.ntf
C:\Windows\System32\expand.exe -I C:\Windows\System32\spool\drivers\W32x86\PCC\ntprint.inf*.cab %LOGONSERVER%\applications\cups_print -F:pscript5.dll
)
)


If not exist %LOGONSERVER%\applications\cups_print\x64\pscript5.dll (
rem Windows 7 64bit drivers
if exist C:\Windows\System32\spool\drivers\x64\PCC\ntprint.inf*.cab (
date /T > %LOGONSERVER%\applications\cups_print\x64\dll_version.txt
echo DLLs obtained from: >> %LOGONSERVER%\applications\cups_print\x64\dll_version.txt
echo Windows 7 System >> %LOGONSERVER%\applications\cups_print\x64\dll_version.txt
C:\Windows\System32\expand.exe -I C:\Windows\System32\spool\drivers\x64\PCC\ntprint.inf*.cab %LOGONSERVER%\applications\cups_print\x64 -F:ps5ui.dll
C:\Windows\System32\expand.exe -I C:\Windows\System32\spool\drivers\x64\PCC\ntprint.inf*.cab %LOGONSERVER%\applications\cups_print\x64 -F:pscript.hlp
C:\Windows\System32\expand.exe -I C:\Windows\System32\spool\drivers\x64\PCC\ntprint.inf*.cab %LOGONSERVER%\applications\cups_print\x64 -F:pscript.ntf
C:\Windows\System32\expand.exe -I C:\Windows\System32\spool\drivers\x64\PCC\ntprint.inf*.cab %LOGONSERVER%\applications\cups_print\x64 -F:pscript5.dll
)
)

rem call logon.bat with the tech group
%LOGONSERVER%\netlogon\logon.bat tech

exit

