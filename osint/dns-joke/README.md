# dns-joke

## Challenge Text
* A system administrator hasn't smiled in days. Legend has it, there is a DNS joke hidden somewhere in www.jerseyctf.com. Can you help us find it to make our system administrator laugh?

## Hint
* How are IP addresses pointed towards domain names?

## Solution
* Use any of the following dig, nslookup, or host commands to search the DNS records of www.jerseyctf.com:
  * dig www.jerseyctf.com txt
  * dig -t txt www.jerseyctf.com +short
  * host -t txt www.jerseyctf.com
  * nslookup -type=txt www.jerseyctf.com
* The flag will be in a string: `jctf{DNS_J0k3s_t@k3_24_hrs}`

## Credit
* Developed by [Logan](https://github.com/Git-Logan)
