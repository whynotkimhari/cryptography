state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    for i in range(4):
        for j in range(4):
            s[i][j] = s[i][j] ^ k[i][j]
    return s

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    array = bytearray()
    for row in matrix:
        for val in row:
            array.append(val)
    return array

print(matrix2bytes(add_round_key(state, round_key)))