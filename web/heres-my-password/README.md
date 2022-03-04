# heres-my-password

## Challenge Text
* Here's the deal - we have a list of 500 users (males, females, and pets) and one password. Log-in with the proper credentials for the flag.
* The password is `lightswitchon_and_offLOL26` and the website is www.jerseyctf.online.

## Hint
* This is not intended to require manual brute force. What are some other types of brute force methods?

## Solution
* Utilize BurpSuite (free version works) to conduct a password spraying brute force attack.
* Configure web browser to be connected to the Burp proxy by setting the HTTP proxy to 127.0.0.1:8080.
* With Intercept enabled in the Proxy tab, navigate to the site and submit any username with the provided password. The POST request will be tracked, and switch over to the HTTP history in the Proxy tab.
* Right click the POST method for the www.jerseyctf.online host, and click Send to Intruder.
* In Positions, click Clear on the right. Highlight the username that was inputted and click Add on the right.
* In Payloads, click Load and select the provided users.txt file. Click Start attack, and then click the Length filter twice so that it orders from greatest to least. In ~5-10 minutes of running the attack, the correct user `Wolverine` will have a larger length than the rest because it logged-in and provided the flag in an alert. Navigate to the site and enter in the proper credentials to see the flag or simply read it in Burp.
* Flag: `jctf{c0NGR@T2_y0U_p@22wORd_SPR@y3D!}`
* Shares website with osint/contributor challenge.

## Credit
* Developed by [Andrew](https://github.com/peppermintpatty5) and [Logan](https://github.com/Git-Logan)
* Additional Resources: https://owasp.org/www-community/attacks/Password_Spraying_Attack and https://www.youtube.com/watch?v=QcQT4acDbnk
