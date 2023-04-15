from Crypto.PublicKey import RSA

with open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der','rb') as f:
    s = f.read()
    key = RSA.importKey(s)
    # Find the modulus of the certificate, giving your answer as a decimal. -> key.n
    print(key.n)