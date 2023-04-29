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

### Bytes and Big Integers
convert int/long to bytes str
```python
from Crypto.Util.number import *
s = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(s))
```

### Encoding Challenge
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
