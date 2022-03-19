# would-you-wordle

## Challenge Text
* Someone left this secret text string and unfinished Wordle. Can you put them together to get the flag?
* pUpPHg3KfB15MG2KGtQQMDEECPOF8oa3VA==

## Hint
* WPA3 (YES), WPA2 (EH), WPA (NO), WEP (NOOOO)

## Solution
* Solve the Wordle to get the Key = "thorn".  Use the RC4 cipher (used by WEP) and the Key to decrypt the string.
* Flag: `jctf{CryptoIsTheKeyToFun}`

## Credit
* Developed by [Mandy](https://github.com/mrsgcyber)
