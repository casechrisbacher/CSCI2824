def first_D_digit_Fib(x):
    a = []
    a.insert(0,1)
    a.insert(1,2)
    i = 1
    j = 0
    
    for i in range(2, 30):
        a.insert(i, a[i-1] + a[i-2])
    for j in range(0,30):
        if(len(a[j]) == x):
            return a[j]

    return -1