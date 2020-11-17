$file = 'GoogleChrome.exe'
$link = "https://www.google.com/chrome/browser/?platform=win64"

$ProgressPreference = 'silentlyContinue'
Invoke-WebRequest($link) -OutFile ".\$file"

#Start-Process -FilePath .\$file -Verb runAs -ArgumentList "--silent"