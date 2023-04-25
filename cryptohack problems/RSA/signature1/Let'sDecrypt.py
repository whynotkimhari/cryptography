import pwn
import json
from pkcs1 import emsa_pkcs1_v15
from Crypto.Util.number import bytes_to_long

# MSG = 'We are hyperreality and Jack and we own CryptoHack.org'
# DIGEST = emsa_pkcs1_v15.encode(MSG.encode(), 256)

# print(DIGEST)



r = pwn.remote('socket.cryptohack.org', 13391)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

r.recvline()
json_send({"option": "get_signature"})
line = json_recv()
print(line)
## "msg": "We are hyperreality and Jack and we own CryptoHack.org" <=> N = pow(bytes_to_long(DIGEST), D, N), DIGEST = emsa_pkcs1_v15.encode(MSG.encode(), 256),SIGNATURE = pow(bytes_to_long(DIGEST), D, N)
## "msg": "I am Mallory own CryptoHack.org" <=> N = 
msg = "I am Mallory own CryptoHack.org"
digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
json_send({"option": "verify", "msg": msg, "N" : hex(int(line["signature"], 16) - bytes_to_long(digest)), "e" : hex(1)})
received = json_recv()
print(received)