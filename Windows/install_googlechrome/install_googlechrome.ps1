$file = 'GoogleChromeStandaloneEnterprise64.msi'
$link = "http://dl.google.com/chrome/install/GoogleChromeStandaloneEnterprise64.msi"

$ProgressPreference = 'silentlyContinue'
Invoke-WebRequest($link) -OutFile ".\$file"

Start-Process msiexec.exe -Wait -ArgumentList "/i $file /quiet"