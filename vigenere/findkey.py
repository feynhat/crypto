import sys
from freqanal import ioc, freq_table
from vigenere import dec

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
        if  abs(nf - 0.065) < abs(cf -0.065):
            closest = i
            cf = nf
    return closest

def main():
    text = ""
    for line in sys.stdin:
        text += line.strip()
    
    kg = 10  #guessed key length
    y = [""]*kg
   
    for i in range(len(text)):
        y[i%kg] += text[i]
   
    k = ""

    for i in range(len(y)):
        s = y[i]
        k += chr(ord("A") + best_guess(s))
    
    print "Best-guess key:", k
    
    print "Vigenere decrypt:"
    print dec(text, k)

if __name__ == '__main__':
    main()

