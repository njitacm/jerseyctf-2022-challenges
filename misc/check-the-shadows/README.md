# check-the-shadows

## Challenge Text
* Someone in operations recovered fragments of an important file from 142.93.56.4 when it was undergoing maintenance. Intel has it that one of the users has some valuable information. SSH into the server and retrieve it.

## Hint
* John once said that "any group is only as strong as the weakest link."

## Solution
* Given a shadow file with the many users of an organization, it could take weeks to brute-force all of the passwords, even with a HPC cluster. If a single user has a weak password, the entire system is vulnuerable.
* Use John the Ripper (or Hashcat, or other equivalent) to carry out a dictionary attack on the given shadow file. As soon as a vulnuerable password is found, ssh into the the server using that username and password.
* Start by probing the /home directory to see which users have home folders. 
* Then, list all of the files in all of the home folders to notice that many files have a file called `file.txt` in them. 
* Search every one of those files using `grep` to see if it contains `jctf` as the flag.
* Some users have a false-flag under their names, but it should be obvious which the true flag is as there is only one flag which is unique.
* Example: User cenmu_vv has the flag, but their password is strong, 8czr702ziyj3ljktdx7a5_fdmwd9vlj.
* John the Ripper found the password for user86, irina, in under a minute. `ssh user86@142.93.56.4`.
* `for folder in /home/*; do ls -l $folder; done` to notice that many users have `file.txt`.
* `for folder in /home/*; do grep 'jctf' $folder/file.txt; done` to find the actual flag.
* Flag: `jctf{o_noes_dicTionarY_atk}`

## Credit
* Developed by SpadeAsInAce
