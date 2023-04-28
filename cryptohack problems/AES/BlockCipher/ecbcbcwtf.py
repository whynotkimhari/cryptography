from Crypto.Util.number import *
from Crypto.Cipher import AES
import os

cipher = 0xaa77805ee52d20fe8337e99ccf286fff2f4d912b8e2d1fe9830eb5cebbff10882ef15a7fe7633fd7d5979ceac88c3d98
deci = 0x4fdb9c134131bfd9f5b37f8d95640b43c905f92e91425bcde055b6a9ba4b04ca7079e71bbf4940d8b45194ef9ade31f5

iv = os.urandom(16)
print(long_to_bytes(bytes_to_long(long_to_bytes(cipher)[0:16])^bytes_to_long(long_to_bytes(deci)[16:32]))
    + long_to_bytes(bytes_to_long(long_to_bytes(cipher)[16:32])^bytes_to_long(long_to_bytes(deci)[32:48]))
    )