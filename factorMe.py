import math
def factorMe(N):
    counter = 3
    root = math.sqrt(N)
    if(N % 2 == 0):
        return (2, int(N/2))
    
    while counter <= root:
        primecounter = 3
        if(N % counter == 0):
            # primeroot = math.sqrt(counter)
            # while primecounter < primeroot:
            #     if(counter % primecounter == 0):
            #         break
            #     primecounter = primecounter + 2
            #     if(primecounter >= primeroot):
            return (counter, int(N/counter))
        counter = counter + 2