def enc(m, k):
    c = ""
    for i in m:
        c += chr((ord(i) - ord('A') + k) % 26 + ord('A'))
    return c

def dec(c, k):
    m = ""
    for i in c:
        m += chr((ord(i) - ord('A') - k) % 26 + ord('A'))
    return m
