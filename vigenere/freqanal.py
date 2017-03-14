from operator import itemgetter
import sys

def nfreq(text, n):
    count = {} 
    for i in range(len(text) - n + 1):
        ngram = text[i:i+n]
        if ngram in count:
            count[ngram]+=1
        else:
            count[ngram]=1
    return sorted(count.items(), reverse=True, key=itemgetter(1))

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

def main():
    text = ""
    for line in sys.stdin:
        text += line.strip()

    for i in range(1, 5):
        print "%d-gram frequencies:" % i
        for x in nfreq(text, i): print x[0], ":", x[1]

    print "Index of Coincidence: ", ioc(text)

if __name__ == '__main__':
    main()
