import pwn
import json

r = pwn.remote('socket.cryptohack.org', 13374)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

r.recvline()
json_send({"option": "get_secret"})
line = json_recv()
print(line)
json_send({"option": "sign", "msg": line["secret"]})
received = json_recv()
print(bytes.fromhex(received["signature"][2:]))