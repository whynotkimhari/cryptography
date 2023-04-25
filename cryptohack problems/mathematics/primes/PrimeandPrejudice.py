### Using https://github.com/loluwot/StrongPseudoPrimeGeneratorMkII/blob/main/sol.py to find prime and base

### after using that, we got
from Crypto.Util.number import getPrime
from sympy import *
import pwn
import json
import math
prime = 254615674198066111348559108472798769684001878358857095506953165173728617744160791637392778869123081942910652286182625202904553164094373753256627211722903336405144072652128620402472907
base = 1030617353352977080364307518770663528633732979071959749923
r = pwn.remote('socket.cryptohack.org', 13385)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

r.recvline()
json_send({'prime': prime, 'base' : base})
line = json_recv()
print(line)