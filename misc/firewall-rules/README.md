# firewall-rules

## Challenge Text
* Liar, Liar, Rules on Fire! A network administrator configured a device's firewall, but made a few errors along the way. Some of your favorite applications may have been denied... We can't worry about that yet, first step is to make sure external hosts aren't able to exploit vulnerable firewall rules.
* Sum the vunerable ports and put the answer in the flag format: jctf{INSERT NUMBER}

## Hint
* Sometimes Google searches lead to numbers!

## Solution
* Pull up list of TCP and UDP port numbers: https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
* Query through each firewall rule and note that the allowed insecure ports that provide remote access or unencrypted connection are: 513 (rlogin), 23 (telnet), 3389 (RDP)
* 513 + 23 + 3389 = jctf{3925}

## Credit
* Developed by [Logan](https://github.com/Git-Logan)
