from pwn import *
from json import loads, dumps

s = b"VOTE FOR PEDRO"
v = int(bytes.hex(s), 16)
print(v)

""" run on sage cell with above v = 1750572331061789800727934052618831

x = mod(v, 2**120).nth_root(3)
hex(x)[2:] = a4c46bfb65e7eccc4e76a1ce2afc6f

"""

io = remote("socket.cryptohack.org", 13375)
io.recvline()
io.sendline(dumps({"option":"vote","vote":"a4c46bfb65e7eccc4e76a1ce2afc6f"}).encode())
print(loads(io.readline())["flag"])
