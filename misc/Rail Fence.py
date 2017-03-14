#Rail Fence Cipher and Counter Rail Fence

def cipher(s, key, graph=False) :
    down=True
    raw_out=[]
    out=''
    i=0
    for x in range(key) :
        raw_out.append({})
    for pos in range(len(s)) :
        raw_out[i][pos]=s[pos]
        if i==key-1 :
            down=False
        if i==0 :
            down=True
        if down :
            i=i+1
        else :
            i=i-1
    for p in raw_out :
        for q in p :
            out+=p[q]
    if graph :
        return raw_out
    return out

def decipher(s, key) :
    map_list=cipher(s, key, True) #CREATING JUST FOR MAPPING - WHICHth CHARACTER OF THE STRING - IS WHICHth CHARACTER OF THE CIPHER
    new={}
    out=''
    s_counter=0
    for x in map_list :
        for y in x :
            new[y]=s[s_counter]
            s_counter+=1
    for p in new :
        out+=new[p]
    return map_list

print cipher("FOOBARBAZQUX",6)
print cipher("FOOBARBAZQUX",3)
print decipher('FZAOBRAQXOUB',3)
