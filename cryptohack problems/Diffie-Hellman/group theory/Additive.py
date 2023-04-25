from Crypto.Util.number import inverse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
# https://crypto.stackexchange.com/questions/12398/diffie-hellman-on-additive-group
Alice1 = {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x643f59eed551ca7c31d18c9679578dd51a16bd7061880c8bacd266fe435814f7860ecf1ab44b612d50aee89d7f6092a6f8c6335d2b4d4a37672e97c786bd0429c6dd6ce8f3e89fc3a120ec82fea15ee4c88169efd1a6c6d0b5daa220e106a440cf611d96353bcd2f8fcc046441447a895e24cef85ba9aa4db7c582cca518712a12859da29a52f47fcf5dd19a6fc91dcf5b7c7dfe556400cd066420f57486bb86ef812ef9a7c6ac3bc67d084c53fff6178dff461e9b53773ac5ceaf8c953885a1"}
Bob =  {"B": "0xe8d6dc4798fa8e681b51a1b4128450ac020eb9f570acb9903a5e1847f1e81605eae157898870e06f18f3721dfd2b4b7cc94ed9e4bb2bf8b9f1976f5fa0cb4057d17b074f41e8bbde0b001c658d6700b3f7e25872565c05e838c4bed56b7ac3788fd3fb75f203658eb3e21973c5b44314fe59b180047bc12124c8174523e4054e47cd17717e04836e40544d925b67e62932eaed0c51ddb8ca42dc8dbc921ee02806e37f5350455874eeebaf9d33225cabdc3311027b6cf17b0553712052aefeb9"}
Alice2 = {"iv": "3153bcc411df9fdea67faa609f976e04", "encrypted": "ef3c08a289064c456b85c9553bc5f8f2e24681f08ebbee4b75e8581019d7413c8e3855ebde5fda997652a5c42114f142"}

p = int(Alice1['p'], 16)
g = int(Alice1['g'], 16)
A = int(Alice1['A'], 16)
B = int(Bob["B"], 16)
iv = Alice2["iv"]
encrypted = Alice2["encrypted"]
a = A * inverse(g, p)


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
    
shared_secret = (a * B) % p

print(decrypt_flag(shared_secret, iv, encrypted))