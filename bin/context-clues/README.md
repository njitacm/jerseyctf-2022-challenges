# context-clues

Reversing challenge using POSIX `makecontext`/`getcontext`/`swapcontext` functions

Developed by [ContronThePanda](https://github.com/PAndaContron), part of [RUSEC](https://rusec.github.io/).

## Solution

Most of the solution entails knowing what these library functions do; from there, it's pretty simple to figure out what the program is doing.
`main` calls `func1` using its context, then `func1` passes control back and forth to `func2` a few times before they return.
Each function performs some transformations on the input buffer,
but tracing these transformations gets complicated because control gets passed back and forth in the middle of loops.
After the transformations, `main` checks if the buffer is equal to some expected value.

We could try to trace these transformations to work backwards from the expected value and get the original, but there's also a more clever approach.
Using Z3, we can make an array of bit vectors, then simulate the transformations on that array, and add the constraint that the result must be equal to the expected value.
Then, the solver should tell us the original input, which should be the flag.
We can simulate the context switches using Python's implementation of coroutines (generators).
To do this, we make one function a generator, and use `next` to pass control to that function, and `yield` to pass control back.
The syntax looks a little bit strange because this isn't really what generators are intended to be used for, but it's effectively equivalent to what the binary does.
See (sol.py)[sol.py] for an implementation of this solution.

Flag: `jctf{0b5OL3sc3nCe_rU1e5_209g9ax}`

---

## Challenge Message

Everyone made a big deal about C++ getting coroutines in 2020, but C has had them for decades if you know where to look.

## Challenge Hints

* Remember to look up terms and function names you've never heard of.
