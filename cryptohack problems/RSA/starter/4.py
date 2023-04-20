def extended_euclid(a, b):
    """
    Returns a tuple (gcd, x, y) such that a*x + b*y = gcd, where gcd is the greatest common divisor of a and b.

    :param a: an integer
    :param b: an integer
    :return: a tuple (gcd, x, y)
    """
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (gcd, x, y)
    
N = (857504083339712752489993810777 - 1) * (1029224947942998075080348647219 - 1)
print(extended_euclid(65537, N))