#!/usr/bin/env python3

from struct import unpack
from binascii import unhexlify

# Helper function; loads data dumped from Ghidra as "Byte String (no spaces)"
def load_dump(filename):
    with open(filename, 'r') as f:
        dump = f.read().strip()
    return unhexlify(dump)

# Load the data for the 3 global arrays
jumps_dump = load_dump('jumps.txt')
perms_dump = load_dump('perms.txt')
accepts_dump = load_dump('accepts.txt')

# Unpack this data into the right type
# Sidenote: tuples are basically just immutable lists in Python,
# so I tend to use them anywhere I have a list I'm not going to modify for the sake of clarity
jumps = unpack(f'<{128*256}I', jumps_dump)
jumps = tuple(jumps[i:i+256] for i in range(0, 128*256, 256))

perms = unpack(f'<{128*8}B', perms_dump)
perms = tuple(perms[i:i+8] for i in range(0, 128*8, 8))

accepts = tuple(bool(x) for x in accepts_dump)

# First, we want to figure out which states are actually reachable at all
reachable = set()
# We can also get the (reachable) parents of each state,
# i.e. the states that can jump directly to that state
parents = tuple(set() for i in range(128))

# We use a recursive function to do a depth-first search on the jumps array
def add_reachable(ind):
    global jumps, reachable, parents
    reachable.add(ind)
    for i in jumps[ind]:
        parents[i].add(ind)
        if i not in reachable:
            add_reachable(i)

# Initial state is always 0 so we start there
add_reachable(0)

# Get a set of all of the reachable accept states
final = {i for i in reachable if accepts[i]}
# You can verify by printing the above set that this assertion is true;
# that is, we only have one reachable accept state
# That means that this *must* be the state we end in
assert(len(final) == 1)
final = next(iter(final))

# We can verify by examining the jump table that the final state has exactly one parent,
# and all of its ancestors also have exactly one parent, going all the way back to state 0
# This means that there is exactly one "route" through the states that results in our input being accepted
route = [final]
# State 0 is the first state, so we keep prepending to the route until we get to 0
while route[0]:
    assert(len(parents[route[0]]) == 1)
    route.insert(0, next(iter(parents[route[0]])))
route = tuple(route)

# Helper function to cycle a list backwards; returns a copy of the list
def invcycle(buff):
    buff = buff[::-1]
    for i in range(1, len(buff)):
        tmp = buff[0]
        buff[0] = buff[i]
        buff[i] = tmp
    buff = buff[::-1]
    return buff

# Now we create inverses of all the transformations;
# we'll use these to run through the route backwards and reconstruct the flag
def invtrans0(buff):
    for _ in range(5):
        buff[:] = invcycle(buff)

def invtrans1(buff):
    for i in range(0, len(buff), 4):
        buff[i:i+4] = invcycle(buff[i:i+4])

def invtrans2(buff):
    for i in range(len(buff)):
        buff[i] = (buff[i] + 256 - 0x5D) & 0xFF

def invtrans3(buff):
    for i in range(len(buff)):
        buff[i] ^= 0x1c

def invtrans4(buff):
    for i in range(len(buff)):
        buff[i] = (buff[i] + 256 - 0x65) & 0xFF
    for _ in range(4):
        buff[:] = invcycle(buff)

def invtrans5(buff):
    for i in range(len(buff)):
        buff[i] = (buff[i] + 256 - 0xAD) & 0xFF
    for i in range(0, len(buff), 3):
        buff[i:i+3] = invcycle(buff[i:i+3])

def invtrans6(buff):
    for i in range(len(buff)):
        buff[i] = (buff[i] + 256 - 0x18) & 0xFF
    for i in range(len(buff)):
        buff[i] ^= 0x65

def invtrans7(buff):
    for i in range(len(buff)):
        buff[i] = (buff[i] + 256 - 0xBE) & 0xFF
    for _ in range(3):
        buff[:] = invcycle(buff)

# In order to get the transform applied at each state,
# we'll run through the route forwards and apply each permutation to this list
curr_transforms = [invtrans0, invtrans1, invtrans2, invtrans3, invtrans4, invtrans5, invtrans6, invtrans7]

# Helper function that does exactly the same thing as the version from the binary,
# except that perm isn't reset at the end because we make a copy of it pretty trivially anyway,
# and it works for lengths other than 8
def permute(arr, perm):
    assert(len(arr) == len(perm))
    assert(set(perm) == set(range(len(perm))))
    for i in range(len(arr)):
        j = i
        while perm[j] >= 0:
            swp = arr[i]
            arr[i] = arr[perm[j]]
            arr[perm[j]] = swp

            tmp = perm[j]
            perm[j] -= len(perm)
            j = tmp

# This holds the transformations applied to the remainder of the flag after each step
# (Technically it holds the inverse of each transform)
transforms = []
# We don't need the last 2 states' transformations because those are never applied
for state in route[:-2]:
    # The binary applies the permutation, then applies the first transformation to the flag buffer;
    # we'll just save the first transformation to our list
    permute(curr_transforms, list(perms[state]))
    transforms.append(curr_transforms[0])
transforms = tuple(transforms)

# Now, we can reconstruct the flag by essentially simulating the route backwards
flag = []
for i in range(len(route)-2, -1, -1):
    # If the flag isn't empty, we apply the inverse of this state's transform to it
    if len(flag):
        transforms[i](flag)
    # Then, we figure out which jump would have to be taken to get to the next state in the route,
    # and prepend the byte that would make it take that jump
    flag.insert(0, jumps[route[i]].index(route[i+1]))
flag = bytes(flag)
print(flag)
