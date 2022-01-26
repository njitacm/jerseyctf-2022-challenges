# hidden-in-plain-sight

## Challenge Text
A file contains the flag but it is encrypted. Normally this would be impossible to crack, but you have the encryption algorithm source code in front of you. Try to shift through it and see the vulnerabilities that can get that flag decrypted!

## Hint
The file looks a little longer than you would expect.

## Solution
* Create a decryptor based around the length of the IV and key which are stored at the end of the encrypted file.
* Flag: `jctf{k3ys_hId3_wh3r3_y0u_l3@sT_3xpeCT_Th3m}`

## Credit
* Developed by [Philip C. Okoh](https://github.com/ByridianBlack), part of [RUSEC](https://rusec.github.io/).
