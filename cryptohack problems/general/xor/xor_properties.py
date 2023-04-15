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