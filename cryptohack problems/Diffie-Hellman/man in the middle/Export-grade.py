p = "0xde26ab651b92a129"
g = "0x2"
A = "0x637430f37c694fa7"
B = "0x7249365a2a8c71ff"
iv =  "31077c28f19c90297f3da6dff6ca3019"
encrypted_flag = "0ebb53dab97122361cfa8cdbb5ddc092a5af41452aae8def0d27181b6ee89839"

p = int(p, 16)
g = int(g, 16)
A = int(A, 16)
B = int(B, 16)
iv = bytes.fromhex(iv)
encrypted_flag = bytes.fromhex(encrypted_flag)

from Crypto.Cipher import AES
from Crypto.Util import number
import hashlib

def decrypt(secret, iv, cipher):
    sha1 = hashlib.sha1()
    sha1.update(str(secret).encode())
    key = sha1.digest()[:16]
    aes = AES.new(key, AES.MODE_CBC, iv)
    plain = aes.decrypt(cipher)
    print(plain)

    
a = 7596561454821291306
secret = pow(B, a, p)
decrypt(secret, iv, encrypted_flag)