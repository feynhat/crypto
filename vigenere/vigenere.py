def enc(m, k):
    c = ""
    for i in range(len(m)):
        x = ord(m[i]) - ord('A')
        inc = ord(k[i % len(k)]) - ord('A')
        c += chr(ord('A') + (x + inc) % 26)
    return c

def dec(c, k):
    m = ""
    for i in range(len(c)):
        y = ord(c[i]) - ord('A')
        red = ord(k[i % len(k)]) - ord('A')
        m += chr(ord('A') + (y - red) % 26)
    return m
