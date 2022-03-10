# going-over

## Challenge Text
* My friends said they were going on a trip but I think they ran into some trouble... nc [server] [port]
* They sent me these two files before we lost contact ([src.c](challenge/files/src.c) and [going-over](challenge/going-over))

## Hint
* If only there were a way to find the exact location of the ledge... like if the ledge had an address or something

## Solution
* Use pwntools to print `cyclic(100)`, which will return a long string we can use to test buffer overflow (line 7 of `solver.py`)
* Use pwntools to run `going-over` (line 3 of `solver.py`)
* The terminal will say the process is running and output a `pid`
* Run `gdb ./going-over -p [pid]` in a separate terminal
* Run the process in gdb and paste the long string from earlier
* The program will segfault and you can examine which part of the string overwrote the return pointer with `x/xw $rsp`
* We see that `faaa` overwrote the return pointer
* Run `objdump -d going-over | grep grab_ledge` in a terminal to get the address of the `grab_ledge()` function (on my machine, it is `0x4011b6`)
* Use pwntools to get the proper padding with `cyclic_find("faaa")` 
* Connect to the server and port (line 5 of `solver.py`)
* Send the proper padding and the return address (lines 8-11 of `solver.py`)
* A shell is created and then you can do `cat flag.txt` to read the flag file
* Flag: `jctf{ph3w_ju57_1n_71m3}`

## Credit
* Developed by Penelope
