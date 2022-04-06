# secret-message

## Challenge Text
* There are two bank heist organizations communicating by sending images of expensive assets to each other, could there be a secret message somewhere? Along with the images, they are sending the same secret_key.txt file with encoded text.

## Hint
* Decode, leetcode, three code?

## Solution
* Open the secret_key.txt file - there will be a url encoded string.
* Take the url encoded string and decode it - https://www.urldecoder.org/
* The decoded url string will output a base64 string, decode it - https://www.base64encode.org/
* The decoded base64 string will output a Caesar Cipher encrypted string, decrypt it - https://www.dcode.fr/caesar-cipher
* Use the steghide command to unhide the hidden secret_message.txt file. Using the passphrase `manchester_united_2022` to unlock the file.
  * Command: steghide extract -sf Photo.jpg
* Flag: `jctf{QbxVLJrIbP}`

## Credit
* Developed by [Nishaant Goswamy](https://www.github.com/nishaant215)