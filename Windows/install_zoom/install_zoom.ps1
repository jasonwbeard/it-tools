$file = 'ZoomInstallerFull.msi'
$link = 'https://www.zoom.us/client/latest/ZoomInstallerFull.msi'

$ProgressPreference = 'silentlyContinue'
Invoke-WebRequest($link) -OutFile ".\$file"

Start-Process msiexec.exe -Wait -ArgumentList "/i $file /quiet /qn /norestart ZoomAutoUpdate=`"true`" ZSSOHOST=`"tradeshift`" ZConfig=`"nogoogle=1;nofacebook=1;AutoSSOLogin=1;AutoJoinVOIP=1`""