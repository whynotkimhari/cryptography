import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pwn import xor

cookie = bytes.fromhex("eee380cdcefda943519525e74b682c252ff7fbe634b9cdb5e17c2c84d28ffe1e6587ac61394757ba33ad782e29627bcc")


def response(block, iv):
    url = "http://aes.cryptohack.org/flipping_cookie/check_admin/"
    url += block.hex()
    url += '/'
    url += iv.hex()
    url += "/"
    r = requests.get(url)
    js = r.json()
    print(js)

iv = cookie[:16]
block1 = cookie[16:32]
response(block1, xor(xor(b"admin=False;expi", pad(b"admin=True;", 16)), iv))