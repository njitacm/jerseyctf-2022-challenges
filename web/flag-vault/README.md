# Flag Storage Vault

## Challenge Text
* I'm very organized. I even keep all of my flags neatly organized in a database! But, these are my flags! You don't have access to them... or do you?  Start here: jerseyctf-flag-vault.chals.io

## Hint
* What is the most common type of database?
* What is the flag format? How does that help you?

## Solution
* Recognize that the vulnerability is SQL Injection
* On the login page, put `admin` as the username and `' OR 1=1;--` as the password (or similar payload)
* On the flags page, try `' OR 1=1;--` again
* Realize that it doesn't work here because there are fake flags and only one item is returned
* Use `' OR flag LIKE 'jctf{%` to get the flag with the correct format
* Flag: `jctf{ALMOST_LIKE_A_NEEDLE_IN_A_HAYSTACK}`

## Credit
* Developed by Edward
