# symbolism

A reversing challenge with a binary that runs on a Lisp Machine

Developed by ContronThePanda (GitHub), part of RUSEC.

## Solution

Using `strings` should give you a few keywords to look up, like "Lisp Machine" and "Open Genera".
With those, you should be able to figure out that this looks like a binary for Open Genera.
From here you can install Open Genera (I followed [this guide](https://archives.loomcom.com/genera/genera-install.html)) and get to work.
If you follow this guide, your local machine's file system should be available from the VM under the path `GENERA-VLM:/`.

After getting some familiarity with the OS, you should figure out that you can load a binary with `Load File`.
This imports all of the functions into the global namespace.
You can disassemble a function with `(disassemble #'function-name)`, where `function-name` is the name of the function.
You can again take a look at the `strings` output and guess that `verify-flag` looks like it's probably a relevant function.

It's very hard to find any sort of reference for this assembly language, but most of the instructions have very long names so it's not hard to figure out what's going on.
You can verify experimentally that this function takes 1 argument, which is probably what the first line means, and the comment indicates that this argument is called `F`.
This function:

1. checks the length of `F`, and immediately returns `"Invalid"` if it's not 52
2. uses `map` (a standard Common LISP function) to call `char-map` on each element of `F`, and collects the results into `L`
3. calls a function called `gen-key` with no arguments and stores the results in `K`
4. uses `map` again to XOR `L` and `K`, storing the result in `R`
5. declares a constant list of integers called `C`
6. checks if `R` and `C` are equal; return `"Valid"` if they are and `"Invalid"` if they aren't

We can assume that the input `F` is a string, and this function returns `"Valid"` if that string is the flag, and `"Invalid"` otherwise.
Then, at a higher level: this function maps each character in the input string to a number, generates a "key" (a list of numbers which is the same length),
XORs the two together, and checks if it is equal to an expected value.
Since `gen-key` doesn't take any arguments, it's probably safe to assume that it always returns the same value.
You can verify this experimentally, since all of the functions are exported globally.
You can also look at its disassembly to figure this out; it's pretty complicated but you can probably skim it and see that it doesn't seem to rely on any outside influence.

Now, we can disassemble `char-map`.
This function is essentially just a really big switch statement for every printable ASCII character, mapping each one to a unique integer.

This leaves us with 2 steps for getting the flag back:

1. XOR the expected list (`C`) with the key (`K`) to get the expected value of `L`
2. Reverse the mapping done by `char-map` to get the flag back

Here's a Python script that does this:

```py
#!/usr/bin/env python3

# This is the array the program compares our XORed input with; i.e., what it expects the result to be
expected = [int(x) for x in "3472 2481 3691 2476 650 3021 260 3972 3888 2025 637 1853 1481 2679 2459 35 706 669 2794 2383 3041 3855 2203 1178 577 1942 1417 2513 111 1888 3977 933 1399 2705 1902 3481 3474 3 1349 199 297 1481 3230 1253 3062 1853 246 6 3097 849 4071 2000".split()]

# This is the generated key which is XORed with our input
key = [int(x) for x in "440 1303 2070 897 1724 1262 2383 2553 3784 3437 2614 372 3917 1155 1289 3249 3194 3620 586 3890 1369 2696 1987 3614 953 491 1912 1677 3739 2302 1293 3321 3207 1539 3611 1693 299 2030 3235 1365 2140 1073 1562 3767 957 2045 3058 1881 3289 1201 1964 3073".split()]

# We can XOR these together to figure out what our flag has to be
flag_enc = [a ^ b for a, b in zip(expected, key)]

# Now we just have to map these numbers back to characters

# This will store the mapping from number -> character
# We're adding the one for ~ manually because it's the last case in the code, so it's handled slightly differently
char_map = {1684: '~'}

# We'll parse the disassembly of char-map to get the mapping
with open('char-map.disas', 'r') as f:
    dis = [x.strip() for x in f.readlines()]

# Not 100% sure what the numbers in the left column are since they kinda go out of order sometimes, let's just call them "IDs"
# We can make a map from ID -> list index to look up jumps easily
id_map = {int(x.split()[0]): i for i, x in enumerate(dis)}

for i, ln in enumerate(dis):
    # Each check begins with a PUSH-CONSTANT for the character
    if 'PUSH-CONSTANT' in ln:
        # Get the argument (the constant being pushed)
        arg = ln.split()[-1]

        # Check if the argument is a character literal
        if arg.startswith("'#\\"):
            arg = arg[3:]

            # Space is a special case; it's the only one that's not just encoded as the character it represents
            if arg == 'Space':
                arg = ' '
            # Tilde is the last one, and it's handled differently so we already hardcoded it
            # If we get to tilde we're done
            elif arg == '~':
                break

            # The place the code jumps to if this character matches
            jdest = int(dis[i+2].split()[-1])
            jdest_ind = id_map[jdest]

            # Get the number the code returns in this case
            num = dis[jdest_ind].split()[-1]
            # Larger numbers have a ' in front, we need to handle both cases
            if num[0] == "'":
                num = int(num[1:])
            else:
                num = int(num)

            # Add this to our mapping
            char_map[num] = arg

        else:
            # If we've gotten to one that isn't a character literal, we're done
            break

# Decode and print the flag
flag = ''.join(char_map[x] for x in flag_enc)
print(flag)
```

This script assumes you've stored the disassembly of `char-map` in the file `char-map.disas`.

Flag: `jctf{l0t5_0F_1rriT@tiN9_5tUp1D_p4r3nThEs35_a08n78w0}`

---

## Challenge Message

My friend sent me this weird file. Whenever I ask him what it is, he just keeps saying something about symbols.

## Challenge Hints

* [https://archives.loomcom.com/genera/genera-install.html](https://archives.loomcom.com/genera/genera-install.html)
