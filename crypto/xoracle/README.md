# xoracle

Note: the file [xoracle.py](challenge/xoracle.py) should be provided as part of the challenge,
and it should also be accessible by netcat, running in the same directory as [flag.txt](challenge/flag.txt).

## Challenge Text
* Check out my cool new encryption service! It's very secure!

## Hint
* Read carefully: a small mistake or typo can be all it takes to make an encryption system insecure.

## Solution

Simple XOR-based crypto challenge

The program encrypts your input by XORing it with a randomly generated key.
However, it tries to be lazy, and only regenerates the key if you give it an input that's longer than the current key.
Before taking any input, it encrypts the flag and prints out the ciphertext.
If we just give this string directly back to the program, it doesn't regenerate the key,
so it gets encrypted with the same key again.
XOR has a nice property: it's its own inverse; this means that encrypting twice with the same key gives back the original plaintext.
Now, the program gives it to us as a hex string; we just need to convert it back to ASCII text.
This can be done with Python's `binascii.unhexlify` function.

* Flag: `jctf{1_th0U9hT_1t_w45_53Cure_a07b8a01}`

## Credit
* Developed by [ContronThePanda](https://github.com/PAndaContron), part of [RUSEC](https://rusec.github.io/).
