# misdirection

Simple challenge about file descriptors

Developed by [ContronThePanda](https://github.com/PAndaContron), part of [RUSEC](https://rusec.github.io/).

## Solution

This binary XORs 2 arrays together and uses `write` to write the result to file descriptor 5.
This result is (presumably) the flag.

A file descriptor is basically just an integer that identifies an open file within a process.
By default, file descriptor 0 is `stdin`, 1 is `stdout`, and 2 is `stderr`.

File descriptor 5 isn't open by default, and the program never opens it, so this will result in an error if the program is run normally
(the binary never actually checks if the call succeeded, so we don't see this error).

There are a few ways we can get the flag.
We can use `./misdirection 5>&1`; this uses Bash syntax to redirect FD 5 to FD 1,
which is standard output, so the output gets printed to our terminal.

We can also use `ltrace -s 9999 ./misdirection`, or `strace -s 9999 ./misdirection`.
`ltrace` and `strace` are commands that print out every library call and system call a program makes respectively.
This way, we can see the call to `write` when it happens, even if it doesn't succeed.
By default, these commands only print the first 32 characters of a string;
`-s 9999` increases this limit to 9999.

There are a few other ways to solve this challenge: we could use a debugger, set a breakpoint, and get the flag from memory,
or we could copy the arrays from the binary and XOR them ourselves, but that's way more work.

Flag: `jctf{l00k5_1iK3_u_f0Und_m3_018a09d6}`

---

## Challenge Message

Where'd the flag go?

## Challenge Hints

* There are many ways to solve this challenge, some of which are much easier than others.
