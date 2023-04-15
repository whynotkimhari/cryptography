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