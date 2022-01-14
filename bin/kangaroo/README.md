# kangaroo

Reverse engineering challenge obfuscated with the `setjmp` and `longjmp` functions

Developed by [ContronThePanda](https://github.com/PAndaContron), part of [RUSEC](https://rusec.github.io/).

## Solution

The structure of the binary is essentially a long list of blocks initialized with `setjmp`,
followed by a `longjmp` to the one called `start`.
Pretty much all of the variables in this program are global, and have their names exported with the binary.
Most of the blocks fall into one of two categories:

* "State" blocks, which set the global `nxstate`, call `permute`, and `longjmp` to a block called `control`
* "Transform" blocks, which apply some transformation to the global buffer `flags`, then `longjmp` to one of the state blocks (determined by `nxstate`)

There are also a few other special blocks:

* `start` prints out the initial prompt, then copies `argv[1]` into `flag` and its length into `flag_len`, ensuring that it exists and isn't an empty string,
then finally jumps to the first state block
* `accept` prints a message indicating that the input was accepted, then exits
* `reject` prints a message indicating that the input was rejected, then exits
* `control` increments `flag` and `flag_len` by 1 (effectively cutting off the first character),
then `longjmp`s to one of the transform blocks if the buffer isn't empty,
or to either `accept` or `reject` if it is

Basically, it's a finite state machine that also transforms the flag as it examines it.
The control flow goes something like this:

1. `start` reads in the input and jumps to the first state
2. Each state checks the first character of the current buffer, then sets `nxstate` based on the current state and character,
based on a global array called `jumps`
3. Each state also calls `permute` on the global array `transform_inds`, with a parameter from the `perms` array based on the current state
    * Each `perm` is a permutation of the numbers 0-7; `permute` applies the same permutation to its first argument
4. Then, each state `longjmp`s to `control`
5. `control` first cuts the first character off of the buffer
6. Then, if the buffer isn't empty:
    * `control` jumps to a transform block, which is chosen by `transforms[transform_inds[0]]`
    * There are 8 transform blocks, each of which either shuffles the bytes around, adds some value to all of the bytes mod 256,
    XORs every byte with some value, or some combination of these
    * Then, each transform block jumps to the state given by `states[nxstate]`, cycling back to step 2 with the next character
7. If the buffer is empty, `control` checks `accepts[nxstate]` to see if the next state is an "accept" state;
if it is, it jumps to `accept`, if it isn't, it jumps to `reject`

There are way too many states for us to reason about this manually.
Luckily, most of the relevant information is stored in a few giant global arrays, so we can just dump those and analyze them in Python.
I used Ghidra's copy bytes option, the result is in the (solution folder)[sol].
Now, after looking at the data a little bit there are a few things that we can see:

* Not all of the states are reachable from state 0, so we can completely ignore the ones that aren't
* There's only one reachable accept state, which means we *have* to get to that state for our string to be accepted
* There's only one reachable state that can jump to that state, and only one reachable state that can jump to *that* one,
and so on all the way back to state 0; this means that there's exactly one possible route through the program that ends in an accept state

Now we can recover the flag by doing the following:

* Figure out the route we need to take for the string to be accepted
* Figure out what transformation is applied at each step (since this is independent of the input)
    * This involves running through the route forwards to see how the transformations are permuted at each step
* Run through the route backwards to construct the flag; this involves 2 parts:
    1. Undo the transformation applied at this step
    2. Prepend the byte that would send us to the next state in the route

The (solution folder)[sol] includes a commented Python script with more details.

---

## Challenge Message

I'm feeling pretty JUMPY today. Can you give me a nice flag to JUMP on?

## Challenge Hints

* There's a lot of code, but most of it seems pretty similar. Try to look at the bigger picture.
