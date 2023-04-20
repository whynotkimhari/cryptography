from math import sqrt

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


def main():
    v = (846835985, 9834798552)
    u = (87502093, 123094980)
    guass = Guassian(v,u)
    print(dot_product(guass[0], guass[1]))

if __name__ == "__main__":
    main()