def dec(c, a, b):
    m = ""
    inv26 = {1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11 , 21:5 , 23:17 , 25:25}
    for i in c:
        y = ord(i) - ord("A")
        m += chr(ord("A") + ((y - b) * inv26[a]) % 26)
    return m

def enc(m, a, b):
    c = ""
    for i in m:
        x = ord(i) - ord("A")
        c += chr(ord("A") + (a*x + b) % 26)
    return c

c = "AMWTALAMDWKMOYBAFMUALPALBZXEQJKMOYBAFMUALPALBZXIIWGYWBAVHUKLOTSMPWTOGGXY"
print dec(c, 1, 18)
