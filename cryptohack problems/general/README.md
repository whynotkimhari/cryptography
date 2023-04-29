# ENCODING
## ASCII
convert ascii character in ord back to chr using chr() function
```python
arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for x in arr:
    print(chr(x), end="")
```

## Hex
convert hex str to bytes str using fromhex() function
```python
s = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(s))
```

## Base64
encoded bytes str using base64 lib
```python
import base64
s = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
print(base64.b64encode(bytes.fromhex(s)))
```

## Bytes and Big Integers
convert int/long to bytes str
```python
from Crypto.Util.number import *
s = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(s))
```

## Encoding Challenge
```python
from pwn import remote
from json import loads, dumps
from base64 import b64decode
from codecs import encode

io = remote('socket.cryptohack.org', 13377)
while True:
    enc = loads(io.recvline().decode())
    print(enc)
    if 'flag' in enc: 
        break
    io.sendline(dumps({"decoded": {
        'base64': lambda e: b64decode(e).decode(),
        'hex'   : lambda e: bytes.fromhex(e).decode(),
        'rot13' : lambda e: encode(e, 'rot_13'),
        'bigint': lambda e: bytes.fromhex(e[2:]).decode(),
        'utf-8' : lambda e: ''.join([chr(c) for c in e])
    }[enc['type']](enc['encoded'])}).encode())
```

# XOR
## XOR Starter
xor each char in str with 13
```python
s = "label"
t = 13

for i in range(len(s)):
    print(chr(ord(s[i]) ^ t), end = "")
```

## XOR Properties
```bash
fl the instruction we got
key2 = (key1 ^ key2) ^ key1
key3 = (key2 ^ key3) ^ key2
flag = ((flag ^ key1 ^ key2 ^ key3) ^ key1) ^ key2
then we implement it as
```
```python
from Crypto.Util.number import *

k1 = bytes_to_long(bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"))
k1k2 = bytes_to_long(bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"))
k2k3 = bytes_to_long(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"))
fk1k2k3 = bytes_to_long(bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"))

key2 = k1k2 ^ k1
key3 = k2k3 ^ key2
flag = ((fk1k2k3 ^ k1) ^ key2) ^ key3

bflag = long_to_bytes(flag)
print(bflag)
```

## Favourite Byte
bruteforce to find out
```python
from Crypto.Util.number import *
import base64

b = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bb = bytes.fromhex(b)
for i in range(0, 255):
    s = ""
    for x in bb:
        s = s + chr(x ^ i)
    if s[0:6] == "crypto":
        print(s)
```        

## You either know, XOR you don't
flag format: crypto{
```python
encrypted_msg = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encrypted_msg = bytes.fromhex(encrypted_msg)

flag_format = b"crypto{"
key = [o1 ^ o2
       for (o1, o2) in zip(encrypted_msg, flag_format)] + [ord("y")]

flag = []
key_len = len(key)
for i in range(len(encrypted_msg)):
    flag.append(
        encrypted_msg[i] ^ key[i % key_len]
    )
flag = "".join(chr(o) for o in flag)

print("Flag:")
print(flag)
```

## Lemur XOR
i search XOR 2 img on GG and get this
```python
from PIL import Image, ImageChops

im1 = Image.open("lemur.png")
im2 = Image.open("flag.png")

im3 = ImageChops.difference(im1,im2)

im3.show()
im3.save("final.png")
```
![pic](https://github.com/whynotkimhari/cryptography/blob/main/cryptohack%20problems/general/xor/final.png)

# MATHEMATICS
## Greatest Common Divisor
using gcd func
```python
from math import *
a = 66528
b = 52920
print(gcd(a, b))
```

## Extended GCD
fl the instruction
```python
def extended_gcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)
print("[+] GCD: {}".format(gcd))
print("[+] u,v: {},{}".format(u,v))
print("\n[*] FLAG: crypto{{{},{}}}".format(u,v))
```

## Modular Arithmetic 1
fl the instruction
```python
a = 11 % 6
b = 8146798528947 % 17
print(a if a < b else b)
```

## Modular Arithmetic 2
```bash
note that: (abcd...)%p = (a%p * b%p * c%p ...)%p
so just using that
```
```python
a = 273246787654 % 65537
for i in range(0, 65536 - 1):
    a = (a * 273246787654) % 65537
print(a)
```

## Modular Inverting
```bash
note that: ab % c = 1 entails that b in range(1, c)
```
```python
for i in range(1, 13):
    if 3 * i % 13 == 1:
        print(i)
        break
```

# DATA FORMATS
this [doc](https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html) may help these challenges. I just read the doc and use
## Privacy-Enhanced Mail?
```python
from Crypto.PublicKey import RSA

with open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem','r') as f: 
    key = RSA.importKey(f.read())
    # Extract the private key d as a decimal integer from this PEM-formatted RSA key. -> key.d
    print(key.d)
```

## CERTainly not
```python
from Crypto.PublicKey import RSA

with open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der','rb') as f:
    s = f.read()
    key = RSA.importKey(s)
    # Find the modulus of the certificate, giving your answer as a decimal. -> key.n
    print(key.n)
```

## SSH Keys
```python
from Crypto.PublicKey import RSA

with open('bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub','rb') as f:
    s = f.read()
    key = RSA.importKey(s)
    # Extract the modulus n as a decimal integer from Bruce's SSH public key. -> key.n
    print(key.n)
```

## Transparency
This one is different. I just use [this](https://subdomainfinder.c99.nl/scans/2020-09-10/cryptohack.org) to find the subdomain, then get the flag
