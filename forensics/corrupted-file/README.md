# corrupted-file

## Challenge Text
* Can you find a way to fix our corrupted .jpg file?

## Hint
* No hints

## Solution
* Use a hex editor (https://hexed.it/) and append the missing bytes to the start of the file flag_mod.jpg
* Right click at the top of all the bytes and click **Insert bytes here...**
  * Number of bytes is 4 because jpg file signatures usually have 4 bytes at the front of the hexdump.
* FF D8 FF E0
* Save changes and open the file.
* Flag: `jctf{OaZdSdMo8F}`

## Credit
* Developed by [Nishaant Goswamy](http://www.github.com/nishaant215)
