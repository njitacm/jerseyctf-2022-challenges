# inDEStructible

## Challenge Text
* It's an older code, sir or madam, but it checks out.

## Solution
* Find a DES encryption implementation in your language of choice and start bruteforcing keys (keyspace is 2^56, but the key is going to be < 2^22 so it shouldn't take more than 30 min to bruteforce).
* The exact key was generated by taking the string 'sw' (29559 as an int) and converting it to binary, padded (pre-pending 0s) to 56-bits, and used directly as a key without the permutation.
* Flag: `jctf{p4rty_l1k3_it_1977} `

## Credit
* Developed by SpadeAsInAce