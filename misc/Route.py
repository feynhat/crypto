def map_cipher(s, key) :
    out=[]
    i=0
    for x in range(key) :
        out.append([])
    for char in s :
        out[i].append(char)
        i=i+1
        if i==key :
            i=0
    return out

def cipher(s, key) :
    out=''
    for x in map_cipher(s, key) :
        for y in x :
            out+=y
    return out

def decipher(s, key) :
    out=''
    ref=map_cipher(s, key)
    raw_out={}
    s_counter=0
    for x in range(len(ref)) :
        for y in range(len(ref[x])) :
            ref[x][y]=s[s_counter]
            s_counter+=1
    for x in ref :
        for y in range(len(x)) :
            try :
                raw_out[y]+=x[y]
            except :
                raw_out[y]=x[y]
    for p in raw_out :
        out+=raw_out[p]
    return out
            

print cipher("ILOVEDIGITMAGAZINE",4)
print decipher('IEIGNLDTAEOIMZVGAI',4)

