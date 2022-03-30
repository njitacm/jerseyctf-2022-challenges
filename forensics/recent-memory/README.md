# recent-memory

## Challenge Text
* Use the memory image in the Google drive link below.  An attacker left behind some evidence in the network connections.  Follow the attacker's tracks to find the flag.

https://drive.google.com/drive/folders/1ubSx3pwHOSZ9oCShHBPToVdHjTev7hXL 

## Hint
* Try connecting to the attacker's system.

## Solution
* The flag can be obtained two ways.  Find the nc.exe session in the memory dump and connect to the same host using netcat.

vol -f ~/recent-memory.mem windows.netstat
nc -nv 161.35.53.62 5283

Or you can dump the nc.exe process memory and using strings to find the flag.

* Flag: `jctf{f0ll0w_7h3_7r41l}`

## Credit
* Developed by [Rob Bruder](https://github.com/njccicrob)
