def dot_product(a, b):
    dp = 0
    for i in range(4):
        dp = dp + a[i]*b[i]
    return dp

def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])

def subtract(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])

def mul(k, a):
    return (a[0] * k, a[1] * k, a[2] * k, a[3] * k)

def round_(u, k):
    return (round(u[0], k), round(u[1], k), round(u[2], k), round(u[3], k))

v = [(0,0,0,0), (4,1,3,-1), (2,1,-3,4), (1,0,-2,7), (6, 2, 9, -5)]

u = [(0,0,0,0), (4,1,3,-1)]

for i in range(2, 5):
    s = v[i]
    for j in range(1, i):
        k = dot_product(u[j], s) / dot_product(u[j], u[j])
        s = subtract(s, mul(k, u[j]))
    u.append(s)

for i in range(1, 5):
    print(round_(u[i], 5))
