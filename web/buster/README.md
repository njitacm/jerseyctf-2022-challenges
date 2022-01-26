# buster

NOTE: The provided Python file, `buster.py`, should be run on a server and not be given as part of the challenge; just the URL of the server should be given.

## Challenge Text
* Check out my new site, it has lots of cool pages!

## Hint
* What do HTTP response codes actually mean?

## Solution

Directory enumeration challenge where every request returns a random HTTP status

The root webpage has a comment suggesting that this is probably an enumeration challenge;
i.e., we want to find all of the subpages under this page.
If we try an application normally used for this purpose, like DirBuster, we run into an issue.
All of the pages return a randomized HTTP status, which means that these programs can't automatically figure out what is and isn't a valid page.

The solution is to write our own script to search for the right page.
We'll simply send requests to all of the pages in a wordlist, and see if any of them respond with something that might be the flag.
Here's what that looks like in Python:

```py
from multiprocessing.pool import Pool
from sys import argv
import requests

# I used /opt/dirbuster/directory-list-2.3-small.txt for the file,
# other parameters are self-explanatory
if len(argv) != 4:
    print(f'Usage: {argv[0]} <URL> <brute force file> <num threads>')
    exit(1)

url = argv[1]
fname = argv[2]
numthreads = int(argv[3])

# Prints out the flag if it's in the content of this page
def check_page(name):
    name = name.strip()
    r = requests.get(f'{url}/{name}')
    if 'jctf' in r.text:
        print(r.text)

# Uses a process pool to check all of the pages with names from the file
with open(fname, 'r') as f:
    with Pool(processes=numthreads) as pool:
        pool.map(check_page, f, 256)
```

This uses multithreading to speed things up.
This also means it doesn't actually stop after it prints the flag until it goes through the entire wordlist, so you have to Ctrl-C it manually.

Flag: `jctf{1t5_jUst_4_nUmb3r_ag8h7z8021}`

## Credit
* Developed by [ContronThePanda](https://github.com/PAndaContron), part of [RUSEC](https://rusec.github.io/).
