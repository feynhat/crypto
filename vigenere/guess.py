freq_table = {
    'A': 0.082,
    'B': 0.015,
    'C': 0.028,
    'D': 0.043,
    'E': 0.127,
    'F': 0.022,
    'G': 0.020,
    'H': 0.061,
    'I': 0.070,
    'J': 0.002,
    'K': 0.008,
    'L': 0.040,
    'M': 0.024,
    'N': 0.067,
    'O': 0.075,
    'P': 0.019,
    'Q': 0.001,
    'R': 0.060,
    'S': 0.063,
    'T': 0.091,
    'U': 0.028,
    'V': 0.010,
    'W': 0.023,
    'X': 0.001,
    'Y': 0.020,
    'Z': 0.001,
}

def newfreq(c, g):
    summ = 0.0
    for j in range(26):
        summ += freq_table[chr(ord("A") + j)] * c.count(chr(ord("A") + (j+g)%26))
    return summ/len(c)

def best_guess(c):
    closest = 0
    cf = 0
    for i in range(26):
        nf = newfreq(c, i)
        if  abs(nf - 0.065) < abs(cf -0.065):
            closest = i
            cf = nf
    return closest
