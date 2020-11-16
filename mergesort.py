def mergeSort(x):
    if (len(x) > 1):
        m = int(len(x) / 2)
        listone = x[m:]
        listtwo = x[:m]
        listone = mergeSort(listone)
        listtwo = mergeSort(listtwo)
    else:
        return x
    

    newlist = []
    newlistcount = 0
    o = 0 
    t = 0
    while(len(listone) > o and len(listtwo) > t):
        if(listone[o] <= listtwo[t]):
            print('{}{}{}'.format(listone[o],"<",listtwo[t]))
            newlist.append(listone[o])
            o = o + 1
        else:
            print('{}{}{}'.format(listtwo[t],"<",listone[o]))
            newlist.append(listtwo[t])
            t = t + 1
        newlistcount = newlistcount + 1

    while(len(listone) > o):
        newlist.append(listone[o])
        o += 1
    while(len(listtwo) > t):
        newlist.append(listtwo[t])
        t += 1
        
    return newlist