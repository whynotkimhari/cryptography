from math import *

p = 29
ints = [14, 6, 11]
for intz in ints:
    for i in range(1,p):
        if i*i % p == intz:
            print(i)
            break
