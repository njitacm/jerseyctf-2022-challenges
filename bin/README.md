# BIN

- BIN --> Binary Exploitation + Reversing

## Easy Challenges
| Challenge Name  | Description | Hint
|:-- | :-- | :---
| [patches](patches) | Given an objdump of an executable, figure out what hexadecimal instructions are needed to nop to get the jctf flag to stdout | The [Intel Manual](https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf) might be overkill, but maybe reviewing Intel Assembly and their corresponding opcodes might help to crack the challenge. **Simply enter the opcodes**
| [misdirection](misdirection) | Where'd the flag go? | There are many ways to solve this challenge, some of which are much easier than others.
| [win-bin-analysis](win-bin-analysis) | Find the key hidden in the Windows executable files. | .exe's arent the only type of executable file.

## Medium Challenges
| Challenge Name  | Description | Hint
|:-- | :-- | :---
| [context-clues](context-clues) | Everyone made a big deal about C++ getting coroutines in 2020, but C has had them for decades if you know where to look. | Remember to look up terms and function names you've never heard of.
| [block-game](block-game) | There's mining, and there's crafting, but something seems off... | This doesn't look like a standalone program, I wonder if it depends on something else to run.
| [going-over](going_over) | My friends said they were going on a trip but I think they ran into some trouble... nc 0.cloud.chals.io 10197. They sent me these two files before we lost contact ([src.c](challenge/files/src.c) and [going-over](challenge/going-over)) | If only there were a way to find the exact location of the ledge... like if the ledge had an address or something

## Hard Challenges
| Challenge Name  | Description | Hint
|:-- | :-- | :---
| [symbolism](symbolism) | My friend sent me this weird file. Whenever I ask him what it is, he just keeps saying something about symbols. | https://archives.loomcom.com/genera/genera-install.html
| [kangaroo](kangaroo) | I'm feeling pretty JUMPY today. Can you give me a nice flag to JUMP on? | There's a lot of code, but most of it seems pretty similar. Try to look at the bigger picture.
