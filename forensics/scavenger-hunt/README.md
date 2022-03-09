# scavenger-hunt

## Challenge Text
* My friend told me he hid a flag for me on this server!
* Username: jersey
* Password: securepassword

## Hint
* If only there were a way to see all folders... even hidden ones
* I wonder where passwords are typically stored on ssh servers

## Solution
* Run `ls` to find the `folder` folder in `/home/jersey/jersey` and cd into it
* Run `ls -a` to find the hidden `.secret_folder` folder inside of `folder` and cd into it
* Read the file `flag.txt` inside of `.secret_folder` with cat, which tells you to look at the users and their passwords
* Read `/etc/passwd` using cat and find that the last user is `hey_that_package_is_sus`
* Look through the installed packages (i.e. with the command `apt search flag`) and find the custom package called `notaflag`
* Run `apt info notaflag` to read its description, which directs you to its manual
* Run `man notaflag` to read the man pages and under BUGS is the flag
* Flag: `jctf{f1n4LLy_f0uND_1T}`

## Credit
* Developed by Penelope
