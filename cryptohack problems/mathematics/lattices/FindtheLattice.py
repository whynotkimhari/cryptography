

from math import sqrt
from Crypto.Util.number import getPrime, inverse, bytes_to_long

def decrypt(q, h, f, g, e):
    a = (f * e) % q
    m = ((f * e) % q * inverse(f, g)) % g
    return m

def dot_product(a, b):
    dp = 0
    for i in range(2):
        dp = dp + a[i]*b[i]
    return dp

def size(v):
    return sqrt(v[0]**2 + v[1]**2)

def subtract(a, b):
    return (a[0] - b[0], a[1] - b[1])

def mul(k, a):
    return (a[0] * k, a[1] * k)

def Guassian(v1, v2):
    # print(v1, v2)
    if size(v2) <= size(v1):
        c = v2
        v2 = v1
        v1 = c
    # print(v1, v2)
    m = round(dot_product(v1, v2) / dot_product(v1, v1))
    if m == 0:
        return (v1, v2)
    v2 = subtract(v2, mul(m, v1))
    return Guassian(v1, v2)

q = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257
h = 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523
v = (1, h)
u = (0, q)
f, g = Guassian(v, u)[1]
m = decrypt(q,h,f,g,e)
print(bytes.fromhex(hex(m)[2:]).decode())