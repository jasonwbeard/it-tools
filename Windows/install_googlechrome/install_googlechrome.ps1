$file = 'GoogleChromeStandaloneEnterprise.msi'
$link = "http://dl.google.com/chrome/install/GoogleChromeStandaloneEnterprise.msi"

$ProgressPreference = 'silentlyContinue'
Invoke-WebRequest($link) -OutFile ".\$file"

Start-Process msiexec.exe -Wait -ArgumentList "/i $file /quiet"