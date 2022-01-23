# win-bin-analysis

# Challenge Message
* Find the key hidden in the Windows executable files.

# Hint
* .exe's arent the only type of executable file.

# Solution

Analyze the .dll (not the .exe) in Ghidra, search for strings, find a bunch of strings that get outputed when the file is executed, get one of the strings, and decrypt using one of the strings as a key and one string saying the encryption algorithm.

````````````
flag: jctf{00g@_B000G@@_B1LL_G8S_wAs-H3Re}
password: HKEY_CURRENT_USER
encryption: AES(CBC)
fakeFlag: njsctf{look-harder}
encrypt: flag-U2FsdGVkX1+/+Gg+TT1OswZb7zJBF954sV9CPYr9yjuECuBh60j/qG3Kw4Hk9/l6fu5ibkYarZWNBByLBuGrYQ==
````````````
