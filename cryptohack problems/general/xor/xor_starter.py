s = "label"
t = 13

for i in range(len(s)):
    print(chr(ord(s[i]) ^ t), end = "")