
"""
Given a prime number n
the task is to find its primitive root under modulo n. 
The primitive root of a prime number n is an integer r between[1, n-1] 
such that the values of r^x(mod n) where x is in the range[0, n-2] are different. 
Return -1 if n is a non-prime number.
""" 

p = 28151

for i in range(1, p):
    s = []
    found = True
    for j in range(p - 1):
        s.append(pow(i, j, p))
    if(len(s) == len(set(s))):
        print(i)
        break