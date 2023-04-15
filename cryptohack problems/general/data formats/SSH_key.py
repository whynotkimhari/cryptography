from Crypto.PublicKey import RSA

with open('bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub','rb') as f:
    s = f.read()
    key = RSA.importKey(s)
    # Extract the modulus n as a decimal integer from Bruce's SSH public key. -> key.n
    print(key.n)