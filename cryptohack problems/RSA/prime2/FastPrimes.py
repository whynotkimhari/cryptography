from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, inverse
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

with open('RSA\prime2\key_17a08b7040db46308f8b9a19894f9f95.pem','r') as f: 
    key = RSA.importKey(f.read())
    # Extract the private key d as a decimal integer from this PEM-formatted RSA key. -> key.d
    print(key.n)
# http://factordb.com/index.php?query=4013610727845242593703438523892210066915884608065890652809524328518978287424865087812690502446831525755541263621651398962044653615723751218715649008058509
# key.n = 4013610727845242593703438523892210066915884608065890652809524328518978287424865087812690502446831525755541263621651398962044653615723751218715649008058509
n = 4013610727845242593703438523892210066915884608065890652809524328518978287424865087812690502446831525755541263621651398962044653615723751218715649008058509
p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
q = 77342270837753916396402614215980760127245056504361515489809293852222206596161

e = 0x10001
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
ciphertext = '249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28'

key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)

print(cipher.decrypt(bytes.fromhex(ciphertext)))
