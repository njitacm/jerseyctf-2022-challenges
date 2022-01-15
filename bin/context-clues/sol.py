#!/usr/bin/env python3

from z3 import *

# Array of 32 bit vectors, one for each character
flag = tuple(BitVec(f'c{i}', 8) for i in range(32))
# This is the one we actually modify
inp = list(flag)
# Expected result, exported from Ghidra
exp = [0x6a, 0x63, 0x39, 0x30, 0x2e, 0x2b, 0x34, 0x4e, 0x4c, 0x1b, 0x4f, 0x2d, 0x5b, 0xb, 0x79, 0x1c, 0x20, 0x7b, 0xa, 0x6b, 0x4f, 0x20, 0x11, 0x72, 0x70, 0x23, 0x63, 0x77, 0x18, 0x3a, 0x6a, 0x5e]

# Sanity check to make sure I copied this properly
assert(len(exp) == 32)

# Helper function to swap 2 elements of inp
def swap(i, j):
    inp[i], inp[j] = inp[j], inp[i]

# Copy of func1; we'll model func2 as a generator and use `next` to pass control to it
def func1():
    g = func2()
    for i in range(6, 0x1c):
        inp[i] ^= 0x37
        if i == 0x10:
            next(g)
    swap(5, 24)
    for i in range(3, 0x16):
        inp[i] ^= inp[i-1]
        if i == 7:
            next(g)
    swap(6, 9)
    for i in range(0xd, 0x1e):
        swap(i, 12)
        if i == 0x15:
            next(g)
    swap(15, 27)
    # In the binary, the context for func1 returns to the context for func2;
    # to simulate this, we pass control to func2 one last time
    next(g)

# Copy of func2; we'll use `yield` to pass control back to func1
def func2():
    for i in range(3, 0x1d):
        swap(i, 2)
        if i == 0xb:
            yield
    swap(11, 20)
    for i in range(0xc, 0x20):
        inp[i] ^= inp[i-1]
        if i == 0x14:
            yield
    swap(30, 27)
    for i in range(4, 0x12):
        inp[i] ^= 0x78
        if i == 0xe:
            yield
    swap(25, 28)
    # In the binary, the context for func2 returns directly to the context for main;
    # we simulate this by returning control to func1, which then returns to main
    yield

func1()

# Create the solver and add the constraints
s = Solver()
for a, b in zip(inp, exp):
    s.add(a == b)

# Assert that the solver found a solution
assert(s.check() == sat)

model = s.model()

# Get the value the solver assigned to each character and combine them into a byte string
flag = bytes(model[c].as_long() for c in flag)
print(flag)
