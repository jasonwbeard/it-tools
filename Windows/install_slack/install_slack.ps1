$file = 'SlackSetup.exe'
$link = "https://slack.com/ssb/download-win64"

$ProgressPreference = 'silentlyContinue'
Invoke-WebRequest($link) -OutFile ".\$file"

Start-Process -FilePath .\$file -ArgumentList "-s"