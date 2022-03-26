#!/usr/bin/env python3

from os import urandom
from binascii import hexlify, unhexlify

class Cipher:
    def __init__(self):
        self.key = b''
    def encrypt(self, data):
        if len(data) > len(self.key):
            self.key = urandom(len(data))
        return bytes(a ^ b for a, b in zip(data, self.key))

cipher = Cipher()

with open('/root/flag.txt', 'rb') as f:
    flag = f.read().strip()

flag = cipher.encrypt(flag)
flag = hexlify(flag)

print("Welcome to my SUPER secure encryption service!")
print("To show you just how secure my service is, I'm gonna GIVE you the encrypted version of my flag.")
print("Why? Because I'm CONFIDENT you can't decrypt it.")
print(f"Here it is: {flag}")
print()
print("Now that you've been ensured that my service is SECURE, you should give it a try!")

while True:
    try:
        print("Give me some data:")
        inp = input()
    except:
        break
    try:
        inp = unhexlify(inp)
    except:
        print("That's not valid!")
        continue
    ct = cipher.encrypt(inp)
    ct = hexlify(ct)
    print(f"Here it is: {ct}")
