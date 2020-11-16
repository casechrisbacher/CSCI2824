def sequence_slayer(x):
    a = []
    a.insert(0,1)
    a.insert(1,2)

    for i in range(2, 50):
        a.insert(i, (i**2)*a[i-1] - a[i-2])
    
    return a[x]

