def powerSet(A):
    myset = [[]]
    powercount = 2**len(A) - 1
    for i in range(0, len(A)):
        myset.extend([[A[i]]])
        for k in range(1, len(myset) - 1):
            myset.extend([myset[k] + [A[i]]])
    return myset
print(powerSet([1,2,3,4]))