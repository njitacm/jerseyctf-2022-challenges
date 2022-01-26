# we-will

## Challenge Text
* A flag was left behind but it seems to be protected.

## Hint
* The challenge name should help you figure out how to open it.

## Solution
* Brute force the password protected ZIP file
* The password is: *@@!^^$25Jjersey

```
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt flag.zip
```

## Credit
* Developed by [Rob](https://github.com/njccicrob)
