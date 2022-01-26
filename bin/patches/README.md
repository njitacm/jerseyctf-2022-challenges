# patches

## Challenge Text
* Given an objdump of an executable, figure out what hexadecimal instructions are needed to nop to get the jctf flag to stdout

## Hint
* The [Intel Manual](https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf) might be overkill, but maybe reviewing Intel Assembly and their corresponding opcodes might help to crack the challenge. **Simply enter the opcodes**

## Solution
* Follow the Control Flow to Determine what opcode you have to nop  
* Flag: `jctf{7e0a}`

## Credit
* Developed by [Andres](https://github.com/AOrps)
