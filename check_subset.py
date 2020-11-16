def check_subset(A, B):
    existcount = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if(A[i] == B[j]):
                existcount += 1
        
    if(existcount == len(B) or len(A) == 0):
        return True
    else:
        return False