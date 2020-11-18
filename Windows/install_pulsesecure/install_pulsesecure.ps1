Start-Process msiexec.exe -Wait -ArgumentList "/i $psscriptroot\PulseSecure.x64.msi CONFIGFILE=$psscriptroot\Default.pulsepreconfig /qn /norestart"

Start-Sleep -Seconds 3
Start-Process "C:\Program Files (x86)\Common Files\Pulse Secure\JamUI\jamCommand.exe" -Wait -ArgumentList "-ImportFile `"Default.pulsepreconfig`""
Start-Sleep -Seconds 3
Stop-Process "pulse.exe"