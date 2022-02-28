# bank-clients

## Challenge Text
* While in Rome, a few heisters spotted a computer in the dumpster outside of a bank and took it. After brute forcing the computer credentials and getting in with "admin/password", there was a password-protected client database discovered. A Desktop sticky note had the following information: "To fellow bank employee - a way to remember each database PIN is that it is 4-digits ranging between 1000 and 9999". It appears the sticky note was auto-translating from another language as well - let's turn that off. Are you able to assist the heisters from here?

## Hint
* After scrolling down, there was additional text on the Desktop sticky note that says "wyptbt lza zlwalt". These bank employees should be removed from the payroll immediately...

## Solution
* Utilize the keepass2john John the Ripper tool to get a password hash from the .kdbx file. `keepass2john clients.kdbx > keepassHash.txt`
* Use a [caesar cipher decoder](https://www.dcode.fr/caesar-cipher) on "wyptbt lza zlwalt" to get "primum est septem", which means "the first one is seven" in English after being translated from Latin on Google Translate. Rome is connected to the caesar cipher and also to the Latin language.
* Narrow the PIN list down to the range of 7000-7999 based on this finding. This output list can be made in a simple Python script, but other methods work equally fine. For example: 
```
for i in range(7000, 7999):
	print(i)
```
* Type `python3 listScript.py > database-passwords.txt` to send the output to a text file.
* Run John the Ripper on the password hash using the PIN range via `john --wordlist=database-passwords.txt keepassHash.txt`
* Hashcat is also an option
* After a few minutes, PIN: 7182
* Enter 7182 into the KeePass database file and the flag is labeled.
* Flag: `jctf{R1ch_p3rson_#4}`

## Credit
* Developed by [Logan](https://github.com/Git-Logan)
