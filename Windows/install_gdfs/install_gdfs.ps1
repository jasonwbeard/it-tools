$file = 'GoogleDriveFSSetup.exe'
$link = "https://dl.google.com/drive-file-stream/GoogleDriveFSSetup.exe"

$ProgressPreference = 'silentlyContinue'
Invoke-WebRequest($link) -OutFile ".\$file"

Start-Process -FilePath .\$file -ArgumentList "--silent --desktop_shortcut --gsuite_shortcuts=false" -verb runAs -Wait