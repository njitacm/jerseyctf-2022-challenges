# file-zip-cracker

## Challenge Text
* We have a secret file that is password protected. However, we have obtained a wordlist of actors that is part of the password. The password is the combination of one of names on the list with a year.
  * Format: "Actor_NameYYYY"  
  * Example : "Henry_Cavill1964"
* Fix the script to brute force the password.

## Hint
* No hints

## Solution
1. To fix the script:
    * Fix Line 23 : `numbers_set = '0123456789'`
    * Add line 20: `file1 = open('actorList.txt', 'r')`
    * Add line 21: `Lines = file1.readlines()`
    * Add line 27 : `for actor_name in Lines:`
    * Change line 30 to: `password = actor_name.strip()+''.join(c)`
2. After opening the folder there is a txt file that is encoded with ROT13. Use a ROT13 decoder to decode the message to get the code to unlock the next zip file.
3. After opening the 2nd zip file the flag is in a mp3 file. But it is not mp3 file - it is actually a gif file. The file extension has to be renamed to gif to open the file.
* Flag: `jctf{ew8WhHuhmv}`

## Credit
* Developed by [Nishaant Goswamy](http://www.github.com/nishaant215)