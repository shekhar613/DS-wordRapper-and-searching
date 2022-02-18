def wordRapper(s):
    sl = []
    s2 = ""
    for i in range(len(s)):
        if s[i] not in [""," ","   ",","]:
            s2+=s[i]
        else:
            sl.append(s2)
            s2=""
    
    print(f"Listed words : \n{sl}\n")
    sorting_string(sl)

def sorting_string(s):
    counter = len(s)-1
    for i in range(len(s)-1): # list traversing
        for j in range(counter): # passes counter
            if len(s[j])>len(s[j+1]):  # swapping the elements
                c = s[j]
                s[j] = s[j+1]
                s[j+1] = c
        counter-=1
    
    print(f"Sorted words : \n{s}\n")
    remove_dupplicates(s)
    

def remove_dupplicates(s):
    s2 = []
    for i in s:
        if i not in s2:
            s2.append(i)
    print(f"Sorted distinct words : \n{s2}\n")
    
wordRapper('''In literary theory, a text is any object that can be "read", whether this object is a work of literature, a street sign, an arrangement of buildings on a city block, or styles of clothing. It is a coherent set of signs that transmits some kind of informative message. Wikipedia''')



