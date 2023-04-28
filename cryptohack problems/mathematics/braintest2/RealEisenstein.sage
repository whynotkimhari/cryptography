from decimal import *
import math

getcontext().prec = int(100)

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]

keys = [Decimal(int(_)).sqrt() for _ in PRIMES]

arr = [int(v * int(16) ** int(64)) for v in keys]

ct = 1350995397927355657956786955603012410260017344805998076702828160316695004588429433

def enc(res):
    h = Decimal(int(0))
    for i in range(len(keys)):
        h += res[i] * keys[i]
    ct = int(h * int(16) ** int(64))
    return ct

def sol(N):
    ln = len(arr)
    A = Matrix(ZZ, ln + 1, ln + 1)
    for i in range(ln):
        A[i,i] = 1
        A[i, ln] = arr[i] // N
        A[ln, i] = 64

    A[ln,ln] = ct // N

    res = A.LLL()

    for i in range(ln + 1):
        flag = True
        for j in range(ln):
            if -64 <= res[i][j] < 64:
                continue
            flag = False
            break
        if flag:
            vec = [int(v + 64) for v in res[i][:-1]]
            ret = enc(vec)
            if ret == ct:
                print(N, bytes(vec))
            else:
                print("No", ret, bytes(vec))
            return bytes(vec)
    

for i in range(2, 100000):
    try:
        if b'crypto' in sol(i):
            break
    except TypeError:
        continue