# infected

**Challenged by NJCCIC**

## Challenge Text
* A host on the network was infected with a remote access trojan.  A memory image of the host can be found [here](https://drive.google.com/drive/folders/1YJN9tqjKSIRcYD3Wb4ZH1xo2DlnCuJEB).
* The flag is the process name followed by the PID.  Format jctf{processname.exe:1234}

## Hint
* No hints

## Solution
* A few ways to solve this one.  If you list the running processes from the memory image using 'vol -f ~/infected.mem windows.pslist' you will see an svchost.exe process that was launched from cmd.exe which is not normal.  svchost.exe with the PID is the flag.

Another way, you can run 'vol -f ~/infected.mem windows.malfind' which comes back with a few processes that are possibly infected svchost.exe being the correct one.


* Flag: `jctf{svchost.exe:7756}`

## Credit
* Developed by [Rob Bruder](https://github.com/njccicrob)
