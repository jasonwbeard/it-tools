$file = 'LastPassInstaller.msi'
$link = 'https://download.cloud.lastpass.com/windows_installer/LastPassInstaller.msi'

$ProgressPreference = 'silentlyContinue'
Invoke-WebRequest($link) -OutFile ".\$file"

Start-Process msiexec.exe -Wait -ArgumentList "/i $file /quiet"