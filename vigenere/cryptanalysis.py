import sys
from operator import itemgetter

# taken from Stinson's Cryptography: Theory and Practice
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

def ioc(m):
    ind = 0.0
    n = len(m)
    for x in range(26):
        fi = m.count(chr(x + ord("A")))
        ind += fi*(fi-1)
    ind /= n*(n-1)
    return ind

def nfreq(text, n):
    count = {} 
    for i in range(len(text) - n + 1):
        ngram = text[i:i+n]
        if ngram in count:
            count[ngram]+=1
        else:
            count[ngram]=1
    return sorted(count.items(), reverse=True, key=itemgetter(1))

def dec(c, k):
    m = ""
    for i in range(len(c)):
        y = ord(c[i]) - ord('A')
        red = ord(k[i % len(k)]) - ord('A')
        m += chr(ord('A') + (y - red) % 26)
    return m

def cfs(l):
    m = min(l)
    for i in range(m, 1, -1):
        if all([j % i == 0 for j in l]):
            return i
    
def kasiski(c, n):
    grams = [x[0] for x in nfreq(c, n)[:5]]
    guesses = {}
    for g in grams:
        ids = []
        start = 0
        while c[start:].find(g) != -1:
            off = c[start:].index(g)
            ids.append(off + start)
            start += off + 1
        diff = [(ids[i+1] - ids[i]) for i in range(len(ids) - 1)]
        guesses[g] = cfs(diff)
    return guesses

def Mg(c, g):
    summ = 0.0
    for j in range(26):
        summ += freq_table[chr(ord("A") + j)] * c.count(chr(ord("A") + (j+g)%26))
    return summ/len(c)

def best_guess(c):
    closest = 0
    cf = 0
    for i in range(26):
        nf = Mg(c, i)
        if  abs(nf - 0.065) < abs(cf -0.065): # Index of Coincidence for English language : 0.065 (Stinson)
            closest = i
            cf = nf
    return closest

def main():
    text = ""
    for line in sys.stdin:
        text += line.strip()
   
    guess_length = kasiski(text, 3)
    print "Guessed key lengths (Kasiski's Test):"
    for g in guess_length:
        print "\tInspecting trigram: ", g, "\tGuessed-length:", guess_length[g]
    ls = [x[1] for x in guess_length.items() if x[1] != None]
    kg = max(set(ls), key=ls.count)
    print "\nBest Guess Length: ", kg
    
    y = [""]*kg
   
    for i in range(len(text)):
        y[i%kg] += text[i]
   
    k = ""

    for i in range(len(y)):
        s = y[i]
        k += chr(ord("A") + best_guess(s))
    
    print "\nBest-guess key:", k
    
    print "\nVigenere decrypt:"
    print dec(text, k)

if __name__ == '__main__':
    main()
