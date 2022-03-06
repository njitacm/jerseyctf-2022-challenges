#Open file for processing.
$file_in = Get-Content -Path ".\dnsmasq-ip-extract-dnsmasq.log"

#Output file for answer (will be hashed later for the flag).
$file_out = ".\powershell_answer.txt"

#Clear contents of output file if it exists.
if (Test-Path $file_out)
{
    Clear-Content($file_out)
}

#List to store discovered IP addresses.
$ip_list = @()

#Populate IP list, this will deduplicate addresses and maintain the
#order presented in the logs (important for correct hash generation).
foreach ($line in $file_in)
{   
    $ip = $line.split(" ")[-1] -replace "`n",""
    if ($ip_list -notcontains $ip)
    {
        $ip_list += $ip
    }
}

#Calculate hash for each IP and write to file.
foreach($ip in $ip_list)
{
    $ip_hash = Get-FileHash -InputStream ([System.IO.MemoryStream]::New([System.Text.Encoding]::ASCII.GetBytes($ip)))
    "$($ip) $($ip_hash.Hash.toLower())" | Out-File -Append -FilePath "powershell_answer.txt" 
}

#Get hash of output file and create flag.
#Participants can generate hash in a terminal or other program.
$output_hash = (Get-FileHash $file_out).Hash.toLower()
Write-Output("jctf{$output_hash}")